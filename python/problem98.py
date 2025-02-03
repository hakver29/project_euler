import math
from collections import defaultdict

def isSquare(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

def calculateSum(word):
    S = ''
    for i in range(len(word)):
        S += str(ord(word[i])-64)
    return int(S)

def sort_string(s):
    return ''.join(sorted(s))

def group_words_by_sorted_key(words):
    grouped = defaultdict(list)
    for word in words:
        sorted_key = ''.join(sorted(word))
        grouped[sorted_key].append(word)
    return dict(grouped)

def remove_small_entries(d):
    return {key: value for key, value in d.items() if len(value) >= 2}

def get_ranges(dictionary):
    min, max = float('inf'), 0
    for key in dictionary:
        if len(key) < min:
            min = len(key)
        if len(key) > max:
            max = len(key)
    return min, max

def get_squares(min,max)->list:
    n = 0
    L = []
    while len(str(n**2)) <= max:
        if len(str(n**2)) >= min:
            L.append(str(n**2))
        n += 1
    return L


def can_map_number_to_string(number_str, string):
    # Check if both have the same length
    if len(number_str) != len(string):
        return False, defaultdict

    digit_to_char = {}
    char_to_digit = {}

    for digit, char in zip(number_str, string):
        # Check if the digit is already mapped
        if digit in digit_to_char:
            if digit_to_char[digit] != char:
                return False, defaultdict  # Digit maps to different characters
        else:
            digit_to_char[digit] = char

        # Check if the character is already mapped
        if char in char_to_digit:
            if char_to_digit[char] != digit:
                return False, defaultdict  # Character maps to different digits
        else:
            char_to_digit[char] = digit

    return True, digit_to_char

def main():
    file = open("p098_words.txt", "r")
    M = file.read().replace("\"", "").split(",")
    M_dict = group_words_by_sorted_key(M)
    M_dict_filtered = remove_small_entries(M_dict)
    max_square = 0
    (min_square_range,max_square_range) = get_ranges(M_dict_filtered)
    L = get_squares(min_square_range,max_square_range)
    for key in M_dict_filtered:
        mappings = [s for s in L if len(s) == len(key)]
        word1 = M_dict_filtered[key][0]
        word2 = M_dict_filtered[key][1]
        for mapping in mappings:
            (can_map_number, char_to_digit) = can_map_number_to_string(word1, mapping)
            if can_map_number:
                word2_number = "".join([char_to_digit[i] for i in word2])
                word1_number = "".join([char_to_digit[i] for i in word1])
                if word2_number in mappings:
                    word1_number = int(word1_number)
                    word2_number = int(word2_number)
                    if max(word1_number, word2_number) > max_square:
                        max_square = max(word1_number, word2_number)

    return max_square

print(main())