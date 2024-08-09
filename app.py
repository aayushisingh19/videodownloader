import streamlit as st
import os
import yt_dlp as youtube_dl
import base64

def download_video(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', None)
            video_filename = ydl.prepare_filename(info_dict)
        return video_title, video_filename
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

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
        video_title, video_filename = download_video(url, save_path)
        
        if video_title:
            st.success(f"Downloaded: {video_title}")
            st.info(f"Saved to: {save_path}")

            # Provide a download link
            with open(video_filename, "rb") as file:
                btn = st.download_button(
                    label="Click here to download",
                    data=file,
                    file_name=os.path.basename(video_filename),
                    mime="video/mp4"
                )
        else:
            st.error("Failed to download the video.")
