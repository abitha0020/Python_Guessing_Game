from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Number Guessing Game", width=400, height=250)
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.addLabel(text="Guess a number between 1 and 100:", row=0, column=0, columnspan=2, sticky="NSEW")
        self.guess_field = self.addIntegerField(value=0, row=1, column=0, sticky="NSEW")
        self.guess_button = self.addButton(text="Submit Guess", row=1, column=1, command=self.check_guess)
        self.result_label = self.addLabel(text="", row=2, column=0, columnspan=2, sticky="NSEW")
        self.attempts_label = self.addLabel(text="Attempts: 0", row=3, column=0, columnspan=2, sticky="NSEW")
        self.new_game_button = self.addButton(text="New Game", row=4, column=0, columnspan=2, command=self.new_game)
        self.new_game_button["state"] = "disabled"

    def check_guess(self):
        guess = self.guess_field.getNumber()
        self.attempts += 1
        if guess < self.secret_number:
            self.result_label["text"] = "Too low!"
        elif guess > self.secret_number:
            self.result_label["text"] = "Too high!"
        else:
            self.result_label["text"] = "Correct! You guessed the number!"
            self.new_game_button["state"] = "normal"
            self.guess_button["state"] = "disabled"
        self.attempts_label["text"] = f"Attempts: {self.attempts}"

    def new_game(self):
        # Reset the game
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.guess_field.setNumber(0)
        self.result_label["text"] = ""
        self.attempts_label["text"] = "Attempts: 0"
        self.guess_button["state"] = "normal"
        self.new_game_button["state"] = "disabled"

def main():
    GuessingGame().mainloop()

if __name__ == "__main__":
    main()
