def mutate_string(string, position, character):
    new_str = ""
    for i in range(len(string)):
        if i == position:
            new_str += character
        else:
            new_str += string[i]
    return new_str
