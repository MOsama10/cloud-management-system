import subprocess
from tkinter import simpledialog, messagebox

def stop_container():
    try:
        container_id = simpledialog.askstring("Stop Container", "Enter container ID or name:")
        if not container_id:
            return messagebox.showerror("Error", "No container ID provided.")

        subprocess.run(["docker", "stop", container_id], check=True)
        messagebox.showinfo("Success", f"Container '{container_id}' stopped successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to stop container:\n{e}")
 
