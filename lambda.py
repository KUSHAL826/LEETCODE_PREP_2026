students=[{"name":"Kushal","roll":10,"marks":9.05},
          {"name":"Gagan","roll":11,"marks":9.0},
          {"name":"Bhuvan","roll":12,"marks":8.8}
        ]
students.sort(key=lambda x:x["marks"],reverse=False)
print(students)
print("NAME\t\tMARKS")

for student in students:
    print(f"{student['name']}\t\t{student['marks']}")
