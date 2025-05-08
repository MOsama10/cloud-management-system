# import sys
# import os
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
#                            QLabel, QWidget, QMessageBox, QTextEdit, QSplitter,
#                            QHBoxLayout, QInputDialog, QLineEdit, QDialog, QGroupBox,
#                            QScrollArea, QSizePolicy)
# from PyQt5.QtCore import Qt, QSize
# from PyQt5.QtGui import QFont, QIcon, QPixmap

# # Import modules
# from modules.vm_manager import create_vm
# from modules.dockerfile_creator import create_dockerfile
# from modules.docker_builder import build_docker_image
# from modules.docker_image_lister import list_docker_images
# from modules.container_lister import list_running_containers
# from modules.container_stopper import stop_container
# from modules.image_searcher import search_local_image
# from modules.dockerhub_searcher import search_dockerhub_image
# from modules.image_puller import pull_docker_image

# class ModernInputDialog(QDialog):
#     """A modern-looking input dialog for getting text input from the user."""
    
#     def __init__(self, parent=None, title="Input", label="Enter value:", default="", echo_mode=QLineEdit.Normal):
#         super().__init__(parent)
#         self.setWindowTitle(title)
#         self.resize(400, 100)
        
#         # Create layout
#         layout = QVBoxLayout(self)
        
#         # Add label
#         self.label = QLabel(label)
#         self.label.setFont(QFont("Arial", 10))
#         layout.addWidget(self.label)
        
#         # Add text field
#         self.input_field = QLineEdit(default)
#         self.input_field.setEchoMode(echo_mode)
#         self.input_field.setMinimumHeight(30)
#         self.input_field.setFont(QFont("Arial", 10))
#         layout.addWidget(self.input_field)
        
#         # Add buttons
#         button_layout = QHBoxLayout()
        
#         self.ok_button = QPushButton("OK")
#         self.ok_button.setDefault(True)
#         self.ok_button.clicked.connect(self.accept)
        
#         self.cancel_button = QPushButton("Cancel")
#         self.cancel_button.clicked.connect(self.reject)
        
#         button_layout.addWidget(self.ok_button)
#         button_layout.addWidget(self.cancel_button)
#         layout.addLayout(button_layout)
        
#         # Set style
#         self.setStyleSheet("""
#             QDialog {
#                 background-color: #f5f5f5;
#             }
#             QLabel {
#                 color: #2c3e50;
#             }
#             QLineEdit {
#                 border: 1px solid #bdc3c7;
#                 border-radius: 4px;
#                 padding: 5px;
#             }
#             QPushButton {
#                 background-color: #3498db;
#                 color: white;
#                 border-radius: 4px;
#                 padding: 6px 12px;
#                 font-weight: bold;
#             }
#             QPushButton:hover {
#                 background-color: #2980b9;
#             }
#             QPushButton:pressed {
#                 background-color: #1f618d;
#             }
#         """)
    
#     def get_input(self):
#         """Show the dialog and return the input text if accepted, None otherwise."""
#         result = self.exec_()
#         if result == QDialog.Accepted:
#             return self.input_field.text()
#         return None

# class ModernTextInputDialog(QDialog):
#     """A modern-looking dialog for getting multiline text input from the user."""
    
#     def __init__(self, parent=None, title="Text Input", label="Enter text:", default=""):
#         super().__init__(parent)
#         self.setWindowTitle(title)
#         self.resize(500, 300)
        
#         # Create layout
#         layout = QVBoxLayout(self)
        
#         # Add label
#         self.label = QLabel(label)
#         self.label.setFont(QFont("Arial", 10))
#         layout.addWidget(self.label)
        
#         # Add text edit
#         self.text_edit = QTextEdit(default)
#         self.text_edit.setFont(QFont("Consolas", 10))
#         layout.addWidget(self.text_edit)
        
#         # Add buttons
#         button_layout = QHBoxLayout()
        
#         self.ok_button = QPushButton("OK")
#         self.ok_button.setDefault(True)
#         self.ok_button.clicked.connect(self.accept)
        
