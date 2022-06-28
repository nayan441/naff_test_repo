import frappe
import datetime as dt


def all():
    print("\n\n\n")
    new_doc = frappe.get_doc({"doctype":"scheduler_event_doctype","content":"hello nayan"})
    new_doc.insert()
    frappe.db.commit()
    print("------------------------all")
def daily():
    new_doc = frappe.db.get_list(
        'Vaccination',
        fields=['id','date','species'],
        order_by='date desc',
        as_list=True
    )
    today=dt.date.today()
    print("\n")
    print("Today  "+str(today))
    print("-"*40)

    for i in new_doc: # Looping tuple data
        print("\n")
        print("Id : "+str(i[0])+"   "+"Registration Date : "+ str(i[1])+"  "+"Species : "+str(i[2]))    
        x = today- i[1]
        
        print("Difference in days  : "+str(x.days))
        
        if x.days % 2 == 0:
            new_doc = frappe.get_doc({"doctype":"scheduler_event_doctype","content":f"Two days frequency of {i[0]}"})
            new_doc.insert()
            frappe.db.commit()
        if x.days % 3 == 0:
            new_doc = frappe.get_doc({"doctype":"scheduler_event_doctype","content":f"Three days frequency of {i[0]}"})
            new_doc.insert()
            frappe.db.commit()
        if x.days % 365 == 0 and i[2]=="Bovine":
            new_doc = frappe.get_doc({"doctype":"scheduler_event_doctype","content":f"365 days frequency of {i[0]} Bovine"})
            print(f"\n365 days frequency of Id: {i[0]} Bovine")
            new_doc.insert()
            frappe.db.commit()
        if x.days % 182 ==0 and i[2]=="Feline":
            new_doc = frappe.get_doc({"doctype":"scheduler_event_doctype","content":f"132 days frequency of {i[0]} Feline"})
            print(f"\n 182 days frequency of Id:{i[0]} Feline")
            new_doc.insert()
            frappe.db.commit()
        print("-"*40)
    print("-------------------------------Daily Cron---------------------------------")
    print("-------------------------------Code Updated on Windows Machine---------------------------------")
