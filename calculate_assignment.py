def calculate_assignment(assignments_arg):
    sum_of_grades = 0
    for grade in assignments_arg.values():
        sum_of_grades += grade
    final_grade = round(sum_of_grades / len(assignments_arg), 2)
    print(final_grade)
