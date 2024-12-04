import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usain = Runner('Усейн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for r in cls.all_results:
            print(r)

    def test_runner1(self):
        tournament = Tournament(90, self.usain, self.nick)
        all_results = tournament.start()
        self.all_results.append(all_results)
        self.assertTrue(all_results[max(all_results.keys())] == "Ник")

    def test_runner2(self):
        tournament = Tournament(90, self.andrey, self.nick)
        all_results = tournament.start()
        self.all_results.append(all_results)
        self.assertTrue(all_results[max(all_results.keys())] == "Ник")

    def test_runner3(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        all_results = tournament.start()
        self.all_results.append(all_results)
        self.assertTrue(all_results[max(all_results.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
