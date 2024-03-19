# import tkinter as tk
# from tkinter import messagebox
# from youtube_search import YoutubeSearch
# from pytube import YouTube
# import cv2
# from PIL import Image, ImageTk
#
# class YouTubePlayer:
#     def __init__(self, root):
#         self.root = root
#         self.video_urls = {}
#
#         # Color Palette
#         self.bg_color = "#336699"
#         self.button_color = "#4CAF50"
#         self.text_color = "white"
#
#         # Main Frame
#         self.main_frame = tk.Frame(root, bg=self.bg_color)
#         self.main_frame.pack(fill="both", expand=True)
#
#         # Title Label
#         self.title_label = tk.Label(self.main_frame, text="NENOGZAR YOUTUBE VIDEO PLAYER", font=("Arial", 24, "bold"),
#                                     fg=self.text_color, bg=self.bg_color)
#         self.title_label.pack(pady=10)
#
#         # Search Frame
#         self.search_frame = tk.Frame(self.main_frame, bg=self.bg_color)
#         self.search_frame.pack(fill="x")
#
#         # Search Entry
#         self.search_entry = tk.Entry(self.search_frame)
#         self.search_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)
#
#         # Search Button
#         self.search_button = tk.Button(self.search_frame, text="Search YouTube", command=self.search_and_play,
#                                        bg=self.button_color, fg=self.text_color)
#         self.search_button.pack(side="left", padx=5, pady=5)
#
#         # List Frame
#         self.list_frame = tk.Frame(self.main_frame, bg=self.bg_color)
#         self.list_frame.pack(side="left", fill="both", expand=False)
#
#         # Video Listbox
#         self.lst = tk.Listbox(self.list_frame, width=45, height=20, bg=self.bg_color, fg=self.text_color)
#         self.lst.pack(side="left", fill="both", expand=True)
#
#         # Scrollbar
#         self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical", command=self.lst.yview)
#         self.scrollbar.pack(side="right", fill="y")
#         self.lst.config(yscrollcommand=self.scrollbar.set)
#
#         # Button Frame
#         self.button_frame = tk.Frame(self.main_frame, bg=self.bg_color)
#         self.button_frame.pack(side="bottom", fill="x")
#
#         # Play Button
#         self.play_button = tk.Button(self.button_frame, text="Play", command=self.play_video, bg=self.button_color,
#                                      fg=self.text_color)
#         self.play_button.pack(side="left", padx=5, pady=5)
#
#         # Stop Button
#         self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_video, bg=self.button_color,
#                                      fg=self.text_color)
#         self.stop_button.pack(side="left", padx=5, pady=5)
#
#         # Current Video Label
#         self.current_video_label = tk.Label(root, text="No video selected", bg=self.bg_color, fg=self.text_color)
#         self.current_video_label.pack(pady=5)
#
#         # Bindings
#         self.lst.bind("<<ListboxSelect>>", self.show_video)
#
#     def search_and_play(self):
#         query = self.search_entry.get()
#         search_results = YoutubeSearch(query, max_results=5).to_dict()
#         if search_results:
#             self.lst.delete(0, tk.END)
#             for result in search_results:
#                 video_title = result['title']
#                 video_url = 'https://www.youtube.com' + result['url_suffix']
#                 self.lst.insert(tk.END, video_title)
#                 self.video_urls[video_title] = video_url  # Store title and URL in dictionary
#             self.save_results()  # Save updated list of videos
#
#     def play_video(self):
#         if self.lst.curselection():
#             title = self.lst.get(self.lst.curselection())
#             video_url = self.video_urls.get(title)  # Get URL from dictionary
#             print("Playing video:", video_url)  # Print URL for debugging
#
#             # Load the video with pytube
#             yt = YouTube(video_url)
#             stream = yt.streams.first()  # Get the first available stream
#
#             # Download the video
#             stream.download(filename="temp_video.mp4")
#
#             # Play the video using OpenCV
#             cap = cv2.VideoCapture("temp_video.mp4")
#
#             # Function to update the video frames
#             def update():
#                 ret, frame = cap.read()
#                 if ret:
#                     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                     frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
#                     video_label.config(image=frame)
#                     video_label.image = frame
#                     video_label.after(30, update)
#                 else:
#                     cap.release()
#                     video_label.destroy()
#
#             # Create a label to display the video
#             video_label = tk.Label(self.root)
#             video_label.pack()
#
#             # Start updating the video frames
#             update()
#
#             self.current_video_label.config(text=f"Playing: {title}")
#         else:
#             print("No video selected.")
#
#     def stop_video(self):
#         self.current_video_label.config(text="Video stopped")
#
#     def save_results(self):
#         with open("YouTube_list.txt", "a") as file:
#             for title, url in self.video_urls.items():
#                 file.write(f"{title}: {url}\n")
#
#     def show_video(self, event):
#         pass
#
# root = tk.Tk()
# root.geometry("800x600+300+50")
# root.title("NENOGZAR YouTube Player")
# root.configure(bg="#336699")
# video_player = YouTubePlayer(root)
# root.mainloop()
#