#         self.cancel_button = QPushButton("Cancel")
#         self.cancel_button.clicked.connect(self.reject)
        
#         button_layout.addWidget(self.ok_button)
#         button_layout.addWidget(self.cancel_button)
#         layout.addLayout(button_layout)
        
#         # Set style
#         self.setStyleSheet("""
#             QDialog {
#                 background-color: #f5f5f5;
#             }
#             QLabel {
#                 color: #2c3e50;
#             }
#             QTextEdit {
#                 border: 1px solid #bdc3c7;
#                 border-radius: 4px;
#                 padding: 5px;
#             }
#             QPushButton {
#                 background-color: #3498db;
#                 color: white;
#                 border-radius: 4px;
#                 padding: 6px 12px;
#                 font-weight: bold;
#             }
#             QPushButton:hover {
#                 background-color: #2980b9;
#             }
#             QPushButton:pressed {
#                 background-color: #1f618d;
#             }
#         """)
    
#     def get_text(self):
#         """Show the dialog and return the text if accepted, None otherwise."""
#         result = self.exec_()
#         if result == QDialog.Accepted:
#             return self.text_edit.toPlainText()
#         return None

# def modern_askstring(parent, title, prompt, default=""):
#     """Create and show a modern input dialog."""
#     dialog = ModernInputDialog(parent, title, prompt, default)
#     return dialog.get_input()

# def modern_text_input(parent, title, prompt, default=""):
#     """Create and show a modern text input dialog."""
#     dialog = ModernTextInputDialog(parent, title, prompt, default)
#     return dialog.get_text()

# class CloudManagerApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
        
#     def init_ui(self):
#         # Set window properties
#         self.setWindowTitle("Cloud Management System")
#         self.setGeometry(100, 100, 900, 600)
        
#         # Create central widget
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
        
#         # Create main layout
#         main_layout = QHBoxLayout(central_widget)
        
#         # Create a splitter for resizable panels
#         splitter = QSplitter(Qt.Horizontal)
#         main_layout.addWidget(splitter)
        
#         # Create left panel (buttons)
#         left_panel = QWidget()
#         left_layout = QVBoxLayout(left_panel)
#         left_layout.setContentsMargins(15, 15, 15, 15)
#         left_layout.setSpacing(10)
        
#         # Add title
#         title_label = QLabel("Cloud Management System")
#         title_label.setFont(QFont("Arial", 16, QFont.Bold))
#         title_label.setAlignment(Qt.AlignCenter)
#         title_label.setMargin(10)
#         left_layout.addWidget(title_label)
        
#         # Create scroll area for buttons
#         scroll_area = QScrollArea()
#         scroll_area.setWidgetResizable(True)
#         scroll_area.setFrameShape(QScrollArea.NoFrame)
        
#         # Create widget to hold buttons inside scroll area
#         scroll_widget = QWidget()
#         buttons_layout = QVBoxLayout(scroll_widget)
#         buttons_layout.setSpacing(10)
        
#         # Add button groups
#         self.add_button_group(buttons_layout, "Virtual Machine", [
#             ("Create Virtual Machine", lambda: self.execute_action(create_vm, True, True))
#         ])
        
#         self.add_button_group(buttons_layout, "Docker Images", [
#             ("Create Dockerfile", lambda: self.execute_action(create_dockerfile, True, True)),
#             ("Build Docker Image", lambda: self.execute_action(build_docker_image, True)),
#             ("List Docker Images", lambda: self.execute_action(list_docker_images)),
#             ("Search Local Image", lambda: self.execute_action(search_local_image, True)),
#             ("Search DockerHub", lambda: self.execute_action(search_dockerhub_image, True)),
#             ("Pull Docker Image", lambda: self.execute_action(pull_docker_image, True))
#         ])
        
#         self.add_button_group(buttons_layout, "Containers", [
#             ("List Running Containers", lambda: self.execute_action(list_running_containers)),
#             ("Stop Container", lambda: self.execute_action(stop_container, True))
#         ])
        
