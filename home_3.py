import time

class Timer:
    def __init__(self, initial_time):
        self.initial_time = initial_time
        self.current_time = initial_time
        self.running = False

    def get_time(self):
        return self.current_time

    def start(self):
        if not self.running:
            self.running = True
            while self.current_time > 0:
                print(f"Осталось времени: {self.current_time} сек.")
                time.sleep(1)
                self.current_time -= 1
            print("Таймер истек!")
            self.running = False

    def reset(self):
        self.current_time = self.initial_time
        if not self.running:
            print(f"Таймер сброшен Текущее значение: {self.current_time} сек.")

my_timer = Timer(10)

print(f"Текущее значение времени: {my_timer.get_time()} сек.")
my_timer.start()
my_timer.reset()