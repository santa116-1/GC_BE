import asyncio
import websockets
import json
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Propulsion

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

async def handle_connection(websocket):
    print("✅ Client connected")
    try:
        async for message in websocket:
            data = json.loads(message)
            ship_id = data.get('ship_id')

            if ship_id is None:
                await websocket.send(json.dumps({"error": "No ship_id provided"}))
                continue

            while ship_id:
            # Fetch data for the specific ship_id
                session = SessionLocal()
                try:
                    propulsion_data = get_propulsion_data_by_id(session, ship_id)
                    if propulsion_data:
                        await websocket.send(json.dumps({"propulsion_data": propulsion_data}))
                    else:
                        await websocket.send(json.dumps({"error": f"No data found for ship_id {ship_id}"}))
                finally:
                    session.close()
                await asyncio.sleep(10)
                
    except websockets.exceptions.ConnectionClosed:
        print("❌ Client disconnected")
    except Exception as e:
        print(f"⚠️ Error: {e}")

# Start the WebSocket Server
async def main():
    async with websockets.serve(handle_connection, "0.0.0.0", 9000):
        print("🚀 WebSocket server started on ws://0.0.0.0:9000")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