import tkinter as tk
from youtube_search import YoutubeSearch
from pytube import YouTube
import cv2
from PIL import Image, ImageTk


class YouTubePlayer:
    def __init__(self, root):
        self.root = root
        self.video_urls = {}
        self.bg_color = "#336699"
        self.button_color = "#4CAF50"
        self.text_color = "white"
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill="both", expand=True)
        self.title_label = tk.Label(self.main_frame, text="NENOGZAR YOUTUBE VIDEO PLAYER", font=("Arial", 24, "bold"),
                                    fg=self.text_color, bg=self.bg_color)
        self.title_label.pack(pady=10)
        self.search_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.search_frame.pack(fill="x")
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)
        self.search_button = tk.Button(self.search_frame, text="Search YouTube", command=self.search_and_play,
                                       bg=self.button_color, fg=self.text_color)
        self.search_button.pack(side="left", padx=5, pady=5)
        self.list_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.list_frame.pack(side="left", fill="both", expand=False)
        self.lst = tk.Listbox(self.list_frame, width=45, height=20, bg=self.bg_color, fg=self.text_color)
        self.lst.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical", command=self.lst.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.lst.config(yscrollcommand=self.scrollbar.set)
        self.button_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.button_frame.pack(side="bottom", fill="x")
        self.play_button = tk.Button(self.button_frame, text="Play", command=self.play_video, bg=self.button_color,
                                     fg=self.text_color)
        self.play_button.pack(side="left", padx=5, pady=5)
        self.pause_button = tk.Button(self.button_frame, text="Pause", command=self.pause_video, bg=self.button_color,
                                      fg=self.text_color)
        self.pause_button.pack(side="left", padx=5, pady=5)
        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_video, bg=self.button_color,
                                     fg=self.text_color)
        self.stop_button.pack(side="left", padx=5, pady=5)
        self.current_video_label = tk.Label(root, text="No video selected", bg=self.bg_color, fg=self.text_color)
        self.current_video_label.pack(pady=5)
        self.video_label = tk.Label(root)
        self.video_label.pack()
        self.cap = None
        self.paused = False
        self.lst.bind("<<ListboxSelect>>", self.show_video)

    def search_and_play(self):
        query = self.search_entry.get()
        search_results = YoutubeSearch(query, max_results=5).to_dict()
        if search_results:
            self.lst.delete(0, tk.END)
            for result in search_results:
                video_title = result['title']
                video_url = 'https://www.youtube.com' + result['url_suffix']
                self.lst.insert(tk.END, video_title)
                self.video_urls[video_title] = video_url
            self.save_results()

    def play_video(self):
        if self.lst.curselection():
            title = self.lst.get(self.lst.curselection())
            video_url = self.video_urls.get(title)
            yt = YouTube(video_url)
            stream = yt.streams.first()
            stream.download(filename="temp_video.mp4")
            self.cap = cv2.VideoCapture("temp_video.mp4")
            self.update()
            self.current_video_label.config(text=f"Playing: {title}")
        else:
            print("No video selected.")

    def pause_video(self):
        if self.cap is not None:
            if self.paused:
                self.paused = False
            else:
                self.paused = True

    def stop_video(self):
        if self.cap is not None:
            self.cap.release()
            self.video_label.destroy()
            self.current_video_label.config(text="Video stopped")

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            if not self.paused:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.video_label.config(image=frame)
                self.video_label.image = frame
        else:
            self.cap.release()
            self.video_label.destroy()
            self.current_video_label.config(text="Video stopped")
        self.root.after(30, self.update)

    def save_results(self):
        with open("YouTube_list.txt", "a") as file:
            for title, url in self.video_urls.items():
                file.write(f"{title}: {url}\n")

    def show_video(self, event):
        pass


root = tk.Tk()
root.geometry("800x600+300+50")
root.title("NENOGZAR YouTube Player")
root.configure(bg="#336699")
video_player = YouTubePlayer(root)
root.mainloop()
