import os

# import uvicorn

# from fastapi import FastAPI,  Request
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse


# app = FastAPI()
# app.mount("/MP3", StaticFiles(directory = "Otp/Audio"), name = "static")
# @app.get("/audio.wav")
# def read_root(request: Request):
#     # xD = request.query_params.get("text")
#     return FileResponse('Otp/Audio/output.wav', media_type='audio/wav')


# uvicorn.run(app, host="192.168.1.3", port=443)

# import requests

# webhook = "http://117.205.180.205:443/webhook?user_id=1234"
# data = {
#     "user_id": 1,
#     "state": "Hello, this is a test message",
#     "uuid": "1234567890",
#     "model": "hi-IN-SwaraNeural",
#     "user_id": "1234"
# }
# response = requests.post(webhook, json=data)
# print(response.text)

# def delete_audios(user_id):
#     for file in os.listdir("Otp/Audio"):
#         if str(user_id) in file:
#             os.remove(f"Otp/Audio/{file}")

# delete_audios(2142595466)

