import tkinter as tk
import os
import webbrowser
from youtube_srch import YoutubeSearch
from pytube import YouTube

class YouTubePlayer:
    def __init__(self, root):
        self.root = root
        self.video_urls = {}

        # Color Palette
        self.bg_color = "#336699"
        self.button_color = "#4CAF50"
        self.text_color = "white"

        # Main Frame
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill="both", expand=True)

        # Title Label
        self.title_label = tk.Label(self.main_frame, text="NENOGZAR YOUTUBE VIDEO PLAYER", font=("Arial", 24, "bold"),
                                    fg=self.text_color, bg=self.bg_color)
        self.title_label.pack(pady=10)

        # Search Frame
        self.search_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.search_frame.pack(fill="x")

        # Search Entry
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        # Search Button
        self.search_button = tk.Button(self.search_frame, text="Search YouTube", command=self.search_and_play,
                                       bg=self.button_color, fg=self.text_color)
        self.search_button.pack(side="left", padx=5, pady=5)

        # List Frame
        self.list_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.list_frame.pack(side="left", fill="both", expand=False)

        # Video Listbox
        self.lst = tk.Listbox(self.list_frame, width=45, height=20, bg=self.bg_color, fg=self.text_color)
        self.lst.pack(side="left", fill="both", expand=True)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical", command=self.lst.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.lst.config(yscrollcommand=self.scrollbar.set)

        # Button Frame
        self.button_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.button_frame.pack(side="bottom", fill="x")

        # Play Button
        self.play_button = tk.Button(self.button_frame, text="Play", command=self.play_video, bg=self.button_color,
                                     fg=self.text_color)
        self.play_button.pack(side="left", padx=5, pady=5)

        # Stop Button
        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_video, bg=self.button_color,
                                     fg=self.text_color)
        self.stop_button.pack(side="left", padx=5, pady=5)

        # Current Video Label
        self.current_video_label = tk.Label(root, text="No video selected", bg=self.bg_color, fg=self.text_color)
        self.current_video_label.pack(pady=5)

        # Bindings
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
                self.video_urls[video_title] = video_url  # Store title and URL in dictionary
            self.save_results()  # Save updated list of videos

    def play_video(self):
        if self.lst.curselection():
            title = self.lst.get(self.lst.curselection())
            video_url = self.video_urls.get(title)  # Get URL from dictionary
            print("Playing video:", video_url)  # Print URL for debugging

            webbrowser.open(video_url)
            self.current_video_label.config(text=f"Playing: {title}")
        else:
            print("No video selected.")

    def stop_video(self):
        self.current_video_label.config(text="Video stopped")

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
