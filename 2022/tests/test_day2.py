import unittest

import Day_2.rsp as rsp

class TestOutcomePoints(unittest.TestCase):
    def test_outcome_points(self):
        # 1 defeats 3, p1 wins
        self.assertEqual(rsp.outcome_points(1, 3), 0, "Should be 0")
        # 3 defeats 2, p1 wins
        self.assertEqual(rsp.outcome_points(3, 2), 0, "Should be 0")
        # 2 defeats 1, p1 wins
        self.assertEqual(rsp.outcome_points(2, 1), 0, "Should be 0")
        
        # 1 defeats 3, p2 wins
        self.assertEqual(rsp.outcome_points(3, 1), 6, "Should be 6")
        # 3 defeats 2, p2 wins
        self.assertEqual(rsp.outcome_points(2, 3), 6, "Should be 6")
        # 2 defeats 1, p2 wins
        self.assertEqual(rsp.outcome_points(1, 2), 6, "Should be 6")
        

if __name__ == "__main__":
    unittest.main()