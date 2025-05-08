# import tkinter as tk
# from tkinter import messagebox
# from modules.vm_manager import create_vm
# from modules.dockerfile_creator import create_dockerfile
# from modules.docker_builder import build_docker_image
# from modules.docker_image_lister import list_docker_images
# from modules.container_lister import list_running_containers
# from modules.container_stopper import stop_container
# from modules.image_searcher import search_local_image
# from modules.dockerhub_searcher import search_dockerhub_image
# from modules.image_puller import pull_docker_image

# class CloudManagerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Cloud Management System")
#         self.root.geometry("400x500")

#         tk.Label(root, text="Cloud Management System", font=("Arial", 16)).pack(pady=10)

#         actions = [
#             ("Create Virtual Machine", create_vm),
#             ("Create Dockerfile", create_dockerfile),
#             ("Build Docker Image", build_docker_image),
#             ("List Docker Images", list_docker_images),
#             ("List Running Containers", list_running_containers),
#             ("Stop Container", stop_container),
#             ("Search Local Image", search_local_image),
#             ("Search DockerHub", search_dockerhub_image),
#             ("Pull Docker Image", pull_docker_image)
#         ]

#         for text, command in actions:
#             tk.Button(root, text=text, width=30, command=command).pack(pady=5)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CloudManagerApp(root)
#     root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox, Frame, scrolledtext
import os
import sys
from tkinter import font as tkfont

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.vm_manager import create_vm
from modules.dockerfile_creator import create_dockerfile
from modules.docker_builder import build_docker_image
from modules.docker_image_lister import list_docker_images
from modules.container_lister import list_running_containers
from modules.container_stopper import stop_container
from modules.image_searcher import search_local_image
from modules.dockerhub_searcher import search_dockerhub_image
from modules.image_puller import pull_docker_image

class CustomEntry(ttk.Entry):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = 'grey'
        self.default_fg_color = self['foreground']
        
        self.bind("<FocusIn>", self._focus_in)
        self.bind("<FocusOut>", self._focus_out)
        
        self._focus_out(None)
    
    def _focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(foreground=self.default_fg_color)
    
    def _focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(foreground=self.placeholder_color)

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class TextDialog(tk.Toplevel):
    def __init__(self, parent, title, prompt=""):
        super().__init__(parent)
        self.title(title)
        self.result = None
        self.geometry("500x400")
        self.minsize(500, 400)
        
        self.configure(bg="#f0f0f0")
        
        # Make dialog modal
        self.transient(parent)
        self.grab_set()
        
        # Style the dialog
        self.style = ttk.Style(self)
        
        # Create a frame for the label and text widget
        frame = ttk.Frame(self, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Label
        ttk.Label(frame, text=prompt, wraplength=480).pack(pady=(0, 10), anchor="w")
        
        # Text widget with syntax highlighting capabilities
        self.text_widget = scrolledtext.ScrolledText(
            frame,
            wrap=tk.WORD,
            width=50,
            height=15,
            font=("Consolas", 11)
        )
        self.text_widget.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.text_widget.focus_set()
        
        # Button frame
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Cancel and OK buttons
        ttk.Button(button_frame, text="Cancel", command=self.cancel).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="OK", command=self.ok, style="Accent.TButton").pack(side=tk.RIGHT)
        
        # Handle window close
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        
        # Position the dialog
        self.center_window()
        
        # Wait for the window to appear
        self.wait_visibility()
        
        # Wait for the window to be destroyed
        self.wait_window()
    
    def center_window(self):
        """Center the dialog window on the screen."""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def ok(self):
        """Process the OK button click."""
        self.result = self.text_widget.get("1.0", tk.END).strip()
        self.destroy()
    
    def cancel(self):
        """Process the Cancel button click."""
        self.result = None
        self.destroy()