#         # Add spacer at the bottom
#         buttons_layout.addStretch()
        
#         # Set the scroll widget and add to layout
#         scroll_area.setWidget(scroll_widget)
#         left_layout.addWidget(scroll_area)
        
#         # Create right panel (output)
#         right_panel = QWidget()
#         right_layout = QVBoxLayout(right_panel)
#         right_layout.setContentsMargins(15, 15, 15, 15)
        
#         output_label = QLabel("Output")
#         output_label.setFont(QFont("Arial", 12, QFont.Bold))
#         right_layout.addWidget(output_label)
        
#         self.output_text = QTextEdit()
#         self.output_text.setReadOnly(True)
#         self.output_text.setFont(QFont("Consolas", 10))
#         self.output_text.setMinimumWidth(400)
#         right_layout.addWidget(self.output_text)
        
#         # Add clear button for output
#         clear_button = QPushButton("Clear Output")
#         clear_button.clicked.connect(self.clear_output)
#         right_layout.addWidget(clear_button)
        
#         # Add panels to splitter
#         splitter.addWidget(left_panel)
#         splitter.addWidget(right_panel)
        
#         # Set initial sizes (40% for left panel, 60% for right panel)
#         splitter.setSizes([360, 540])
        
#         # Apply stylesheet for the entire application
#         self.set_stylesheet()
        
#         # Display welcome message
#         self.update_output("Welcome to Cloud Management System\n\nThis application helps you manage virtual machines and Docker containers. Use the buttons on the left to perform various operations.")
    
#     def add_button_group(self, parent_layout, group_title, buttons):
#         """Add a group of buttons with a title."""
#         group_box = QGroupBox(group_title)
#         group_box.setFont(QFont("Arial", 11, QFont.Bold))
        
#         # Create layout for the group
#         group_layout = QVBoxLayout()
#         group_layout.setSpacing(8)
        
#         # Add buttons to the group
#         for text, command in buttons:
#             button = QPushButton(text)
#             button.setFont(QFont("Arial", 10))
#             button.setMinimumHeight(36)
#             button.clicked.connect(command)
#             group_layout.addWidget(button)
        
#         group_box.setLayout(group_layout)
#         parent_layout.addWidget(group_box)
    
#     def execute_action(self, action_func, use_askstring=False, use_text_input=False):
#         """Execute an action and handle any exceptions."""
#         try:
#             if use_askstring and use_text_input:
#                 action_func(self, modern_askstring, modern_text_input)
#             elif use_askstring:
#                 action_func(self, modern_askstring)
#             else:
#                 action_func(self)
#         except Exception as e:
#             self.update_output(f"An error occurred: {str(e)}")
#             QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
    
#     def update_output(self, text):
#         """Update the output text area with the given text."""
#         self.output_text.setPlainText(text)
    
#     def clear_output(self):
#         """Clear the output text area."""
#         self.output_text.clear()
    
#     def set_stylesheet(self):
#         """Apply a stylesheet to the application."""
#         self.setStyleSheet("""
#             QMainWindow {
#                 background-color: #f5f5f5;
#             }
#             QLabel {
#                 color: #2c3e50;
#             }
#             QPushButton {
#                 background-color: #3498db;
#                 color: white;
#                 border-radius: 4px;
#                 padding: 6px;
#                 font-weight: bold;
#             }
#             QPushButton:hover {
#                 background-color: #2980b9;
#             }
#             QPushButton:pressed {
#                 background-color: #1f618d;
#             }
#             QTextEdit {
#                 background-color: white;
#                 border: 1px solid #bdc3c7;
#                 border-radius: 4px;
#                 padding: 5px;
#             }
#             QGroupBox {
#                 border: 1px solid #bdc3c7;
#                 border-radius: 5px;
#                 margin-top: 10px;
#                 padding-top: 15px;
#             }
#             QGroupBox::title {
#                 subcontrol-origin: margin;
#                 subcontrol-position: top center;
#                 padding: 0 5px;
#                 color: #2c3e50;
#             }
#         """)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = CloudManagerApp()
#     window.show()
#     sys.exit(app.exec_())

