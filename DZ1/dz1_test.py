"""Unit tests for TicTac"""
import unittest
from dz1 import TicTac


class TestTicTac(unittest.TestCase):
    '''Testing class'''

    def setUp(self):
        self.tests = [
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

    def test_check_win(self):
        ''' check_win function test'''
        for test in self.tests:
            game = TicTac()
            game.board = test['board']
            if test['err']:
                with self.assertRaises(Exception):
                    game.check_win()
            else:
                self.assertEqual(game.check_win(), test['ret'])


if __name__ == "__main__":
    unittest.main()
