import sys
import os

sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from scripts.search_valley_ranch import SearchValleyRanch
from scripts.search_macarthur import SearchMacArthur

import testtools as testtools

if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(SearchValleyRanch),
        test_loader.loadTestsFromTestCase(SearchMacArthur)
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
