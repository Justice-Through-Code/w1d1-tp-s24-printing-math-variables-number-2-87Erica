# Calcuting weighted average grade for students in three subjects_Erica Graham
def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Enter student name:")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = input("Enter Math score:")
    science_score = input("Enter Science score:")
    english_score = input("Enter English score:")

    # Calculate the average grade
    # Converted strings into integers using the int()
    average_grade = (int(math_score) + int(science_score) + int(english_score)) / 3
    
    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    #For windows I need to use python -m pytest test_grade_calculator.py
    print(f"{student_name}, {average_grade:.2f}")