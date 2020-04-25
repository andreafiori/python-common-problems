import unittest
from src.design_patterns.behavioral.command import MenuItem, DeleteFileCommand, HideFileCommand

class ChainingMethodTest(unittest.TestCase):
    def setUp(self) -> None:
        self.item1 = MenuItem(DeleteFileCommand())
        self.item2 = MenuItem(HideFileCommand())

        # restoring `test-file`
        # self.item1.on_undo_press()

        # restoring test - file

        # hiding `test-file`
        # self.item2.on_do_press('test-file')

        # self.item2.on_undo_press()
        # un - hiding test - file

    def test_deleting_test_file(self):
        self.item1.on_do_press('test-file')