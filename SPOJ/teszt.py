import unittest
from unittest.mock import patch
from io import StringIO

from feladat import Prime_Generator

class TestPrimeGenerator(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '1 10', '3 5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_0(self, mock_stdout, mock_input):
        Prime_Generator()
        self.assertEqual(mock_stdout.getvalue().strip(), "2\n3\n5\n7\n\n3\n5")

    @patch('builtins.input', side_effect=['1', '1 10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_1(self, mock_stdout, mock_input):
        Prime_Generator()
        self.assertEqual(mock_stdout.getvalue().strip(), "2\n3\n5\n7")

    @patch('builtins.input', side_effect=['1', '10 20'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_2(self, mock_stdout, mock_input):
        Prime_Generator()
        self.assertEqual(mock_stdout.getvalue().strip(), "11\n13\n17\n19")

    @patch('builtins.input', side_effect=['2', '5 10', '11 15'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_3(self, mock_stdout, mock_input):
        Prime_Generator()
        self.assertEqual(mock_stdout.getvalue().strip(), "5\n7\n\n11\n13")

    @patch('builtins.input', side_effect=['1', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_4(self, mock_stdout, mock_input):
        Prime_Generator()
        self.assertEqual(mock_stdout.getvalue().strip(), "")  
    
    @patch('builtins.input', side_effect=['1', '1 5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_5(self, mock_stdout, mock_input):
        Prime_Generator()
        self.assertEqual(mock_stdout.getvalue().strip(), "2\n3\n5")

    @patch('builtins.input', side_effect=['1', '7 7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_6(self, mock_stdout, mock_input):
        Prime_Generator()
        self.assertEqual(mock_stdout.getvalue().strip(), "7")

    @patch('builtins.input', side_effect=['1', '4 4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_7(self, mock_stdout, mock_input):
        Prime_Generator()
        self.assertEqual(mock_stdout.getvalue().strip(), "")  

    @patch('builtins.input', side_effect=['1', '8 10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_8(self, mock_stdout, mock_input):
        Prime_Generator()
        self.assertEqual(mock_stdout.getvalue().strip(), "")  

    @patch('builtins.input', side_effect=['1', '11 13'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_9(self, mock_stdout, mock_input):
        Prime_Generator()
        self.assertEqual(mock_stdout.getvalue().strip(), "11\n13")

if __name__ == "__main__":
    unittest.main()