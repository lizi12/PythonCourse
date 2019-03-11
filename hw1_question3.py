def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    res = {}

    for key in subj1_all_students:
        if key not in subj2_all_students or key == "course_name":
            continue
        if max(subj1_all_students[key]) > max(subj2_all_students[key]):
            res[key] = subj1_all_students["course_name"]
        else:
            res[key] = subj2_all_students["course_name"]
    return res

#table = compare_subjects_within_student(math_all_students, history_all_students)
#print(table)                                  

if __name__ == '__main__':
    # Question 3

    """data- the grades of students organized in two different dictionaries per subject. 
    the students names are the keys and their grades are the values (first exam is first).
    each dictionry inclueds subject key which its value is the subject name at the end of the dict. """
    math_all_students = {
    "course_name": "math",
    "Kelly": [78,100],
    "Brenda": [100,90],
    "Noam": [87,59],
    "Yael": [95,89],
    "Yotam": [58,76],
    "Gili": [88,85]
    }

    history_all_students = {
    "course_name": "history",
    "Brenda": [94,99],
    "Noam": [60,100],
    "Yael": [85,62],
    "Yotam": [55,91],
    "Gili": [70,98],
    "Dino": [50,50]
    }
    subj1_all_students = math_all_students
    subj2_all_students = history_all_students
    print("Question 3 solution: ")
    compare_subjects_within_student(subj1_all_students, subj2_all_students)                                  

    
    
