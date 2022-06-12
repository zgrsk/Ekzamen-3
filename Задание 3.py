class Tomato:
    # Статическое свойство
    states = {0: 'Посадка', 1: 'Росток', 2: 'Зеленый помидор', 3: 'Красный помидор'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Выращиваем помидоры
    def grow(self):
        if self._state < 3:
            self._state += 1
        print('Помидор', self._index, '-', Tomato.states[self._state])

    # Проверяем зрелость
    def is_ripe(self):
        if self._state == 3:
            return True
        return False


class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()
        print('Садовник закончил')

    # Собираем урожай
    def harvest(self):
        print('Садовник собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая закончен')
        else:
            print('Слишком рано. Помидоры еще не зрелые.')

    # Статический метод
    @staticmethod
    def knowledge_base():
        print('''В лунку при посадке рекомендуется добавить 0,5-1 ч.л суперфосфата, затем хорошо пролить лунку, 
чтобы гранулы удобрения смешались с почвой и не обожгли корни растений. 
После высадки в грунт рассаду хорошо поливают и оставляют в покое примерно на неделю.
В дальнейшем томаты поливают раз в 7 дней. Норма расхода воды: для низкорослых сортов – 2–3 л на куст, 
для среднерослых – 5–7 л, для высокорослых – 10 л. По возможности используйте капельный полив. 
Поливать необходимо регулярно  по мере необходимости- томат любит хорошее увлажнение почвы 
и умеренную влажность воздуха. Если в теплице ощущается духота, необходимо проветрить. 
Поливать помидоры лучше всего ранним утром, под корень.''')


Gardener.knowledge_base()
tomato_bush_1 = TomatoBush(4)
gardener = Gardener('Роберт', tomato_bush_1)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
