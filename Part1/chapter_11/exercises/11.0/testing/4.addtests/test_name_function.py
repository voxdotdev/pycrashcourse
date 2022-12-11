"""
Adding new Tests 

Now that we know get_formatted_name() works for simple names again, let's 
write a second test for people who include a middle name. 

We do this by adding another method to the class NamesTestCase:
"""

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_Name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_Name(self):
        """Do names like 'Wolfgang Amadeus Mozart work?"""
        formatted_name = get_formatted_name('wolfgang','mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

"""
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

Both tests passed which means we know it will accept both variations of input!
"""