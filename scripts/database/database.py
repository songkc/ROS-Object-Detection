import psycopg2


class database:
    def __init__(self):
        self.conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        if (self.conn):
            print("Opened database successfully!")
        else:
            print("Failed to open database!")

    def deleteTable(self, table):
        if (self.conn):
            cur = self.conn.cursor()
            cur.execute("DROP TABLE "+table)
            self.conn.commit()
            print("Delete table successfully!")

    def createTable(self):
        if (self.conn):
            cur = self.conn.cursor()
            # 创建表原图origins
            cur.execute('''CREATE TABLE IF NOT EXISTS origins
                        (
                        id SERIAL NOT NULL PRIMARY KEY,
                        imgPath CHAR(64) NOT NULL
                        )''')
            # 创建表已标记过的图tagged
            cur.execute('''CREATE TABLE IF NOT EXISTS tagged
                        (
                        id SERIAL NOT NULL PRIMARY KEY REFERENCES origins(id) ,
                        imgPath CHAR(64) NOT NULL ,
                        isTagged BOOLEAN
                        )''')
            # 创建表结果results
            cur.execute('''CREATE TABLE IF NOT EXISTS results
                        (
                        id SERIAL NOT NULL PRIMARY KEY REFERENCES origins(id) ,
                        imgPath CHAR(64) NOT NULL
                        )''')
            self.conn.commit()
            print("Create table successfully!")

    # 以下函数的参数都为字符串
    # 插入，tabel为表的名称，value为形如“1, 'Paul', 32, 'California', 20000.00”的字符串
    def insert(self, table, value):
        if (self.conn):
            cur = self.conn.cursor()
            if (table == "tagged"):
                cur.execute("INSERT INTO " + table + " (imgPath,isTagged) VALUES (" + value + ")")
            else:
                cur.execute("INSERT INTO " + table + " (imgPath) VALUES (" + value + ")")
            self.conn.commit()
            print("Insert record into table " + table + " successfully!")

    # 选择,attr为要查询的属性，为“id，name, address"这样的字符串，table为表的名称
    def select(self, attr, table):
        if (self.conn):
            cur = self.conn.cursor()
            cur.execute("SELECT "+attr+" from "+table)
            rows = cur.fetchall()
            for row in rows:
                for attr in row:
                    print(attr)
                print("\n")
            return rows

    # 更新
    def update(self, id, attr, value, table):
        if (self.conn) :
            cur = self.conn.cursor()
            cur.execute("UPDATE "+table+" set "+attr+" = "+value+" where id = "+id)
            self.conn.commit()
            print("update finished")

    # 删除
    def delete(self, id, table):
        if (self.conn):
            cur = self.conn.cursor()
            cur.execute("DELETE from "+table+" where id="+id)
            self.conn.commit()
            print("delete finished")
