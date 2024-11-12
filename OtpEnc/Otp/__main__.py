import asyncio
import uvicorn


from fastapi import FastAPI, Request

from .modules.update_user import update_user
from fastapi.responses import FileResponse
from . import otpbot, helper, LOGGER
from .modules.database.main_db import SelfDestruct



app = FastAPI()
@app.post("/webhook")
async def webhook_listener(request: Request):
    data = await request.json()
    user_id = request.query_params.get("user_id")
    # LOGGER.info(data)
    await update_user(user_id, data)
    return {"status": "Webhook received successfully"}


@app.get("/audio")
def read_root(request: Request):
    file_path = request.query_params.get("file_id")
    return FileResponse(file_path, media_type='audio/wav')


@app.get("/ip")
async def read_item(request: Request):
    print(request.headers)
    ip_Ad = request.client.host
    print(f"\n\n{ip_Ad}\n\n")
    return {"ip": ip_Ad}

async def fastapi_server():
    port = 4000
    LOGGER.info(f"Starting FastAPI on port {port}...")
    config = uvicorn.Config(app=app, host="0.0.0.0", port=port, loop="none")
    # config = uvicorn.Config(app=app, host="192.168.1.5", port=8000, loop="none")
    server = uvicorn.Server(config=config)
    await server.serve()

async def main():
    if SelfDestruct().get_status()[0] == 0:
        exit("Bot has self destructed itself, Exiting...")
    LOGGER.info("Starting main asyncio loop...")
    loop1 = loop.create_task(fastapi_server())
    loop2 = loop.create_task(otpbot.start())
    loop3 = loop.create_task(helper.start())
    await asyncio.wait([loop1, loop2, loop3])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
