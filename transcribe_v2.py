import os
from dotenv import load_dotenv
import cloudconvert
import requests
from faster_whisper import WhisperModel
load_dotenv()

ffmpeg_path = r"C:\Program Files\ffmpeg\bin"
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]


print("Loading Faster Whisper model... (this may take a moment)")
MODEL = WhisperModel(
    "base",
    device="cpu",         
    compute_type="int8"   
)


CLOUDCONVETER_API=os.getenv('CLOUD_CONVERT_KEY')


cloudconvert.configure(api_key=CLOUDCONVETER_API, sandbox=False)

def extract_audio(video_path: str):
    print(f"☁️ Uploading {video_path} to CloudConvert...")

    # Create a CloudConvert job with 3 tasks
    job = cloudconvert.Job.create(
        payload={
            "tasks": {
                "upload_task": {"operation": "import/upload"},
                "convert_task": {
                    "operation": "convert",
                    "input": "upload_task",
                    "output_format": "wav" },
                    "export_task": {"operation": "export/url", "input": "convert_task"},
            }
        }
    )

    # Find the upload task
    upload_task = next(
        (t for t in job["tasks"] if t["name"] == "upload_task"), None
    )

    if upload_task is None:
        raise RuntimeError("Upload task not found in CloudConvert job")

    # Upload the file
    upload = cloudconvert.Task.upload(file_name=video_path, task=upload_task)
    print("Uploaded to CloudConvert ✔️")

    # Wait for conversion to finish
    job = cloudconvert.Job.wait(id=job["id"])

    for task in job["tasks"]:
        print("\n--- TASK REPORT ---")
        print("Name:", task["name"])
        print("Operation:", task["operation"])
        print("Status:", task["status"])
        print("Message:", task.get("message"))
        print("Code:", task.get("code"))

    # Find export task and grab the file URL
    export_task = next(
        (t for t in job["tasks"] if t["name"] == "export_task"),
        None
    )

    if not export_task:
        raise RuntimeError("Export task not found in job")

    if export_task["status"] != "finished":
        raise RuntimeError(f"Export task failed: {export_task}")

    if not export_task.get("result") or not export_task["result"].get("files"):
        raise RuntimeError(f"No files returned from export task: {export_task}")

    file_url = export_task["result"]["files"][0]["url"]

    # Download the WAV
    audio_path = video_path.rsplit(".", 1)[0] + ".wav"
    print(f"💾 Downloading audio to: {audio_path}")

    response = requests.get(file_url, stream=True)
    response.raise_for_status()

    with open(audio_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print("Download complete ✔")
    print("File exists after download:", os.path.exists(audio_path))
    print("File size:", os.path.getsize(audio_path))

    return audio_path

def transcribe(video_path: str) -> str:
    audio_path = extract_audio(video_path)

    print("Audio path:", audio_path)

    segments, info = MODEL.transcribe(
        audio_path,
        beam_size=5  
    )

    transcript = ""
    for segment in segments:
        transcript += segment.text

    transcript = transcript.strip()

    if os.path.exists(audio_path):
        os.remove(audio_path)

    return transcript