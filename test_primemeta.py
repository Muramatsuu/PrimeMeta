# test_primemeta.py
"""
Tests for PrimeMeta module.
"""

import unittest
from primemeta import PrimeMeta

class TestPrimeMeta(unittest.TestCase):
    """Test cases for PrimeMeta class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeMeta()
        self.assertIsInstance(instance, PrimeMeta)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeMeta()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
