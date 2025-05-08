import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                           QLabel, QWidget, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Import the same modules as in the original but updated for PyQt
from modules.vm_manager import create_vm
from modules.dockerfile_creator import create_dockerfile
from modules.docker_builder import build_docker_image
from modules.docker_image_lister import list_docker_images
from modules.container_lister import list_running_containers
from modules.container_stopper import stop_container
from modules.image_searcher import search_local_image
from modules.dockerhub_searcher import search_dockerhub_image
from modules.image_puller import pull_docker_image

class CloudManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Cloud Management System")
        self.setGeometry(300, 300, 450, 550)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title label
        title_label = QLabel("Cloud Management System")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Style sheet for buttons
        button_style = """
        QPushButton {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 8px;
            font-size: 12px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #1f618d;
        }
        """
        
        # Add buttons with the same actions as in the original
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
            button = QPushButton(text)
            button.setStyleSheet(button_style)
            button.setMinimumHeight(40)
            button.clicked.connect(lambda checked, cmd=command: self.execute_action(cmd))
            main_layout.addWidget(button)
            
        # Add some stretch at the end to push everything to the top
        main_layout.addStretch()
        
        # Set the overall application style
        self.setStyleSheet("""
        QMainWindow {
            background-color: #f5f5f5;
        }
        QLabel {
            color: #2c3e50;
            margin-bottom: 10px;
        }
        """)
    
    def execute_action(self, action_func):
        try:
            action_func()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CloudManagerApp()
    window.show()
    sys.exit(app.exec_())
