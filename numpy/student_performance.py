import numpy as np

# Student data
students = np.array(["A", "B", "C", "D", "E", "F", "G", "H"])
subjects = np.array(["Python", "Math", "AI", "NumPy", "SQL"])

marks = np.array([
    [85, 78, 92, 88, 76],
    [72, 90, 65, 80, 85],
    [95, 88, 96, 94, 91],
    [45, 55, 40, 50, 60],
    [68, 72, 75, 70, 80],
    [88, 95, 90, 92, 89],
    [35, 42, 38, 45, 50],
    [78, 82, 85, 79, 88]
])

print("===== STUDENT PERFORMANCE ANALYTICS =====")

# 1. Dataset information
print("\n--- Dataset Information ---")
print("Total Students:", marks.shape[0])
print("Total Subjects:", marks.shape[1])
print("Total Marks Entries:", marks.size)

# 2. Individual student and subject data
print("\n--- Individual Data ---")
print("Marks of Student C:", marks[2])
print("AI Marks of all students:", marks[:, 2])
print("Marks of first three students:\n", marks[:3])
print("Python and Math marks of A, B and C:\n", marks[:3, :2])

# 3. Statistical analysis
print("\n--- Statistical Analysis ---")
print("Overall Average:", np.mean(marks))
print("Overall Highest Mark:", np.max(marks))
print("Overall Lowest Mark:", np.min(marks))
print("Median Marks:", np.median(marks))

student_avg = np.mean(marks, axis=1)
subject_avg = np.mean(marks, axis=0)

print("Student Averages:", student_avg)
print("Subject Averages:", subject_avg)

# 4. Highest and lowest performers
print("\n--- Performance Ranking ---")

highest_student_index = np.argmax(student_avg)
lowest_student_index = np.argmin(student_avg)

print("Highest Performing Student:",
      students[highest_student_index],
      "Average:", student_avg[highest_student_index])

print("Lowest Performing Student:",
      students[lowest_student_index],
      "Average:", student_avg[lowest_student_index])

highest_subject_index = np.argmax(subject_avg)
lowest_subject_index = np.argmin(subject_avg)

print("Highest Average Subject:",
      subjects[highest_subject_index])

print("Lowest Average Subject:",
      subjects[lowest_subject_index])

# 5. Boolean masking
print("\n--- Filtering Students ---")

above_80 = student_avg > 80
below_50 = student_avg < 50

print("Students scoring above 80 average:", students[above_80])
print("Students scoring below 50 average:", students[below_50])

failed_in_any_subject = np.any(marks < 40, axis=1)

print("Students with marks below 40 in any subject:",
      students[failed_in_any_subject])

ai_scores_90_plus = marks[:, 2] >= 90

print("Students scoring 90 or more in AI:",
      students[ai_scores_90_plus])

# 6. Sorting and ranking
print("\n--- Sorting and Ranking ---")

sorted_ai_marks = np.sort(marks[:, 2])
print("Sorted AI Marks:", sorted_ai_marks)

sorted_indices = np.argsort(student_avg)[::-1]

print("Student Ranking:")

for index in sorted_indices:
    print(students[index], ":", student_avg[index])

top_3_indices = sorted_indices[:3]

print("Top 3 Students:", students[top_3_indices])

# 7. Grace marks
print("\n--- Grace Marks ---")

grace_marks = np.clip(marks + 5, 0, 100)

print("Original Marks:\n", marks)
print("Marks after adding 5 grace marks:\n", grace_marks)

# 8. Percentage calculation
print("\n--- Percentage Calculation ---")

total_marks = np.sum(marks, axis=1)
percentage = (total_marks / (marks.shape[1] * 100)) * 100

print("Total Marks:", total_marks)
print("Student Percentages:", percentage)

# 9. Normalization
print("\n--- Min-Max Normalization ---")

normalized_marks = (marks - np.min(marks)) / (
    np.max(marks) - np.min(marks)
)

print("Normalized Marks:\n", normalized_marks)

# 10. Subject-wise improvement analysis
print("\n--- Subject Analysis ---")

weak_subject = subjects[np.argmin(subject_avg)]
strong_subject = subjects[np.argmax(subject_avg)]

print("Strongest Subject:", strong_subject)
print("Weakest Subject:", weak_subject)

# 11. Final report
print("\n===== FINAL REPORT =====")

print("Number of Students:", len(students))
print("Number of Subjects:", len(subjects))
print("Class Average:", np.mean(marks))
print("Top Student:", students[np.argmax(student_avg)])
print("Weakest Subject:", subjects[np.argmin(subject_avg)])
print("Students Needing Attention:", students[failed_in_any_subject])




