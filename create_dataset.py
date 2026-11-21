import csv

columns = ['Student ID', 'Department', 'Level', 'Attendance Percentage', 'Average Examination Score']
students = [['24/15653', 'Political Science ', 300, 92, 92], ['24/15701', 'Public Health Science ', 400, 71, 77], ['24/13725', 'Mathematics ', 300, 68, 82], ['24/13904', 'Criminology ', 100, 91, 94], ['24/14162', 'Human Anatomy ', 300, 87, 73], ['24/15627', 'Mass communication ', 400, 88, 75], ['24/14843', 'Data Science', 400, 79, 83], ['24/13888', 'Human Physiology ', 400, 85, 96], ['24/15115', 'Software Engineering', 200, 97, 86], ['24/14837', 'Cyber Security', 200, 76, 79], ['24/15214', 'Biochemistry ', 300, 93, 85], ['24/13233', 'Nursing ', 100, 90, 91], ['24/13724', 'Psychology ', 100, 66, 59], ['24/15332', 'Accounting', 400, 81, 70], ['24/15532', 'Computer Science', 100, 98, 62], ['24/15739', 'Broadcasting ', 200, 84, 80], ['24/13770', 'Law', 200, 96, 88], ['24/15774', 'Microbiology ', 200, 74, 68], ['24/13711', 'Architecture ', 300, 95, 64], ['24/14429', 'Industrial chemistry ', 100, 89, 89]]

with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(students)

print(f"Created student_dataset.csv with {len(students)} records.")
