#Создаем класс Country с четырьмя свойствами: name (название), s (площадь), capital (столица) и people (количество населения)
class Country:
    def __init__(self, name, s, capital, people):
        self._name = name
        self._s = s
        self._capital = capital
        self._people = people
# Каждое свойство определено с использованием декоратора @property, который позволяет получать доступ к значениям этих свойств и задавать новые значения с помощью сеттеров
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def capital(self):
        return self._capital

    @capital.setter
    def capital(self, new_capital):
        self._capital = new_capital

    @property
    def people(self):
        return self._people

    @people.setter
    def people(self, new_people):
        self._people = new_people

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, new_s):
        self._s = new_s

# Создание экземпляра объекта класса Country
cntr = Country('Беларусь', 207600, 'Минск', 9000034)

# Вывод информации об объекте
print(f'Название: {cntr.name}')
print(f'Площадь: {cntr.s}')
print(f'Столица: {cntr.capital}')
print(f'Кол-во населения: {cntr.people}')

# Изменение значений свойств с помощью сеттеров
cntr.name = 'Турция'
cntr.s = 783562
cntr.capital = 'Анкара'
cntr.people = 84000078

# Вывод измененной информации об объекте
print(f'Другая страна: {cntr.name}')
print(f'Площадь: {cntr.s}')
print(f'Столица: {cntr.capital}')
print(f'Кол-во населения: {cntr.people}')