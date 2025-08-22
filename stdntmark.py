import matplotlib.pyplot as plt
student_names = ["Sanjay", "Rahul", "Karan", "Wasim", "Ramesh", "Ajay", "Sartraj", "Priya"]
student_marks = [35, 50, 20, 45, 25, 40, 25, 40]
marks_perc = []
for x in student_marks:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)
def marks_line_chart():
    plt.plot(student_names, student_marks)
    plt.title("Student Mark Graph")
    plt.xlabel("Student Name")
    plt.ylabel("Student Mark")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(student_names, marks_perc)
    plt.title("Students' Percentage Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Percentage")
    plt.show()
percentage_bar_chart()