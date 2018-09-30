import pymysql

DEMO_MATCH_ID = 151595


def get_match_record(match_id):
    try:
        db = pymysql.connect("localhost", "debian-sys-maint", "sA2GgzwqSssyMRNO", "nba_composer")
        cursor = db.cursor()
        sql = "SELECT * FROM textrecord WHERE match_id = %d ORDER BY section_num, time_to_end DESC" % match_id
        cursor.execute(sql)
        results = cursor.fetchall()
        # for row in results:
        #     print(row)
        return results
    except Exception as err:
        print(err.with_traceback())
    finally:
        db.close()


def get_home_player_data(match_id):
    try:
        db = pymysql.connect("localhost", "debian-sys-maint", "sA2GgzwqSssyMRNO", "nba_composer")
        cursor = db.cursor()
        sql = "SELECT * FROM playerdata WHERE match_id = %d AND isHostTeam = '%s'" % (match_id, '1')
        cursor.execute(sql)
        results = cursor.fetchall()
        # for row in results:
        #     print(row)
        return results
    except Exception as err:
        print(err.with_traceback())
    finally:
        db.close()


def get_away_player_data(match_id):
    try:
        db = pymysql.connect("localhost", "debian-sys-maint", "sA2GgzwqSssyMRNO", "nba_composer")
        cursor = db.cursor()
        sql = "SELECT * FROM playerdata WHERE match_id = %d AND isHostTeam = '%s'" % (match_id, '0')
        cursor.execute(sql)
        results = cursor.fetchall()
        # for row in results:
        #     print(row)
        return results
    except Exception as err:
        print(err.with_traceback())
    finally:
        db.close()


if __name__ == '__main__':
    get_match_record(DEMO_MATCH_ID)
    get_home_player_data(DEMO_MATCH_ID)
    print('-' * 200)
    get_away_player_data(DEMO_MATCH_ID)

