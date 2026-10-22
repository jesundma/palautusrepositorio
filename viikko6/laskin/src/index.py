from tkinter import Tk
from kayttoliittyma import Kayttoliittyma
from sovelluslogiikka import Sovelluslogiikka


def main():
    sovellus = Sovelluslogiikka()

    window = Tk()
    window.title("Laskin")

    kayttoliittyma = Kayttoliittyma(sovellus, window) #adding comment to make pylint fail for too long line but now it is 100 chars so have to write really long line
    kayttoliittyma.kaynnista()

    window.mainloop()

if __name__ == "__main__":
    main()
