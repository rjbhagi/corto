import requests


# requests.post("https://389f-117-205-180-135.ngrok-free.app/webhook?user_id=2142595466", json={"status": "Connected", "callsid": "1234567890"})

# # # post = requests.post(url = "https://api.otp.ceo/voice/create-call", 
# # #     json = {
# # #     "to_": "918172821187",
# # #     "from_": "918172821187",
# # #     "webhookurl": f"https://224d-117-205-180-135.ngrok-free.app/webhook?user_id=1123",
# # #     "apikey": "6c699-8697e-0548b-fbbc6"
# # #     })

# # # print(post.content)


request = {
    "callsid": "38727bfabc1cbddd2",
    "audiourl": "https://tmpfiles.org/dl/4766123/audio_2024-04-08_21-53-55_g711.org__2.wav",
    "apikey": "a7c4f-b4e6e-164d0-3a784"
    }
# post = requests.post("https://api.otp.ceo/voice/play-text", json = request)
# print(post.status_code)