# Copyright (c) 2026, 	 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PracticeTask(Document):
	def validate(self):
        	if not self.task_title:
            		frappe.throw("Task Title is required!")
	def before_save(self):
        	if self.task_title:
            		self.task_title = self.task_title.upper()
	def on_update(self):
    		frappe.logger().info(f"Practice Task updated: {self.name}")
	def on_submit(self):
    		frappe.logger().info(f"Practice Task submitted: {self.name}")
	def on_cancel(self):
    		frappe.logger().info(
        	f"Practice Task cancelled: {self.name}"
 		)
	def on_trash(self):
    		frappe.logger().info(
        	f"Practice Task deleted: {self.name}"
    		)
@frappe.whitelist()
def get_task_status(task_name):
    doc = frappe.get_doc("Practice Task", task_name)
    doc.check_permission("read")

    return {
        "task_title": doc.task_title,
        "completed": doc.completed
    }
