print("CW28 by Lenny Metlitsky 4/19/23")

with open("cw28data.txt", "r") as file_obj:
    data = file_obj.read()

data = data.strip().split("\n")

def studentAverage(student : str):
    items = student.split()
    grades = [float(item) for item in items if item.isdigit()]
    return sum(grades) / len(grades) 

def studentAverageDropLowest(student : str):
    items = student.split()
    grades = [float(item) for item in items if item.isdigit()]
    grades.remove(min(grades))
    return sum(grades) / len(grades) 

def compareAverages(averages : list):
    for student_data in averages:
        name = student_data.split()[1]
        print(f"Student {name}, avg: {studentAverage(student_data)}, dropped_lowest: {studentAverageDropLowest(student_data)}")

compareAverages(data)