class ModernInputDialog(tk.Toplevel):
    def __init__(self, parent, title, prompt, show=None):
        super().__init__(parent)
        self.title(title)
        self.result = None
        self.geometry("400x150")
        self.minsize(400, 150)
        
        self.configure(bg="#f0f0f0")
        
        # Make dialog modal
        self.transient(parent)
        self.grab_set()
        
        # Create a frame for the label and entry widget
        frame = ttk.Frame(self, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Label
        ttk.Label(frame, text=prompt, wraplength=360).pack(pady=(0, 10), anchor="w")
        
        # Entry widget
        self.entry = ttk.Entry(frame, width=50, show=show)
        self.entry.pack(fill=tk.X, pady=(0, 20))
        self.entry.focus_set()
        
        # Button frame
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X)
        
        # Cancel and OK buttons
        ttk.Button(button_frame, text="Cancel", command=self.cancel).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="OK", command=self.ok, style="Accent.TButton").pack(side=tk.RIGHT)
        
        # Handle window close
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        
        # Enter key binding
        self.entry.bind("<Return>", lambda event: self.ok())
        
        # Position the dialog
        self.center_window()
        
        # Wait for the window to appear
        self.wait_visibility()
        
        # Wait for the window to be destroyed
        self.wait_window()
    
    def center_window(self):
        """Center the dialog window on the screen."""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def ok(self):
        """Process the OK button click."""
        self.result = self.entry.get()
        self.destroy()
    
    def cancel(self):
        """Process the Cancel button click."""
        self.result = None
        self.destroy()

def modern_askstring(parent, title, prompt, **kwargs):
    """Modern replacement for simpledialog.askstring."""
    dialog = ModernInputDialog(parent, title, prompt, **kwargs)
    return dialog.result

def modern_text_input(parent, title, prompt="", **kwargs):
    """Modern replacement for multiline text input."""
    dialog = TextDialog(parent, title, prompt, **kwargs)
    return dialog.result

class CloudManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cloud Management System")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # Configure the grid layout
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=0)  # Header
        self.root.rowconfigure(1, weight=1)  # Content
        self.root.rowconfigure(2, weight=0)  # Footer
        
        # Set the application style
        self.setup_styles()
        
        # Create header frame
        self.create_header()
        
        # Create content frame
        self.create_content()
        
        # Create footer
        self.create_footer()
        
        # Create output frame
        self.create_output_frame()

    def setup_styles(self):
        """Set up the ttk styles for the application."""
        self.style = ttk.Style()
        
        # Configure the main styles
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("Header.TFrame", background="#2c3e50")
        self.style.configure("Footer.TFrame", background="#ecf0f1")
        
        # Configure button styles
        self.style.configure("TButton", font=("Segoe UI", 10))
        self.style.configure("Accent.TButton", background="#3498db", foreground="white")
        
        # Configure label styles
        self.style.configure("Header.TLabel", 
                           font=("Segoe UI", 18, "bold"), 
                           foreground="white", 
                           background="#2c3e50")
        self.style.configure("SubHeader.TLabel", 
                           font=("Segoe UI", 12), 
                           foreground="#7f8c8d", 
                           background="#f0f0f0")
        
        # Configure the category labels
        self.style.configure("Category.TLabel", 
                           font=("Segoe UI", 12, "bold"), 
                           foreground="#2c3e50", 
                           background="#f0f0f0")
        
        # Configure the section frames
        self.style.configure("Section.TFrame", 
                           background="#ffffff", 
                           relief="solid", 
                           borderwidth=1)
        
        # Configure the action buttons
        self.style.configure("Action.TButton", 
                           font=("Segoe UI", 10), 
                           background="#3498db", 
                           foreground="white")
        self.style.map("Action.TButton", 
                      background=[("active", "#2980b9"), ("pressed", "#1f618d")])
        
    def create_header(self):
        """Create the application header."""
        header_frame = ttk.Frame(self.root, style="Header.TFrame")
        header_frame.grid(row=0, column=0, sticky="ew")
        
        # Add padding to the header
        header_frame.columnconfigure(0, weight=1)
        header_frame.columnconfigure(1, weight=0)
        
        # Add the title
        title_label = ttk.Label(header_frame, 
                              text="Cloud Management System", 
                              style="Header.TLabel")
        title_label.grid(row=0, column=0, padx=20, pady=15, sticky="w")
        
        # Add a subtitle
        subtitle_label = ttk.Label(header_frame, 
                                 text="Manage Docker containers and QEMU virtual machines", 
                                 foreground="#bdc3c7", 
                                 background="#2c3e50", 
                                 font=("Segoe UI", 10))
        subtitle_label.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="w")
        
    def create_content(self):
        """Create the main content area."""
        # Create a frame for the content with scrolling
        content_frame = ScrollableFrame(self.root)
        content_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        # Configure the grid for the scrollable frame
        content_frame.scrollable_frame.columnconfigure(0, weight=1)
        
        # Create Docker section
        self.create_docker_section(content_frame.scrollable_frame)
        
        # Create VM section
        self.create_vm_section(content_frame.scrollable_frame)
        
    def create_docker_section(self, parent):
        """Create the Docker management section."""
        # Section label
        docker_label = ttk.Label(parent, text="Docker Management", style="Category.TLabel")
        docker_label.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="w")
        
        # Docker section frame
        docker_frame = ttk.Frame(parent, style="Section.TFrame")
        docker_frame.grid(row=1, column=0, padx=10, pady=(0, 20), sticky="ew")
        
        # Configure the grid for the Docker frame
        docker_frame.columnconfigure(0, weight=1)
        docker_frame.columnconfigure(1, weight=1)
        docker_frame.columnconfigure(2, weight=1)
        
        # Docker actions
        docker_actions = [
            ("Create Dockerfile", self.create_dockerfile_wrapper, "Create a new Dockerfile for container images"),
            ("Build Docker Image", self.build_docker_image_wrapper, "Build a Docker image from a Dockerfile"),
            ("List Docker Images", list_docker_images, "View all Docker images on your system"),
            ("List Running Containers", list_running_containers, "View all running Docker containers"),
            ("Stop Container", stop_container, "Stop a running Docker container"),
            ("Search Local Image", search_local_image, "Search for Docker images on your local system"),
            ("Search DockerHub", search_dockerhub_image, "Search for Docker images on DockerHub"),
            ("Pull Docker Image", pull_docker_image, "Download a Docker image from DockerHub")
        ]
        
        # Create action buttons for Docker
        for i, (text, command, description) in enumerate(docker_actions):
            row = i // 3
            col = i % 3
            
            # Create a frame for each action
            action_frame = ttk.Frame(docker_frame)
            action_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # Action button
            btn = ttk.Button(action_frame, text=text, command=command, width=20)
            btn.pack(pady=(0, 5))
            
            # Description label
            desc_label = ttk.Label(action_frame, text=description, wraplength=180, foreground="#7f8c8d")
            desc_label.pack()
            
    def create_vm_section(self, parent):
        """Create the VM management section."""
        # Section label
        vm_label = ttk.Label(parent, text="VM Management", style="Category.TLabel")
        vm_label.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")
        
        # VM section frame
        vm_frame = ttk.Frame(parent, style="Section.TFrame")
        vm_frame.grid(row=3, column=0, padx=10, pady=(0, 20), sticky="ew")
        
        # Create VM button
        vm_button_frame = ttk.Frame(vm_frame)
        vm_button_frame.pack(padx=20, pady=20)
        
        vm_btn = ttk.Button(vm_button_frame, text="Create Virtual Machine", command=create_vm, width=25)
        vm_btn.pack()
        
        vm_desc = ttk.Label(vm_button_frame, 
                         text="Create and configure a new QEMU virtual machine", 
                         wraplength=300, 
                         foreground="#7f8c8d")
        vm_desc.pack(pady=(5, 0))
        
    def create_footer(self):
        """Create the application footer."""
        footer_frame = ttk.Frame(self.root, style="Footer.TFrame")
        footer_frame.grid(row=2, column=0, sticky="ew")
        
        # Add status label
        status_label = ttk.Label(footer_frame, 
                               text="Ready", 
                               foreground="#7f8c8d", 
                               background="#ecf0f1")
        status_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Add version label
        version_label = ttk.Label(footer_frame, 
                                text="v1.0.0", 
                                foreground="#7f8c8d", 
                                background="#ecf0f1")
        version_label.pack(side=tk.RIGHT, padx=10, pady=5)
        
    def create_output_frame(self):
        """Create an output frame for displaying results."""
        # Create a PanedWindow to divide the main content and output
        self.paned_window = ttk.PanedWindow(self.root, orient=tk.VERTICAL)
        self.paned_window.grid(row=1, column=0, sticky="nsew")
        
        # Add the existing content to the PanedWindow
        self.paned_window.add(self.root.grid_slaves(row=1, column=0)[0])
        
        # Create the output frame
        self.output_frame = ttk.Frame(self.paned_window)
        self.paned_window.add(self.output_frame)
        
        # Configure the output frame
        self.output_frame.columnconfigure(0, weight=1)
        self.output_frame.rowconfigure(0, weight=0)
        self.output_frame.rowconfigure(1, weight=1)
        
        # Output label
        output_label = ttk.Label(self.output_frame, 
                               text="Output", 
                               style="Category.TLabel")
        output_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
        
        # Output text widget
        self.output_text = tk.Text(self.output_frame, 
                                  wrap=tk.WORD, 
                                  height=10, 
                                  bg="#f9f9f9", 
                                  font=("Consolas", 10))
        self.output_text.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
        
        # Add a scrollbar to the output text
        output_scrollbar = ttk.Scrollbar(self.output_frame, 
                                      orient="vertical", 
                                      command=self.output_text.yview)
        output_scrollbar.grid(row=1, column=1, pady=(0, 10), sticky="ns")
        self.output_text.config(yscrollcommand=output_scrollbar.set)
        
        # Make the output text read-only
        self.output_text.config(state=tk.DISABLED)
        
    def update_output(self, text):
        """Update the output text widget with new text."""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state=tk.DISABLED)
        
    # Wrapper methods for Docker operations with enhanced input dialogs
    def create_dockerfile_wrapper(self):
        path = modern_askstring(self.root, "Dockerfile Path", "Enter path to save Dockerfile (e.g., C:\\docker\\Dockerfile):")
        if not path:
            return
            
        content = modern_text_input(self.root, "Dockerfile Content", "Enter Dockerfile content:")
        if not content:
            return
            
        try:
            with open(path, "w") as f:
                f.write(content)
            messagebox.showinfo("Success", f"Dockerfile created at:\n{path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create Dockerfile:\n{e}")
    
    def build_docker_image_wrapper(self):
        try:
            dockerfile_dir = modern_askstring(self.root, "Dockerfile Directory", "Enter directory path containing Dockerfile:")
            if not dockerfile_dir or not os.path.isdir(dockerfile_dir):
                return messagebox.showerror("Error", "Invalid directory.")
    
            image_name = modern_askstring(self.root, "Image Name", "Enter image name (e.g., myimage):")
            if not image_name:
                return
                
            tag = modern_askstring(self.root, "Image Tag", "Enter tag (e.g., latest):")
            
            import subprocess
            full_tag = f"{image_name}:{tag}" if tag else image_name
            command = ["docker", "build", "-t", full_tag, dockerfile_dir]
            
            # Show a message that building is in progress
            self.update_output(f"Building Docker image '{full_tag}'...\nThis may take a few moments.")
            
            # Run the build process
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            
            # Update the output with the result
            if process.returncode == 0:
                self.update_output(f"Docker image '{full_tag}' built successfully.\n\n{stdout}")
                messagebox.showinfo("Success", f"Docker image '{full_tag}' built successfully.")
            else:
                self.update_output(f"Failed to build Docker image:\n\n{stderr}")
                messagebox.showerror("Error", f"Failed to build image. See output for details.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to build image:\n{e}")

if __name__ == "__main__":
    # Set up the root window
    root = tk.Tk()
    root.title("Cloud Management System")
    
    # Apply a theme
    root.configure(bg="#f0f0f0")
    
    # Create the application
    app = CloudManagerApp(root)
    
    # Run the application
    root.mainloop()
