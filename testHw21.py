from VikaP21Hw21 import FileManager
import unittest

class TestForFileManagers(unittest.TestCase):

    def test_for_file(self):
        with FileManager('homework.log', 'r') as file:
            a = file.read()
            b = 'The file is HomeWork 21'
            self.assertEqual(a, b)

    def test_for_absent_file(self):
        with self.assertRaises(FileNotFoundError):
            with FileManager('hw.txt', 'r') as absent_file:
                absent_file.read()

    def test_for_context_suite(self):
        with self.assertRaises(TypeError):
            with FileManager('homework.log', 'r') as type_err:
                type_err.read()
                type_err.close()


if __name__ == '__main__':
    unittest.main()
