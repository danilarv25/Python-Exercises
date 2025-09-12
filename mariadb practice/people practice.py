import mariadb
connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='daniel',
    password='Biggerdawg123',
    database='people',
    autocommit=True
)
print("Connection Successful")

def get_employee_by_last_name(connection, last_name):
    sql = 'select number,last_name,first_name,salary from employee where last_name = ?'
    cursor = connection.cursor()
    cursor.execute(sql,(last_name,))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[-1]} euros per month.")
    else:
        print(f"No employees with the last name {last_name} found.")
    cursor.close()

def update_salary_by_last_name(connection, new_salary, last_name):
    salupdate = 'update employee set salary = ? where last_name = ?'
    cursor = connection.cursor()
    cursor.execute(salupdate,(new_salary,last_name,))
    connection.commit()
    sqlcheck = 'select last_name,first_name,salary from employee where last_name = ?'
    cursor.execute(sqlcheck,(last_name,))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(f"Employee {row[1]} {row[0]} now has a salary of: {row[2]}")
    else:
        print(f"No employees with the last name {last_name} found.")
    cursor.close()

ln = input("Enter employee's last name: ")
get_employee_by_last_name(connection, ln)
ln = input("Enter employee's last name for inputting new salary: ")
salary = int(input("Enter new salary: "))
update_salary_by_last_name(connection, salary, ln)
connection.close()
print("Connection closed")