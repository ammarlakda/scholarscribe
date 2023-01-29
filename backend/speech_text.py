import whisper
def speech_text(audio):
    model = whisper.load_model("base")
    result = model.transcribe(audio)
    return result["text"]