import subprocess
from PyQt5.QtWidgets import QMessageBox

def run_container(parent, askstring_func):
    """
    Run a Docker container from an image.
    
    Args:
        parent: The parent widget for dialog boxes
        askstring_func: Function to get input from user
    """
    # Ask for the image name
    image_name = askstring_func(parent, "Run Container", "Enter the image name:", "")
    if not image_name:
        return
    
    # Ask for the container name
    container_name = askstring_func(parent, "Run Container", "Enter a name for the container (optional):", "")
    
    # Ask for ports to map (format: host_port:container_port)
    port_mapping = askstring_func(parent, "Run Container", "Enter port mapping (e.g., 8080:80) (optional):", "")
    
    # Ask for environment variables
    env_vars = askstring_func(parent, "Run Container", "Enter environment variables (KEY=VALUE,KEY2=VALUE2) (optional):", "")
    
    # Build the docker run command
    cmd = ["docker", "run", "-d"]
    
    # Add container name if provided
    if container_name:
        cmd.extend(["--name", container_name])
    
    # Add port mapping if provided
    if port_mapping:
        ports = port_mapping.split(",")
        for port in ports:
            if port.strip():
                cmd.extend(["-p", port.strip()])
    
    # Add environment variables if provided
    if env_vars:
        env_list = env_vars.split(",")
        for env in env_list:
            if env.strip():
                cmd.extend(["-e", env.strip()])
    
    # Add the image name
    cmd.append(image_name)
    
    try:
        # Execute the docker run command
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            container_id = result.stdout.strip()
            output_text = f"Container started successfully!\n\nContainer ID: {container_id}"
            
            # Get additional container information
            inspect_cmd = ["docker", "inspect", "--format='{{.Name}} - {{.NetworkSettings.IPAddress}}'", container_id]
            inspect_result = subprocess.run(inspect_cmd, capture_output=True, text=True)
            
            if inspect_result.returncode == 0:
                output_text += f"\nContainer details: {inspect_result.stdout.strip()}"
                
            parent.update_output(output_text)
        else:
            parent.update_output(f"Failed to start container:\n{result.stderr}")
            QMessageBox.warning(parent, "Container Error", f"Failed to start container:\n{result.stderr}")
    except Exception as e:
        parent.update_output(f"Error running container: {str(e)}")
        QMessageBox.critical(parent, "Error", f"Error running container: {str(e)}")
