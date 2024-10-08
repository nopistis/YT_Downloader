from pytube import YouTube
import yt_dlp as youtube_dl
import os


def download_with_pytube(url, output_path):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()

        if not video_stream:
            raise Exception("No suitable video stream found.")

        print(f"Downloading '{yt.title}' with pytube...")
        video_stream.download(output_path)
        print("Download completed successfully with pytube!")
        return True

    except Exception as e:
        print(f"An error occurred with pytube: {e}")
        return False


def download_with_youtube_dl(url, output_path):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(output_path, 'downloaded_video.%(ext)s'),  # Custom filename
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'postprocessor_args': [
                '-c:v', 'copy',
                '-c:a', 'copy',
            ],
            'nopart': True,  # Disable creating temporary .part files
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading '{url}' with yt-dlp...")
            ydl.download([url])

        print("Download completed successfully with yt-dlp!")
        return True

    except Exception as e:
        print(f"An error occurred with yt-dlp: {e}")
        return False

    
def download_youtube_video(url, output_path="."):
    if not download_with_pytube(url, output_path):
        if not download_with_youtube_dl(url, output_path):
            print("Both pytube and yt-dlp failed to download the video.")
        else:
            print("Downloaded with yt-dlp as a fallback.")
    else:
        print("Downloaded with pytube.")


a = input("Enter URL:")
b = input("Enter path to download")

download_youtube_video(a, b)
