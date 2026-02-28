def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(avg):
    if avg >= 75:
        return "Distinction"
    elif avg >= 60:
        return "Credit"
    else:
        return "General Pass"

marks_input = input("Enter marks separated by commas: ")
student_marks = list(map(int, marks_input.split(",")))

average = calculate_average(student_marks)

print("Average:", average)
print("Grade:", get_grade(average))


def highest_mark(marks):
    return max(marks)
print("Highest Mark:", highest_mark(student_marks))
