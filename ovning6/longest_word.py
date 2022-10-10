def word_length(string):
    counter = 0
    max_length = 0
    for char in string:
        if char.isalpha():
            counter += 1
        else:
            if counter > max_length:
                max_length = counter
            counter = 0
    if counter > max_length:
        max_length = counter
    return max_length

def longest_word(string):
    current_wrd = ""
    longest_wrd = ""
    for char in string:
        if char.isalpha():
            current_wrd += char
        else:
            if len(current_wrd) > len(longest_wrd):
                longest_wrd = current_wrd
            current_wrd = ""
    if len(current_wrd) > len(longest_wrd):
        longest_wrd = current_wrd
    return longest_wrd

def load_file(file_name):
    with open(file_name, encoding='utf8') as f:
        text = f.read()
        text = text.replace("\n", " ")
        text = text.replace("\t", " ")
    return text

phrase = "Flott är hoooooottttttt"
print(word_length(phrase))
print(longest_word(phrase))

text = load_file("dearest_creature.txt")
print(longest_word(text))