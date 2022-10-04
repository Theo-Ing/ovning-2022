def txt_to_list(filename):
    with open(filename, encoding='utf8') as f:
        raw_string = f.read()
        result = raw_string.split(sep="\n")
    return result

print(txt_to_list("test.txt"))