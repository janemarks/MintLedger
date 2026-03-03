# test_mintledger.py
"""
Tests for MintLedger module.
"""

import unittest
from mintledger import MintLedger

class TestMintLedger(unittest.TestCase):
    """Test cases for MintLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintLedger()
        self.assertIsInstance(instance, MintLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
