def TaoDB(dbname: str):
    import mysql.connector
    db = mysql.connector.connect(host='113.161.84.155', user='root', passwd='khongco')
    sql = "CREATE DATABASE {0}".format(dbname)
    cursor = db.cursor()
    cursor.execute(sql)
    print("Da Tao Database {0}".format(dbname))
    cursor.close()
    db.close()


def TaoTable(name: str):
    pass


def ThemRec():
    pass


def XoaRec():
    pass


def UpdateRec():
    pass


def makecenter(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
