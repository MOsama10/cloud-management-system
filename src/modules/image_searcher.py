def search_local_image(parent=None, modern_askstring=None):
    """
    Search for a Docker image on the local system.
    
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
        keyword = modern_askstring(parent, "Search Image", "Enter image name or tag to search:")
        if not keyword:
            return
        
        result = subprocess.run(["docker", "images"], capture_output=True, text=True)
        
        if result.returncode == 0:
            # Get the header line
            lines = result.stdout.splitlines()
            header = lines[0] if lines else ""
            
            # Filter lines containing the keyword
            matches = [line for line in lines if keyword.lower() in line.lower()]
            
            if matches and header not in matches:
                matches.insert(0, header)  # Add header if not already included
            
            output = "\n".join(matches)
            
            # Display output in the output text widget if available
            if hasattr(parent, "update_output"):
                parent.update_output(output if matches else f"No images found for: {keyword}")
                
            if matches:
                messagebox.showinfo("Search Results", output)
            else:
                messagebox.showinfo("Search Results", f"No images found for: {keyword}")
        else:
            error_message = result.stderr.strip()
            if hasattr(parent, "update_output"):
                parent.update_output(f"Error searching for images:\n\n{error_message}")
            messagebox.showerror("Error", f"Search failed:\n{error_message}")
    except Exception as e:
        messagebox.showerror("Error", f"Search failed:\n{e}")
