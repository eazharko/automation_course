students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print("Students " + ', '.join(students) + (" study these subjects: " + ', '.join(subjects)))

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
sentence = "Students " + ', '.join(students) + " study these subjects: " + ', '.join(subjects)
print(sentence)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
student_1, student_2, student_3 = students
subject_1, subject_2, subject_3 = subjects
sentence = "Students {0}, {1}, {2} study these subjects: {3}, {4}, {5}"
print(sentence.format(student_1, student_2, student_3, subject_1, subject_2, subject_3))

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
student_1, student_2, student_3 = students
subject_1, subject_2, subject_3 = subjects
sentence = f'Students {student_1}, {student_2}, {student_3} study these subjects: {subject_1}, {subject_2}, {subject_3}'
print(sentence)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
sentence = f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}"
print(sentence)