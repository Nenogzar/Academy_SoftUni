import tkinter as tk
from tkinter import ttk
from urllib import request

class ImageSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Search App")

        self.search_label = ttk.Label(root, text="Enter image URL:")
        self.search_label.pack(pady=5)

        self.search_entry = ttk.Entry(root, width=30)
        self.search_entry.pack(pady=5)

        self.search_button_google = ttk.Button(root, text="Search (Google)", command=lambda: self.search_images("google"))
        self.search_button_google.pack(pady=5)

        self.search_button_bing = ttk.Button(root, text="Search (Bing)", command=lambda: self.search_images("bing"))
        self.search_button_bing.pack(pady=5)

        self.search_button_tineye = ttk.Button(root, text="Search (TinEye)", command=lambda: self.search_images("tineye"))
        self.search_button_tineye.pack(pady=5)

        self.result_text = tk.Text(root, wrap="word", width=50, height=10)
        self.result_text.pack(pady=5)

    def search_images(self, engine):
        query = self.search_entry.get()
        if query:
            if engine == "google":
                url = f"https://www.google.com/searchbyimage?image_url={query}"
            elif engine == "bing":
                url = f"https://www.bing.com/images/searchbyimage?url={query}"
            elif engine == "tineye":
                url = f"https://www.tineye.com/search/?url={query}"

            # Отваряме URL адреса
            request.urlopen(url)
        else:
            self.result_text.insert(tk.END, "Please enter an image URL.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSearchApp(root)
    root.mainloop()
