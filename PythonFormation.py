import tkinter as tk
from tkinter import messagebox

import Level1 as a
import Level2 as b
import Level3 as d

class PythonFormationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Formation")
        root.geometry("1250x1000")
        self.current_level = 1
        self.question_number = 1

        self.label = tk.Label(master, text="Python Formation\nThe following formation consists of three dificulty"\
        " levels that will test your basics skills in the Python programming language.\n"\
        "The Formation will start from level 1 and throughout the process you will "\
        "have the option to go up if you feel comfortable "\
        "where you are. Press 'Enter' after each question to get the following one.\nDisclaimer: Do not worry if get an incorrect answer because it could simply be an additional space or a small typo.\nJust be sure to compare your answer with the correct one.\n"\
        "Enjoy!")
          
        self.label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_formation)
        self.start_button.pack()

        self.thank_you_label = tk.Label(master, text="Thank you for completing the Python Formation!")
        self.thank_you_label.pack_forget()  

    def start_formation(self):
        self.label.config(text=f"Level {self.current_level} - Question {self.question_number}")
        self.start_button.destroy()

        self.question_text = tk.StringVar()
        self.question_text.set(self.get_question())

        self.question_label = tk.Label(self.master, textvariable=self.question_text)
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        self.next_button = tk.Button(self.master, text="Enter", command=self.next_question)
        self.next_button.pack()

    def get_question(self):
        if self.current_level == 1:
            return a.get_question(self.question_number)
        elif self.current_level == 2:
            return b.get_question(self.question_number)
        elif self.current_level == 3:
            return d.get_question(self.question_number)

    def next_question(self):
        answer = self.answer_entry.get()
        correct_answer = self.get_correct_answer()

        if answer == correct_answer:
            messagebox.showinfo("Correct", "You got it!")
        else:
            messagebox.showinfo("Incorrect", f"Incorrect. The correct answer is: {correct_answer}")

        self.question_number += 1
        
        if (self.current_level == 1 and self.question_number <= 20) or (self.current_level == 2 and self.question_number <= 14) or (self.current_level == 3 and self.question_number <= 10):
            self.question_text.set(self.get_question())
            self.label.config(text=f"Level {self.current_level} - Question {self.question_number}")
            self.answer_entry.delete(0, tk.END)
            self.check_halfway_point()
    
        else:
            # Check if the user has completed the current level
            if self.current_level == 1:
                messagebox.showinfo("Level Complete", "Congratulations! You have completed Level 1.")
                # Move on to Level 2
                self.current_level = 2
                self.question_number = 1
                self.question_text.set(self.get_question())
                self.label.config(text=f"Level {self.current_level} - Question {self.question_number}")
                self.check_halfway_point()

            elif self.current_level == 2:
                messagebox.showinfo("Level Complete", "Congratulations! You have completed Level 2.")
                # Move on to Level 3
                self.current_level = 3
                self.question_number = 1
                self.question_text.set(self.get_question())
                self.label.config(text=f"Level {self.current_level} - Question {self.question_number}")

            elif self.current_level == 3:
                messagebox.showinfo("Congratulations", "You have completed the Python Formation!")
            


    def get_correct_answer(self):
        if self.current_level == 1:
            return a.get_correct_answer(self.question_number)
        elif self.current_level == 2:
            return b.get_correct_answer(self.question_number)
        elif self.current_level == 3:
            return d.get_correct_answer(self.question_number)
    
    def check_halfway_point(self):
        halfway_point = 0
        if self.current_level == 1:
            halfway_point = 11
        elif self.current_level == 2:
            halfway_point = 8
       

        if self.question_number == halfway_point:
            ans = messagebox.askquestion("Halfway Point", "Do you want to skip to the next level? (Answer: yes or no)")
            if ans == 'yes':
                self.skip_to_next_level()
            else:
                self.show_completion_message()
    
    def skip_to_next_level(self):
        if self.current_level <= 2:
            messagebox.showinfo("Skipping to Next Level", f"You are now skipping to Level {self.current_level + 1}.")
            self.current_level += 1
            self.question_number = 1
            self.question_text.set(self.get_question())
            self.label.config(text=f"Level {self.current_level} - Question {self.question_number}")
        else:
            messagebox.showinfo("End of Formation", "You have completed the Python Formation!")
            self.show_completion_message()

    def show_completion_message(self):
        if self.current_level == 3:
            messagebox.showinfo("Congratulations", "You have completed the Python Formation!")
            self.label = tk.Label(self, text="Thank you for completing the Python Formation!")
        
          
            self.label.pack()

        elif (self.current_level == 1 and self.question_number == 20) or (self.current_level == 2 and self.question_number == 14) or (self.current_level == 3 and self.question_number == 10):
            messagebox.showinfo("Level Complete", f"Congratulations! You have completed Level {self.current_level}.")
    
        
    def show_thank_you_label(self):
        self.thank_you_label.pack()


# Create the main window
root = tk.Tk()

# Create the application
app = PythonFormationApp(root)

# Run the main loop
root.mainloop()
