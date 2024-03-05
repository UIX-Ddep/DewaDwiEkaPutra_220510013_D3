import bcrypt
from db import DBConnection as mydb

class Users:
    def __init__(self):
        self.__id= None
        self.__email= None
        self.__password= None
        self.__uservalid = None
        self.__passwordvalid = None
        self.__loginvalid = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = bcrypt.hashpw(value.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
    
    
    @property
    def loginvalid(self):
        return self.__loginvalid

    @loginvalid.setter
    def loginvalid(self, value):
        self.__loginvalid = value

    def cekUsername(self, email):
        self.conn = mydb()
        sql="SELECT * FROM users WHERE email='" + email + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__email = self.result[1]
            self.__password = self.result[2]
            self.affected = self.conn.cursor.rowcount 
            self.__uservalid = True
        else:
            self.__email = ''                 
            self.__password = ''                                   
            self.affected = 0
            self.__uservalid = False
        return self.__uservalid
    
    def cekPassword(self, password):
        hashedpass = self.__password.encode('utf-8')
        password_bytes = password.encode('utf-8')
        d =bcrypt.checkpw(password_bytes,hashedpass)
        if d:
            self.__passwordvalid=True
        else:
            self.__passwordvalid=False
        return self.__passwordvalid
        
    def Validasi(self, email, password):
        a = self.cekUsername(email)
        if a :
            # Hash Password yang diberikan oleh pengguna sebelum membandingkan 
            b = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            # bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
            if b :
                self.__loginvalid=True
            else:
                self.__loginvalid=False
        else:
           self.__loginvalid=False
        
        val = [self.__email, self.__loginvalid]
        return val

