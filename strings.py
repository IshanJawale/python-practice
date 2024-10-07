course = 'python for beginners'
print(course)
print(course.upper())
print(course.find('e'))
# find() finds the index of the sting: p y t h o n  f o r  b  e  g  i  n  n  e  r  s
#                                      0 1 2 3 4 5  6 7 8  12 13 14 15 16 17 18 19 20
# for 'e' find() prints '12'
print(course.find('z'))
# find() prints -1 if the character dosen't exist and is case sensitive
print(course.replace('for', '4'))  # replaces for with 4
print(course.title())   # prints first letter of all words in uppercase

# in operator
# since python is present in course therefore the output is true
print('python' in course)
# since boolean is not present in course therefore the output is false
print('boolean' in course)
