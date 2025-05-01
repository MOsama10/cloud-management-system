import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import json
import os

def create_vm():
    def run_vm(config):
        try:
            command = [
                "qemu-system-x86_64",
                "-m", str(config["memory"]),
                "-smp", str(config["cpu"]),
                "-hda", config["disk"]
            ]
            subprocess.run(command, check=True)
            messagebox.showinfo("Success", "VM started successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start VM:\n{e}")

    choice = messagebox.askquestion("Input Method", "Use config file?\nClick 'Yes' for file, 'No' for manual input.")

    if choice == "yes":
        filepath = simpledialog.askstring("Config File", "Enter full path to JSON config file:")
        if filepath and os.path.exists(filepath):
            with open(filepath, "r") as f:
                config = json.load(f)
                run_vm(config)
        else:
            messagebox.showerror("Error", "Invalid file path.")
    else:
        try:
            cpu = simpledialog.askinteger("CPU", "Enter number of CPUs:")
            memory = simpledialog.askinteger("Memory", "Enter RAM (in MB):")
            disk = simpledialog.askstring("Disk", "Enter path to disk image (e.g., C:\\\\vm\\\\disk.img):")
            config = {"cpu": cpu, "memory": memory, "disk": disk}
            run_vm(config)
        except Exception as e:
            messagebox.showerror("Error", f"Input error:\n{e}")
