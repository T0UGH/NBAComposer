import pymysql


def main():
    try:
        db = pymysql.connect("localhost", "debian-sys-maint", "sA2GgzwqSssyMRNO", "rhyme_helper")
        cursor = db.cursor()
        sql = "SELECT * FROM user"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            print("id=%s,name=%s" % (id, name))
    except Exception as err:
        print(err.with_traceback())
    finally:
        db.close()


if __name__ == '__main__':
    main()

