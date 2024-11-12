import azure.cognitiveservices.speech as speechsdk

# from Otp.modules.database.main_db import TTS/


def text_to_speech(text, output_file, model="hi-IN-SwaraNeural"):
    speech_key = "05821237f84745efb15cd94d2e2b5228"  # Replace with your Speech service key
    service_region = "japaneast"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_voice_name = model
    audio_config = speechsdk.audio.PullAudioOutputStream()
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Riff8Khz16BitMonoPcm)
    speech_config.enable_audio_logging = False
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = synthesizer.speak_text_async(text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        audio_data = result.audio_data
        with open(output_file, "wb+") as audio_file:
            audio_file.write(audio_data)
        print(f'Text-to-speech conversion successful. Audio saved to {output_file}')
    else:
        print(f'Text-to-speech conversion failed: {result.reason}')

# text_to_speech("Hello, this is a test message", "Otp/audio/output.wav")
