import subprocess
from tkinter import simpledialog, messagebox

def search_local_image():
    try:
        keyword = simpledialog.askstring("Search Image", "Enter image name or tag to search:")
        if not keyword:
            return messagebox.showerror("Error", "No image name provided.")

        result = subprocess.run(["docker", "images"], capture_output=True, text=True, check=True)
        matches = [line for line in result.stdout.splitlines() if keyword.lower() in line.lower()]
        
        if matches:
            messagebox.showinfo("Search Results", "\n".join(matches))
        else:
            messagebox.showinfo("Search Results", f"No images found for: {keyword}")
    except Exception as e:
        messagebox.showerror("Error", f"Search failed:\n{e}")
 
