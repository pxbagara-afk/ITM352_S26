def get_character_frequencies(input_string):
    frequencies = {}
    for char in input_string:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


if __name__ == "__main__":
    mydict = get_character_frequencies("Snow White and the Seven Dwarves")
    print(mydict)