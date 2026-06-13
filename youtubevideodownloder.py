import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video():
    url = url_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Video downloaded successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x200")

title_label = tk.Label(root, text="YouTube Video Downloader", font=("Arial", 16))
title_label.pack(pady=10)

url_label = tk.Label(root, text="Enter Video URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_btn = tk.Button(root, text="Download", command=download_video)
download_btn.pack(pady=20)

root.mainloop()