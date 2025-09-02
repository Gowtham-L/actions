# Copyright (c) 2025, gowtham and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestBuildAction(FrappeTestCase):
	def test_full_name_correctly_set(self):
		test_driver = frappe.new_doc("Build Action")
		test_driver.first_name = "John"
		test_driver.last_name = "Doe"
		test_driver.license_number = "DL123456"
		test_driver.save()

		self.assertEqual(test_driver.full_name, "John Doe")
