
import json

import time

from hardware.pixhawk import Pixhawk

from hardware.camera import Camera

from hardware.lidar import Lidar

from autonomy.path_planner import PathPlanner

from autonomy.detector import Detector

from autonomy.avoidance import Avoidance

from utils.logger import setup_logger



def load_config(config_path):

    with open(config_path, 'r') as f:

        return json.load(f)



def main():

    config = load_config('config/config.json')

    logger = setup_logger(config['logging']['file'], config['logging']['level'])



    logger.info("Initializing Disaster Drone System...")



    

    pixhawk = Pixhawk(config['hardware']['pixhawk']['port'], config['hardware']['pixhawk']['baudrate'])

    camera = Camera(config['hardware']['camera']['id'], config['hardware']['camera']['resolution'])

    lidar = Lidar(config['hardware']['lidar']['port'], config['hardware']['lidar']['baudrate'])



    pixhawk.connect()

    camera.start()

    lidar.start()



    

    planner = PathPlanner(config['autonomy']['search_area'])

    detector = Detector()

    avoidance = Avoidance(2.0) 



    

    pixhawk.arm()

    pixhawk.takeoff(config['autonomy']['altitude'])



    path = planner.plan_coverage_path()



    for waypoint in path:

        logger.info(f"Moving to waypoint: {waypoint}")

        



        distance = lidar.get_distance()

        if avoidance.check_obstacle(distance):

            logger.warning("Obstacle detected!")

            



        frame = camera.capture_frame()

        if detector.detect_person(frame):

            logger.info("Person detected!")

            



        time.sleep(1)



    pixhawk.land()

    camera.stop()

    logger.info("Mission completed.")



if __name__ == "__main__":

    main()

