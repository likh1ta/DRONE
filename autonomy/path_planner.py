
class PathPlanner:

    def __init__(self, search_area):

        self.search_area = search_area



    def plan_coverage_path(self):

        print(f"Planning path for area: {self.search_area}")

        

        return [(0, 0), (10, 0), (10, 10), (0, 10)]

