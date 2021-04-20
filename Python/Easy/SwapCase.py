def swap_case(s):
    new_s = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                new_s += char.lower()
            else:
                new_s += char.upper()
        else:
            new_s += char
    return new_s
