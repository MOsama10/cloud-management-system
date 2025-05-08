import tkinter as tk
from tkinter import messagebox
import subprocess
import json
import os

def create_vm(parent=None, modern_askstring=None, modern_text_input=None):
    """
    Create and run a virtual machine using QEMU.
    
    Args:
        parent: The parent window for dialogs
        modern_askstring: Function to display modern string input dialog
        modern_text_input: Function to display modern text input dialog
    """
    # Use default dialogs if custom ones aren't provided
    if modern_askstring is None:
        from tkinter import simpledialog
        modern_askstring = simpledialog.askstring
    
    if parent is None:
        parent = tk._default_root
    
    def run_vm(config):
        try:
            command = [
                "qemu-system-x86_64",
                "-m", str(config["memory"]),
                "-smp", str(config["cpu"]),
                "-hda", config["disk"]
            ]
            
            # Optional: Add output to the application's output area if available
            try:
                result = subprocess.run(command, capture_output=True, text=True, check=True)
                # If there's an update_output function available, use it
                if hasattr(parent, "update_output"):
                    parent.update_output(f"VM started with configuration:\nCPU: {config['cpu']}\nMemory: {config['memory']} MB\nDisk: {config['disk']}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to start VM:\n{e}")
                return
                
            messagebox.showinfo("Success", "VM started successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start VM:\n{e}")

    choice = messagebox.askquestion("Input Method", "Use config file?\nClick 'Yes' for file, 'No' for manual input.")

    if choice == "yes":
        filepath = modern_askstring(parent, "Config File", "Enter full path to JSON config file:")
        if filepath and os.path.exists(filepath):
            try:
                with open(filepath, "r") as f:
                    config = json.load(f)
                    # Validate required fields
                    if not all(key in config for key in ["cpu", "memory", "disk"]):
                        messagebox.showerror("Error", "Config file missing required fields (cpu, memory, disk)")
                        return
                    run_vm(config)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Invalid JSON format in config file.")
            except Exception as e:
                messagebox.showerror("Error", f"Error reading config file:\n{e}")
        else:
            messagebox.showerror("Error", "Invalid file path.")
    else:
        try:
            # Get VM parameters from user
            cpu_input = modern_askstring(parent, "CPU", "Enter number of CPUs:")
            if not cpu_input:
                return
            
            memory_input = modern_askstring(parent, "Memory", "Enter RAM (in MB):")
            if not memory_input:
                return
                
            disk = modern_askstring(parent, "Disk", "Enter path to disk image (e.g., C:\\vm\\disk.img):")
            if not disk:
                return
                
            # Convert and validate input
            try:
                cpu = int(cpu_input)
                memory = int(memory_input)
                
                if cpu <= 0 or memory <= 0:
                    raise ValueError("CPU and Memory must be positive values")
                    
                config = {"cpu": cpu, "memory": memory, "disk": disk}
                run_vm(config)
                
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid input: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Input error:\n{e}")
