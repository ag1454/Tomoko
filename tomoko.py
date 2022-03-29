# tomoko2.py
# Abigail Garrido

# This program lets you play a Tamagotchi-like game.
# Do what Tomoko wants quickly or else she will leave.

# "black market tamagotchi"
# i like games and thought it would be fun to code
# BUTTONS...THOSE BUTTONS...AND GRAPHICS
# wanted to add a timer

import random
from random import choice, randint
import time
from graphics import *

def titleScreen(win):
    title_image = Image(Point(25, 40), "Title.gif")
    title_image.draw(win)

    instructions = Text(Point(25, 23), "Do what Tomoko wants before"
                        + " she leaves!")
    instructions.draw(win)
    instructions.setFace("courier")
    instructions.setStyle("italic")

    start_button = Rectangle(Point(20, 10), Point(30, 5))
    start_button.draw(win)
    start_button.setFill(color_rgb(255, 153, 204))

    start_text = Text(Point(25, 7.5), "START")
    start_text.draw(win)

    while True:
        click = win.getMouse()
        click_x = click.getX()
        click_y = click.getY()

        if (click_x > 20 and click_x < 30 and click_y > 5 and click_y < 10):
            title_image.undraw()
            instructions.undraw()
            start_button.undraw()
            start_text.undraw()
            break
    
def buttonText(win):
    one = "FEED"
    two = "PET"
    three = "PLAY"

    words = ["FEED", "PET", "PLAY"]
    word1 = random.choice(words)
    words.remove(word1)
    word2 = random.choice(words)
    words.remove(word2)
    word3 = random.choice(words)

    return word1, word2, word3

def clickButtons(click_x, click_y, word, word1, word2, word3):
    if (word1 == word and click_x > 3 and click_x < 13 and
                click_y > 5 and click_y < 10):
        return True
    elif (word2 == word and click_x > 20 and click_x < 30 and
            click_y > 5 and click_y < 10):
        return True
    elif (word3 == word and click_x > 37 and click_x < 47 and
            click_y > 5 and click_y < 10):
        return True

def wrongButton(click_x, click_y, word, word1, word2, word3):
    if (word1 != word and click_x > 3 and click_x < 13 and
                click_y > 5 and click_y < 10):
        return True
    elif (word2 != word and click_x > 20 and click_x < 30 and
            click_y > 5 and click_y < 10):
        return True
    elif (word3 != word and click_x > 37 and click_x < 47 and
            click_y > 5 and click_y < 10):
        return True

def actTomoko(win, status, standby_bars, tomoko_image1, tomoko_image2,
               word1, word2, word3, choice):
    tomoko_image1.undraw()
    tomoko_image2.undraw()
    count = 0
    standby_bars.undraw()

    if (choice == 1):
        word = "FEED"
        standby_bars = Image(Point(25, 45), "Hungry1.gif")
        standby_bars.draw(win)

        status.setText("Tomoko is hungry! Feed her!")

        hungry_tomoko = Image(Point(25, 30), "Hungry.gif")
        hungry_tomoko.draw(win)
    elif (choice == 2):
        word = "PET"
        standby_bars = Image(Point(25, 45), "Happiness1.gif")
        standby_bars.draw(win)

        status.setText("Tomoko looks sad... Give her a pet!")

        sad_tomoko = Image(Point(25, 30), "Sad.gif")
        sad_tomoko.draw(win)
    else:
        word = "PLAY"
        standby_bars = Image(Point(25, 45), "Interest1.gif")
        standby_bars.draw(win)

        status.setText("Tomoko looks bored... Play with her!")

        bored_tomoko = Image(Point(25, 30), "Bored.gif")
        bored_tomoko.draw(win)
    
    while True:
        click = win.getMouse()
        click_x = click.getX()
        click_y = click.getY()

        if (clickButtons(click_x, click_y, word, word1, word2, word3)):
            status.setText("Good job!")
            standby_bars.undraw()
            standby_bars = Image(Point(25, 45), "Standby-Bars.gif")
            standby_bars.draw(win)

            if (choice == 1):
                hungry_tomoko.undraw()
            elif (choice == 2):
                sad_tomoko.undraw()
            else:
                bored_tomoko.undraw()

            for i in range (3):
                tomoko_happy1 = Image(Point(25, 30), "Happy-Tomoko.gif")
                tomoko_happy1.draw(win)
                time.sleep(1)
                tomoko_happy1.undraw()
                tomoko_happy2 = Image(Point(25, 30), "Happy-Tomoko-I.gif")
                tomoko_happy2.draw(win)
                time.sleep(1)
                tomoko_happy2.undraw()
            status.undraw()
            standby_bars.undraw()
            break
        elif (wrongButton(click_x, click_y, word, word1, word2, word3)):
            status.setText("That's not what Tomoko wants!")
            standby_bars.undraw()
            count = count + 1

            if (choice == 1):
                standby_bars = Image(Point(25, 45), "Hungry2.gif")
                standby_bars.draw(win)
            elif (choice == 2):
                standby_bars = Image(Point(25, 45), "Happiness2.gif")
                standby_bars.draw(win)
            else:
                standby_bars = Image(Point(25, 45), "Interest2.gif")
                standby_bars.draw(win)

            if (count == 2):
                if (choice == 1):
                    hungry_tomoko.undraw()
                    standby_bars.undraw()
                    return False
                elif (choice == 2):
                    sad_tomoko.undraw()
                    standby_bars.undraw()
                    return False
                else:
                    bored_tomoko.undraw()
                    standby_bars.undraw()
                    return False

