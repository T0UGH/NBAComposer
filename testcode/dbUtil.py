import pymysql

DEMO_MATCH_ID = 151596


def extract_config_line(line):
    return line[line.find("=")+1:-2]


def get_connection():
    db_config = get_config()
    db = pymysql.connect(*db_config)
    return db


def get_config():
    configs = []
    with open('dbconfig', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            configs.append(extract_config_line(line))
    return configs


def get_match_record(match_id):
    try:
        db = get_connection()
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
        db = get_connection()
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
        db = get_connection()
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


def get_match_team_names(match_id):
    try:
        db = get_connection()
        cursor = db.cursor()
        sql = "SELECT guest_team, host_team FROM game WHERE match_id = %d" % match_id
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[1], result[0]
    except Exception as err:
        print(err.with_traceback())
    finally:
        db.close()


def get_match_ids():
    try:
        id_list = []
        db = get_connection()
        cursor = db.cursor()
        sql = "SELECT match_id FROM game LIMIT 0, 1000"
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            id_list.append(result[0])
        return id_list
    except Exception as err:
        print(err.with_traceback())
    finally:
        db.close()


if __name__ == '__main__':
    print(get_match_ids())

