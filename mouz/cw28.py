print("CW28 by Lenny Metlitsky 4/19/23")

with open("cw28data.txt", "r") as file_obj:
    data = file_obj.read()

data = data.strip().split("\n")

def studentAverage(student : str):
    items = student.split()
    # Only keep numbers aka the grades
    grades = [float(item) for item in items if item.isdigit()]
    return sum(grades) / len(grades) 

def studentAverageDropLowest(student : str):
    items = student.split()
    # Only keep numbers aka the grades
    grades = [float(item) for item in items if item.isdigit()] 
    grades.remove(min(grades))
    return sum(grades) / len(grades) 

def compareAverages(averages : list):
    calculated_avgs = []
    for student_data in averages:
        name = student_data.split()[1]
        avg = studentAverage(student_data)
        dropped = studentAverageDropLowest(student_data)
        print(f"Student {name}, avg: {avg}, dropped_lowest: {dropped}")
        calculated_avgs.append([avg, dropped])
    return calculated_avgs

calculated_avgs = compareAverages(data)

# Write the computed data
with open("cw28output.txt", "w") as file_obj:
    for i in range(len(data)):
        student_data = data[i].split()
        calculated_avg = [str(x) for x in calculated_avgs[i]]
        student_data = student_data[:2]
        student_data.extend(calculated_avg)
        file_obj.write(" ".join(student_data) + "\n")