import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                           QLabel, QWidget, QMessageBox, QTextEdit, QSplitter,
                           QHBoxLayout, QInputDialog, QLineEdit, QDialog, QGroupBox,
                           QScrollArea, QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap

# Import modules
from modules.vm_manager import create_vm
from modules.dockerfile_creator import create_dockerfile
from modules.docker_builder import build_docker_image
from modules.docker_image_lister import list_docker_images
from modules.container_lister import list_running_containers
from modules.container_stopper import stop_container
from modules.container_runner import run_container
from modules.image_searcher import search_local_image
from modules.dockerhub_searcher import search_dockerhub_image
from modules.image_puller import pull_docker_image

class ModernInputDialog(QDialog):
    """A modern-looking input dialog for getting text input from the user."""
    
    def __init__(self, parent=None, title="Input", label="Enter value:", default="", echo_mode=QLineEdit.Normal):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.resize(400, 100)
        
        # Create layout
        layout = QVBoxLayout(self)
        
        # Add label
        self.label = QLabel(label)
        self.label.setFont(QFont("Arial", 10))
        layout.addWidget(self.label)
        
        # Add text field
        self.input_field = QLineEdit(default)
        self.input_field.setEchoMode(echo_mode)
        self.input_field.setMinimumHeight(30)
        self.input_field.setFont(QFont("Arial", 10))
        layout.addWidget(self.input_field)
        
        # Add buttons
        button_layout = QHBoxLayout()
        
        self.ok_button = QPushButton("OK")
        self.ok_button.setDefault(True)
        self.ok_button.clicked.connect(self.accept)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        
        # Set style
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
            }
            QLabel {
                color: #2c3e50;
            }
            QLineEdit {
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 4px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """)
    
    def get_input(self):
        """Show the dialog and return the input text if accepted, None otherwise."""
        result = self.exec_()
        if result == QDialog.Accepted:
            return self.input_field.text()
        return None

class ModernTextInputDialog(QDialog):
    """A modern-looking dialog for getting multiline text input from the user."""
    
    def __init__(self, parent=None, title="Text Input", label="Enter text:", default=""):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.resize(500, 300)
        
        # Create layout
        layout = QVBoxLayout(self)
        
        # Add label
        self.label = QLabel(label)
        self.label.setFont(QFont("Arial", 10))
        layout.addWidget(self.label)
        
        # Add text edit
        self.text_edit = QTextEdit(default)
        self.text_edit.setFont(QFont("Consolas", 10))
        layout.addWidget(self.text_edit)
        
        # Add buttons
        button_layout = QHBoxLayout()
        
        self.ok_button = QPushButton("OK")
        self.ok_button.setDefault(True)
        self.ok_button.clicked.connect(self.accept)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        
        # Set style
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
            }
            QLabel {
                color: #2c3e50;
            }
            QTextEdit {
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 4px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """)
    
    def get_text(self):
        """Show the dialog and return the text if accepted, None otherwise."""
        result = self.exec_()
        if result == QDialog.Accepted:
            return self.text_edit.toPlainText()
        return None

def modern_askstring(parent, title, prompt, default=""):
    """Create and show a modern input dialog."""
    dialog = ModernInputDialog(parent, title, prompt, default)
    return dialog.get_input()

def modern_text_input(parent, title, prompt, default=""):
    """Create and show a modern text input dialog."""
    dialog = ModernTextInputDialog(parent, title, prompt, default)
    return dialog.get_text()

class CloudManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        # Set window properties
        self.setWindowTitle("Cloud Management System")
        self.setGeometry(100, 100, 900, 600)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QHBoxLayout(central_widget)
        
        # Create a splitter for resizable panels
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        # Create left panel (buttons)
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(15, 15, 15, 15)
        left_layout.setSpacing(10)
        
        # Add title
        title_label = QLabel("Cloud Management System")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setMargin(10)
        left_layout.addWidget(title_label)
        
        # Create scroll area for buttons
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.NoFrame)
        
        # Create widget to hold buttons inside scroll area
        scroll_widget = QWidget()
        buttons_layout = QVBoxLayout(scroll_widget)
        buttons_layout.setSpacing(10)
        
        # Add button groups
        self.add_button_group(buttons_layout, "Virtual Machine", [
            ("Create Virtual Machine", lambda: self.execute_action(create_vm, True, True))
        ])
        
        self.add_button_group(buttons_layout, "Docker Images", [
            ("Create Dockerfile", lambda: self.execute_action(create_dockerfile, True, True)),
            ("Build Docker Image", lambda: self.execute_action(build_docker_image, True)),
            ("List Docker Images", lambda: self.execute_action(list_docker_images)),
            ("Search Local Image", lambda: self.execute_action(search_local_image, True)),
            ("Search DockerHub", lambda: self.execute_action(search_dockerhub_image, True)),
            ("Pull Docker Image", lambda: self.execute_action(pull_docker_image, True))
        ])
        
        self.add_button_group(buttons_layout, "Containers", [
            ("Run Container", lambda: self.execute_action(run_container, True)),
            ("List Running Containers", lambda: self.execute_action(list_running_containers)),
            ("Stop Container", lambda: self.execute_action(stop_container, True))
        ])
        
        # Add spacer at the bottom
        buttons_layout.addStretch()
        
        # Set the scroll widget and add to layout
        scroll_area.setWidget(scroll_widget)
        left_layout.addWidget(scroll_area)
        
        # Create right panel (output)
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(15, 15, 15, 15)
        
        output_label = QLabel("Output")
        output_label.setFont(QFont("Arial", 12, QFont.Bold))
        right_layout.addWidget(output_label)
        
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFont(QFont("Consolas", 10))
        self.output_text.setMinimumWidth(400)
        right_layout.addWidget(self.output_text)
        
        # Add clear button for output
        clear_button = QPushButton("Clear Output")
        clear_button.clicked.connect(self.clear_output)
        right_layout.addWidget(clear_button)
        
        # Add panels to splitter
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        
        # Set initial sizes (40% for left panel, 60% for right panel)
        splitter.setSizes([360, 540])
        
        # Apply stylesheet for the entire application
        self.set_stylesheet()
        
        # Display welcome message
        self.update_output("Welcome to Cloud Management System\n\nThis application helps you manage virtual machines and Docker containers. Use the buttons on the left to perform various operations.")
    
    def add_button_group(self, parent_layout, group_title, buttons):
        """Add a group of buttons with a title."""
        group_box = QGroupBox(group_title)
        group_box.setFont(QFont("Arial", 11, QFont.Bold))
        
        # Create layout for the group
        group_layout = QVBoxLayout()
        group_layout.setSpacing(8)
        
        # Add buttons to the group
        for text, command in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 10))
            button.setMinimumHeight(36)
            button.clicked.connect(command)
            group_layout.addWidget(button)
        
        group_box.setLayout(group_layout)
        parent_layout.addWidget(group_box)
    
    def execute_action(self, action_func, use_askstring=False, use_text_input=False):
        """Execute an action and handle any exceptions."""
        try:
            if use_askstring and use_text_input:
                action_func(self, modern_askstring, modern_text_input)
            elif use_askstring:
                action_func(self, modern_askstring)
            else:
                action_func(self)
        except Exception as e:
            self.update_output(f"An error occurred: {str(e)}")
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
    
    def update_output(self, text):
        """Update the output text area with the given text."""
        self.output_text.setPlainText(text)
    
    def clear_output(self):
        """Clear the output text area."""
        self.output_text.clear()
    
    def set_stylesheet(self):
        """Apply a stylesheet to the application."""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLabel {
                color: #2c3e50;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 4px;
                padding: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
            QTextEdit {
                background-color: white;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                padding: 5px;
            }
            QGroupBox {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 5px;
                color: #2c3e50;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CloudManagerApp()
    window.show()
    sys.exit(app.exec_())
