# import tkinter as tk
# from tkinter import simpledialog, messagebox
# import subprocess
# import json
# import os

# def create_vm():
#     def run_vm(config):
#         try:
#             command = [
#                 "qemu-system-x86_64",
#                 "-m", str(config["memory"]),
#                 "-smp", str(config["cpu"]),
#                 "-hda", config["disk"]
#             ]
#             subprocess.run(command, check=True)
#             messagebox.showinfo("Success", "VM started successfully.")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to start VM:\n{e}")

#     choice = messagebox.askquestion("Input Method", "Use config file?\nClick 'Yes' for file, 'No' for manual input.")

#     if choice == "yes":
#         filepath = simpledialog.askstring("Config File", "Enter full path to JSON config file:")
#         if filepath and os.path.exists(filepath):
#             with open(filepath, "r") as f:
#                 config = json.load(f)
#                 run_vm(config)
#         else:
#             messagebox.showerror("Error", "Invalid file path.")
#     else:
#         try:
#             cpu = simpledialog.askinteger("CPU", "Enter number of CPUs:")
#             memory = simpledialog.askinteger("Memory", "Enter RAM (in MB):")
#             disk = simpledialog.askstring("Disk", "Enter path to disk image (e.g., C:\\\\vm\\\\disk.img):")
#             config = {"cpu": cpu, "memory": memory, "disk": disk}
#             run_vm(config)
#         except Exception as e:
#             messagebox.showerror("Error", f"Input error:\n{e}")
# Modified module: vm_manager.py
# This enhanced version uses the new dialog classes from main.py

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import json
import os

# Import dialogs from main if available, otherwise define them here
try:
    from main import modern_askstring, modern_text_input
except ImportError:
    # Define fallback dialog classes if main module is not available
    class ModernInputDialog(tk.Toplevel):
        def __init__(self, parent, title, prompt, show=None):
            super().__init__(parent)
            self.title(title)
            self.result = None
            self.geometry("400x150")
            self.minsize(400, 150)
            
            self.configure(bg="#f0f0f0")
            
            # Make dialog modal
            self.transient(parent)
            self.grab_set()
            
            # Create a frame for the label and entry widget
            frame = ttk.Frame(self, padding="20")
            frame.pack(fill=tk.BOTH, expand=True)
            
            # Label
            ttk.Label(frame, text=prompt, wraplength=360).pack(pady=(0, 10), anchor="w")
            
            # Entry widget
            self.entry = ttk.Entry(frame, width=50, show=show)
            self.entry.pack(fill=tk.X, pady=(0, 20))
            self.entry.focus_set()
            
            # Button frame
            button_frame = ttk.Frame(frame)
            button_frame.pack(fill=tk.X)
            
            # Cancel and OK buttons
            ttk.Button(button_frame, text="Cancel", command=self.cancel).pack(side=tk.RIGHT, padx=5)
            ttk.Button(button_frame, text="OK", command=self.ok, style="Accent.TButton").pack(side=tk.RIGHT)
            
            # Handle window close
            self.protocol("WM_DELETE_WINDOW", self.cancel)
            
            # Enter key binding
            self.entry.bind("<Return>", lambda event: self.ok())
            
            # Position the dialog
            self.center_window()
            
            # Wait for the window to appear
            self.wait_visibility()
            
            # Wait for the window to be destroyed
            self.wait_window()
        
        def center_window(self):
            """Center the dialog window on the screen."""
            self.update_idletasks()
            width = self.winfo_width()
            height = self.winfo_height()
            x = (self.winfo_screenwidth() // 2) - (width // 2)
            y = (self.winfo_screenheight() // 2) - (height // 2)
            self.geometry(f"{width}x{height}+{x}+{y}")
        
        def ok(self):
            """Process the OK button click."""
            self.result = self.entry.get()
            self.destroy()
        
        def cancel(self):
            """Process the Cancel button click."""
            self.result = None
            self.destroy()
    
    def modern_askstring(parent, title, prompt, **kwargs):
        """Modern replacement for simpledialog.askstring."""
        dialog = ModernInputDialog(parent, title, prompt, **kwargs)
        return dialog.result

    # Note: For brevity, I'm not including the TextDialog class here
    # In a real implementation, you would want to import it or define it fully

    def modern_text_input(parent, title, prompt="", **kwargs):
        """Fallback for text input - uses askstring in this case."""
        return modern_askstring(parent, title, prompt, **kwargs)

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

    # Get the parent window
    parent = tk._default_root

    choice = messagebox.askquestion("Input Method", "Use config file?\nClick 'Yes' for file, 'No' for manual input.")

    if choice == "yes":
        filepath = modern_askstring(parent, "Config File", "Enter full path to JSON config file:")
        if filepath and os.path.exists(filepath):
            with open(filepath, "r") as f:
                config = json.load(f)
                run_vm(config)
        else:
            messagebox.showerror("Error", "Invalid file path.")
    else:
        try:
            cpu = int(modern_askstring(parent, "CPU", "Enter number of CPUs:") or 0)
            memory = int(modern_askstring(parent, "Memory", "Enter RAM (in MB):") or 0)
            disk = modern_askstring(parent, "Disk", "Enter path to disk image (e.g., C:\\\\vm\\\\disk.img):")
            
            if not cpu or not memory or not disk:
                return messagebox.showerror("Error", "All fields are required.")
                
            config = {"cpu": cpu, "memory": memory, "disk": disk}
            run_vm(config)
        except ValueError:
            messagebox.showerror("Error", "CPU and Memory must be numeric values.")
        except Exception as e:
            messagebox.showerror("Error", f"Input error:\n{e}")

# Example of enhancing one of the other modules (container_stopper.py)
# The same pattern can be applied to all other modules

def stop_container():
    try:
        # Get the parent window
        parent = tk._default_root
        
        container_id = modern_askstring(parent, "Stop Container", "Enter container ID or name:")
        if not container_id:
            return messagebox.showerror("Error", "No container ID provided.")

        subprocess.run(["docker", "stop", container_id], check=True)
        messagebox.showinfo("Success", f"Container '{container_id}' stopped successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to stop container:\n{e}")
