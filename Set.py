import random
list_1 = [random.randint(0, 30) for x in range (0, 100)]

unique_number_list = list(set(list_1))

set1 = {"Apple", "Orange", "Banana"}
set2 = {"Pear", "Peach", "Mango", "Banana"}
set1
{'Apple', 'Banana', 'Orange'}
set2
{'Banana', 'Mango', 'Peach', 'Pear'}
set1 | set2
{'Apple', 'Banana', 'Mango', 'Orange', 'Peach', 'Pear'}
set1 & set2
{'Banana'}

my_null_set = set({})
type(my_null_set)
set
my_null_set = {}
type(my_null_set)
dict
