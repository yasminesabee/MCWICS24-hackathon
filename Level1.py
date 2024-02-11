def q1() :
    input("Let us start with an easy one!\nWhat does the print() function do?\n")
    print("Correct Answer:\nThe print function prints the given arguments to the screen.")

def q2():
    input(" ")
    ans = input("Now let's test it out!\nDisplay 'Hello World': ")
    if ans == "print('Hello World')" or ans == "print(\"Hello World\")":
        print("You got it!")
    else :
        print("Correct Answer:\nprint('Hello World') or print(\"Hello World\")\nNotice that we can use both double or single quotes.")
    print("Starting from next question, always use single quotes for autocorrection purposes")
        
def q3():
    input(" ")
    input("What does the input() function do?: ")
    print("Correct Answer:\nThe input function displays the argument to the screen and returns the user's input as a string.")
    
def q4():
    input(" ")
    ans = input("Now let's test it out!\nAsk the user: 'How old are you?' ")
    if ans == "input('How old are you?')":
        print("You got it!")
    else :
        print("Correct Answer: input('How old are you?')")

def q5():
    input(" ")
    ans = input("Create a integer variable named x and has the value 10 (do not use any space): ")
    if ans == 'x=10':
        print("You got it!")
    else :
        print("Correct answer: x=10")

def q6():
    input(" ")
    ans = input("Now, transfer the variable x that you created in the previous question to a string: ")
    if ans == 'str(x)':
        print("You got it!")
    else :
        print("Correct answer: str(x)")

def q7():
    input(" ")
    ans = input("Consider the following line of code:\na = 4.0 * 5\nWhat is the type of the variable a\nA. int\nB. float\nC.str\nChoose the correct answer (A,B or C): \n")
    if ans == 'B':
        print("You got it!")
    else :
        print("Correct answer: B")

def q8():
    input(" ")
    ans = input("What is the output of the following code:\nx = 5\ny = 4.0\nsum = x + y\nprint(sum)\nAnswer: ")
    if ans == '9.0':
        print("You got it!")
    else :
        print("Correct answer: 9.0")

def q9():
    input(" ")
    ans = input("What is the decimal number of the following binary number: 101101\nA.26\nB.54\nC.45\nAnswer: ")
    if ans == 'C':
        print("You got it!")
    else :
        print("Correct answer: C")

def q10():
    input(" ")
    ans = input("What is 17%3?\nA. 2\nB. 5.7\nC. 5\nAnswer: ")
    if ans == 'A':
        print("You got it!")
    else :
        print("Correct answer: A")

def q11():
    input(" ")
    ans = input("What is 78//5?\nA. 3\nB. 5\nC. 15\nAnswer: ")
    if ans == 'C':
        print("You got it!")
    else :
        print("Correct answer: C")

def q12():
    input(" ")
    ans = input("What prints from the following the statement?\nprint('I'+'Love'+'Python')\nAnswer: ")
    if ans == 'ILovePython':
        print("You got it!")
    else :
        print("Correct answer: ILovePython")

def q13():
    input(" ")
    ans = input("What is the output of the following statement?\nprint(int(5.7))\nAnswer: ")
    if ans == '5':
        print("You got it!")
    else :
        print("Correct answer: 5")

def q14():
    input(" ")
    ans = input("What is the binary number of the following decimal number: 438\nA. 011011011\nB. 110110110\nC. 1011010\nAnswer: ")
    if ans == 'B':
        print("You got it!")
    else :
        print("Correct answer: B")


def q15():
    input(" ")
    input("How can you create a comment in Python?\n")
    print("Correct Answer:  It’s easy! Simply put a “#” in front of the lines you wish to comment out. A comment will not affect your code. Don’t be afraid to use them throughout your code; they enhance clarity.")

def q16():
    input(" ")
    input("What is a Boolean variable?\n")
    print("A Boolean is a basic type used to show whether something is true or false.")

def q17():
    input(" ")
    input("What does '\\n' do in a print statement?\n")
    print("Correct Answer: It creates a new line.")

def q18():
    input(" ")
    ans = input("What is the output of the following code:\nx = 4\ny = float(4)\nprint(y)\nAnswer: ")
    if ans == '4.0':
        print("You got it!")
    else :
        print("Correct Answer: 4.0")

def q19():
    input(" ")
    ans = input("Consider the following code:\na = input('How old are you? ')\nWhat is the type of the variable a?\nA. int\nB. str\nC.float\nAnswer: ")
    if ans == "B":
        print("You got it!")
    else :
        print("Correct Answer: B")

