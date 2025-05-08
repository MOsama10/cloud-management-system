def list_running_containers(parent=None):
    """
    List all running Docker containers.
    
    Args:
        parent: The parent window
    """
    import subprocess
    from tkinter import messagebox
    
    try:
        result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
        
        if result.returncode == 0:
            # Format the output nicely
            output = result.stdout.strip()
            
            # Display output in the output text widget if available
            if hasattr(parent, "update_output"):
                parent.update_output(output)
                
            if output:
                messagebox.showinfo("Running Containers", output)
            else:
                messagebox.showinfo("Running Containers", "No containers are currently running.")
        else:
            error_message = result.stderr.strip()
            if hasattr(parent, "update_output"):
                parent.update_output(f"Error listing containers:\n\n{error_message}")
            messagebox.showerror("Error", f"Failed to list running containers:\n{error_message}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to list running containers:\n{e}")
