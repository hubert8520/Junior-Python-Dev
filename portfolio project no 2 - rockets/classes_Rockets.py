'''
Part 1:
- Exercise's aim: create a class of rocket which can go upwards by random value
- To do:
    *Think about which attributes and which methods should rocket have;
    *Create all of these attributes and methods and then create 5 objects
        of class "Rocket" with starting point 0;
    *After that, randomly pick one of those 5 rockets and move it upwards.
        Do this step 10 times and check which of the rockets got to the highest
        position.

Part 2:
- To do:
    *Create a class for a board on which Rockets will move. Think about its
        attributes it should have.
'''
import random
from math import sqrt


class Rocket:
    nextId = 1

    def __init__(self, position_x=0, position_y=0, speed=1):
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
        self.rocketId = Rocket.nextId
        Rocket.nextId += 1

    def move_upwards(self):
        self.position_y += self.speed

    def __str__(self):
        return "Rocket" + str(self.rocketId) + " is on height of " + str(self.position_y)


class RocketBoard:
    height = 800
    width = 600
    listOfRockets = []

    def __init__(self, amountOfRockets: int = 5):
        self.listOfRockets = [Rocket(speed=random.randint(1, 3))
                              for _ in range(amountOfRockets)]

        for _ in range(10):
            # pick a rocket to move
            indexOfRocketToMove = random.randint(
                0, amountOfRockets-1)

            # move picked rocket
            self.listOfRockets[indexOfRocketToMove].move_upwards()

        for rocket in self.listOfRockets:
            print(rocket)

    def __getitem__(self, key):
        return self.listOfRockets[key]

    def __setitem__(self, key, value):
        self.listOfRockets[key].position_y = value

    @staticmethod
    def get_distance_between_rockets(rocket1: Rocket(), rocket2: Rocket()):
        x = abs(rocket1.position_x - rocket2.position_x) ** 2
        y = abs(rocket1.position_y - rocket2.position_y) ** 2
        return sqrt(x + y)
