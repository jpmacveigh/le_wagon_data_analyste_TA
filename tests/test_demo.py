# pylint: disable-all

from pathlib import Path
import unittest

class TestDemo(unittest.TestCase):
    def test_check_file_exists(self):
        self.assertTrue(Path("check").is_file(), msg="Did you create the check file?")
