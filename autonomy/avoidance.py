class Avoidance:
    def __init__(self, min_distance):
        self.min_distance = min_distance

    def check_obstacle(self, distance):
        if distance < self.min_distance:
            print("Obstacle detected! Initiating avoidance maneuver.")
            return True
        return False
