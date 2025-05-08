def create_dockerfile(parent=None, modern_askstring=None, modern_text_input=None):
    """
    Create a Dockerfile at the specified path.
    
    Args:
        parent: The parent window for dialogs
        modern_askstring: Function to display modern string input dialog
        modern_text_input: Function to display modern text input dialog
    """
    import os
    from tkinter import messagebox
    
    # Use default dialogs if custom ones aren't provided
    if modern_askstring is None or modern_text_input is None:
        from tkinter import simpledialog
        modern_askstring = simpledialog.askstring
        modern_text_input = simpledialog.askstring
    
    if parent is None:
        import tkinter as tk
        parent = tk._default_root
    
    try:
        path = modern_askstring(parent, "Dockerfile Path", "Enter path to save Dockerfile (e.g., C:\\docker\\Dockerfile):")
        if not path:
            return
            
        # Ensure the directory exists
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create directory:\n{e}")
                return
            
        content = modern_text_input(parent, "Dockerfile Content", "Enter Dockerfile content:")
        if not content:
            return
            
        try:
            with open(path, "w") as f:
                f.write(content)
                
            # Show success message in output area
            if hasattr(parent, "update_output"):
                parent.update_output(f"Dockerfile created at: {path}\n\nContent:\n{content}")
                
            messagebox.showinfo("Success", f"Dockerfile created at:\n{path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create Dockerfile:\n{e}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create Dockerfile:\n{e}")
