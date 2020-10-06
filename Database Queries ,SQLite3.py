import sqlite3

conn=sqlite3.connect("example1.db")

c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARY KEY,NAME TEXT, SALARY REAL)""")

# c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(101,'TANVER AHMED',1200)")
# c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(102,'Likhon',1300)")
# c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(103,'TANVER Likhon',1400)")
# c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(104,'Likhon AHMED',1500)")
# c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(105,'TANVER AHMED Likhon',1600)")
#
# conn.execute("COMMIT")


#reading
# c.execute("""SELECT * FROM EMP""")
# print(next(c))
#
# for row in c:
#     print(row)


#updating

c.execute("UPDATE emp set salary =6500 where id=102")
conn.execute("commit")

c.execute("SELECT * FROM EMP WHERE ID =102")
print(next(c))

c.execute("""DELETE FROM EMP WHERE ID=103""")
conn.execute("COMMIT")

#reading
c.execute("""SELECT * FROM EMP""")
# print(next(c))

for row in c:
    print(row)