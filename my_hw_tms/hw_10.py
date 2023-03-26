print('hw_10_task_1')  # class auto с атрибутами


class Auto:

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birth(self):
        self.age += 1

    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight


auto = Auto('Volvo', 5, 'Xc90', 'black', 2300)
auto.birth()
auto.move()
auto.stop()

print('hw_10_task_2')
