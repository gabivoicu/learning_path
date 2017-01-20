from __future__ import unicode_literals
import unittest

from learning_path_generator import create_individual_learning_path
DOMAINS_ORDERED = (
                    ('0', ('RF', 'RL', 'RI')), 
                    ('1', ('RF', 'RL', 'RI')), 
                    ('2', ('RF', 'RI', 'RL', 'L')), 
                    ('3', ('RF', 'RL', 'RI', 'L')), 
                    ('4', ('RI', 'RL', 'L')), 
                    ('5', ('RI', 'RL', 'L')), 
                    ('6', ('RI', 'RL'))
                )


class LearningPathTests(unittest.TestCase):

    def test_student_with_no_tests(self):
        self.assertEqual(
            'K.RF,K.RL,K.RI,1.RF,1.RL',
            create_individual_learning_path(DOMAINS_ORDERED, {'Student Name': 'Hermione Granger'})
        )

    def test_student_albin(self):
        self.assertEqual(
            'Albin Stanton,K.RI,1.RI,2.RF,2.RI,3.RF',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '3', 'Student Name': 'Albin Stanton', 
                                        'RF': '2', 'L': '3', 'RI': 'K'})
        )

    def test_student_erik(self):
        self.assertEqual(
            'Erik Purdy,1.RL,1.RI,2.RI,2.RL,2.L',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '1', 'Student Name': 'Erik Purdy', 
                                        'RF': '3', 'L': '1', 'RI': '1'})
        )

    def test_student_aimee(self):
        self.assertEqual(
            'Aimee Cole,K.RF,K.RL,1.RF,1.RL,1.RI',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': 'K', 'Student Name': 'Aimee Cole', 
                                        'RF': 'K', 'L': '2', 'RI': '1'})
        )

    def test_student_frederik(self):
        self.assertEqual(
            'Frederik Schulist,2.RF,3.RF,4.RI,4.RL,4.L',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '4', 'Student Name': 'Frederik Schulist', 
                                        'RF': '2', 'L': '4', 'RI': '4'})
        )

    def test_student_addie(self):
        self.assertEqual(
            'Addie Green,K.RI,1.RI,2.RF,2.RI,2.L',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '3', 'Student Name': 'Addie Green', 
                                        'RF': '2', 'L': '1', 'RI': 'K'})
        )

    def test_student_missouri(self):
        self.assertEqual(
            'Missouri Auer,1.RI,2.RI,2.RL,2.L,3.RL',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '2', 'Student Name': 'Missouri Auer', 
                                        'RF': '4', 'L': '1', 'RI': '1'})
        )

    def test_student_christopher(self):
        self.assertEqual(
            'Christopher Hayes,K.RI,1.RI,2.RI,2.L,3.RI',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '5', 'Student Name': 'Christopher Hayes', 
                                        'RF': '5', 'L': '2', 'RI': 'K'})
        )

    def test_student_enos(self):
        self.assertEqual(
            'Enos Jacobi,K.RF,K.RL,1.RF,1.RL,2.RF',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': 'K', 'Student Name': 'Enos Jacobi', 
                                        'RF': 'K', 'L': '5', 'RI': '4'})
        )

    def test_student_conrad(self):
        self.assertEqual(
            'Conrad Nitzsche,K.RI,1.RF,1.RI,2.RF,2.RI',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '5', 'Student Name': 'Conrad Nitzsche', 
                                        'RF': '1', 'L': '3', 'RI': 'K'})
        )

    def test_student_jazlyn(self):
        self.assertEqual(
            'Jazlyn Wisoky,3.RL,3.L,4.RL,4.L,5.RI',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '3', 'Student Name': 'Jazlyn Wisoky', 
                                        'RF': '4', 'L': '3', 'RI': '5'})
        )

    def test_student_kelley(self):
        self.assertEqual(
            'Kelley Emard,K.RF,K.RI,1.RF,1.RI,2.RF',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '2', 'Student Name': 'Kelley Emard', 
                                        'RF': 'K', 'L': '4', 'RI': 'K'})
        )

    def test_student_dell(self):
        self.assertEqual(
            'Dell Kozey,K.RF,1.RF,2.RF,2.L,3.RF',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '4', 'Student Name': 'Dell Kozey', 
                                        'RF': 'K', 'L': '2', 'RI': '3'})
        )

    def test_student_kraig(self):
        self.assertEqual(
            'Kraig Goldner,2.RI,3.RI,3.L,4.RI,4.RL',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '4', 'Student Name': 'Kraig Goldner', 
                                        'RF': '5', 'L': '3', 'RI': '2'})
        )

    def test_student_stephon(self):
        self.assertEqual(
            'Stephon Ondricka,2.L,3.RI,3.L,4.RI,4.L',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '5', 'Student Name': 'Stephon Ondricka', 
                                        'RF': '5', 'L': 'K', 'RI': '3'})
        )

    def test_student_tracey(self):
        self.assertEqual(
            'Tracey Lind,K.RF,1.RF,1.RL,2.RF,2.RL',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '1', 'Student Name': 'Tracey Lind', 
                                        'RF': 'K', 'L': '1', 'RI': '3'})
        )

    def test_student_elissa(self):
        self.assertEqual(
            'Elissa Schinner,1.RI,2.RI,3.RL,3.RI,4.RI',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '3', 'Student Name': 'Elissa Schinner', 
                                        'RF': '5', 'L': '4', 'RI': '1'})
        )

    def test_student_orpha(self):
        self.assertEqual(
            'Orpha Bartoletti,1.RF,2.RF,2.RI,2.L,3.RF',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '3', 'Student Name': 'Orpha Bartoletti', 
                                        'RF': '1', 'L': 'K', 'RI': '2'})
        )

    def test_student_timothy(self):
        self.assertEqual(
            'Timmothy Torphy,K.RF,K.RI,1.RF,1.RL,1.RI',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '1', 'Student Name': 'Timmothy Torphy', 
                                        'RF': 'K', 'L': '1', 'RI': 'K'})
        )

    def test_student_maia(self):
        self.assertEqual(
            'Maia Torphy,K.RF,1.RF,2.RF,2.RI,2.L',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '3', 'Student Name': 'Maia Torphy', 
                                        'RF': 'K', 'L': '1', 'RI': '2'})
        )

    def test_student_danyka(self):
        self.assertEqual(
            'Danyka Pfeffer,2.L,3.L,4.L,5.RI,5.RL',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '5', 'Student Name': 'Danyka Pfeffer', 
                                        'RF': '5', 'L': '2', 'RI': '5'})
        )

    def test_student_scotty(self):
        self.assertEqual(
            'Scotty Kovacek,K.RF,1.RF,2.RF,2.L,3.RF',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '3', 'Student Name': 'Scotty Kovacek', 
                                        'RF': 'K', 'L': '1', 'RI': '3'})
        )

    def test_student_leo(self):
        self.assertEqual(
            'Leo O\'Connell,K.RL,K.RI,1.RL,1.RI,2.RI',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': 'K', 'Student Name': "Leo O'Connell", 
                                        'RF': '3', 'L': '1', 'RI': 'K'})
        )

    def test_student_cameron(self):
        self.assertEqual(
            'Cameron Prohaska,2.RF,2.RI,3.RF,3.RI,4.RI',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '4', 'Student Name': 'Cameron Prohaska', 
                                        'RF': '2', 'L': '4', 'RI': '2'})
        )

    def test_student_angus(self):
        self.assertEqual(
            'Angus Torp,2.RF,2.L,3.RF,3.L,4.RL',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '4', 'Student Name': 'Angus Torp', 
                                        'RF': '2', 'L': '1', 'RI': '5'})
        )

    def test_student_douglas(self):
        self.assertEqual(
            'Douglas Feil,1.RF,1.RL,1.RI,2.RF,2.RI',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '1', 'Student Name': 'Douglas Feil', 
                                        'RF': '1', 'L': 'K', 'RI': '1'})
        )

    def test_student_maxime(self):
        self.assertEqual(
            'Maxime Runte,K.RL,1.RL,2.RF,2.RL,2.L',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': 'K', 'Student Name': 'Maxime Runte', 
                                        'RF': '2', 'L': 'K', 'RI': '4'})
        )

    def test_student_mortimer(self):
        self.assertEqual(
            'Mortimer Denesik,K.RF,K.RL,1.RF,1.RL,2.RF',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': 'K', 'Student Name': 'Mortimer Denesik', 
                                        'RF': 'K', 'L': '3', 'RI': '2'})
        )

    def test_student_bennett(self):
        self.assertEqual(
            'Bennett Muller,2.L,3.L,4.L,5.RI,5.RL',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '5', 'Student Name': 'Bennett Muller', 
                                        'RF': '5', 'L': '1', 'RI': '5'})
        )

    def test_student_ayana(self):
        self.assertEqual(
            'Ayana Runolfsson,K.RF,1.RF,2.RF,2.RL,2.L',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '2', 'Student Name': 'Ayana Runolfsson', 
                                        'RF': 'K', 'L': '2', 'RI': '5'})
        )

    def test_student_angelina(self):
        self.assertEqual(
            'Angelina Runolfsson,K.RF,1.RF,1.RI,2.RF,2.RI',
            create_individual_learning_path(DOMAINS_ORDERED, {'RL': '3', 'Student Name': 'Angelina Runolfsson', 
                                        'RF': 'K', 'L': '1', 'RI': '1'})
        )

if __name__ == '__main__':
    unittest.main()
