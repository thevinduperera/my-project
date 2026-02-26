def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(avg):
    if avg >= 75:
        return "Distinction"
    elif avg >= 60:
        return "Credit"
    else:
        return "General Pass"

student_marks = [75, 80, 90]
average = calculate_average(student_marks)

print("Average:", average)
print("Grade:", get_grade(average))
