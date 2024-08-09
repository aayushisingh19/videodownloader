import streamlit as st
import os
import yt_dlp as youtube_dl

def download_video(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Download complete!"
    except Exception as e:
        return f"An error occurred: {e}"


# Streamlit UI
st.title("YouTube Video Downloader")

# Input field for the YouTube video URL
url = st.text_input("Enter the YouTube video URL:")

if url:
    # Folder to save the downloaded videos
    save_path = 'downloads/'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    if st.button("Download Video"):
        video_title = download_video(url, save_path)
        
        if video_title:
            st.success(f"Downloaded: {video_title}")
            st.info(f"Saved to: {save_path}")
