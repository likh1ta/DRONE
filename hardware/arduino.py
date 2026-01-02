class Arduino:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.connected = False

    def connect(self):
        print(f"Connecting to Arduino on {self.port} at {self.baudrate}")
        self.connected = True

    def drop_payload(self):
        if self.connected:
            print("Dropping payload...")
        else:
            print("Arduino not connected")
