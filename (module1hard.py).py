grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2,],[4,4,3],[5,5,5,4,5,]]
students = {'Jonny','Bilbo','Steve','Khendrik','Aaron'}
aver_grade0 = sum(grades[0])/len(grades[0])
aver_grade1 = sum(grades[1])/len(grades[1])
aver_grade2 = sum(grades[2])/len(grades[2])
aver_grade3 = sum(grades[3])/len(grades[3])
aver_grade4 = sum(grades[4])/len(grades[4])
students_list = list(students)
students_list.sort()
student_dict = {students_list[0]:aver_grade0,students_list[1]:aver_grade1,students_list[2]:aver_grade2,students_list[3]:aver_grade3,students_list[4]:aver_grade4}
print(student_dict)