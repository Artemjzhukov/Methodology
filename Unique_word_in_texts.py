mutiline_text =
mutiline_text = mutiline_text.replace('\n', "")
# remove special chars, punctuation etc.
cleaned_multiline_text = ""
for char in mutiline_text:
    if char == " ":
        cleaned_multiline_text += char
    elif char.isalnum():  # using the isalnum() method of strings.
        cleaned_multiline_text += char
    else:
        cleaned_multiline_text += " "
cleaned_multiline_text
# Another way of doing this (Faster and less code)
import re

cleaned_multiline_text_2 = re.sub(r'[?|$|.|!|"|,|;|:]',r'',mutiline_text)
cleaned_multiline_text_2

list_of_words = cleaned_multiline_text.split()

# Use set to get unique words
unique_words_as_list = list(set(list_of_words))
len(unique_words_as_list)

# Use dict to do the same
unique_words_as_dict = dict.fromkeys(list_of_words)
len(list(unique_words_as_dict.keys()))

for word in list_of_words:
    if unique_words_as_dict[word] is None:
        unique_words_as_dict[word] = 1
    else:
        unique_words_as_dict[word] += 1
unique_words_as_dict

top_words = sorted(unique_words_as_dict.items(), key=lambda key_val_tuple: key_val_tuple[1], reverse=True)

top_words[:25]
