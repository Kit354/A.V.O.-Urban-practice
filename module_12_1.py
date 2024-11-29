import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk(self):
        test = Runner('Кирилл')
        for ran in range(10):
            test.walk()
        self.assertEqual(test.distance, 50)

    def test_run(self):
        test = Runner('Макс')
        for ran in range(10):
            test.run()
        self.assertEqual(test.distance, 100)

    def test_challenge(self):
        test_1 = Runner('Ваня')
        test_2 = Runner('Миша')
        for ran in range(10):
            test_1.walk()
            test_2.run()
        self.assertNotEqual(test_1.distance, test_2.distance)


if __name__ == "__main__":
    unittest.main()
