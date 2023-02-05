import whisper
def speech_text(audio):
    model = whisper.load_model("base")
    result = model.transcribe(audio, fp16=False)
    return result["text"]