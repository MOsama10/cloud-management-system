import subprocess
from tkinter import simpledialog, messagebox

def search_dockerhub_image():
    try:
        image_name = simpledialog.askstring("Search DockerHub", "Enter image name to search:")
        if not image_name:
            return messagebox.showerror("Error", "No image name provided.")

        result = subprocess.run(["docker", "search", image_name], capture_output=True, text=True, check=True)
        if result.stdout.strip():
            messagebox.showinfo("DockerHub Search Results", result.stdout)
        else:
            messagebox.showinfo("DockerHub Search Results", f"No results found for '{image_name}'.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to search DockerHub:\n{e}")
 
