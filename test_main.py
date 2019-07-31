import unittest

from teamcity.unittestpy import TeamcityTestRunner

if __name__ == '__main__':
    unittest.main(testRunner=TeamcityTestRunner())
