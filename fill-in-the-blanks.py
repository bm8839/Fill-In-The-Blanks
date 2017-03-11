# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min


programming = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___
takes by adding ___2___ separated by commas between the parentheses.
___1___s by default return ___3___ if you don't specify the value to return.
___2___ can be standard data types such as string, number, dictionary,tuple,
and ___4___ or can be more complicated such as objects and lambda functions.'''

programming_answers = ["function","arguments","none","list"]
programming_blanks = ["___1___","___2___","___3___","___4___"]

sports = """When a player ___1___s in baseball its called a ___2___. A ___1___
in football is called a ___3___. A soccer score is called a ___4___.
But in all three of these ___5___ the total number of ___6___ ___1___d
determines the ___7___."""

sports_answers = ["score","run","touchdown","goal","sports","points","winner"]
sports_blanks = ["___1___","___2___","___3___","___4___","___5___","___6___","___7___"]

history = """The ___1___ official American flag had 13 ___2___ and ___3___s.
Today it has a ___3___ for each ___4___. On July 4th, ___5___, Congress
adopted the Declaration of Independence. This date is known as ___6___
day, declaring our ___6___ from British rule."""

history_answers = ["first","stripes","star","state","1776","independence",]
history_blanks = ["___1___","___2___","___3___","___4___","___5___","___6___"]


def para_selection(category):
    """This function takes in the user selected category string and returns the
    appropriate paragraph string and answers list and blanks list from above"""
    if category == "programming":
      return (programming, programming_answers, programming_blanks)
    elif category == "sports":
      return (sports, sports_answers, sports_blanks)
    else:
      return (history, history_answers, history_blanks)


def start_game():
    """Introduces the quiz and prompts the user to pick an area of interest.
    This function has no input but returns the category picked by the user."""
    print "\n", """This is a fill-in-the-blank quiz!

Please select your category by typing it in!
"""
    category = raw_input("Type one of these choices: programming (easy), sports (medium), or history (hard): ")
    category = category.lower()

    """If the user does not select a valid input, this loops continues to ask for a valid input from the user"""
    categories = ["programming","sports","history"]
    while category not in categories:
      print "That's not an option!"
      category = raw_input("Type one of these choices: programming, sports, or history: ")

    """Confirms to the user which category they picked with an instruction about guesses"""
    print "\n", "You've chosen "+ category +"!"
    print "\n", "You will get 3 guesses per blank. Good luck!", "\n"
    return category


def play_game(paragraph,answers,blanks):
    """This function takes inputs of appropriate paragraph and it's corresponding answers
    list and blanks list. It loops through the paragraph for the length of the
    blanks list as long as the user doesn't enter too many wrong guesses. Each
    time a correct answer is given for the corresponding blank the paragraph gets
    updated, the guess counter is restored to its original value, and the user
    is prompted for the next guess. Each time a wrong answer is given the user is
    prompted to try again, the guess counter is decremented, and if too many wrong
    answers are given the game is over. It returns the index counter and the guesses
    counter."""
    guesses = ["0","1","2"]
    index = 0
    guesses_counter = 3
    while index < len(blanks)and guesses_counter > 0:
      print
      user_answer = raw_input("Type in the answer to "+ blanks[index]+" : ")
      user_answer = user_answer.lower()
      if user_answer == answers[index]:
          paragraph = paragraph.replace(blanks[index],user_answer)
          index += 1
          guesses_counter = 3
          print "\n", "You are correct!", "\n", paragraph
      else:
          guesses_counter -= 1
          if guesses_counter >= 0:
            print "\n", "Sorry that's not correct, you have "+guesses[guesses_counter]+" tries remaining"
    return (index, guesses_counter)


def finish_game(index,blanks,guesses_counter):
    """This function takes in the index counter and the guesses counter returned from
    the play_game function along with the blanks list. If the result of playing
    the game is that all blanks are correctly answered, then the user is told
    they win. If the result is too many wrong guesses, the user is told the game
    is over and they are shown the answers if they want to see them. The function
    returns nothing, it only outputs print statements."""
    if index == len(blanks) and guesses_counter > 0:
        print "\n", "YOU WIN! YOU WIN!"
    else:
        print "\n", "GAME OVER!", "\n"
        option = raw_input("Would you like to know the answers? (yes or no): ")
        option = option.lower()
        options = ["yes","no"]
        while option not in options:
          print "That's not an option!"
          option = raw_input("Would you like to know the answers? (yes or no): ")
        if option == "yes":
          print "\n", "Here are the answers:", "\n"
          index = 0
          for blank in blanks:
              print blank + " = " + answers[index]
              index += 1


"""THIS IS THE BEGINNING OF THE MAIN PROGRAM.
First we get the game started by finding out which category the user
wants to play."""
category = start_game()

"""Next calls the function using the category picked by the user to get the appropriate
paragraph string and answer list and blanks list."""
paragraph, answers, blanks = para_selection(category)
print paragraph, "\n"

"""Next instruction calls the function sending the chosen paragraph along with
it's corresponding answer list and blanks list for the user to play the game
and then gets back the index counter and the guesses counter so we'll know
when the game is over and whether the user won or lost."""
index,guesses_counter = play_game(paragraph,answers,blanks)

"""Last but not least we finish the game based on the index counter which tells if
all the blanks were replaced and the guesses_counter which tells us whether the
player used up all their guesses."""
finish_game(index,blanks,guesses_counter)
