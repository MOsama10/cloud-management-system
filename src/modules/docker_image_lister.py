import subprocess
from tkinter import messagebox

def list_docker_images():
    try:
        result = subprocess.run(["docker", "images"], capture_output=True, text=True, check=True)
        if result.stdout.strip():
            messagebox.showinfo("Docker Images", result.stdout)
        else:
            messagebox.showinfo("Docker Images", "No Docker images found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to list Docker images:\n{e}")
