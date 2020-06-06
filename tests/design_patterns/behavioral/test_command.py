import unittest
from src.design_patterns.behavioral.command import MenuItem, DeleteFileCommand, HideFileCommand

class ChainingMethodTest(unittest.TestCase):
    def setUp(self) -> None:
        self.item1 = MenuItem(DeleteFileCommand())
        self.item2 = MenuItem(HideFileCommand())

    def test_deleting_test_file_value(self):
        self.assertEqual(self.item1.on_do_press('test-file'), 'deleting test-file')

    def test_restore_test_file_value(self):
        self.item1.on_do_press('test-file')
        self.assertEqual(self.item1.on_undo_press(), 'restoring test-file')

    def test_restoring_test_file_value_from_item2(self):
        self.assertEqual(self.item2.on_do_press('test-file'), 'hiding test-file')

    def test_hiding_test_file_value_from_item2(self):
        self.item2.on_do_press('test-file')
        self.assertEqual(self.item2.on_undo_press(), 'un-hiding test-file')
