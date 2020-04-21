"""
класс TrafficLight (светофор)
    атрибут color (цвет)
    метод running (запуск)
    переменная для подсчета i
    цикл while для переключнения
    вызов модуля time.sleep(сек) - приостановить выполнение программы на заданное количество секунд.
    создать экземпляр
    вызвать описанный метод
    Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
    выводить соответствующее сообщение и завершать скрипт.
    """

from time import sleep



class TrafficLight:
    __color = ['Red', 'Yellow', 'Green', 'Yellow']

    def running(self):
        i = 0
        while i < 4:
            print(f'переключение светофора\n 'f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            elif i == 3:
                sleep(2)
            i += 1

t = TrafficLight()
t.running()
print(t._TrafficLight__color)
