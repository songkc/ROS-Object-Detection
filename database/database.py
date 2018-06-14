import psycopg2


class database:
    def __init__(self):
        self.conn = psycopg2.connect(database="postgres", user="postgres", password="", host="127.0.0.1", port="5432")
        if (self.conn):
            print("Opened database successfully")
        else:
            print("failed to open database")

    def deleteTable(self, table):
        if (self.conn):
            cur = self.conn.cursor()
            cur.execute("DROP TABLE "+table)
            self.conn.commit()

    def createTable(self):
        if (self.conn):
            cur = self.conn.cursor()
            # 创建表原图origins
            cur.execute('''CREATE TABLE IF NOT EXISTS origins
                        (
                        id int NOT NULL PRIMARY KEY,
                        imgPath CHAR(50) NOT NULL ,
                        isTaged INT 
                        )''')
            # 创建表已标记过的图taged
            cur.execute('''CREATE TABLE IF NOT EXISTS taged
                        (
                        id int NOT NULL PRIMARY KEY REFERENCES origins(id) ,
                        imgPath CHAR(50) NOT NULL ,
                        isTaged INT 
                        )''')
            # 创建表结果results
            cur.execute('''CREATE TABLE IF NOT EXISTS results
                        (
                        id int NOT NULL PRIMARY KEY REFERENCES origins(id) ,
                        imgPath CHAR(50) NOT NULL ,
                        isTaged INT 
                        )''')

    # 以下函数的参数都为字符串
    # 插入，tabel为表的名称，value为形如“1, 'Paul', 32, 'California', 20000.00”的字符串
    def insert(self, table, value):
        if (self.conn):
            cur = self.conn.cursor()
            cur.execute("INSERT INTO " + table + " (id,imgPath,isTaged) VALUES (" + value + ")")
            self.conn.commit()
            print("insert finished")

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
