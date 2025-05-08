
def stop_container(parent=None, modern_askstring=None):
    """
    Stop a running Docker container.
    
    Args:
        parent: The parent window for dialogs
        modern_askstring: Function to display modern string input dialog
    """
    import subprocess
    from tkinter import messagebox
    
    # Use default dialogs if custom ones aren't provided
    if modern_askstring is None:
        from tkinter import simpledialog
        modern_askstring = simpledialog.askstring
    
    if parent is None:
        import tkinter as tk
        parent = tk._default_root
    
    try:
        container_id = modern_askstring(parent, "Stop Container", "Enter container ID or name:")
        if not container_id:
            return
        
        result = subprocess.run(["docker", "stop", container_id], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            # If there's an update_output function available, use it
            if hasattr(parent, "update_output"):
                parent.update_output(f"Container '{container_id}' stopped successfully.\n\n{result.stdout}")
            messagebox.showinfo("Success", f"Container '{container_id}' stopped successfully.")
        else:
            # If there's an update_output function available, use it
            if hasattr(parent, "update_output"):
                parent.update_output(f"Failed to stop container '{container_id}':\n\n{result.stderr}")
            messagebox.showerror("Error", f"Failed to stop container:\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to stop container:\n{e}")
