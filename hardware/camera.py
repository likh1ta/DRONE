class Camera:
    def __init__(self, camera_id, resolution):
        self.camera_id = camera_id
        self.resolution = resolution
        self.active = False

    def start(self):
        print(f"Starting camera {self.camera_id} with resolution {self.resolution}")
        self.active = True

    def capture_frame(self):
        if self.active:
            print("Capturing frame...")
            return "frame_data"
        else:
            print("Camera not active")
            return None

    def stop(self):
        print("Stopping camera")
        self.active = False
