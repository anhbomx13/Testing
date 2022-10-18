import unittest
import number_of_days

class BVA(unittest.TestCase):
    def test_boundary_strong(self):
        """BVA1"""
        month = 0
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA2"""
        month = 1
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA3"""
        month = 2
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 28)
        """BVA4"""
        month = 11
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 30)
        """BVA5"""
        month = 12
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA6"""
        month = 13
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA7"""
        month = 5
        year = -1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA8"""
        month = 5
        year = 0
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA9"""
        month = 5
        year = 1
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA10"""
        month = 5
        year = 2999
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA11"""
        month = 5
        year = 3000
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA12"""
        month = 5
        year = 3001
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA13"""
        month = 5
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)

    def test_boundary_combined(self):
        """BVA14"""
        month = 0
        year = -1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA15"""
        month = 0
        year = 0
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA16"""
        month = 0
        year = 1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA17"""
        month = 0
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA18"""
        month = 0
        year = 2999
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA19"""
        month = 0
        year = 3000
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA20"""
        month = 0
        year = 3001
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA21"""
        month = 1
        year = -1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA22"""
        month = 1
        year = 0
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA23"""
        month = 1
        year = 1
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA24"""
        month = 1
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA25"""
        month = 1
        year = 2999
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA26"""
        month = 1
        year = 3000
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA27"""
        month = 1
        year = 3001
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA28"""
        month = 2
        year = -1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA29"""
        month = 2
        year = 0
        self.assertEqual(number_of_days.numberOfDays(year, month), 29)
        """BVA30"""
        month = 2
        year = 1
        self.assertEqual(number_of_days.numberOfDays(year, month), 28)
        """BVA31"""
        month = 2
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 28)
        """BVA32"""
        month = 2
        year = 2999
        self.assertEqual(number_of_days.numberOfDays(year, month), 28)
        """BVA33"""
        month = 2
        year = 3000
        self.assertEqual(number_of_days.numberOfDays(year, month), 28)
        """BVA34"""
        month = 2
        year = 3001
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA35"""
        month = 5
        year = -1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA36"""
        month = 5
        year = 0
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA37"""
        month = 5
        year = 1
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA38"""
        month = 5
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA39"""
        month = 5
        year = 2999
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA40"""
        month = 5
        year = 3000
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA41"""
        month = 5
        year = 3001
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA42"""
        month = 11
        year = -1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA43"""
        month = 11
        year = 0
        self.assertEqual(number_of_days.numberOfDays(year, month), 30)
        """BVA44"""
        month = 11
        year = 1
        self.assertEqual(number_of_days.numberOfDays(year, month), 30)
        """BVA45"""
        month = 11
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 30)
        """BVA46"""
        month = 11
        year = 2999
        self.assertEqual(number_of_days.numberOfDays(year, month), 30)
        """BVA47"""
        month = 11
        year = 3000
        self.assertEqual(number_of_days.numberOfDays(year, month), 30)
        """BVA48"""
        month = 11
        year = 3001
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA49"""
        month = 12
        year = -1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA50"""
        month = 12
        year = 0
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA51"""
        month = 12
        year = 1
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA52"""
        month = 12
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA53"""
        month = 12
        year = 2999
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA54"""
        month = 12
        year = 3000
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """BVA55"""
        month = 12
        year = 3001
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA56"""
        month = 13
        year = -1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA57"""
        month = 13
        year = 0
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA58"""
        month = 13
        year = 1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA59"""
        month = 13
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA60"""
        month = 13
        year = 2999
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA61"""
        month = 13
        year = 3000
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """BVA62"""
        month = 13
        year = 3001
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')

    def test_special_case(self):
        """BVA63"""
        month = 2
        year = -1
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """BVA64"""
        month = 2
        year = 1500
        self.assertEqual(number_of_days.numberOfDays(year, month), 28)
        """BVA65"""
        month = 2
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 29)
        """BVA66"""
        month = 2
        year = 3000
        self.assertEqual(number_of_days.numberOfDays(year, month), 28)


class EP(unittest.TestCase):
    def test_ep_case(self):
        """EP1"""
        month = 5
        year = 2054
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """EP2"""
        month = 5
        year = 3556
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """EP3"""
        month = 17
        year = 3600
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """EP4"""
        month = -4
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """EP5"""
        month = 2
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 29)
        """EP6"""
        month = 2
        year = 2551
        self.assertEqual(number_of_days.numberOfDays(year, month), 28)
        """EP7"""
        month = 2
        year = 4300
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """EP8"""
        month = 5
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """EP9"""
        month = -4
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')


class CFG(unittest.TestCase):
    def test_ep_case(self):
        """CFG1"""
        month = -2
        year = 4000
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid year')
        """CFG2"""
        month = -2
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 'Invalid month')
        """CFG3"""
        month = 2
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 29)
        """CFG4"""
        month = 3
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """CFG5"""
        month = 4
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 30)
        """CFG6"""
        month = 5
        year = 2019
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """CFG7"""
        month = 5
        year = 2016
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """CFG8"""
        month = 5
        year = 2017
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)

class DFG(unittest.TestCase):
    def test_ep_case(self):
        """DFG1"""
        month = 3
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 31)
        """DFG2"""
        month = 2
        year = 2000
        self.assertEqual(number_of_days.numberOfDays(year, month), 29)
        """DFG3"""
        month = 2
        year = 1900
        self.assertEqual(number_of_days.numberOfDays(year, month), 28)
        """DFG4"""
        month = 2
        year = 2020
        self.assertEqual(number_of_days.numberOfDays(year, month), 29)

if __name__ == '__main__':
    unittest.main(verbosity=2)