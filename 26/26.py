#LIST COMPREHENSION
'''
numbers = [1,2,3]
new_number = [n+1 for n in numbers]
print(new_number)

name = "Angela"
new_name = [l for l in name]
print(new_name)

new_list = [i*2 for i in range(1,5)]
print(new_list)

name_list = ["Shefrin", "Ayra", "Gow", "Ashnaa", "Riithu"]
short_name = [n for n in name_list if len(n) <5]
print(short_name)

cap_names = [n.upper() for n in name_list if len(n)>5]
print(cap_names)
'''

#DICTIONARY COMPREHENSION
"""
name_list = ["Shefrin", "Ayra", "Gow", "Ashnaa", "Riithu"]
import random
student_score = {student:random.randint(1,100) for student in name_list}

print(student_score)

passed_students = {student:val for (student,val) in student_score.items() if val > 60}

print(passed_students)
"""

d = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56,77,95]
}
import pandas
student_dataframe = pandas.DataFrame(d)
# print(student_dataframe)

#loop through data frame
# for (key,val) in student_dataframe.items():
#     print(key)
#     print(val)

#loop through rows of dataframe
for (index,row) in student_dataframe.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Lilly":
        print(row.score)