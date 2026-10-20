import unittest
from edge_rover.controller import GestureController
class TestController(unittest.TestCase):
    def test_unknown_is_stop(self):
        c=GestureController(); self.assertEqual(c.update('unknown',0),'STOP'); self.assertEqual(c.rover.linear,0)
    def test_timeout_stops_rover(self):
        c=GestureController(timeout=1); c.update('thumb_up',0); c.tick(2); self.assertEqual(c.rover.linear,0)
if __name__=='__main__': unittest.main()
