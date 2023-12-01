import unittest


def sum_calibration_values(all_instructions):
    all_sum = 0

    for instruction in all_instructions:
        all_sum += find_numbers(instruction)

    return all_sum


def find_numbers(instruction):
    numbers = [c for c in instruction if c.isdigit()]
    return int(numbers[0] + numbers[-1])


class CalibrationTestCase(unittest.TestCase):
    def test_find_numbers_with_two_digits(self):
        instruction = "pqr3stu8vwx"
        self.assertEqual(find_numbers(instruction), 38)

    def test_find_numbers_with_a_single_digit(self):
        instruction = "treb7uchet"
        self.assertEqual(find_numbers(instruction), 77)


# sum all the values with the given input text
all_instructions = open("input.txt").readlines()
print(sum_calibration_values(all_instructions))

if __name__ == "__main__":
    unittest.main()
