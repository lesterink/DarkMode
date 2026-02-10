# test_darkmode.py
"""
Tests for DarkMode module.
"""

import unittest
from darkmode import DarkMode

class TestDarkMode(unittest.TestCase):
    """Test cases for DarkMode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DarkMode()
        self.assertIsInstance(instance, DarkMode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DarkMode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
