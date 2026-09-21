#keyword arguments
def student_info(**details):
    for i,(keys,value) in enumerate(details.items()):
        print(f"{i}.{keys} - {value}")
    print("-------------------")
student_info(name="KUSHAL",roll=10)
student_info(name="Chandan",roll=11,course="Python")
