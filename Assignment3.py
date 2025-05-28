students = []

def log_activity(func):
    def wrapper(*args, **kwargs):
        print("Function is starting")
        result=func(*args, **kwargs)
        print("Function finished successfully")
        return result
    return wrapper


@log_activity
def add_student(name,roll_number,*marks,**other_info):
    total=sum(marks)
    average=total/len(marks) if marks else 0

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    student={
        "name": name,
        "roll_number": roll_number,
        "marks": list(marks),
        "total": total,
        "average": average,
        "grade": grade
    }

    for key in other_info:
        student[key]=other_info[key]

    students.append(student)
    print(f"Student '{name}' added.")

@log_activity
def display_students():
    if not students:
        print("No student data found.")
        return

    print("\nStudent Info:")
    for student in students:
        print(f"\nName: {student['name']}")
        print(f"Roll No: {student['roll_number']}")
        print(f"Marks: {student['marks']}")
        print(f"Total: {student['total']}")
        print(f"Grade: {student['grade']}")


add_student("Monica", 101, 90, 85, 88, grade="A", gender="Female")
add_student("Anu", 102, 78, 80, 74, grade="B")
display_students()