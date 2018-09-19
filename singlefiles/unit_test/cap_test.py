import unittest
import cap


class capitaltest(unittest.TestCase):

	def test_checkcapital(self):
		text='hello world'
		result=cap.capit(text)
		self.assertEqual(result,'Hello World')


if __name__ == '__main__':
	unittest.main()