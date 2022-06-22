import frappe

def all():
    print("\n\n\n")
    new_doc = frappe.get_doc({"doctype":"scheduler_event_doctype","content":"hello nayan"})
    new_doc.insert()
    frappe.db.commit()
    print("------------------------all")
def cron():
    new_doc = frappe.get_doc({"doctype":"scheduler_event_doctype","content":"hello yadav"})
    new_doc.insert()
    frappe.db.commit()
    print("-------------------------------cron")
