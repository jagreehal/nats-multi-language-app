import asyncio
import json
import random
from nats.aio.client import Client as NATS
from decimal import Decimal
from datetime import datetime


async def add_numbers(msg):
    try:
        data = json.loads(msg.data.decode())
        requestId = data.get("requestId", "unknown")
        num1 = Decimal(str(data.get("num1", "0")))
        num2 = Decimal(str(data.get("num2", "0")))

        random_sleep = random.uniform(5, 10)
        print(f"[{datetime.now().isoformat()}] {requestId}: Simulating delay of {random_sleep:.2f} seconds...")
        await asyncio.sleep(random_sleep)

        result = num1 + num2

        print(f"[{datetime.now().isoformat()}] {requestId}: Adding {num1} + {num2} = {result}")

        await msg.respond(json.dumps({"requestId": requestId, "status": "success", "result": str(result)}).encode())

    except Exception as e:
        print(f"[{datetime.now().isoformat()}] {requestId}: Error processing message: {e}")

        await msg.respond(json.dumps({"requestId": requestId, "status": "error", "error": str(e)}).encode())


async def main():
    nc = NATS()
    await nc.connect(servers=["nats://localhost:4222"])

    print(f"[{datetime.now().isoformat()}] Connected to NATS")

    await nc.subscribe("rpc.add", cb=add_numbers)

    try:
        while True:
            await asyncio.sleep(1)
    finally:
        await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
