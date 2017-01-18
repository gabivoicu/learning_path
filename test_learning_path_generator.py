from __future__ import unicode_literals
import unittest

from learning_path_generator import create_individual_learning_path


class LearningPathTests(unittest.TestCase):

    def test_student_with_no_tests(self):
        self.assertEqual(
            'K.RF,K.RL,K.RI,1.RF,1.RL',
            create_individual_learning_path([])
        )

    def test_student_data_from_files(self):
        # for each line in student_tests.csv, test result against sample_solution.csv


if __name__ == '__main__':
    unittest.main()
