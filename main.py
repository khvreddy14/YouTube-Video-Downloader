import os
import tkinter as tk
from tkinter import ttk, messagebox
import yt_dlp

DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

def download_video():
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        progress_label.config(text="Downloading...")

        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(
                DOWNLOAD_FOLDER,
                '%(title)s.%(ext)s'
            )
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        progress_label.config(text="Download Complete!")
        messagebox.showinfo("Success", "Video downloaded successfully!")

    except Exception as e:
        progress_label.config(text="Download Failed!")
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("600x300")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="YouTube Video Downloader",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

url_label = tk.Label(
    root,
    text="Enter YouTube URL:"
)
url_label.pack()

url_entry = tk.Entry(
    root,
    width=60
)
url_entry.pack(pady=10)

download_button = ttk.Button(
    root,
    text="Download",
    command=download_video
)
download_button.pack(pady=15)

progress_label = tk.Label(
    root,
    text="Waiting for URL..."
)
progress_label.pack(pady=10)

root.mainloop()