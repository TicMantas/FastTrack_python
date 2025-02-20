import random

tank = [4, 4]
target = [1, 8]


class Warzone:
    def __init__(self, tank, target):
        self.tank = tank
        self.target = target
        self.tank_direction = "^"

    def update_tank_direction(self, direction):
        self.tank_direction = direction

    def draw_map(self):
        for i in range(10):
            for y in range(10):
                if (i, y) == tuple(self.tank):
                    print(self.tank_direction, end=" ")
                elif (i, y) == tuple(self.target):
                    print("o", end=" ")
                else:
                    print("_", end=" ")
            print()
        print()


class Tank:
    def __init__(self, tank, war_zone):
        self.tank = tank
        self.war_zone = war_zone

    def move_tank(self, move):
        if move == "w":
            if self.tank[0] > 0:
                self.tank[0] -= 1
            self.war_zone.update_tank_direction("^")
        elif move == "s":
            if self.tank[0] < 9:
                self.tank[0] += 1
            self.war_zone.update_tank_direction("v")
        elif move == "a":
            if self.tank[1] > 0:
                self.tank[1] -= 1
            self.war_zone.update_tank_direction("<")
        elif move == "d":
            if self.tank[1] < 9:
                self.tank[1] += 1
            self.war_zone.update_tank_direction(">")
        elif move == "e":
            self.check_hit()
        else:
            print("*******************Invalid move*************************")

    def check_hit(self):
        if (self.tank[1] == target[1]) and self.war_zone.tank_direction in ["^", "v"]:
            print("Direct hit! Target destroyed!")
            self.war_zone.target[0] = random.randint(0, 9)
            self.war_zone.target[1] = random.randint(0, 9)
        elif (self.tank[0] == target[0]) and self.war_zone.tank_direction in ["<", ">"]:
            print("Direct hit! Target destroyed!")
            self.war_zone.target[0] = random.randint(0, 9)
            self.war_zone.target[1] = random.randint(0, 9)
        else:
            print("Missed the target!")

class Game:
    def __init__(self):
        self.war_zone = Warzone(tank, target)
        self.tank = Tank(tank, self.war_zone)

    def play(self):
        while True:
            self.war_zone.draw_map()
            move = input("Enter your move (up(w), down(s), right(d), left(a), fire(e), quit(q)): ").lower()
            if move == "q":
                print("Quitting the game. Goodbye!")
                break
            self.tank.move_tank(move)


# Run the game
if __name__ == "__main__":
    game = Game()
    game.play()