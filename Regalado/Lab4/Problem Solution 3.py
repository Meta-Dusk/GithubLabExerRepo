import unittest
import oxo_dialog_ui


class TestCode(unittest.TestCase):
    def test_oxo(self):
        self.assertEqual(oxo_dialog_ui.startGame(), list(" "*9) )
    def test_restore_game(self):
        self.assertEqual(oxo_dialog_ui.resumeGame(), list(" " * 9))

if __name__ == "__main__":
    unittest.main()
