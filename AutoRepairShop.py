class AutoRepairShop:


    def __init__(self, company_name, car_mark, city, post_code, country, cars=list()): #Создание class AutoRepairShop с его аргументами
        self.cars = cars
        self.company_name = company_name
        self.car_mark = car_mark
        self.city = city
        self.post_code = post_code
        self.country = country

    def addCarInArray(self): #Метод class AutoRepairShop который создает автомастерскую
        mas = list()
        mas.append(self.company_name)
        mas.append(self.car_mark)
        mas.append(self.city)
        mas.append(self.post_code)
        mas.append(self.country)
        self.cars.append(mas)
        print("\n Auto repair shop {} added".format(self.company_name))

    def findCar(self, name): #Метод class AutoRepairShop который ищет автомастерскую по Сity
        for i in self.cars.__iter__():
            if name == i[2]:
                print('\n Company Name: {}\n Car Mark: {}\n City: {}\n Postal Code: {}\n Country: {}'.format(i[0], i[1], i[2], i[3], i[4]))

    def removeCar(self, name): #Метод class AutoRepairShop который принимает параметр Company Name и удаляет автомастерскую)
        for i in self.cars.__iter__():
            if name == i[0]:
                self.cars.remove(i)
                print(" Auto repair shop {}".format(name) + ' deleted')

    def PrintCar(self): #Метод class AutoRepairShop который делает вывод автмастерской в красивом виде
        for i in self.cars.__iter__():
            print('\n Company Name: {}\n Car Mark: {}\n City: {}\n Postal Code: {}\n Country: {}'.format(i[0], i[1], i[2], i[3], i[4]))