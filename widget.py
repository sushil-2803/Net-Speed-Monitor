import tkinter as tk
import psutil
import wmi
import threading
import time

class NetSpeedWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("NetSpeed")
        self.root.geometry("200x80+100+100")
        self.root.overrideredirect(True)  # Creates a borderless window
        self.root.attributes("-topmost", True)
        self.root.configure(bg='black')
        self.root.attributes("-alpha", 0.8) # Set window transparency

        self.last_upload = 0
        self.last_download = 0
        self.upload_speed = "0 B/s"
        self.download_speed = "0 B/s"

        self.network_interface = self.get_active_network_interface()

        # Create and pack the labels
        self.upload_label = tk.Label(root, text=f"↑ {self.upload_speed}", font=("Helvetica", 12), bg="black", fg="white")
        self.upload_label.pack(pady=(10, 0))

        self.download_label = tk.Label(root, text=f"↓ {self.download_speed}", font=("Helvetica", 12), bg="black", fg="white")
        self.download_label.pack(pady=(0, 10))
        
        # Make the window draggable
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<ButtonRelease-1>", self.stop_move)
        self.root.bind("<B1-Motion>", self.do_move)

        # Start the network monitoring in a separate thread
        self.monitor_thread = threading.Thread(target=self.update_speed, daemon=True)
        self.monitor_thread.start()

    def get_active_network_interface(self):
        """Identifies the primary active network interface."""
        try:
            c = wmi.WMI()
            query = "SELECT * FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled = True"
            for interface in c.query(query):
                # This logic can be adjusted to more robustly find the primary interface
                if interface.DefaultIPGateway:
                    return interface.Description
        except Exception as e:
            print(f"Could not get network interface: {e}")
            return None

    def update_speed(self):
        """Continuously updates the network speed."""
        while True:
            net_io = psutil.net_io_counters(pernic=True)
            if self.network_interface in net_io:
                interface_stats = net_io[self.network_interface]
                
                upload = interface_stats.bytes_sent
                download = interface_stats.bytes_recv

                if self.last_upload > 0:
                    self.upload_speed = self.format_speed(upload - self.last_upload)
                if self.last_download > 0:
                    self.download_speed = self.format_speed(download - self.last_download)

                self.last_upload = upload
                self.last_download = download

                # Update the GUI from the main thread
                self.root.after(0, self.update_labels)

            time.sleep(1)

    def update_labels(self):
        """Updates the text of the labels in the GUI."""
        self.upload_label.config(text=f"↑ {self.upload_speed}")
        self.download_label.config(text=f"↓ {self.download_speed}")

    def format_speed(self, speed_bytes):
        """Formats the speed from bytes per second to a readable format."""
        if speed_bytes < 1024:
            return f"{speed_bytes} B/s"
        elif speed_bytes < 1024**2:
            return f"{speed_bytes / 1024:.2f} KB/s"
        elif speed_bytes < 1024**3:
            return f"{speed_bytes / 1024**2:.2f} MB/s"
        else:
            return f"{speed_bytes / 1024**3:.2f} GB/s"
    
    # --- Window Dragging Functions ---
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = NetSpeedWidget(root)
    root.mainloop()