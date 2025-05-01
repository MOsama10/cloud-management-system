import subprocess
from tkinter import simpledialog, messagebox

def pull_docker_image():
    try:
        image_name = simpledialog.askstring("Pull Image", "Enter full image name (e.g., python:3.9):")
        if not image_name:
            return messagebox.showerror("Error", "No image name provided.")

        subprocess.run(["docker", "pull", image_name], check=True)
        messagebox.showinfo("Success", f"Image '{image_name}' pulled successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to pull image:\n{e}")
 
