def pull_docker_image(parent=None, modern_askstring=None):
    """
    Pull a Docker image from DockerHub.
    
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
        image_name = modern_askstring(parent, "Pull Image", "Enter full image name (e.g., python:3.9):")
        if not image_name:
            return
        
        # Show a message that pulling is in progress
        if hasattr(parent, "update_output"):
            parent.update_output(f"Pulling Docker image '{image_name}'...\nThis may take a few moments.")
        
        result = subprocess.run(["docker", "pull", image_name], capture_output=True, text=True)
        
        if result.returncode == 0:
            # Show success message in output area
            if hasattr(parent, "update_output"):
                parent.update_output(f"Image '{image_name}' pulled successfully.\n\n{result.stdout}")
            messagebox.showinfo("Success", f"Image '{image_name}' pulled successfully.")
        else:
            # Show error in output area
            if hasattr(parent, "update_output"):
                parent.update_output(f"Failed to pull image '{image_name}':\n\n{result.stderr}")
            messagebox.showerror("Error", f"Failed to pull image:\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to pull image:\n{e}")
