import unittest
from unittest.mock import patch
from io import StringIO
from feladat import picad

class TestPrimeGenerator(unittest.TestCase):
    @patch('builtins.input', side_effect=['5 10', '4', '1 8', '5 8', '7 10', '8 9'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_1(self, mock_stdout, mock_input):
        picad()
        self.assertEqual(mock_stdout.getvalue().strip(), "1 4")

    @patch('builtins.input', side_effect=['5 20', '3', '5 20', '5 10', '11 20'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_2(self, mock_stdout, mock_input):
        picad()
        self.assertEqual(mock_stdout.getvalue().strip(), "2 2")

    @patch('builtins.input', side_effect=['1 2', '2', '1 1', '2 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_3(self, mock_stdout, mock_input):
        picad()
        self.assertEqual(mock_stdout.getvalue().strip(), "1 1")

    @patch('builtins.input', side_effect=['5 10', '3', '1 5', '5 10', '11 15'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_4(self, mock_stdout, mock_input):
        picad()
        self.assertEqual(mock_stdout.getvalue().strip(), "1 2")

    @patch('builtins.input', side_effect=['1 8', '4', '1 8', '2 3', '1 7', '8 9'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_5(self, mock_stdout, mock_input):
        picad()
        self.assertEqual(mock_stdout.getvalue().strip(), "2 3")

    @patch('builtins.input', side_effect=['15 20', '3', '1 5', '6 10', '11 14'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_6(self, mock_stdout, mock_input):
        picad()
        self.assertEqual(mock_stdout.getvalue().strip(), "0 0")

    @patch('builtins.input', side_effect=['10 20', '5', '5 25', '8 22', '10 15', '12 18', '19 21'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_7(self, mock_stdout, mock_input):
        picad()
        self.assertEqual(mock_stdout.getvalue().strip(), "3 4")

    @patch('builtins.input', side_effect=['10 20', '6', '5 12', '10 15', '14 20', '18 22', '8 16', '11 19'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_8(self, mock_stdout, mock_input):
        picad()
        self.assertEqual(mock_stdout.getvalue().strip(), "2 4")

    @patch('builtins.input', side_effect=['0 10', '4', '0 5', '5 10', '3 7', '7 9'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_9(self, mock_stdout, mock_input):
        picad()
        self.assertEqual(mock_stdout.getvalue().strip(), "1 3")

    @patch('builtins.input', side_effect=['25 35', '7', '10 20', '15 25', '28 32', '30 40', '33 35', '36 50', '25 30'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_10(self, mock_stdout, mock_input):
        picad()
        self.assertEqual(mock_stdout.getvalue().strip(), "1 3")


if __name__ == "__main__":

    unittest.main()