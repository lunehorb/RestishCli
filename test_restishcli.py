# test_restishcli.py
"""
Tests for RestishCli module.
"""

import unittest
from restishcli import RestishCli

class TestRestishCli(unittest.TestCase):
    """Test cases for RestishCli class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RestishCli()
        self.assertIsInstance(instance, RestishCli)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RestishCli()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
