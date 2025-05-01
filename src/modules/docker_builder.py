import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import os

def build_docker_image():
    try:
        dockerfile_dir = simpledialog.askstring("Dockerfile Directory", "Enter directory path containing Dockerfile:")
        if not dockerfile_dir or not os.path.isdir(dockerfile_dir):
            return messagebox.showerror("Error", "Invalid directory.")

        image_name = simpledialog.askstring("Image Name", "Enter image name (e.g., myimage):")
        tag = simpledialog.askstring("Image Tag", "Enter tag (e.g., latest):")

        full_tag = f"{image_name}:{tag}" if tag else image_name
        command = ["docker", "build", "-t", full_tag, dockerfile_dir]

        subprocess.run(command, check=True)
        messagebox.showinfo("Success", f"Docker image '{full_tag}' built successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to build image:\n{e}")
