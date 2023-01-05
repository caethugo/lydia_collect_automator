import unittest
from functions import randomfunc

if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test_suite)


#Let's write a fake test function to try unit testing: 
def test_randomfunc():
    # Call the function being tested
    result = randomfunc()

    # Assert that the function behaves as expected
    assert result == 4