import tkinter as tk
from tkinter import messagebox
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from PIL import Image, ImageTk
import io
import requests
import pytube

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.video_urls = {}
        self.current_video = None

        # Color Palette
        self.bg_color = "#336699"
        self.button_color = "#4CAF50"
        self.text_color = "white"

        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill="both", expand=True)

        self.title_label = tk.Label(self.main_frame, text="YOUTUBE VIDEO PLAYER", font=("Arial", 24, "bold"),
                                    fg=self.text_color, bg=self.bg_color)
        self.title_label.pack(pady=10)

        self.search_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.search_frame.pack(fill="x")

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.search_button = tk.Button(self.search_frame, text="Search YouTube", command=self.search_and_play,
                                       bg=self.button_color, fg=self.text_color)
        self.search_button.pack(side="left", padx=5, pady=5)

        self.save_button = tk.Button(self.search_frame, text="Save", command=self.save_results, bg=self.button_color,
                                     fg=self.text_color)
        self.save_button.pack(side="left", padx=5, pady=5)

        self.list_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.list_frame.pack(side="left", fill="both", expand=False)

        self.button_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.button_frame.pack(side="bottom", fill="x")

        self.lst = tk.Listbox(self.list_frame, width=30, height=20, bg=self.bg_color, fg=self.text_color)
        self.lst.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical", command=self.lst.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.lst.config(yscrollcommand=self.scrollbar.set)

        self.play_button = tk.Button(self.button_frame, text="Play", command=self.play_video, bg=self.button_color,
                                     fg=self.text_color)
        self.play_button.pack(side="left", padx=5, pady=5)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_video, bg=self.button_color,
                                     fg=self.text_color)
        self.stop_button.pack(side="left", padx=5, pady=5)

        self.current_video_label = tk.Label(root, text="No video selected", bg=self.bg_color, fg=self.text_color)
        self.current_video_label.pack(pady=5)

        self.player_frame = tk.Frame(self.main_frame)
        self.player_frame.pack(side="right", fill="both", expand=True)

        self.lst.bind("<<ListboxSelect>>", self.show_video)


        self.load_saved_results()

    def search_and_play(self):

        API_KEY = "enter you API cay"

        # Създаване на обект за достъп до YouTube Data API
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        query = self.search_entry.get()
        try:
            search_response = youtube.search().list(
                q=query,
                part='snippet',
                type='video',
                maxResults=5
            ).execute()

            self.lst.delete(0, tk.END)
            self.video_urls.clear()

            for item in search_response['items']:
                video_title = item['snippet']['title']
                video_id = item['id']['videoId']
                video_url = f"https://www.youtube.com/watch?v={video_id}"

                self.lst.insert(tk.END, video_title)
                self.video_urls[video_title] = video_id

        except HttpError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def play_video(self):
        if self.lst.curselection():
            title = self.lst.get(self.lst.curselection())
            video_id = self.video_urls.get(title)  # Get video ID from dictionary
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            self.current_video_label.config(text=f"Playing: {title}")

            try:
                video = pytube.YouTube(video_url)
                stream = video.streams.filter(progressive=True, file_extension='mp4').first()
                video_data = requests.get(stream.url).content
                video_stream = io.BytesIO(video_data)
                video_stream.seek(0)

                self.current_video = Image.open(video_stream)
                self.current_video.thumbnail((640, 480), Image.ANTIALIAS)
                photo_image = ImageTk.PhotoImage(self.current_video)

                video_label = tk.Label(self.player_frame, image=photo_image)
                video_label.image = photo_image
                video_label.pack()

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while playing the video: {e}")

        else:
            messagebox.showerror("Error", "No video selected.")

    def stop_video(self):
        if self.current_video:
            self.current_video_label.config(text="Video stopped")
            for widget in self.player_frame.winfo_children():
                widget.destroy()
        else:
            messagebox.showerror("Error", "No video is currently playing.")

    def save_results(self):
        with open("YouTube_list.txt", "a") as file:  # Append mode to append new results
            for title, url in self.video_urls.items():
                file.write(f"{title}: {url}\n")

    def load_saved_results(self):
        try:
            with open("YouTube_list.txt", "r") as file:
                for line in file:
                    if ':' in line:
                        title, url = line.strip().split(': ', 1)
                        self.video_urls[title] = url
                        self.lst.insert(tk.END, title)
        except FileNotFoundError:
            print("No saved results found.")

    def show_video(self, event):
        pass

root = tk.Tk()
root.geometry("800x600+300+50")
root.title("YouTube Player")
root.configure(bg="#336699")
video_player = VideoPlayer(root)
root.mainloop()
