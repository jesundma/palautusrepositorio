from tkinter import Tk
from kayttoliittyma import Kayttoliittyma
from sovelluslogiikka import Sovelluslogiikka


def main():
    sovellus = Sovelluslogiikka()

    window = Tk()
    window.title("Laskin")

    Kayttoliittyma(sovellus, window)

    window.mainloop()


if __name__ == "__main__":
    main()
