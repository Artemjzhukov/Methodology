my_string = 'Hello World!'
my_string
'Hello World!'
my_string = "Hello World 2!"
my_string
'Hello World 2!'
my_multiline_string = """It started here
But continued here.
"""
my_multiline_string
'It started here\n\nBut continued here.\n'


my_str = "Hello World!"
my_str[0]
'H'
my_str[4]
'o'
my_str[len(my_str) - 1]
'!'
my_str[-1]
'!'


my_str = "Hello World! I am learning data wrangling"
my_str[2:11]
'llo World'
my_str[-31:]
'd! I am learning data wrangling'
my_str[-10:-1]
' wranglin'


my_str = "Name, Age, Sex, Address"
list_1 = my_str.split(",")
list_1
['Name', ' Age', ' Sex', ' Address']
" | ".join(list_1)
'Name |  Age |  Sex |  Address'
