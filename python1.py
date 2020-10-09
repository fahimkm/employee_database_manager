import sqlite3
from employee import Employee

def create_table():
    conn = sqlite3.connect('employee.db')
    #conn = sqlite3.connect(':memory:') creates new database from scratch in memory,useful for testing 
    cur = conn.cursor()
    conn.execute("""create table if not exists employees (
                first text,
                last text,
                pay integer
                )""")

    conn.commit()
    conn.close()

def add_employee(emp):
    
    conn = sqlite3.connect('employee.db')
    cur = conn.cursor()
    cur.execute("insert into employees values (?,?,?)",(emp.first,emp.last,emp.pay))
    cur.execute("insert into employees values (:first,:last,:pay)",{'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay})
    conn.commit()
    conn.close()

def view_table():
    conn = sqlite3.connect('employee.db')
    cur = conn.cursor()
    cur.execute("select *from employees where last=?",('mohd',))
    #cur.execute("select *from employees where last=:last",{'last':'mohd'})
    print(cur.fetchall())
    conn.commit()
    conn.close()    



#create_table()
emp_1 = Employee('Sam','Smith',90000)
emp_2 = Employee('Jane','Smith',80000)
add_employee(emp_1)
view_table()


