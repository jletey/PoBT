#!/usr/bin/env python3
## Imports
import unittest
## Implementation of test_get_pssm
def test_get_pssm(self):
    # Import get_pssm
    from get_pssm import get_pssm
## Test my code
test_code = unittest.TestSuite()
test_code.addTest(test_get_pssm)
runner = unittest.TextTestRunner(verbosity=2).run(test_code)
