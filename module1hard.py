grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
first = sum(grades[0]) / len(grades[0])
second = sum(grades[1]) / len(grades[1])
third = sum(grades[2]) / len(grades[2])
fourth = sum(grades[3]) / len(grades[3])
fifth = sum(grades[4]) / len(grades[4])
my_list1 = students
my_list1 = sorted(my_list1)
my_list2 = [first, second, third, fourth, fifth]
str(my_list1)
str(my_list2)
set = {}
for key in my_list1:
    for value in my_list2:
        set[key] = value
        my_list2.remove(value)
        break
print(str(set))