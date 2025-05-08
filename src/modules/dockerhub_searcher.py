def search_dockerhub_image(parent=None, modern_askstring=None):
    """
    Search for a Docker image on DockerHub.
    
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
        image_name = modern_askstring(parent, "Search DockerHub", "Enter image name to search:")
        if not image_name:
            return
        
        # Show a searching message in the output area if available
        if hasattr(parent, "update_output"):
            parent.update_output(f"Searching DockerHub for '{image_name}'...")
        
        result = subprocess.run(["docker", "search", image_name], capture_output=True, text=True)
        
        if result.returncode == 0:
            output = result.stdout.strip()
            
            # Display output in the output text widget if available
            if hasattr(parent, "update_output"):
                if output:
                    parent.update_output(output)
                else:
                    parent.update_output(f"No results found for '{image_name}'.")
                
            if output:
                messagebox.showinfo("DockerHub Search Results", output)
            else:
                messagebox.showinfo("DockerHub Search Results", f"No results found for '{image_name}'.")
        else:
            error_message = result.stderr.strip()
            if hasattr(parent, "update_output"):
                parent.update_output(f"Error searching DockerHub:\n\n{error_message}")
            messagebox.showerror("Error", f"Failed to search DockerHub:\n{error_message}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to search DockerHub:\n{e}")
