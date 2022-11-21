import mysql.connector

mydb = mysql.connector.connect(**st.secrets["mysql"])
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Train2 (Train_No int, Name varchar(30), Train_Type varchar(20), Source varchar(20), Destination varchar(20), Availability varchar(5));')


def add_data_customer(c_id, cust_name, cust_mobile, cust_email, check_in, check_out):
    c.execute('INSERT INTO customer (c_id, cust_name, cust_mobile, cust_email, check_in, check_out) VALUES (%d,%s,%d,%s,%s,%s);',
              (c_id, cust_name, cust_mobile, cust_email, check_in, check_out))
    mydb.commit()


def view_all_customer():
    c.execute('SELECT * FROM customer')
    customers = c.fetchall()
    return customers


def view_all_emp():
    c.execute('SELECT * from emp')
    emp = c.fetchall()
    return emp


def get_details(train_name):
    c.execute('SELECT * FROM Train2 WHERE Name="{}"'.format(train_name))
    data = c.fetchall()
    return data


def edit_details(new_train_no, new_train_name, new_train_type, new_source, new_dest, new_available, train_no, train_name, train_type, source, dest, available):
    c.execute("UPDATE Train2 SET Train_No=%s, Name=%s, Train_Type=%s, Source=%s, Destination=%s, Availability=%s WHERE "
              "Train_No=%s and Name=%s and Train_Type=%s and Source=%s and Destination=%s and Availability=%s", (new_train_no, new_train_name, new_train_type, new_source, new_dest, new_available, train_no, train_name, train_type, source, dest, available))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(c_id):
    c.execute('DELETE FROM customer WHERE c_id="{}"'.format(c_id))
    mydb.commit()
