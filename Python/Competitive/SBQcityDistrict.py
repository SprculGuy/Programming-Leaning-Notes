# Enter your code here. Read input from STDIN. Print output to STDOUT

class City:
    def __init__(self, pinCode, name, population, area):
        self.pinCode = pinCode
        self.name = name
        self.population = population
        self.area = area


class District:
    def __init__(self, districtName, cityList):
        self.districtName = districtName
        self.cityList = cityList
        
    def findMinimumCityByPinCode(self):
        for city in self.cityList:
            print(city)
        
        return city
    
    def sortCityByPopulation(self):
        pass
    



if __name__ == "__main__":
    with open("sbq.txt") as fo:
        n = int(fo.readline())
        city_objects = []
        for i in range(n):
            pinCode = int(fo.readline())
            name = fo.readline()
            population = int(fo.readline())
            area = int(fo.readline())
            obj = City(pinCode, name, population, area)
            city_objects.append(obj)
        obj1 = District('X', city_objects)
        obj1.findMinimumCityByPinCode()
        obj1.sortCityByPopulation()
         