def choiceMade(choice, feed, pet, play, win, status, standby_bars,
               tomoko_image1, tomoko_image2):
    word1, word2, word3 = buttonText(win)
    text1 = Text(Point(8, 7.5), word1)
    text1.draw(win)
    text2 = Text(Point(25, 7.5), word2)
    text2.draw(win)
    text3 = Text(Point(42, 7.5), word3)
    text3.draw(win)

    if (choice == 1):
        feed = actTomoko(win, status, standby_bars, tomoko_image1,
                      tomoko_image2, word1, word2, word3, choice)
    elif (choice == 2):
        pet = actTomoko(win, status, standby_bars, tomoko_image1,
                            tomoko_image2, word1, word2, word3, choice)
    else:
        play = actTomoko(win, status, standby_bars, tomoko_image1,
                            tomoko_image2, word1, word2, word3, choice)
        
    text1.undraw()
    text2.undraw()
    text3.undraw()

    return feed, pet, play

def main():
    win = GraphWin("Tomoko", 500, 500)
    win.setCoords(0, 0, 50, 50)
    win.setBackground(color_rgb(250, 250, 250))

    titleScreen(win)

    button1 = Rectangle(Point(3, 10), Point(13, 5))
    button1.draw(win)
    button1.setFill(color_rgb(255, 153, 204))
    button2 = Rectangle(Point(20, 10), Point(30, 5))
    button2.draw(win)
    button2.setFill(color_rgb(255, 153, 204))
    button3 = Rectangle(Point(37, 10), Point(47, 5))
    button3.draw(win)
    button3.setFill(color_rgb(255, 153, 204))

    while True:    
        status = Text(Point(25, 16), "Tomoko is currently pleased with you.")
        status.draw(win)
        status.setFace("courier")

        feed = True
        pet = True
        play = True

        standby_bars = Image(Point(25, 45), "Standby-Bars.gif")
        standby_bars.draw(win)

        for i in range(3):
            tomoko_image1 = Image(Point(25, 30), "Tomoko.gif")
            tomoko_image1.draw(win)
            time.sleep(1)
            tomoko_image1.undraw()
            tomoko_image2 = Image(Point(25, 30), "Tomoko-I.gif")
            tomoko_image2.draw(win)
            time.sleep(1)
            tomoko_image2.undraw()

        choice = randint(1, 3)

        feed, pet, play = choiceMade(choice, feed, pet, play, win, status,
                                     standby_bars, tomoko_image1,
                                     tomoko_image2)

        if (feed == False or pet == False or play == False):
            button1.undraw()
            button2.undraw()
            button3.undraw()
            note = Image(Point(25, 35), "Gameover.gif")
            note.draw(win)
            status.setText("You later find a note from Tomoko." +
                           "\nShe has left to find a better owner." +
                           "\nClick anywhere to close.")
            break

    win.getMouse()
    win.close()

main()
