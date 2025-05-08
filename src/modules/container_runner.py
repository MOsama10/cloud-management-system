def run_container(parent=None, modern_askstring=None):
    """
    Run a Docker container from an image.
    
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
        # Get the image name
        image_name = modern_askstring(parent, "Run Container", "Enter the image name:")
        if not image_name:
            return
            
        # Get container name (optional)
        container_name = modern_askstring(parent, "Container Name", "Enter container name (optional):")
        
        # Get port mappings (optional)
        port_mapping = modern_askstring(parent, "Port Mapping", "Enter port mapping (e.g., 8080:80) (optional):")
        
        # Get environment variables (optional)
        env_vars = modern_askstring(parent, "Environment Variables", "Enter environment variables (e.g., VAR1=value1,VAR2=value2) (optional):")
        
        # Get volume mappings (optional)
        volume_mapping = modern_askstring(parent, "Volume Mapping", "Enter volume mapping (e.g., /host/path:/container/path) (optional):")
        
        # Get detach mode
        detach_mode = messagebox.askyesno("Detach Mode", "Run container in detached mode?")
        
        # Build the docker run command
        command = ["docker", "run"]
        
        # Add detach flag if selected
        if detach_mode:
            command.append("-d")
        
        # Add container name if provided
        if container_name:
            command.extend(["--name", container_name])
        
        # Add port mapping if provided
        if port_mapping:
            command.extend(["-p", port_mapping])
        
        # Add environment variables if provided
        if env_vars:
            for env_var in env_vars.split(","):
                if "=" in env_var:
                    command.extend(["-e", env_var.strip()])
        
        # Add volume mapping if provided
        if volume_mapping:
            command.extend(["-v", volume_mapping])
        
        # Add the image name
        command.append(image_name)
        
        # Show starting message in output area
        if hasattr(parent, "update_output"):
            parent.update_output(f"Starting container from image '{image_name}'...\n\nCommand: {' '.join(command)}")
        
        # Run the container
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            container_id = result.stdout.strip()
            success_message = f"Container started successfully.\nContainer ID: {container_id}"
            
            # Show success message in output area
            if hasattr(parent, "update_output"):
                parent.update_output(success_message)
                
            messagebox.showinfo("Success", success_message)
        else:
            error_message = f"Failed to start container:\n{result.stderr}"
            
            # Show error message in output area
            if hasattr(parent, "update_output"):
                parent.update_output(error_message)
                
            messagebox.showerror("Error", error_message)
    except Exception as e:
        error_message = f"Failed to run container:\n{e}"
        
        # Show error message in output area
        if hasattr(parent, "update_output"):
            parent.update_output(error_message)
            
        messagebox.showerror("Error", error_message)
