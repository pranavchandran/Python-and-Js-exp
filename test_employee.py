
import unittest
from unittest import *

from employee import Employee

class TestEMployee(unittest.TestCase):

	@classmethod
	def setupClass(cls):
		print('setupClass')

	@classmethod	
	def tearDownClass(cls):
		print('tearDownClass')

	def setUp(self):
		print('setUp')
		self.emp_1 = Employee('elsa','able',50000)
		self.emp_2 = Employee('sue','smith',60000)
		
	def tearDown(self):
		print('tearDown\n')

	def test_email(self):
		print('test_email')
		# emp_1 = Employee('elsa','able',50000)
		# emp_2 = Employee('sue','smith',60000)

		self.assertEqual(self.emp_1.email,'elsa.able@email.com')

		self.emp_1.first = 'raj'
		self.emp_2.first = 'kumar'

		self.assertEqual(self.emp_1.email,'raj.able@email.com')
		self.assertEqual(self.emp_2.email,'kumar.smith@email.com')

	def test_fullname(self):
		print('test_fullname')
		# self = Employee('elsa','able',50000)
		# self.emp_2 = Employee('sue','smith',60000)

		self.assertEqual(self.emp_1.fullname,'elsa able')
		self.assertEqual(self.emp_2.fullname,'sue smith')

		self.emp_1.first = 'John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.fullname,'John able')
		self.assertEqual(self.emp_2.fullname,'Jane smith')

	def test_apply_raise(self):
		print('test apply_raise')
		# self = Employee('elsa','able',50000)
		# self.emp_2 = Employee('sue','smith',60000)

		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay,52500)
		self.assertEqual(self.emp_2.pay,63000)

	def test_monthly_schedule(self):
		with patch('employee.requests.get')as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.emp_1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/able/May')
			self.assertEqual(schedule,'Success')

			mocked_get.return_value.ok = False

			schedule = self.emp_2.monthly_schedule('June')
			mocked_get.assert_called_with('http://company.com/smith/June')
			self.assertEqual(schedule,'Success')

if __name__ == '__main__':
	unittest.main()