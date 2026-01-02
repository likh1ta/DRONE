
class Lidar:

    def __init__(self, port, baudrate):

        self.port = port

        self.baudrate = baudrate

        self.active = False



    def start(self):

        print(f"Starting LiDAR on {self.port} at {self.baudrate}")

        self.active = True



    def get_distance(self):

        if self.active:

            

            return 10.0

        else:

            print("LiDAR not active")

            return -1

