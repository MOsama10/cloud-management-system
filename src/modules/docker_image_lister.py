def list_docker_images(parent=None):
    """
    List all Docker images on the system.
    
    Args:
        parent: The parent window
    """
    import subprocess
    from tkinter import messagebox
    
    try:
        result = subprocess.run(["docker", "images"], capture_output=True, text=True)
        
        if result.returncode == 0:
            output = result.stdout.strip()
            
            # Display output in the output text widget if available
            if hasattr(parent, "update_output"):
                parent.update_output(output)
                
            if output:
                messagebox.showinfo("Docker Images", output)
            else:
                messagebox.showinfo("Docker Images", "No Docker images found.")
        else:
            error_message = result.stderr.strip()
            if hasattr(parent, "update_output"):
                parent.update_output(f"Error listing Docker images:\n\n{error_message}")
            messagebox.showerror("Error", f"Failed to list Docker images:\n{error_message}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to list Docker images:\n{e}")
