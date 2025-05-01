import subprocess
from tkinter import messagebox

def list_running_containers():
    try:
        result = subprocess.run(["docker", "ps"], capture_output=True, text=True, check=True)
        if result.stdout.strip():
            messagebox.showinfo("Running Containers", result.stdout)
        else:
            messagebox.showinfo("Running Containers", "No containers are currently running.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to list running containers:\n{e}")
 
