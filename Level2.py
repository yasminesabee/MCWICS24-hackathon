def q1():
    ans = input("What type of error will the following statement produce:\nprint('Hackathon' + 2024)\nA. TypeError\nB. NameError\nC. SyntaxError\nAnswer (A,B or C): ")
    if ans == 'A':
        print("You got it!")
    else :
        print("Correct Answer: A\n2024 should be a string for the concatenation to work; this type of error is raised whenever an operation is performed on an object type that isn't supported.")

def q2():
    input(" ")
    ans = input("What type of error will the following statement produce:\nx = 10\ny = 20\nprint(z + y)\nA. TypeError\nB. NameError\nC. SyntaxError\nAnswer: ")
    if ans == 'B':
        print("You got it")
    else :
        print("Correct Answer: B\nz should be defines for the addition to work. This type of error is raised whenever the program tries to use a variable that isn't defined.")
    

def q3():
    input(" ")
    ans = input("What type of error will the following statement produce:\nprint 'Hello World'\nA. TypeError\nB. NameError\nC. SyntaxError\nAnswer: ")
    if ans == 'C':
        print("You got it")
    else :
        print("Correct Answer: C\nParentheses should surround 'Hello World'. This type of error is raised whenever the programmer makes mistakes using the language.")

def q4():
    input(" ")
    ans = input("True or False: A void function can only return a string or an integer. Enter T for true or F for false.\nAnswer: ")
    if ans == 'F':
        print("You got it!")
    else :
        print("Correct answer: F\nA void function does not return any value")

def q5():
    input(" ")
    ans = input("True or False: A fruitful function returns any type of value. Enter T for true or F for false.\nAnswer: ")
    if ans == 'T':
        print("You got it!")
    else :
        print("Correct answer: T")

def q6():
    input(" ")
    input("What does the following program do:\npassing_grade = 60\ngrades = [56, 72, 67, 89]\nresult = []\nfor grade in grades:\n\tif grade >= passing_grade:\n\t\tresult.append('Pass')\n\telse:\n\t\tresult.append('Fail')\nprint(result)\nAnswer: ")
    print("Correct answer: The program will iterate over a list of grades. For every grade, it will indicate in a new list, 'result', whether the grade constitutes a pass or fail based on a predetermined passing grade")

def q7():
    input(" ")
    input("Create the base structure for an if-else statement using one if, one elif and one else. Do this on the side on a piece of paper or using favorite IDE, once you are ready to compare your answer press enter. ")
    print("Correct Answer:\nif #condition1:\n\t#action\nelif #condition2:\n\t#action\nelse:\n\t#action")

def q8():
    input("What does the following program do:\nx = 8\nif x > 0:\n\ty = x\n\tprint(y)\nelse:\n\tz = 1 / x\n\tprint(round(z,2))\nAnswer: ")
    print("Correct answer: The program will check if x is smaller than 0. If it is, it will assign to y the value of x, and print y. If it isn’t, it will assign to z the value 1/x, and print z rounded to two decimals places.")

def q9():
    input(" ")
    input("Tranform the following for loop into a while loop:\nfor x in range(10):\n\tprint(x)\nWright your answer on the side and when you are ready to compare it press enter. ")
    print("Correct Answer:\nwhile x < 10:\n\tprint(x)\n\tx += 1\nDon't forget to add an increment value in your while loops!")

def q10():
    input(" ")
    ans = input("How do you generate a random number between 0 and 1, assuming the random module has already been imported.\n Answer: ")
    if ans == 'random.random()':
        print("You got it")
    else :
        print("Correct Answer: random.random()")

def q11():
    input(" ")
    ans = input("What is the correct way to define a function:\nA. def NameOfFunction:\nB. NameOfFucntion():\nC.def NameOfFunction():\nD. def NameOfFunction()\nAnswer: ")
    if ans == 'C':
        print("You got it")
    else:
        print("Correct Answer: C")

def q12():
    input(" ")
    ans = input("Which of the following options are all immutable:\nA. List, String, Dictionnaries\nB. Integer, String, Tuple\nC. List, String, Float\nAnswer: ")
    if ans == 'B':
        print("You got it")
    else:
        print("Correct Answer: B")
        
def q13():
    input(" ")
    input("Write a docstring for the following function:\ndef addFloats(x, y):\n\tz = x + y\n\treturn round(z, 2)\nWrite your answer on the side and when you are ready to compare answers, press enter. ")
    print("\"\"\"(float, float) -> float\n\nReturns the sum of two floats x and y rounded by two values.\n\n>>> Example 1\n>>> Example 2\n>>> Example 3\n\"\"\"\n\nor\n\n\"\"\"\nReturn the sum of two floats x and y rounded by two values.\n\nParameters:\n\tx: a float\n\ty: a float\nReturns:\n\tz(float):The sum of the two provided floats\n\n>>> Example 1\n>>> Example 2\n>>> Example 3\n\"\"\"")
    
def q14():
    input(" ")
    ans = input("How many times will the word 'Hello' print in the following program:\nfor x in range(3):\n\tprint('Hello')\n\tfor y in range (5):\n\t\tprint('Hello')\nAnswer: ")
    if ans == '18':
        print("You got it")
    else:
        print("Correct Answer: 18")

