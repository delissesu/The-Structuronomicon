"""
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and print each one on a new line.

There are students in this class whose names and grades are provided as input. The lowest grade belongs to Tina. The second lowest grade belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    from typing import List, Union

    student_grade: List[List[Union[str, float]]] = []
    
    for _ in range(int(input())):  # Loop for number of students
        name : str = input()
        score : float = float(input())
        student_grade.append([name, score])
    
    # Sort the student_grade list by grades
    student_grade.sort(key=lambda x: x[1])
    
    # Find the second lowest grade
    lowest_grade = student_grade[0][1]
    second_lowest = None
    for student in student_grade:
        if student[1] > lowest_grade:
            second_lowest = student[1]
            break
    
    if second_lowest is None:
        print("Not enough unique grades to determine the second lowest.")
        exit()
    
    # Collect students with the second lowest grade
    second_lowest_students = [student[0] for student in student_grade if student[1] == second_lowest]
    second_lowest_students.sort()
    
    for name in second_lowest_students:
        print(name)