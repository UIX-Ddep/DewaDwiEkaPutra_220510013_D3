# Nama file: db.py
import mysql.connector as mc

class DBConnection:

    def __init__(self):
        self.host = 'Localhost'
        self.port = 3306
        self.name = 'mydb'
        self.user = 'root'
        self.password = ''
        self.conn = None
        self.cursor = None
        self.result = None
        self.connected = False
        self.affected = 0
        self.connect()

    @property
    def connection_status(self):
        return self.connected

    def connect(self):
        try:
            self.conn = mc.connect(
                host=self.host,
                port=self.port,
                database=self.name,
                user=self.user,
                password=self.password
            )
            self.connected = True
            self.cursor = self.conn.cursor()
        except mc.Error as e:
            print(f"Error: {e}")
            self.connected = False

    def disconnect(self):
        if self.connected:
            self.conn.close()
            self.connected = False
        else:
            self.conn = None

    def findOne(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    def findAll(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result

    def insert(self, sql, values=None):
        self.connect()
        self.cursor.execute(sql, values)
        self.conn.commit()
        self.affected = self.cursor.rowcount
        return self.affected

    def update(self, sql, values=None):
        self.connect()
        self.cursor.execute(sql, values)
        self.conn.commit()
        self.affected = self.cursor.rowcount
        return self.affected

    def delete(self, sql, values=None):
        self.connect()
        self.cursor.execute(sql, values)
        self.conn.commit()
        self.affected = self.cursor.rowcount
        return self.affected

    def show(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    @property
    def info(self):
        if self.connected:
            return f"Server is running on {self.host} using port {self.port}"
        else:
            return "Server is offline."

A = DBConnection()
B = A.info
print(B)
