import unittest
from DZ1 import TicTac


class TestTicTac(unittest.TestCase):

    def test_check_win(self):
        tests = [
            {
                'board': ['X', 'X', 'X', 'O', 'X', 'O',
                          'X', 'O', 'O'],
                'err': False,
                'ret': 'X'
            },
            {
                'board': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                'err': False,
                'ret': False
            },
            {
                'board': ['X', 'O', 'O', 'X', 5, 6, 'X', 8, 9],
                'err': False,
                'ret': 'X'
            },
            {
                'board': ['X', 'O', 3, 'X', 5, 6, 'X', 8, 9],
                'err': False,
                'ret': 'X'
            },
            {
                'board': None,
                'err': True,
                'ret': None
            },
            {
                'board': ['X', 'O', 'O', 'O', 'X', 'X', 'O', 'X', 'O'],
                'err': False,
                'ret': False
            }

        ]
        for t in tests:
            b = TicTac()
            b.board = t['board']
            if t['err'] == True:
                with self.assertRaises(Exception):
                    b.check_win()
            else:
                self.assertEqual(b.check_win(), t['ret'])


if __name__ == "__main__":
    unittest.main()
