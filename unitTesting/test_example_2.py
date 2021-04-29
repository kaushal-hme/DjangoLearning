import unittest
def div(a,b):
	return a/b
class raiseTest(unittest.TestCase):
   def testraise(self):
      print(self.assertRaises(ZeroDivisionError, div, 1,0))
      	
if __name__ == '__main__':
   unittest.main()
