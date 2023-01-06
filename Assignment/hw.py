def grading(hw):
    result = []
    
    for student_grades in hw:
        student = [student_grades[0]]
        if len(student_grades[1]) == 5:
            scores = sorted(student_grades[1])[1:]
            avg = sum(scores) / 4
        else:
            scores = sorted(student_grades[1])[2:]
            avg = sum(scores) / 4
        
        student.append(avg)
        result.append(student)
    
    return result
