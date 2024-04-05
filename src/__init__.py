import sys
import unittest

sys.path.append('../flet-box')
loader     = unittest.TestLoader()
testSuite  = loader.discover('src')
testReuner = unittest.TextTestRunner(verbosity=3)
testReuner.run(testSuite)
