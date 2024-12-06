import unittest
import tests_12_3

test_Run_Tour = unittest.TestSuite()
test_Run_Tour.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_Run_Tour.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_Run_Tour)
