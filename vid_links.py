import yt_dlp
import tempfile
import os
import re

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