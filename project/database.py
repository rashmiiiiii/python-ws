import sqlite3

host_name="data.db"
def create_table():
    try:
        conn=sqlite3.connect(host_name)
        cursor =conn.cursor()
        cursor.execute("create table Student(reg integer primary key,name text,sem integer,placed integer)")
    
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()
def add_new_student(reg,name,sem,placed):
    try:
        conn=sqlite3.connect(host_name)
        cursor =conn.cursor()
        cursor.execute("insert into student (reg,name,sem,placed) values(?,?,?,?)",(reg,name,sem,placed))
        conn.commit()

    except Exception as e:
        print(f"{str(e)}")

    finally:
        conn.close()
    
def show_students():
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("select reg,name,sem,placed from student ")
        rows = cursor.fetchall()
        for row in rows:
            status = "placed" if row[3] == 1 else "Not placed"
            print(f"{row[0]},{row[1]},{row[2]} and {status}")
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()

def update_stu_status(reg,placed):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("update student set placed =  ? where reg = ?",(placed,reg))
        conn.commit()
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()
def show_students_regno(reg):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("select reg,name,sem,placed from student where reg = ?",(reg,))
        row = cursor.fetchone()
        if row:
            status = "placed" if row[3] == 1 else "Not placed"
            print(f"{row[0]},{row[1]},{row[2]} and {status}")
        else:
            print("students details not found")
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()


#create_table()
#add_new_student(1001,'abhi',7,1)
#add_new_student(1002,'joy',7,1)
#add_new_student(1003,'malya',7,1)
#add_new_student(1004,'rajath',7,0)
#show_students()
#update_stu_status(1004,1)
show_students_regno(1004)

