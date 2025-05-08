def build_docker_image(parent=None, modern_askstring=None):
    """
    Build a Docker image from a Dockerfile.
    
    Args:
        parent: The parent window for dialogs
        modern_askstring: Function to display modern string input dialog
    """
    import subprocess
    import os
    from tkinter import messagebox
    
    # Use default dialogs if custom ones aren't provided
    if modern_askstring is None:
        from tkinter import simpledialog
        modern_askstring = simpledialog.askstring
    
    if parent is None:
        import tkinter as tk
        parent = tk._default_root
    
    try:
        dockerfile_dir = modern_askstring(parent, "Dockerfile Directory", "Enter directory path containing Dockerfile:")
        if not dockerfile_dir:
            return
            
        if not os.path.isdir(dockerfile_dir):
            messagebox.showerror("Error", "Invalid directory.")
            return
            
        if not os.path.isfile(os.path.join(dockerfile_dir, "Dockerfile")):
            messagebox.showerror("Error", "No Dockerfile found in the specified directory.")
            return
    
        image_name = modern_askstring(parent, "Image Name", "Enter image name (e.g., myimage):")
        if not image_name:
            return
                
        tag = modern_askstring(parent, "Image Tag", "Enter tag (e.g., latest):")
        
        full_tag = f"{image_name}:{tag}" if tag else image_name
        command = ["docker", "build", "-t", full_tag, dockerfile_dir]
        
        # Show a message that building is in progress
        if hasattr(parent, "update_output"):
            parent.update_output(f"Building Docker image '{full_tag}'...\nThis may take a few moments.")
        
        # Run the build process
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        
        # Update the output with the result
        if process.returncode == 0:
            if hasattr(parent, "update_output"):
                parent.update_output(f"Docker image '{full_tag}' built successfully.\n\n{stdout}")
            messagebox.showinfo("Success", f"Docker image '{full_tag}' built successfully.")
        else:
            if hasattr(parent, "update_output"):
                parent.update_output(f"Failed to build Docker image:\n\n{stderr}")
            messagebox.showerror("Error", f"Failed to build image. See output for details.")
                
    except Exception as e:
        messagebox.showerror("Error", f"Failed to build image:\n{e}")
