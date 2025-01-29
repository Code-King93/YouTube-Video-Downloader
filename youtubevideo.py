import os
import subprocess
import sys

# Paths
download_dir = r"C:\Users\timsp\OneDrive\Scripts\Youtube Video Downloader\Videos Downloaded"

video_url = "https://www.youtube.com/watch?v=3igFMIZesNc"

# Ensure the download directory exists
os.makedirs(download_dir, exist_ok=True)

# Step 1: Download the best quality video
yt_dlp_cmd = [
    "yt-dlp",
    "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",
    "--merge-output-format", "mp4",
    "-o", os.path.join(download_dir, "%(title)s.%(ext)s"),
    video_url
]

print("\n📥 Downloading video...")
try:
    subprocess.run(yt_dlp_cmd, check=True, capture_output=True, text=True)
    print("✅ Download completed successfully!")
except subprocess.CalledProcessError as e:
    print(f"❌ Error downloading video: {e}")
    print("🔍 Error output:", e.stderr)
    sys.exit(1)
