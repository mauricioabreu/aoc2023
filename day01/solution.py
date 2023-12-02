import unittest


def sum_calibration_values(all_instructions):
    first_sum, second_sum = 0, 0

    for instruction in all_instructions:
        first, second = find_numbers(instruction)
        first_sum += first
        second_sum += second

    return first_sum, second_sum


def find_numbers(instruction):
    digits = []
    digits_as_letters = []

    number_words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for i in range(len(instruction)):
        if instruction[i].isdigit():
            digits.append(instruction[i])
            digits_as_letters.append(instruction[i])
        for word in number_words:
            if instruction[i : i + len(word)] == word:
                digits_as_letters.append(number_words[word])

    only_digits = 0
    letter_digits = 0

    if digits:
        only_digits = int(digits[0] + digits[-1])

    if digits_as_letters:
        letter_digits = int(digits_as_letters[0] + digits_as_letters[-1])

    return only_digits, letter_digits


class CalibrationTestCase(unittest.TestCase):
    def test_find_numbers_with_two_digits(self):
        instruction = "pqr3stu8vwx"
        only_digits, _ = find_numbers(instruction)
        self.assertEqual(only_digits, 38)

    def test_find_numbers_with_a_single_digit(self):
        instruction = "treb7uchet"
        only_digits, _ = find_numbers(instruction)
        self.assertEqual(only_digits, 77)

    def test_find_numbers_as_letters(self):
        instruction = "two1nine"
        _, letter_digits = find_numbers(instruction)
        self.assertEqual(letter_digits, 29)

        instruction = "twone"
        _, letter_digits = find_numbers(instruction)
        self.assertEqual(letter_digits, 21)


# sum all the values with the given input text
all_instructions = open("input.txt").readlines()
print(sum_calibration_values(all_instructions))

if __name__ == "__main__":
    unittest.main()
