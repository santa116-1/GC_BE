import asyncio
import websockets
import json
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Propulsion, Commnication, Telemetry

# Fetch Propulsion Data by ship_id from the Database
def get_propulsion_data_by_id(session: Session, ship_id: int):
    data = session.query(Propulsion).filter(Propulsion.ship_id == ship_id).all()
    return [
        {
            "ship_id": record.ship_id,
            "latitude": record.latitude,
            "longitude": record.longitude,
            "speed": record.speed,
            "direction": record.direction,
            "roll": record.roll,
            "pitch": record.pitch,
            "yaw": record.yaw,
            "rudder_output": record.rudder_output,
            "rudder_angle": record.rudder_angle,
        }
        for record in data
    ]

def get_communication_data(session: Session, ship_id: int):
    data = session.query(Commnication).filter(Commnication.ship_id == ship_id).all()
    return [
        {
            "id": record.id,
            "ship_id": record.ship_id,
            "wifi_status": record.wifi_status,
            "wifi_rssi": record.wifi_rssi,
            "gps_status": record.gps_status,
            "gps_quality": record.gps_quality,
        }
        for record in data
    ]

def get_telemetry_data(session: Session, ship_id: int):
    data = session.query(Telemetry).filter(Telemetry.ship_id == ship_id).all()
    return [
        {
            "id": record.id,
            "ship_id": record.ship_id,
            "thruster_output": record.thruster_output,
            "thruster_rotation_speed": record.thruster_rotation_speed,
            "thruster_voltage": record.thruster_voltage,
            "thruster_current": record.thruster_current,
            "battery_1_remaining": record.battery_1_remaining,
            "battery_1_voltage": record.battery_1_voltage,
            "battery_1_charging_status": record.battery_1_charging_status,
            "battery_2_remaining": record.battery_2_remaining,
            "battery_2_voltage": record.battery_2_voltage,
            "battery_2_charging_status": record.battery_2_charging_status,
            "battery_3_remaining": record.battery_3_remaining,
            "battery_3_voltage": record.battery_3_voltage,
            "battery_3_charging_status": record.battery_3_charging_status,
            "pcu_voltage": record.pcu_voltage,
            "pcu_current": record.pcu_current,
            "solar_voltage": record.solar_voltage,
            "solar_current": record.solar_current,
            "body_temperature": record.body_temperature,
        }
        for record in data
    ]

async def handle_connection(websocket):
    print("✅ Client connected")
    try:
        async for message in websocket:
            data = json.loads(message)
            ship_id = data.get('ship_id')
            data_type = data.get('data_type')
            print("✅✅✅", data_type)
            if ship_id is None or data_type is None:
                await websocket.send(json.dumps({"error": "Missing ship_id or data_type"}))
                continue

            # Start periodic data updates every 10 seconds
            try:
                while True:
                    session = SessionLocal()
                    response = {}

                    # Handle Propulsion Data
                    if data_type == 'propulsion' or data_type == 'all':
                        propulsion_data = get_propulsion_data_by_id(session, ship_id)
                        if propulsion_data:
                            response['propulsion_data'] = propulsion_data
                        else:
                            response['error'] = f"No propulsion data found for ship_id {ship_id}"

                    # Handle Communication Data
                    if data_type == 'communication' or data_type == 'all':
                        communication_data = get_communication_data(session, ship_id)
                        if communication_data:
                            response['communication_data'] = communication_data
                        else:
                            response['error'] = f"No communication data found for ship_id {ship_id}"

                    await websocket.send(json.dumps(response))

                    session.close()

                    # Wait for 10 seconds before fetching and sending data again
                    await asyncio.sleep(10)

            except websockets.exceptions.ConnectionClosed:
                print("❌ Client disconnected")
                break 

            except Exception as e:
                print(f"⚠️ Error: {e}")
                await websocket.send(json.dumps({'error': str(e)}))

    except websockets.exceptions.ConnectionClosed:
        print("❌ Client disconnected")
    except Exception as e:
        print(f"⚠️ Error: {e}")

async def main():
    async with websockets.serve(handle_connection, "0.0.0.0", 9000):
        print("🚀 WebSocket server started on ws://0.0.0.0:9000")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())