def q1():
    input("Create a function that will yake as input a minimum value and a maximum value. The function will return a random value between the given inputs WITHOUT using the built in randint function. Assume the random module has already been imported.\nWrite your answer on the side and when you are ready to compare answers, press enter. ")
    print("Answer:\ndef random_value(min_value, max_value):\n\tvalue = (random.random() * (max_value - min_value)) + min_value\n\treturn value")

def q2():
    input(" ")
    ans = input("What will be the Output of the following program:\nl = [[1,2,3],[4,5,6][7,8,9],[10,11,12],[13,14,15]]\nnew_list = l\nnew_list[1][2] = 16\nprint(l)\nAnswers: ")
    if ans == '[[1,2,3].[4,5,16],[7,8,9],[10,11,12],[13,14,15]]':
        print("You got it!")
    else:
        print("Correct Answer: [[1,2,3].[4,5,16],[7,8,9],[10,11,12],[13,14,15]]")

def q3():
    input(" ")
    ans = input("What will be the output of the following program:\nl = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]\nprint(list[1][2])\nAnswer: ")
    if ans == '6':
        print("You got it!")
    else:
        print("Correct Answer: 6")

def q4():
    input(" ")
    ans = input("What will the following program display?:\ndict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday':6, 'Sunday': 7}\ndict.pop('Thursday')\nprint(dict)\nAnswer: ")
    if ans == "{'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}":
        print("You got this!")
    else:
        print("Correct Answer:\n{'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}")

def q5():
    input(" ")
    ans = input("What happends is __name__ == 'main' is False?\nAnswer: ")
    print("If this occurs, the codefollowing the if __name__ == 'main' will not be executed.")

def q6():
    input("Write a class constructor named Schedule with the following attributes that needto be initialized: course, professor, location, number_credits.\nWrite your answer on the side and when you are ready to compare answers, press enter")
    print("Your answer should look something like this!:\nclass Schedule:\n\tdef __init__(self,c,p,l,num):\n\t\tself.course = c\n\t\tslef.prodessor = p\n\t\tslef.location = l\n\t\tself.number_of_credits = num")

def q7():
    input(" ")
    input("Create the base structure to raise an exception.\nWrite your answer on the side and when you are ready to compare answers, press enter")
    print("try:\n\t#action\nExcept #Error:\n\t#action")

def q8():
    input(" ")
    input("What does the finally keyword will do in an exception handling?\nAnswer: ")
    print("Correct answer: The finally keyword will make sure the block following it is always executed no matter what.")

def q9():
    input(" ")
    ans = ("What is the output of the following Object Oriented Program:\n"\
           "class Employee:\n\t"\
           "def __init__(self, n, j, s):\n\t\t"\
           "self.name = n\n\t\t"\
           "self.job = j\n\t\t"\
           "self.salary = s\n\n"\
           "class Departments:\n\t"\
           "def __init__(self, d, c, b, n = []):\n\t\t"\
           "self.department = d\n\t\t"\
           "self.chiefofficer = c\n\t\t"\
           "self.budget = b\n\t\t"\
           "self.positions = n\n\n\t"\
           "def add_in_department(self, name, job, salary):\n\t\t"\
           "self.positions.append(job)\n\n"\
           "if __name__ == '__main__':\n\t"\
           "employee1 = Employee('Eric', 'Senior Manager', 70000)\n\t"\
           "department = Departments('Finance', 'Adam', 15000000, ['CEO', 'Senior Manager', 'Director'])\n\t"\
           "department.add_in_department('Leila', 'Analyst', 65000)\n\t"\
           "print(department.positions)\n\nAnswer: ")
    if ans == " ['CEO', 'Senior Manager', 'Director', 'Analyst']":
        print("You got it")
    else:
        print("Correct answer: ['CEO', 'Senior Manager', 'Director', 'Analyst']")

    
        
def q10():
    input(" ")
    input("Last question, you can do it! What is the difference between a class and an object, and how do they interact with each other?\nAnswer: ")
    print("Correct answer: A class defines a new type from which objects are created.")

