"""
Project Title: Math Quiz Game
Description: A command-line math quiz application that generates random arithmetic 
             questions, evaluates user input, handles exceptions, and tracks scores.
Module: Math & Random Module & Functions
"""

import random

def generate_question():
    """
    Function to generate a random math question and its correct answer.
    Demonstrates the use of the random module and basic arithmetic operators.
    """
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operators = ['+', '-', '*']
    op = random.choice(operators)
    
    # Calculate the correct answer based on the selected operator
    if op == '+':
        correct_answer = num1 + num2
    elif op == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
        
    return num1, num2, op, correct_answer

def run_quiz(total_questions=5):
    """
    Main function to execute the quiz loop, handle user input, 
    and calculate the final score using conditional statements and exception handling.
    """
    print("========================================")
    print("      WELCOME TO THE MATH QUIZ GAME     ")
    print("========================================")
    print(f"You will be tested with {total_questions} random math questions.")
    print("Let's see how many you can get right!\n")
    
    score = 0
    
    # Using a for loop to control the number of questions
    for i in range(1, total_questions + 1):
        num1, num2, op, correct_answer = generate_question()
        
        # Exception handling to prevent crashes from invalid text inputs
        try:
            user_answer = int(input(f"Question {i}: What is {num1} {op} {num2}? -> "))
            
            if user_answer == correct_answer:
                print("Correct! Great job! 🎉\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {correct_answer}.\n")
                
        except ValueError:
            print("Invalid input! Please enter a valid integer. This counts as incorrect.\n")
            
    display_results(score, total_questions)

def display_results(score, total_questions):
    """
    Function to display the final score and performance rating.
    """
    print("========================================")
    print("              QUIZ FINISHED             ")
    print("========================================")
    print(f"Your Final Score: {score} out of {total_questions}")
    
    percentage = (score / total_questions) * 100
    if percentage == 100:
        print("Rating: Outstanding! Perfect score! 🌟")
    elif percentage >= 60:
        print("Rating: Good job! Well played. 👍")
    else:
        print("Rating: Keep practicing! You can do better next time. 💪")

# Program Execution Entry Point
if __name__ == "__main__":
    run_quiz()