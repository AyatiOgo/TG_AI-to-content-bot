import os
import shutil
import subprocess
import whisper


def find_ffmpeg():
    path = shutil.which("ffmpeg")
    if path:
        print(f"✅ FFmpeg found at: {path}")
        return path

    common_paths = [
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe",
        r"C:\Users\AYATI\ffmpeg\bin\ffmpeg.exe",
    ]
    for p in common_paths:
        if os.path.exists(p):
            print(f"✅ FFmpeg found at: {p}")
            return p

    raise FileNotFoundError(
        "❌ FFmpeg not found! Make sure it's installed and in your PATH."
    )

FFMPEG_PATH = find_ffmpeg()

print("Loading Whisper model... (this may take a moment)")
MODEL = whisper.load_model("base")


def extract_audio(video_path: str) -> str:
    audio_path = video_path.rsplit(".", 1)[0] + ".wav"
    print(f"🎙️ Extracting audio from: {video_path}")
    print(f"🎙️ Audio will be saved to: {audio_path}")

    command = [
        FFMPEG_PATH,
        "-i", video_path,
        "-vn",
        "-ar", "16000",
        "-ac", "1",
        "-y",
        audio_path
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ FFmpeg stderr: {result.stderr}")
        raise Exception(f"FFmpeg failed: {result.stderr}")

    print(f"🎙️ Audio saved to: {audio_path}")
    return audio_path


def transcribe(video_path: str) -> str:
    audio_path = extract_audio(video_path)

    result = MODEL.transcribe(audio_path)
    transcript = result["text"].strip()

    if os.path.exists(audio_path):
        os.remove(audio_path)

    return transcript