# This demos the Simple-Test, Parameter-Range, and Collection-Order patterns in unit testing

import unittest


def add(a, b):
    return a + b


def calculate_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def sort_scores_high_to_low(scores):
    return sorted(scores, reverse=True)


class TestSimplePatterns(unittest.TestCase):

    def test_simple_test_pattern(self):
        # Simple-Test Pattern:
        # One clear input and one expected output.
        result = add(2, 3)
        self.assertEqual(result, 5)


    def test_parameter_range_pattern(self):
        # Parameter-Range Pattern:
        # Test low, middle, high, and invalid values.
        self.assertEqual(calculate_grade(0), "F")
        self.assertEqual(calculate_grade(59), "F")
        self.assertEqual(calculate_grade(60), "D")
        self.assertEqual(calculate_grade(75), "C")
        self.assertEqual(calculate_grade(89), "B")
        self.assertEqual(calculate_grade(90), "A")
        self.assertEqual(calculate_grade(100), "A")

        with self.assertRaises(ValueError):
            calculate_grade(-1)

        with self.assertRaises(ValueError):
            calculate_grade(101)


    def test_collection_order_pattern(self):
        # Collection-Order Pattern:
        # Make sure a returned collection is in the correct order.
        scores = [70, 100, 85, 90]
        result = sort_scores_high_to_low(scores)

        self.assertEqual(result, [100, 90, 85, 70])


if __name__ == "__main__":
    unittest.main()