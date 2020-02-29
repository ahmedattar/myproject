from models import OrbitPath, NearEarthObject


class NEODatabase(object):
    """
    Object to hold Near Earth Objects and their orbits.

    To support optimized date searching, a dict mapping of all orbit date paths to the Near Earth Objects
    recorded on a given day is maintained. Additionally, all unique instances of a Near Earth Object
    are contained in a dict mapping the Near Earth Object name to the NearEarthObject instance.
    """

    def __init__(self, filename):
        """
        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        """
        # TODO: What data structures will be needed to store the NearEarthObjects and OrbitPaths?
        # TODO: Add relevant instance variables for this.
        self.filename = filename
        self.date_to_neos_map = {}
        self.name_to_neo_map = {}


    def load_data(self, filename=None):
        """
        Loads data from a .csv file, instantiating Near Earth Objects and their OrbitPaths by:
           - Storing a dict of orbit date to list of NearEarthObject instances
           - Storing a dict of the Near Earth Object name to the single instance of NearEarthObject
        :param filename:
        :return:
        """

        if not (filename or self.filename):
            raise Exception('Cannot load data, no filename provided')

        filename = filename or self.filename

        # TODO: Load data from csv file.
        # TODO: Where will the data be stored?
        with open(filename, mode='r') as CSV_File:
            CSV_Reader = csv.DictReader(CSV_File)
            line_count = 0
            for row in CSV_Reader:
                if line_count == 0:
                    line_count = 1
                    continue
                orbit_path = OrbitPath(**row)
                if not self.name_to_neo_map.get(row['name'], None):
                    self.name_to_neo_map[row['name']] = NearEarthObject(**row)

                near_earth_object = self.name_to_neo_map.get(row['name'], None)
                near_earth_object.update_orbits(orbit_path)

                if not self.date_to_neos_map.get(row['close_approach_date'], None):
                    self.date_to_neos_map[row['close_approach_date']] = []

                self.date_to_neos_map[row['close_approach_date']].append(
                    near_earth_object)

        return None

    def get_date_to_neos_map(self):

        # this function returns the date_to_neos_map variable content
        return self.date_to_neos_map

    def get_name_to_neo_map(self):
        # this function returns the name_to_neo_map variable content
        return self.name_to_neo_map

