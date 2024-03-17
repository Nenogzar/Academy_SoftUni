import tkinter as tk
import vlc
from youtube_search import YoutubeSearch
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.instance = vlc.Instance('--no-xlib')  # Create a VLC instance
        self.player = self.instance.media_player_new()  # Create a media player
        self.video_urls = {}  # Initialize video URL dictionary

        # Color Palette
        self.bg_color = "#336699"
        self.button_color = "#4CAF50"
        self.text_color = "white"

        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill="both", expand=True)

        self.title_label = tk.Label(self.main_frame, text="VIDEO PLAYER", font=("Arial", 24, "bold"), fg=self.text_color, bg=self.bg_color)
        self.title_label.pack(pady=10)

        self.search_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.search_frame.pack(fill="x")

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.search_button = tk.Button(self.search_frame, text="Search YouTube", command=self.search_and_play, bg=self.button_color, fg=self.text_color)
        self.search_button.pack(side="left", padx=5, pady=5)

        self.save_button = tk.Button(self.search_frame, text="Save", command=self.save_results, bg=self.button_color, fg=self.text_color)
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

        self.play_button = tk.Button(self.button_frame, text="Play", command=self.play_video, bg=self.button_color, fg=self.text_color)
        self.play_button.pack(side="left", padx=5, pady=5)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_video, bg=self.button_color, fg=self.text_color)
        self.stop_button.pack(side="left", padx=5, pady=5)

        self.current_video_label = tk.Label(root, text="No video selected", bg=self.bg_color, fg=self.text_color)
        self.current_video_label.pack(pady=5)

        self.player_frame = tk.Frame(self.main_frame)
        self.player_frame.pack(side="right", fill="both", expand=True)

        self.lst.bind("<<ListboxSelect>>", self.show_video)

        # Load saved video list when the application starts
        self.load_saved_results()

    def search_and_play(self):
        query = self.search_entry.get()
        search_results = YoutubeSearch(query, max_results=5).to_dict()
        if search_results:
            self.lst.delete(0, tk.END)
            for result in search_results:
                video_title = result['title']
                video_url = 'https://www.youtube.com' + result['url_suffix']
                self.lst.insert(tk.END, video_title)
                self.video_urls[video_title] = video_url  # Store title and URL in dictionary
            self.save_results()  # Save updated list of videos

    def play_video(self):
        if self.lst.curselection():
            title = self.lst.get(self.lst.curselection())
            video_url = self.video_urls.get(title)  # Get URL from dictionary
            print("Playing video:", video_url)  # Print URL for debugging

            try:
                # Use pytube to get the video URL
                yt = YouTube(video_url)
                video_url = yt.streams.filter(progressive=True, file_extension='mp4').first().url

                media = self.instance.media_new(video_url)
                self.player.set_media(media)
                self.player.set_hwnd(self.player_frame.winfo_id())
                self.player.play()
                self.current_video_label.config(text=f"Playing: {title}")
            except AgeRestrictedError as e:
                print("Age restricted video:", e)
                self.current_video_label.config(text="This video is age-restricted.")
            except Exception as e:
                print("Error:", e)
                self.current_video_label.config(text="An error occurred while playing the video.")
        else:
            print("No video selected.")

    def stop_video(self):
        self.player.stop()
        self.current_video_label.config(text="Video stopped")

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
        # Add implementation to show the selected video
        pass

root = tk.Tk()
root.geometry("800x600+300+50")
root.title("VLC Player")
root.configure(bg="#336699")
video_player = VideoPlayer(root)
root.mainloop()
