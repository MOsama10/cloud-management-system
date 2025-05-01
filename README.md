
# ☁️ Cloud Management System  

**A Python-based GUI for managing QEMU Virtual Machines and Docker Containers**  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey)

## 📖 Overview  
An intuitive graphical interface for provisioning and managing:  
- **QEMU/KVM Virtual Machines** (CPU, memory, disk configuration)  
- **Docker** (Image building, container lifecycle management, DockerHub integration)  

Designed for students, DevOps practitioners, and cloud computing enthusiasts.  

---

## ✨ Key Features  

### Virtual Machine Management  
- 🖥️ Interactive VM creation wizard  
- ⚙️ JSON-based configuration templates  
- 📊 Resource allocation (vCPUs, RAM, disk images)  

### Docker Operations  
- 🐳 Dockerfile generation & image building  
- 🔍 Local/DockerHub image search  
- 🏗️ Container lifecycle controls (run/stop/inspect)  

---

## ⚙️ Technical Stack  

| Component          | Technology       |
|--------------------|------------------|
| Core Language      | Python 3.8+      |
| GUI Framework      | Tkinter          |
| Virtualization     | QEMU 6.0+        |
| Container Runtime  | Docker Engine    |

---

## 📂 Repository Structure  
```bash
.
CloudManagementSystem/
├── docs/                       # Documentation files
├── src/                        # Source code
│   ├── main.py                 # Application entry point
│   └── modules/                # Core functionality modules
│       ├── vm_manager.py       # QEMU VM lifecycle management
│       ├── dockerfile_creator.py # Dockerfile generation
│       ├── docker_builder.py   # Docker image building
│       ├── docker_image_lister.py # Local image inventory
│       ├── container_lister.py # Running container management
│       ├── container_stopper.py # Container termination
│       ├── image_searcher.py   # Local image search
│       ├── dockerhub_searcher.py # DockerHub integration
│       └── image_puller.py     # Image download utility
├── tests/                      # Test scripts
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started  

### Clone the Project  
```bash
git clone https://github.com/MOsama10/cloud-management-system.git
cd cloud-management-system
```

### Prerequisites  
- Python 3.8+  
- QEMU ≥6.0 (`sudo apt install qemu-system-x86`)  
- Docker Engine ([Installation guide](https://docs.docker.com/engine/install/))  

### Installation  
```bash
pip install -r requirements.txt
```

### Launching the Application  
```bash
python src/main.py
```

---

## 🧩 Example Usage  

### Creating a VM via Config File  
```json
// samples/vm_config.json
{
  "name": "ubuntu-vm",
  "cpus": 2,
  "memory_mb": 2048,
  "disk_path": "/var/lib/vm/ubuntu.qcow2"
}
```

### Building a Docker Image  
1. Use the GUI to generate a `Dockerfile`  
2. Build with:  
```bash
docker build -t my-app .
```

---

## 📧 Contact  
**Developer**: [Mohamed Osama]  
**Course**: Cloud Computing & Networking  
**Institution**: [Nile University]  

---

