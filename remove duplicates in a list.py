numbers = [1, 3, 4, 2, 1, 6, 3, 8, 7, 3, 4, 8, 5, 5, 9, 1, 8, 3, 9, 3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
