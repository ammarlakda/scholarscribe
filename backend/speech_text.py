import whisper

model = whisper.load_model("base")
result = model.transcribe("backend/audio.mp3")
print(result["text"])