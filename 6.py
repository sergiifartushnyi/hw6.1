import string


def get_characters_between(letter_pair):

    all_letters = string.ascii_letters

    letter_pair = letter_pair.strip('"')
    start_letter, end_letter = letter_pair.split("-")

    start_index = all_letters.index(start_letter)
    end_index = all_letters.index(end_letter)

    result = all_letters[start_index:end_index + 1]

    return result

input_letters = input("Введіть дві літери через дефіс:")
print(get_characters_between(input_letters))