def get_question(question_number):
    if question_number == 1:
        return "What type of error will the following statement produce:\nprint('Hackathon' + 2024)\nA. TypeError\nB. NameError\nC. SyntaxError\nAnswer (A,B or C): "
    elif question_number == 2:
        return "What type of error will the following statement produce:\nx = 10\ny = 20\nprint(z + y)\nA. TypeError\nB. NameError\nC. SyntaxError\nAnswer: "
    elif question_number == 3:
        return "What type of error will the following statement produce:\nprint 'Hello World'\nA. TypeError\nB. NameError\nC. SyntaxError\nAnswer: "
    elif question_number == 4:
        return "True or False: A void function can only return a string or an integer. Enter T for true or F for false.\nAnswer: "
    elif question_number == 5:
        return "True or False: A fruitful function returns any type of value. Enter T for true or F for false.\nAnswer: "
    elif question_number == 6:
        return "What does the following program do:\npassing_grade = 60\ngrades = [56, 72, 67, 89]\nresult = []\nfor grade in grades:\n\tif grade >= passing_grade:\n\t\tresult.append('Pass')\n\telse:\n\t\tresult.append('Fail')\nprint(result)\nAnswer: "
    elif question_number == 7:
        return "Create the base structure for an if-else statement using one if, one elif and one else. Do this on the side on a piece of paper or using favorite IDE, once you are ready to compare your answer press enter. "
    elif question_number == 8:
        return "What does the following program do:\nx = 8\nif x > 0:\n\ty = x\n\tprint(y)\nelse:\n\tz = 1 / x\n\tprint(round(z,2))\nAnswer: "
    elif question_number == 9:
        return "Tranform the following for loop into a while loop:\nfor x in range(10):\n\tprint(x)\nWright your answer on the side and when you are ready to compare it press enter. "
    elif question_number == 10:
        return "How do you generate a random number between 0 and 1, assuming the random module has already been imported.\n Answer: "
    elif question_number == 11:
        return "What is the correct way to define a function:\nA. def NameOfFunction:\nB. NameOfFucntion():\nC.def NameOfFunction():\nD. def NameOfFunction()\nAnswer: "
    elif question_number == 12:
        return "Which of the following options are all immutable:\nA. List, String, Dictionnaries\nB. Integer, String, Tuple\nC. List, String, Float\nAnswer: "
    elif question_number == 13:
        return "Write a docstring for the following function:\ndef addFloats(x, y):\n\tz = x + y\n\treturn round(z, 2)\nWrite your answer on the side and when you are ready to compare answers, press enter. "
    elif question_number == 14:
        return "How many times will the word 'Hello' print in the following program:\nfor x in range(3):\n\tprint('Hello')\n\tfor y in range (5):\n\t\tprint('Hello')\nAnswer: "

def get_correct_answer(question_number):
    if question_number == 1:
        correct_answer = "A\n2024 should be a string for the concatenation to work; this type of error is raised whenever an operation is performed on an object type that isn't supported."
        return correct_answer
    elif question_number == 2:
        correct_answer = "B\nz should be defines for the addition to work. This type of error is raised whenever the program tries to use a variable that isn't defined."
        return correct_answer
    elif question_number == 3:
        correct_answer = "C\nParentheses should surround 'Hello World'. This type of error is raised whenever the programmer makes mistakes using the language."
        return correct_answer
    elif question_number == 4:
        correct_answer = "F\nA void function does not return any value"
        return correct_answer
    elif question_number == 5:
        correct_answer = "T"
        return correct_answer
    elif question_number == 6:
        correct_answer = "The program will iterate over a list of grades. For every grade, it will indicate in a new list, 'result', whether the grade constitutes a pass or fail based on a predetermined passing grade."
        return correct_answer
    elif question_number == 7:
        correct_answer = "\nif #condition1:\n\t#action\nelif #condition2:\n\t#action\nelse:\n\t#action"
        return correct_answer
    elif question_number == 8:
        correct_answer = "The program will check if x is smaller than 0. If it is, it will assign to y the value of x, and print y. If it isn’t, it will assign to z the value 1/x, and print z rounded to two decimals places."
        return correct_answer
    elif question_number == 9:
        correct_answer = "\nwhile x < 10:\n\tprint(x)\n\tx += 1\nDon't forget to add an increment value in your while loops!"
        return correct_answer
    elif question_number == 10:
        correct_answer = "random.random()"
        return correct_answer
    elif question_number == 11:
        correct_answer ="C"
        return correct_answer
    elif question_number == 12:
        correct_answer = "B"
        return correct_answer
    elif question_number == 13:
        correct_answer = "\"\"\"(float, float) -> float\n\nReturns the sum of two floats x and y rounded by two values.\n\n>>> Example 1\n>>> Example 2\n>>> Example 3\n\"\"\"\n\nor\n\n\"\"\"\nReturn the sum of two floats x and y rounded by two."
        return correct_answer
    elif question_number == 14:
        correct_answer = "18"
        return correct_answer







    

