import whisper
def speech_text(audio):
    model = whisper.load_model("base")
    result = model.transcribe("backend/"+audio)
    return result["text"]