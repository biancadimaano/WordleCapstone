import turtle
from xml.etree.ElementTree import TreeBuilder  # An included library with Python install.
import random

word_dic = open("python word dictionary.txt", "r")

word_dic_list = word_dic.readlines()

#Setting up the game window.
turtle.title("Capstone Game - Bianca Dimaano")
turtle.bgcolor("black")
turtle.setup(width=500, height=500)

#Function for writing text, including the text colour, location on screen, alignment on screen, font, size, and emphasis (bold,italics,etc.).
def write_text(textcol,x_axis,y_axis,texttitle,textalign,textfont,size,emphasis):
    text = turtle.Turtle()
    text.speed(0)
    text.color(textcol)
    text.penup()
    text.hideturtle()
    text.setposition(x_axis,y_axis)
    text.write(texttitle, align=textalign, font=(textfont, size, emphasis))

#Text for the title.
write_text("white", 0, 210, "Welcome to WORDLE by Bianca!", "center", "Verdana", 15, "bold")
write_text("white", 0, 190, "Guess the 5 letter word in 6 tries or less!", "center", "Verdana", 10, "normal")

#Text for the rules.
write_text("gray35", -120, 160, "GRAY LETTER", "left", "Verdana", 10, "bold")
write_text("white", 45, 160, "= is not in the word", "center", "Verdana", 10, "normal")
write_text("gold2", -185, 145, "YELLOW LETTER", "left", "Verdana", 10, "bold")
write_text("white", 65, 145, "= is in the word, but in the wrong spot", "center", "Verdana", 10, "normal")
write_text("lime green", -165, 130, "GREEN LETTER", "left", "Verdana", 10, "bold")
write_text("white", 65, 130, "= is in the word, in the correct spot!", "center", "Verdana", 10, "normal")

#The word that must be guessed.
guess_this_word = random.choice(word_dic_list)
#Will turn the word that must be guessed into a list.
word_list = list(guess_this_word.lower())
#X coordinates for where each letter is written on the screen.
guess_x_axis = [-60, -30, 0, 30, 60]
#Tracks how many guesses have been made.
guess_total = 0
#Y coordinates for the word, will change when a new word is guessed so that it will be written
#below the last word.
y_axis_guesses = 0
#List of the user's guesses.
guess_list = []
#Creates a dictionary, will correlate each of the letters in the user's guess with its index number.
guess_letter_keys = {}
#Separates the letters in the user's guess and adds it to a list.
word_guess = []

#Creates a list, the colour corresponding to each guess will be added to this list.
colours_of_guess = [[] for i in range(6)]
#Makes a list full of zeroes, will then get updated to track how many correct (green) letters are in the user's guesses.

def green_letter(guess_index):
    colours_of_guess[guess_index].append("green")
    write_letter = word_guess[guess_index][(guess_letter_keys[word_guess[guess_index][i]]-1)]
    write_text("lime green", guess_x_axis[i], 100-y_axis_guesses, write_letter.upper(), "center", "Verdana", 30, "bold")

def yellow_letter(guess_index):
    colours_of_guess[guess_index].append("yellow")
    write_letter = word_guess[guess_index][(guess_letter_keys[word_guess[guess_index][i]]-1)]
    write_text("gold2", guess_x_axis[i], 100-y_axis_guesses, write_letter.upper(), "center", "Verdana", 30, "bold")

#Will prompt the user to enter their guess, if the word is not 5 letters long or does not exclusively
#contain letters, they can try again. It will then print the word onto the screen.
while guess_total < 6:
    guess = turtle.textinput("Enter your guess!", "What do you think the word is?").lower()
    while len(guess) < 5 or len(guess) > 5:
        guess = turtle.textinput("Enter your guess!", "Your guess must be 5 letters long! What do you think the word is?")
    while guess.isalpha() == False:
        guess = turtle.textinput("Enter your guess!", "Your guess must contain only letters and no spaces! What do you think the word is?")
    else:
        guess_list.append(guess)
        guess_total += 1
        y_axis_guesses += 40

    for i in range (5):
            guess_letter_keys[guess[i]] = i+1
    word_guess.append(list(guess))

    #Gray text of the user's guess.
    for i in range(5):
        write_letter = str(guess_list[guess_total-1][i])
        write_text("gray35", guess_x_axis[i], 100-y_axis_guesses, str.upper(write_letter), "center", "Verdana", 30, "bold")


    #Will check each letter in the user's guess to see if the letter is in the word or not, then will write the word in
    #the colours that match the user's guess. If the user guesses the word correctly before 6 tries, the game will end.
    
    green_letter_sum = 0
    

    for i in range(5):
        if word_guess[guess_total-1][i] in word_list:
            if word_guess[guess_total-1][i] == word_list[i]:
                green_letter(guess_total-1)
                green_letter_sum += 1
                continue
            
            elif word_guess[guess_total-1][i] != word_list[i]:
                yellow_letter(guess_total-1)
                continue
            
        else:
            colours_of_guess[guess_total-1].append("gray")
            continue
            green_amt[guess_total-1] = green_letter_sum
        if green_letter_sum == 5:
            break

    if green_letter_sum == 5:    
        break


#Reveals the word.
write_text("white", 0, -190, "The word was: " + str.upper(str(guess_this_word)), "center", "Verdana", 15, "bold")

#If the user guessed the word correctly, it will say good job. If they got it incorrectly, it will say good try.
if str.lower(str.strip(guess_this_word)) in guess_list:
    write_text("lime green", 0, -210, "You guessed it! Good job!", "center", "Verdana", 15, "bold")
else:
    write_text("firebrick3", 0, -210, "Good try!", "center", "Verdana", 15, "bold")

#Makes sure the window does not immediately close down upon starting.
turtle.mainloop()
word_dic.close()

