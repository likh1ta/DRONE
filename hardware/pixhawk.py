class Pixhawk:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.connected = False

    def connect(self):
        print(f"Connecting to Pixhawk on {self.port} at {self.baudrate}")
        self.connected = True

    def arm(self):
        if self.connected:
            print("Arming drone...")
        else:
            print("Pixhawk not connected")

    def takeoff(self, altitude):
        if self.connected:
            print(f"Taking off to {altitude}m")
        else:
            print("Pixhawk not connected")

    def land(self):
        if self.connected:
            print("Landing...")
        else:
            print("Pixhawk not connected")
