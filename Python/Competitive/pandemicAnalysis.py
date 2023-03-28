class City:
    def __init__(self, city_id, state_name, city_name, no_of_tests, no_of_positive):
        self.city_id = city_id
        self.state_name = state_name
        self.city_name = city_name
        self.no_of_tests = no_of_tests
        self.no_of_positive = no_of_positive

class PandemicAnalysis:
    def __init__(self, analysis_name, city_list):
        self.analysis_name = analysis_name
        self.city_list = city_list
    
    def get_StateWithMaxPositiveCases(self):

        return 
    
    def get_citiesMoreThanPercentage(self, percentage):
        
        return


if __name__ == "__main__":
    with open("pandemic.txt") as fo:
        n = int(fo.readline())
        city_list = []
        for i in range(n):
            city_id = int(fo.readline())
            state_name = fo.readline()
            city_name = fo.readline()
            no_of_tests = int(fo.readline())
            no_of_positive = int(fo.readline())
            object = City(city_id, state_name, city_name, no_of_tests, no_of_positive)
            city_list.append(object)


        percentage = int(fo.readline())
