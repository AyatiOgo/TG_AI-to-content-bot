import yt_dlp
import tempfile
import os
import re

ffmpeg_path = r"C:\Program Files\ffmpeg\bin"
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]

def download_audio_from_url(url: str, user_id: int):
    temp_dir = tempfile.gettempdir()
    output_path = os.path.join(temp_dir, f"audio_{user_id}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',  # 🎵 Audio only
        'outtmpl': output_path,
        'quiet': True,
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        audio_path = os.path.splitext(filename)[0] + ".wav"

    return audio_path

def download_video_from_url(url: str) -> str:
    temp_dir = tempfile.gettempdir()
    output_path = os.path.join(temp_dir, "link_video.%(ext)s")

    ydl_opts = {
        "outtmpl": output_path,
        "format": "mp4/bestvideo+bestaudio/best",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return filename

def contains_url(text: str) -> bool:
    url_pattern = r"(https?://\S+)"
    return re.search(url_pattern, text) is not None