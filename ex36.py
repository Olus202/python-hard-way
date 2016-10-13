from sys import exit

def python_room():
    print "You are it the room where you have to answer three Python question."
    print "Are you ready for it?"

    answer = raw_input("(yes/no)>>> ")

    if answer == "yes":
        python_questions()
    elif answer == "no":
        game_over("If you are not ready...")
    else:
        print "You are not understand... 'yes' or 'no'!\n"
        print "-" * 10
        print "\nOnce again..."
        python_room()

def python_questions():
    print "Ok, so questions...\n"

    questions = [
    "Is it true, that the index of '2' in ['hallo', 2, ['second', 'list'] is 1?",
    "Is it correct syntax: 'import sys form *'",
    "Is the if-statement a loop?"
    ]

    for q in questions:
        print q
        answer = raw_input("yes or now? > ")

        if answer == "yes":
            print "\nGood answer! Now choose next question.\n"
        elif answer == "now":
            game_over("Sorry... It's wrong answer.")
        else:
            game_over("You are not so smart to type 'yes' or 'now'.")

    print "\nYou van leave the room. You are free now!"

    raw_input("\nPress ENTER to leave the room.")
    exit(0)


def game_over(why):
    print why, "Game over..."

    raw_input("\nPress something.")
    exit(0)


python_room()
