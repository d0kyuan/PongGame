# -*- coding: utf-8 -*-
import sqlite3
import sys
import os
import time
import signal
from kivy.utils import platform
import linecache
import sys
import os
class cMydb(object):
    temp_value = None
    temp_array = []
    conn = None



    def PrintException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        # print("sys")
        # print(sys.version_info)
        # print("sys")

        # print('EXCEPTION IN (%s, LINE %s "%s"): '%(str(filename), str(lineno), str(line.strip()), str(exc_obj)))

        # print 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    # 建立資料庫與建立連線
    def build(self):
        global conn
        if platform == u'android':
            conn = sqlite3.connect(u'/storage/emulated/0/game.db')
        elif platform == "ios":
            conn = sqlite3.connect(os.path.expanduser('~/Documents/game.db'))
        else:
            conn = sqlite3.connect(u'game.db')
        c = None
        c = conn.cursor()


        c.execute(u'''create table if not exists tb_RoomId(
                roomid varchar(250) not null,
                PRIMARY KEY (roomid)
            )''')
        conn.commit()

        c.execute(u'''create table if not exists tb_Setting(

                mKey varchar(20) not null,
                mValue varchar(200) not null,
                PRIMARY KEY (mKey)
            )''')
        conn.commit()




        oFeedback = self.gatvalue("tb_Setting","count(*)","mKey  like  'Paddle'","")
        if oFeedback[0][0]  <=0 :
            self.setvalue("tb_Setting","mKey,mValue","'%s','%s'"%("Paddle","(0,0,0)"))

        oFeedback = self.gatvalue("tb_Setting","count(*)","mKey  like 'Background'","")
        if oFeedback[0][0]  <=0 :
            self.setvalue("tb_Setting","mKey,mValue","'%s','%s'"%("Background","(0,0,0)"))


        oFeedback = self.gatvalue("tb_Setting","count(*)","mKey  like 'Ball'","")
        if oFeedback[0][0]  <=0 :
            self.setvalue("tb_Setting","mKey,mValue","'%s','%s'"%("Ball","(0,0,0)"))

        # 設定資料表
    def setvalue(self,table_n, table_c, table_v):
        try:
            c = conn.cursor()
            c.execute(u"insert into " + (table_n) +
                      u"(" + (table_c) + u") values(" + (table_v) + u")")
            conn.commit()
            insert_id = c.lastrowid
            print (u"insert into " + (table_n) +
                  u"(" + (table_c) + u") values(" + (table_v) + u")"
            )
            print("insert id ",insert_id)
            return insert_id
        except:
            print (u"insert into " + (table_n) +
                  u"(" + (table_c) + u") values(" + (table_v) + u")"
            )
            self.PrintException()
            return False

    def gatvalue(self,table_n, table_c,table_v, table_e):
        global conn
        try:
            if table_v == u"" or None:
                c = conn.cursor()
                c.execute(u"SELECT " + table_c + u" FROM " + table_n + table_e)
                row = c.fetchall()
            else:

                c = conn.cursor()
                c.execute(u"SELECT " + table_c + u" FROM " +
                          table_n + u" WHERE " + table_v + table_e)

                row = c.fetchall()
            print (u"SELECT " + table_c + u" FROM " +
                            table_n + u" WHERE " + table_v + table_e)

            return row
        except:
            print (u"SELECT " + table_c + u" FROM " +
                            table_n + u" WHERE " + table_v + table_e)
            self.PrintException()
            return False

    def updatevalue(self,table_n, table_v, table_e):
        global conn
        try:
            c = conn.cursor()
            c.execute(u"update " + (table_n) + u" set " +
                      (table_v) + u" WHERE " + (table_e) )
            conn.commit()

            return True
        except:
            print (u"update " + (table_n) + u" set " +
                  (table_v) + u" WHERE " + (table_e))
            self.PrintException()
            return False

    def sql_commend(self,sql):
        global conn
        try:
            c = conn.cursor()
            c.execute(sql)
            row = c.fetchall()

            return row
        except:
            print (sql)
            self.PrintException()
            return False

    # 關閉資料庫連線
    def close(self):
        global conn
        try:
            conn.close()
        except:
            self.PrintException()

    def get(self):
        pass

    def set(self):
        pass
