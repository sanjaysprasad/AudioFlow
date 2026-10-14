import subprocess
import os
from pathlib import Path

def sanitize_url(url):
    url = url.replace("music.youtube.com", "www.youtube.com")
    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
        url = f"https://www.youtube.com/watch?v={video_id}"
    if "&si=" in url:
        url = url.split("&si=")[0]
    elif "?si=" in url:
        url = url.split("?si=")[0]
    return url

def get_downloads_folder():
    downloads = str(Path.home() / "Downloads")
    if not os.path.exists(downloads):
        os.makedirs(downloads)
    return downloads

def download_youtube_media(url, folder, format_choice, quality):
    output_template = f"{folder}/%(title)s.%(ext)s"
    command = [
        "yt-dlp", "--add-metadata", "--embed-thumbnail",
        "-o", output_template,
        url
    ]
    if format_choice == "mp3":
        command += [
            "-x", "--audio-format", "mp3", "--audio-quality", quality
        ]
    elif format_choice == "mp4":
        resolution_map = {
            "480": "bestvideo[height<=480]+bestaudio/best[height<=480]",
            "720": "bestvideo[height<=720]+bestaudio/best[height<=720]",
            "1080": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
            "2160": "bestvideo[height<=2160]+bestaudio/best[height<=2160]",
        }
        format_string = resolution_map.get(quality, resolution_map["480"])
        command += ["-f", format_string, "--merge-output-format", "mp4"]
    print(f"Download folder: {folder}")
    try:
        subprocess.run(command, check=True)
        print("Download and conversion complete.")
    except subprocess.CalledProcessError as e:
        print(f"yt-dlp error: {e}")

def download_playlist(url, folder, format_choice, quality):
    output_template = f"{folder}/%(playlist)s/%(title)s.%(ext)s"
    command = [
        "yt-dlp", "--yes-playlist", "--add-metadata", "--embed-thumbnail",
        "-o", output_template,
        url
    ]
    if format_choice == "mp3":
        command += [
            "-x", "--audio-format", "mp3", "--audio-quality", quality
        ]
    elif format_choice == "mp4":
        resolution_map = {
            "480": "bestvideo[height<=480]+bestaudio/best[height<=480]",
            "720": "bestvideo[height<=720]+bestaudio/best[height<=720]",
            "1080": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
            "2160": "bestvideo[height<=2160]+bestaudio/best[height<=2160]",
        }
        format_string = resolution_map.get(quality, resolution_map["480"])
        command += ["-f", format_string, "--merge-output-format", "mp4"]
    print(f"Download folder: {folder}")
    try:
        subprocess.run(command, check=True)
        print("Playlist download complete.")
    except subprocess.CalledProcessError as e:
        print(f"yt-dlp error: {e}")

def main():
    print("==== YouTube to MP3/MP4 Downloader ====")
    print("1. Single Video")
    print("2. Playlist")
    choice = input("Enter choice (1 or 2): ").strip()
    url = input("Enter YouTube video/playlist URL: ").strip()
    url = sanitize_url(url)

    format_choice = input("Choose format - mp3 or mp4: ").strip().lower()
    if format_choice == "mp3":
        bitrate = input("Enter MP3 bitrate (192, 256, 320) [default 192]: ").strip()
        if bitrate not in ['192', '256', '320']:
            print("Invalid bitrate. Defaulting to 192kbps.")
            bitrate = '192'
        quality = bitrate
    elif format_choice == "mp4":
        resolution = input("Enter video resolution (480, 720, 1080, 2160) [default 480]: ").strip()
        if resolution not in ['480', '720', '1080', '2160']:
            print("Invalid resolution. Defaulting to 480p.")
            resolution = '480'
        quality = resolution
    else:
        print("Invalid format. Exiting.")
        return

    folder = get_downloads_folder()
    print(f"Download folder: {folder}")

    if choice == "1":
        download_youtube_media(url, folder, format_choice, quality)
    elif choice == "2":
        download_playlist(url, folder, format_choice, quality)
    else:
        print("Invalid choice! Exiting.")

if __name__ == "__main__":
    main()
