import matplotlib.pyplot as plt
import pandas as pd
data = {
    'Name':['A', 'B', 'C', 'D', 'E'],
    'Maths': [78, 45, 89, 66, 55],
    'Science': [88, 76, 67, 90, 72],
    'English': [70, 65, 80, 60, 75]
}
df = pd.DataFrame(data)
print(df)
plt.plot(df['Name'], df['Maths'], marker = 'o')
plt.title('Math score of students')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()
plt.bar(df['Name'], df['Science'], color = 'orange')
plt.title('Science Scores of the students')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()
plt.hist(df['English'], bins=5, color='green', edgecolor='black')
plt.title('Distribution of English Marks')
plt.xlabel('Marks Range')
plt.ylabel('Number of students')
plt.show()
plt.scatter(df['Maths'], df['Science'], color='red')
plt.title('Maths vs Science performance')
plt.xlabel('Maths Marks')
plt.ylabel('Science Marks')
plt.show()
marks = [78, 88, 70]
subjects = ['Maths', 'Science', 'English']
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title('subject-wise perfomance of student A')
plt.show()