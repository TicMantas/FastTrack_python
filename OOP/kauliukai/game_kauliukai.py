import random

class Player:
    def __init__(self, name):
        self._name = name
        self._history = []    # Saugo kiekvieno raundo rezultatus
        self._total_score = 0 # Bendras taškų skaičius

    @property
    def name(self):
        return self._name

    @property
    def history(self):
        return self._history

    @property
    def total_score(self):
        return self._total_score

    def add_round(self, round_result):
        """Prideda naujo raundo rezultatą ir atnaujina bendrą rezultatą."""
        self._history.append(round_result)
        self._total_score += sum(round_result)

class DiceGame:
    def __init__(self):
        self.players = []
        self.dice_count = 0
        self.dice_faces = []
        self.rounds = 10

    def get_game_config(self):
        # Įvedame kauliukų skaičių (1-5)
        while True:
            try:
                self.dice_count = int(input("Įveskite kauliukų skaičių (1-5): "))
                if 1 <= self.dice_count <= 5:
                    break
                else:
                    print("Prašome įvesti skaičių tarp 1 ir 5.")
            except ValueError:
                print("Neteisinga įvestis. Bandykite dar kartą.")

        # Įvedame kiekvieno kauliuko puselių skaičių (1-100)
        for i in range(self.dice_count):
            while True:
                try:
                    faces = int(input(f"Enter {i+1}-ojo kauliuko puselių skaičių (1-100): "))
                    if 1 <= faces <= 100:
                        self.dice_faces.append(faces)
                        break
                    else:
                        print("Enter a valid number. From 1 to 100.")
                except ValueError:
                    print("invalidate input. please enter a valid number.")

    def add_players(self):
        # Įvedame žaidėjų skaičių
        while True:
            try:
                num_players = int(input("Enter number of players: "))
                if num_players > 0:
                    break
                else:
                    print("Number of players must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Sukuriame žaidėjų objektus
        for i in range(num_players):
            name = input(f"Enter {i+1} player name : ")
            self.players.append(Player(name))

    def play(self):
        print("\nGame Start!")
        # Vykdome 10 raundų
        for round_number in range(1, self.rounds + 1):
            print(f"\nRound {round_number}:")

            for player in self.players:
                round_result = []
                for faces in self.dice_faces:
                    roll = random.randint(1, faces)
                    round_result.append(roll)
                player.add_round(round_result)
                print(f"{player.name} Play: {round_result} | Sum: {sum(round_result)}")

    def get_winner(self):
        if not self.players:
            return None
        max_score = max(player.total_score for player in self.players)
        winners = [player for player in self.players if player.total_score == max_score]
        return winners

    def print_history(self):
        print("\nGame History:")
        for player in self.players:
            print(f"\n{player.name}:")
            for i, round_result in enumerate(player.history, 1):
                print(f"  Raundas {i}: {round_result} | Sum: {sum(round_result)}")
            print(f"  Result: {player.total_score}")

def main():
    game = DiceGame()
    game.get_game_config()
    game.add_players()
    game.play()
    game.print_history()

    winners = game.get_winner()
    if winners:
        if len(winners) == 1:
            print(f"\nWinner: {winners[0].name} su {winners[0].total_score} points!")
        else:
            print("\nEqual game:")
            for player in winners:
                print(f"  {player.name} - {player.total_score} points")

if __name__ == "__main__":
    main()
