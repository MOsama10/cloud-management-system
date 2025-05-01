import tkinter as tk
from tkinter import messagebox
from modules.vm_manager import create_vm
from modules.dockerfile_creator import create_dockerfile
from modules.docker_builder import build_docker_image
from modules.docker_image_lister import list_docker_images
from modules.container_lister import list_running_containers
from modules.container_stopper import stop_container
from modules.image_searcher import search_local_image
from modules.dockerhub_searcher import search_dockerhub_image
from modules.image_puller import pull_docker_image

class CloudManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cloud Management System")
        self.root.geometry("400x500")

        tk.Label(root, text="Cloud Management System", font=("Arial", 16)).pack(pady=10)

        actions = [
            ("Create Virtual Machine", create_vm),
            ("Create Dockerfile", create_dockerfile),
            ("Build Docker Image", build_docker_image),
            ("List Docker Images", list_docker_images),
            ("List Running Containers", list_running_containers),
            ("Stop Container", stop_container),
            ("Search Local Image", search_local_image),
            ("Search DockerHub", search_dockerhub_image),
            ("Pull Docker Image", pull_docker_image)
        ]

        for text, command in actions:
            tk.Button(root, text=text, width=30, command=command).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CloudManagerApp(root)
    root.mainloop()
