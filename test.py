students = {}

# Add a few students test scores.
students['Andre'] = 20
students['Ryan'] = 67
students['Alex'] = 85
students['Ted'] = 75

sorted_alphabetical = sorted(students, key=students.get, reverse=True)
for key in sorted_alphabetical:
    print(key + ' scored ' + str(students[key]))
print(sorted_alphabetical)