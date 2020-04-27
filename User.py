class User:

    def __init__(self, name, city, email, post_code, country, users=list()):#Создание class User с его аргументами
        self.users = users
        self.name = name
        self.city = city
        self.email = email
        self.post_code = post_code
        self.country = country

    def addUserInArray(self): #Метод class User который добавляет пользователя в временный лист mas и потом добавляет его в главный лист users
        mas = list()
        mas.append(self.name)
        mas.append(self.city)
        mas.append(self.email)
        mas.append(self.post_code)
        mas.append(self.country)
        self.users.append(mas)
        print("\n User {} added".format(self.name))

    def findUser(self, name): #Метод class User который ищет пользователя по name (Дополнительный метод который нигде не вызывается,но я его добавил)
        for i in self.users.__iter__():
            if name == i[0]:
                print(i)

    def removeUser(self, name): #Метод class User который удаляет пользователя принимает параметр name (Имя пользователя)
        for i in self.users.__iter__():
            if name == i[0]:
                self.users.remove(i)
                print("\n User {}".format(name) + ' deleted')

    def Print(self): #Метод class User который выводит всех пользователей в красивом виде
        for i in self.users.__iter__():
            print(
                '\n Name: {}\n City: {}\n Email: {}\n Postal Code: {}\n Country: {}'.format(i[0], i[1], i[2], i[3], i[4]))

