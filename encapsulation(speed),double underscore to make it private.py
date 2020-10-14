class Speed:
    def __init__(self):
        self.speed=10
        self.__speed_new=80

#double underescore to make the things private __speed_new
    def display(self):
        print("speed:",self.speed)
        print("speed:",self.__speed_new)
#speed can be made private,but still can be modified
#to solve this getters and setters are used
si=Speed()
si.speed=100
print(si.speed)
si.__speed_new=120
print(si.__speed_new)