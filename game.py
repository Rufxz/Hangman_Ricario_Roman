from random import *
from tkinter import *
from tkinter import messagebox
from sqdb import Database


# check if user won or lost
def check_win(gui, g):
    if g.hidden_word == list(g.word):
        gui.message_win(g)
    elif g.attempts >= 11:
        gui.message_lose(g)


# check if input (letter) is right
def check_letter(gui, game, letter):
    if letter in game.word:
        game.replace_letters(letter)
    elif game.attempts <= 10:
        game.attempts += 1

    gui.draw()
    check_win(gui, game)


# turn word to list of underscores "_"
def hide_letters(string):
    hidden_letters = []
    for i in range(len(string)):
        hidden_letters.append("_")

    return hidden_letters


class TouchIntoDatabase:
    def __init__(self):
        self.db = Database("Hangman.db")

    def get_valid_word_to_be_execute(self):
        value = self.db.get_valid_guessing_word(randint(1, 7))
        the_word = str(value[-1])
        return the_word


class Game:
    def __init__(self, word):
        messagebox.showinfo("Welcome to Hangman", "By Roman & Ricario")
        self.attempts = 0
        self.options = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U",
                        "V",
                        "W", "X", "Y", "Z"]
        self.word = word
        self.hidden_word = hide_letters(word)

    # reset the values of the game
    def restart(self, word):
        self.attempts = 0
        self.word = word
        self.hidden_word = hide_letters(word)

    # change hidden_word's guessed letter
    def replace_letters(self, letter):
        for i in range(len(self.word)):
            if letter == self.word[i]:
                del self.hidden_word[i]
                self.hidden_word.insert(i, letter)


class Gui:
    def __init__(self, game):
        self.game = game
        self.window = Tk()
        self.window.geometry("850x500")
        self.dbd = TouchIntoDatabase()
        self.window.title("Hangman")
        self.photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"),
                       PhotoImage(file="images/hang2.png"),
                       PhotoImage(file="images/hang3.png"),
                       PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
                       PhotoImage(file="images/hang6.png"),
                       PhotoImage(file="images/hang7.png"),
                       PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"),
                       PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

        self.button_container = Frame(self.window, relief=RAISED)
        self.button_container.place(x=30, y=450)

        self.image = Label(self.window, image=self.photos[game.attempts])
        self.image.place(x=50, y=50)

        self.score = Label(self.window, text=' '.join(game.hidden_word), font=("Comic Sans", 15))
        self.score.place(x=350, y=300)

        # create a buttons with options " A, B, C... "
        for letter in game.options:
            Button(self.button_container, text=letter, command=lambda l=letter, g=game: check_letter(self, game, l),
                   font=("Comic Sans", 15),
                   state=ACTIVE).pack(side=LEFT)

        self.window.mainloop()

    # draw a hangman and hidden word
    def draw(self):
        self.image.config(image=self.photos[self.game.attempts])
        self.score.config(text=' '.join(self.game.hidden_word))

    # show win message
    def message_win(self, game):
        if messagebox.askyesno(title="Hangman", message="You won! Restart?"):

            game.restart(self.dbd.get_valid_word_to_be_execute())
            self.draw()
        else:
            exit()

    # show lose message
    def message_lose(self, game):
        if messagebox.askyesno(title="Hangman", message="You lost! Restart?"):

            game.restart((self.dbd.get_valid_word_to_be_execute()))
            self.draw()
        else:
            exit()


touch = TouchIntoDatabase()
hangman = Game(touch.get_valid_word_to_be_execute())
view = Gui(hangman)
