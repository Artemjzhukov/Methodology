
Dict example

dict_1 = {"key1": "value1", "key2": "value2"}

dict_1

{'key1': 'value1', 'key2': 'value2'}

dict_2 = {"key1": 10, "key2": ["list_element1", 34], "key3": "value3", "key4": {"subkey1": "v1"}, "key5": 4.5}

dict_2

{'key1': 10,
 'key2': ['list_element1', 34],
 'key3': 'value3',
 'key4': {'subkey1': 'v1'},
 'key5': 4.5}

dict_2["key2"]

['list_element1', 34]

dict_2["key2"] = "My new value"
dict_2["key2"]

'My new value'

dict_2

{'key1': 1,
 'key2': 'My new value',
 'key3': 'value3',
 'key4': {'subkey1': 'v1'},
 'key5': 4.5}

dict_2 = {"key1": 1, "key2": ["list_element1", 34], "key3": "value3", "key4": {"subkey1": "v1"}, "key5": 4.5}

for k, v in dict_2.items():
    print("{}: {}".format(k, v))

key1: 1
key2: ['list_element1', 34]
key3: value3
key4: {'subkey1': 'v1'}
key5: 4.5

for i in dict_2:
    print(i)

key1
key2
key3
key4
key5

import random
list_1 = [random.randint(0, 30) for x in range (0, 100)]
unique_number_list = list(dict.fromkeys(list_1).keys())
unique_number_list

[22,
 18,
 30,
 0,
 12,
 13,
 2,
 1,
 21,
 19,
 28,
 10,
 24,
 9,
 4,
 3,
 17,
 26,
 7,
 23,
 14,
 6,
 27,
 15,
 20,
 11,
 16,
 8]

dict_2 = {"key1": 1, "key2": ["list_element1", 34], "key3": "value3", "key4": {"subkey1": "v1"}, "key5": 4.5}

dict_2

{'key1': 1,
 'key2': ['list_element1', 34],
 'key3': 'value3',
 'key4': {'subkey1': 'v1'},
 'key5': 4.5}

del dict_2["key2"]
dict_2

{'key1': 1, 'key3': 'value3', 'key4': {'subkey1': 'v1'}, 'key5': 4.5}

list_1 = [x for x in range(0, 10)]
list_1

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

dict_1 = {x : x**2 for x in list_1}

dict_1

{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

dict_1 = dict([('Tom', 100), ('Dick', 200), ('Harry', 300)])
dict_1

{'Tom': 100, 'Dick': 200, 'Harry': 300}

dict_1 = dict(Tom=100, Dick=200, Harry=300)
dict_1

{'Tom': 100, 'Dick': 200, 'Harry': 300}

