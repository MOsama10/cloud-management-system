import tkinter as tk
from tkinter import simpledialog, messagebox
import os

def create_dockerfile():
    try:
        path = simpledialog.askstring("Dockerfile Path", "Enter path to save Dockerfile (e.g., C:\\\\docker\\\\Dockerfile):")
        if not path:
            return messagebox.showerror("Error", "No path provided.")

        content = simpledialog.askstring("Dockerfile Content", "Enter Dockerfile content (e.g., FROM python:3.9):")
        if not content:
            return messagebox.showerror("Error", "No content provided.")

        with open(path, "w") as f:
            f.write(content)

        messagebox.showinfo("Success", f"Dockerfile created at:\n{path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create Dockerfile:\n{e}")
