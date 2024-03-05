# Nama File: Bioskop.py
from db import DBConnection as mydb

class Bioskop:

    def __init__(self):
        self.__id = None
        self.__no_transaksi = None
        self.__nama = None
        self.__film = None
        self.__tgl = None
        self.__no_kursi = None
        self.__harga_tiket = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def no_transaksi(self):
        return self.__no_transaksi

    @no_transaksi.setter
    def no_transaksi(self, value):
        self.__no_transaksi = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def film(self):
        return self.__film

    @film.setter
    def film(self, value):
        self.__film = value
    
    @property
    def jadwal(self):
        return self.__jadwal

    @jadwal.setter
    def jadwal(self, value):
        self.__jadwal = value

    @property
    def no_kursi(self):
        return self.__no_kursi

    @no_kursi.setter
    def no_kursi(self, value):
        self.__no_kursi = value

    @property
    def harga_tiket(self):
        return self.__harga_tiket

    @harga_tiket.setter
    def harga_tiket(self, value):
        self.__harga_tiket = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__no_transaksi, self.__nama, self.__film, self.__jadwal, self.__no_kursi, self.__harga_tiket)
        sql = "INSERT INTO bioskop (no_transaksi, nama, film, jadwal, no_kursi, harga_tiket) VALUES (%s, %s, %s,%s, %s, %s)"
        self.affected = self.conn.insert(sql, val)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__no_transaksi, self.__nama, self.__film, self.__jadwal, self.__no_kursi, self.__harga_tiket, id)
        sql = "UPDATE bioskop SET no_transaksi = %s, nama = %s, film = %s, jadwal = %s, no_kursi = %s, harga_tiket = %s WHERE id = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateByNoTransaksi(self, no_transaksi):
        self.conn = mydb()
        val = (self.__nama, self.__film, self.__jadwal, self.__no_kursi, self.__harga_tiket, no_transaksi)
        sql = "UPDATE bioskop SET  no_transaksi = %s, film = %s, jadwal = %s, no_kursi = %s, harga_tiket = %s WHERE no_transaksi = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM bioskop WHERE id = %s"
        self.affected = self.conn.delete(sql, (id,))
        self.conn.disconnect()
        return self.affected

    def deleteByNoTransaksi(self, no_transaksi):
        self.conn = mydb()
        sql = "DELETE FROM bioskop WHERE no_transaksi = %s"
        self.affected = self.conn.delete(sql, (no_transaksi,))
        self.conn.disconnect()
        return self.affected

    def getById(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM bioskop WHERE id = %s"
        self.result = self.conn.findOne(sql, (id,))
        self.__no_transaksi = self.result[1]
        self.__nama = self.result[2]
        self.__film = self.result[3]
        self.__jadwal = self.result[4]
        self.__no_kursi = self.result[5]
        self.__harga_tiket = self.result[6]
        self.conn.disconnect()
        return self.result

    def getByNoTransaksi(self, no_tansaksi):
        a = str(no_tansaksi)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM bioskop WHERE no_transaksi = %s"
        self.result = self.conn.findOne(sql, (b,))
        if self.result is not None:
            self.__no_transaksi = self.result[1]
            self.__nama = self.result[2]
            self.__film = self.result[3]
            self.__jadwal = self.result[4]
            self.__no_kursi = self.result[5]
            self.__harga_tiket = self.result[6]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__no_transaksi = ''
            self.__nama = ''
            self.__film = ''
            self.__jadwal = ''
            self.__no_kursi = ''
            self.__harga_tiket = ''
            self.affected = 0
        self.conn.disconnect()
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM bioskop"
        self.result = self.conn.findAll(sql)
        return self.result

A = Bioskop()
no_transaksi = '4444'
A.deleteByNoTransaksi(no_transaksi)
B = A.getAllData()
print(B)
