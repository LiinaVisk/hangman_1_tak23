import time

class GameTime:
    def __init__(self, lbl_time):
        # Konstruktor, initsialiseerib mänguaja objekti
        self.__lbl_time = lbl_time
        self.__counter = 0
        self.__running = False

    @property
    def counter(self):
        # Tagastab mänguaja loenduri väärtuse
        return self.__counter

    def update(self):
        # Värskendab mänguaega ja kuvab selle sildil
        if self.__running:
            if self.__counter == 0:
                display = "00:00:00"
            else:
                display = time.strftime("%H:%M:%S", time.gmtime(self.__counter))

            self.__lbl_time["text"] = display
            self.__lbl_time.after(1000, self.update)
            self.__counter += 1

    def start(self):
        # Algatab mänguaja loenduri värskendamise
        self.__running = True
        self.update()

    def stop(self):
        # Peatab mänguaja loenduri värskendamise
        self.__running = False

    def reset(self):
        # Lähtestab mänguaja loenduri ja kuvab selle algväärtuseks
        self.__counter = 0
        self.__lbl_time["text"] = "00:00:00"
