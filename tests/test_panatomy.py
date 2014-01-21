from unittest import TestCase
import panatomy, sys

class TestGetClasses(TestCase):
        def test_empty(self):
            f = panatomy.Panatomy()
            ret = f.get_classes(path="../tests/test_panatomy.py", target_name="unittest.TestCase")
            self.assertEqual(ret, None)

if __name__=="__main__":
	unittest.run()
