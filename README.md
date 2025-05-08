# Cloud Management System

## Overview

The Cloud Management System is a desktop application built with Python and PyQt5 that provides a unified interface for managing virtual machines and Docker containers. The application offers an intuitive GUI to perform common cloud management operations, making it easier for users to interact with virtualization technologies without needing to remember complex command-line instructions.

## Features

### Virtual Machine Management
- Create and run virtual machines using QEMU
- Configure VMs with custom CPU, memory, and disk settings
- Load VM configurations from JSON files

### Docker Image Management
- Create Dockerfiles with a built-in editor
- Build Docker images from existing Dockerfiles
- List available Docker images on the local system
- Search for images locally or on DockerHub
- Pull Docker images from DockerHub

### Container Management
- Run Docker containers with customizable settings
  - Port mapping
  - Environment variables
  - Custom container names
- List running containers
- Stop running containers

## System Requirements

- Python 3.6 or higher
- PyQt5
- Docker installed and running
- QEMU (for VM functionality)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MOsama10/cloud-management-system.git
   cd cloud-management-system
   ```

2. Install required dependencies:
   ```bash
   pip install PyQt5
   ```

3. Ensure Docker is installed and running:
   ```bash
   docker --version
   ```

4. For VM functionality, ensure QEMU is installed:
   ```bash
   qemu-system-x86_64 --version
   ```

## Usage

### Starting the Application

Run the main script to start the application:

```bash
python src/main.py
```

### Using the Application

The application window is divided into two main sections:
- **Left Panel**: Contains buttons grouped by functionality for performing various operations
- **Right Panel**: Displays output from operations

#### Creating a Dockerfile

1. Click on "Create Dockerfile" in the Docker Images section
2. Enter the path where you want to save the Dockerfile
3. Enter the Dockerfile content in the text editor
4. Click OK to save the Dockerfile

#### Building a Docker Image

1. Click on "Build Docker Image"
2. Enter the directory containing the Dockerfile
3. Enter a name for the image
4. Enter a tag (optional)
5. Wait for the build process to complete

#### Running a Container

1. Click on "Run Container"
2. Enter the image name
3. Enter an optional container name
4. Enter optional port mappings (e.g., 8080:80)
5. Enter optional environment variables (e.g., KEY=VALUE)
6. The container will start in detached mode

#### Creating a Virtual Machine

1. Click on "Create Virtual Machine"
2. Choose between using a config file or manual input
3. If using a config file, enter the path to the JSON file
4. If using manual input, enter CPU, memory, and disk image details
5. The VM will start using QEMU

## Project Structure

```
cloud-management-system/
├── src/
│   ├── main.py                  # Main application entry point
│   └── modules/                 # Functional modules
│       ├── container_lister.py  # List running containers
│       ├── container_runner.py  # Run containers
│       ├── container_stopper.py # Stop containers
│       ├── docker_builder.py    # Build Docker images
│       ├── docker_image_lister.py # List Docker images
│       ├── dockerfile_creator.py # Create Dockerfiles
│       ├── dockerhub_searcher.py # Search DockerHub
│       ├── image_puller.py      # Pull Docker images
│       ├── image_searcher.py    # Search local images
│       └── vm_manager.py        # Manage virtual machines
```

## Implementation Details

### Modern UI

The application uses PyQt5 to provide a modern and responsive user interface. Key UI components include:

- **Modern Dialog Boxes**: Custom dialog boxes with improved appearance
- **Scrollable Button Panel**: Groups functional buttons by category
- **Splitter Panel**: Allows resizing the left and right panels
- **Styled Components**: Consistent styling across the application

### Error Handling

The application implements robust error handling to:
- Catch and display Docker command errors
- Handle file and directory access issues
- Validate user input before executing commands

### Subprocess Management

Operations that interact with the Docker CLI or QEMU use Python's subprocess module to:
- Execute commands asynchronously
- Capture stdout and stderr for display in the UI
- Parse command output for user-friendly display

## Configuration

### VM Configuration JSON Format

When using a JSON file for VM configuration, use the following format:

```json
{
  "cpu": 2,
  "memory": 2048,
  "disk": "/path/to/disk.img"
}
```

## Troubleshooting

### Common Issues

1. **"Docker command not found"**:
   - Ensure Docker is installed and added to your PATH
   - Restart the application after installing Docker

2. **"Failed to connect to Docker daemon"**:
   - Make sure the Docker service is running
   - On Linux, ensure your user has permissions to access Docker

3. **"QEMU command not found"**:
   - Install QEMU for VM functionality
   - Add QEMU to your PATH environment variable

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## Acknowledgments

- PyQt5 for the GUI framework
- Docker for container management functionality
- QEMU for virtual machine management
