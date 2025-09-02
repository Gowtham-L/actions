# Copyright (c) 2025, gowtham and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BuildAction(Document):
	def before_save(self):
		#self.full_name = f"{self.first_name} {self.last_name}"
		if self.last_name:
			# Set full name before saving the document
			self.full_name = f"{self.first_name} {self.last_name}"
		else: 
			self.full_name = self.first_name