def get_question(question_number):
    if question_number == 1:
        return "Create a function that will yake as input a minimum value and a maximum value. The function will return a random value between the given inputs WITHOUT using the built in randint function. Assume the random module has already been imported.\nWrite your answer on the side and when you are ready to compare answers, press enter. "
    elif question_number == 2:
        return "What will be the Output of the following program:\nl = [[1,2,3],[4,5,6][7,8,9],[10,11,12],[13,14,15]]\nnew_list = l\nnew_list[1][2] = 16\nprint(l)\nAnswers: "
    elif question_number == 3:
        return "What will be the output of the following program:\nl = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]\nprint(list[1][2])\nAnswer: "
    elif question_number == 4:
        return "What will the following program display?:\ndict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday':6, 'Sunday': 7}\ndict.pop('Thursday')\nprint(dict)\nAnswer: "
    elif question_number == 5:
        return "What happends is __name__ == 'main' is False?\nAnswer: "
    elif question_number == 6:
        return "Write a class constructor named Schedule with the following attributes that need to be initialized: course, professor, location, number_credits.\nWrite your answer on the side and when you are ready to compare answers, press enter"
    elif question_number == 7:
        return "Create the base structure to raise an exception.\nWrite your answer on the side and when you are ready to compare answers, press enter"
    elif question_number == 8:
        return "What does the finally keyword will do in an exception handling?\nAnswer: "
    elif question_number == 9:
        return "What is the output of the following Object Oriented Program:\n"\
                "class Employee:\n\t"\
                "def __init__(self, n, j, s):\n\t\t"\
                "self.name = n\n\t\t"\
                "self.job = j\n\t\t"\
                "self.salary = s\n\n"\
                "class Departments:\n\t"\
                "def __init__(self, d, c, b, n = []):\n\t\t"\
                "self.department = d\n\t\t"\
                "self.chiefofficer = c\n\t\t"\
                "self.budget = b\n\t\t"\
                "self.positions = n\n\n\t"\
                "def add_in_department(self, name, job, salary):\n\t\t"\
                "self.positions.append(job)\n\n"\
                "if __name__ == '__main__':\n\t"\
                "employee1 = Employee('Eric', 'Senior Manager', 70000)\n\t"\
                "department = Departments('Finance', 'Adam', 15000000, ['CEO', 'Senior Manager', 'Director'])\n\t"\
                "department.add_in_department('Leila', 'Analyst', 65000)\n\t"\
                "print(department.positions)\n\nAnswer: "
    elif question_number == 10:
        return "Last question, you can do it! What is the difference between a class and an object, and how do they interact with each other?\nAnswer: "

def get_correct_answer(question_number):
    if question_number == 1:
        correct_answer = "\ndef random_value(min_value, max_value):\n\tvalue = (random.random() * (max_value - min_value)) + min_value\n\treturn value"
        return correct_answer
    elif question_number == 2:
        correct_answer = "[[1,2,3].[4,5,16],[7,8,9],[10,11,12],[13,14,15]]"
        return correct_answer
    elif question_number == 3:
        correct_answer = "6"
        return correct_answer
    elif question_number == 4:
        correct_answer = "\n{'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}"
        return correct_answer
    elif question_number == 5:
        correct_answer = "If this occurs, the codefollowing the if __name__ == 'main' will not be executed."
        return correct_answer
    elif question_number == 6:
        correct_answer = "\nclass Schedule:\n\tdef __init__(self,c,p,l,num):\n\t\tself.course = c\n\t\tslef.prodessor = p\n\t\tslef.location = l\n\t\tself.number_of_credits = num"
        return correct_answer
    elif question_number == 7:
        correct_answer = "try:\n\t#action\nExcept #Error:\n\t#action"
        return correct_answer
    elif question_number == 8:
        correct_answer = "The finally keyword will make sure the block following it is always executed no matter what."
        return correct_answer
    elif question_number == 9:
        correct_answer = "['CEO', 'Senior Manager', 'Director', 'Analyst']"
        return correct_answer
    elif question_number == 10:
        correct_answer = "A class defines a new type from which objects are created."
        return correct_answer




