import unittest
from hardware.pixhawk import Pixhawk
from hardware.camera import Camera

class TestHardware(unittest.TestCase):
    def test_pixhawk_connection(self):
        pixhawk = Pixhawk("/dev/ttyACM0", 57600)
        pixhawk.connect()
        self.assertTrue(pixhawk.connected)

    def test_camera_activation(self):
        camera = Camera(0, [1920, 1080])
        camera.start()
        self.assertTrue(camera.active)

if __name__ == '__main__':
    unittest.main()
