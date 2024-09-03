import yt_dlp
import os

def download_highest_quality_audio(url, download_path):
    ydl_opts = {
        'format': 'bestaudio/best',  # Select the best available audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to mp3 format
            'preferredquality': '320',  # Set the quality to 320 kbps, which is the highest for mp3
        }],
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Save the file to the specified directory
        'noplaylist': True,  # Download only a single video (not a playlist)
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter path to download:")
    # Validate the download path
    if not os.path.exists(download_path):
        print(f"The path '{download_path}' does not exist. Please enter a valid path.")
    else:
        download_highest_quality_audio(video_url, download_path)
