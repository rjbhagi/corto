import json
import asyncio
import requests

from .. import (
    WEBHOOK_URL, 
    OTP_API, 
    AUDIO_SERVER, 
    LOGGER, 
    API_URL
)

# OTP_API = "bf61f600-68a4-4477-a9d7-f280bef0eabd"
# TOKEN = "6863850335:AAHv4IxABKSPqqoUCpaDIa0cNpusG8ArSqM"
# AUDIO_SERVER = "http://117.205.180.205:443/audio"
# WEBHOOK_URL = "http://117.205.180.205:443/webhook"
class Api:

    async def create_call(self, user_id: str, victim_no: str, calling_no: str, amd: bool = True):
        victim_no = str(victim_no)
        calling_no = str(calling_no)
        webhook_url = f"{WEBHOOK_URL}?user_id={user_id}"
        data = {
            "to_": victim_no,
            "from_": calling_no,
            "callbackurl": webhook_url,
            "apikey": OTP_API,
            "amd": 'true'
        }
        try:
            response = requests.post(f"{API_URL}/v2/create-call", json=data, timeout=2)
        except requests.exceptions.Timeout:
            return 200
        return response.status_code

    async def play_text(self, call_id: str, text: str, model: str = "hi-IN-SwaraNeural", endcall = False):
        data = {
            "text": text,
            "voice": model,
            "call_id": call_id
        }
        response = requests.post(f"{API_URL}/v2/play-text", json=data)
        if endcall == True:
            await asyncio.sleep(5)
            await self.end_call(call_id)
        return response.json()

    async def end_call(self, user_id, call_id: str):
        await asyncio.sleep(2)
        data = {
            "call_id": call_id,
            "callbackurl": f"{WEBHOOK_URL}?user_id={user_id}",
        }
        response = requests.post(f"{API_URL}/v2/hangup", json=data)
        return response.json()
    
    def hold_call(self, call_id: str):
        data = {
            "call_id": call_id
        }
        response = requests.post(f"{API_URL}/v2/hold", json=data)
        return response.json()

    def unhold_call(self, call_id: str):
        data = {
            "call_id": call_id
        }
        response = requests.post(f"{API_URL}/v2/unhold", json=data)
        return response.json()

    def gather_digits(self, call_id: str, text: str, model: str = "bn-IN-TanishaaNeural", digits: int = 4):
        data = {
            "text": text,
            "voice": model,
            "call_id": call_id,
            "maxDigits": digits
        }
        response = requests.post(f"{API_URL}/v2/gather-text", json=data)
        return response.json()

    async def play_audio(self, user_id, call_id: str, audio: str, end_call = False):
        print(f"{WEBHOOK_URL}?user_id={user_id}")
        data = {
            "audioUrl": audio,
            "call_id": call_id,
            "callbackurl": f"{WEBHOOK_URL}?user_id={user_id}",
        }
        response = requests.post(f"{API_URL}/v2/play-audio", json=data)
        if end_call == True:
            await asyncio.sleep(2)
            await self.end_call(user_id, call_id)
        return response.json()

    async def gather_audio(self, user_id, call_id: str, audio: str, digits: int = 1) -> dict:

        data = {
            "audioUrl": audio,
            "call_id": call_id,
            "maxDigits": int(digits),
            "validDigits": "1234567890",
            "callbackurl": f"{WEBHOOK_URL}?user_id={user_id}",
        }
        response = requests.post(f"{API_URL}/v2/gather-audio", json=data)
        return response.json()