def q20():
    input(" ")
    ans = input("Conider the following line of code:\nb = '4.0'\nWhat is the type of the variable b?\nA. int\nB. str\nC.float\nAnswer: ")
    if ans == "B":
        print("You got it!")
    else :
        print("Correct Answer: B")

def get_question(question_number):
    if question_number == 1:
        return "What does the print() function do?"
    elif question_number == 2:
        return "Now let's test it out!\nDisplay 'Hello World': "
    elif question_number == 3:
        return "What does the input() function do?: "
    elif question_number == 4:
        return "Now let's test it out!\nAsk the user: 'How old are you?' "
    elif question_number == 5:
        return "Create a integer variable named x and has the value 10 (do not use any space):"
    elif question_number == 6:
        return "Now, transfer the variable x that you created in the previous question to a string: "
    elif question_number == 7:
        return "Consider the following line of code:\na = 4.0 * 5\nWhat is the type of the variable a\nA. int\nB. float\nC.str\nChoose the correct answer (A,B or C):"
    elif question_number == 8:
        return "What is the output of the following code:\nx = 5\ny = 4.0\nsum = x + y\nprint(sum)\nAnswer: "
    elif question_number == 9:
        return "What is the decimal number of the following binary number: 101101\nA.26\nB.54\nC.45\nAnswer: "
    elif question_number == 10:
        return "What is 17%3?\nA. 2\nB. 5.7\nC. 5\nAnswer: "
    elif question_number == 11:
        return "What is 78//5?\nA. 3\nB. 5\nC. 15\nAnswer: "
    elif question_number == 12:
        return "What prints from the following the statement?\nprint('I'+'Love'+'Python')\nAnswer: "
    elif question_number == 13:
        return "What is the output of the following statement?\nprint(int(5.7))\nAnswer: "
    elif question_number == 14:
        return "What is the binary number of the following decimal number: 438\nA. 011011011\nB. 110110110\nC. 1011010\nAnswer: "
    elif question_number == 15:
        return "How can you create a comment in Python?\n"
    elif question_number == 16:
        return "What is a Boolean variable?\n"
    elif question_number == 17:
        return "What does '\\n' do in a print statement?\n"
    elif question_number == 18:
        return "What is the output of the following code:\nx = 4\ny = float(4)\nprint(y)\nAnswer: "
    elif question_number == 19:
        return "Consider the following code:\na = input('How old are you? ')\nWhat is the type of the variable a?\nA. int\nB. str\nC.float\nAnswer: "
    elif question_number == 20:
        return "Conider the following line of code:\nb = '4.0'\nWhat is the type of the variable b?\nA. int\nB. str\nC.float\nAnswer: "

def get_correct_answer(question_number):
    if question_number == 1:
        correct_answer = "The print function prints the given arguments to the screen."
        return correct_answer
    elif question_number == 2:
        correct_answer = "print('Hello World')"
        return correct_answer
    elif question_number == 3:
        correct_answer = "\nThe input function displays the argument to the screen and returns the user's input as a string."
        return correct_answer
    elif question_number == 4:
        correct_answer = "input('How old are you?')"
        return correct_answer
    elif question_number == 5:
        correct_answer = "x=10"
        return correct_answer
    elif question_number == 6:
        correct_answer = "str(x)"
        return correct_answer
    elif question_number == 7:
        correct_answer = "B"
        return correct_answer
    elif question_number == 8:
        correct_answer = "9.0"
        return correct_answer
    elif question_number == 9:
        correct_answer = "C"
        return correct_answer
    elif question_number == 10:
        correct_answer = "A"
        return correct_answer
    elif question_number == 11:
        correct_answer = "C"
        return correct_answer
    elif question_number == 12:
        return "ILovePython"
        return correct_answer
    elif question_number == 13:
        correct_answer = "5"
        return correct_answer
    elif question_number == 14:
        correct_answer = "B"
        return correct_answer
    elif question_number == 15:
        correct_answer = "It's easy! Simply put a “#” in front of the lines you wish to comment out. A comment will not affect your code. Don’t be afraid to use them throughout your code; they enhance clarity."
        return correct_answer
    elif question_number == 16:
        correct_answer = "A Boolean is a basic type used to show whether something is true or false."
        return correct_answer
    elif question_number == 17:
        correct_answer = "It creates a new line."
        return correct_answer
    elif question_number == 18:
        correct_answer = "4.0"
        return correct_answer
    elif question_number == 19:
        correct_answer = "B"
        return correct_answer
    elif question_number == 20:
        correct_answer = "B"
        return correct_answer










    
        
    
        