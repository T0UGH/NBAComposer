import testcode.dbUtil as dbUtil

MATCH_ID = 155902


def get_home_record(match_id):
    return dbUtil.get_home_record(match_id)


def get_away_record(match_id):
    return dbUtil.get_away_record(match_id)


def generate_player_list(records):
    player_list = []
    for record in records:
        text = record[4]
        if "阵容调整" in text:
            player_sub_list = analysis_change_text(text)
            player_list += player_sub_list
    return list(set(player_list))


def analysis_change_text(change_team_text):
    left_index = change_team_text.find("(") + 1
    right_index = change_team_text.find(")")
    pieces = change_team_text[left_index:right_index].split("; ")
    return pieces


def find_who_score(text, player_list):
    for player in player_list:
        if player in text:
            return player


def find_star(records):
    player_list = generate_player_list(records)
    player_dict = {player: 0 for player in player_list}
    for record in records:
        text = record[4]
        if "三分球进" in text:
            print(record)
            player_dict[find_who_score(text, player_list)] += 3
        elif "两分球进" in text:
            print(record)
            player_dict[find_who_score(text, player_list)] += 2
        elif "罚球命中" in text:
            print(record)
            player_dict[find_who_score(text, player_list)] += 1
        else:
            pass
    return player_dict


if __name__ == '__main__':
    records = get_home_record(MATCH_ID)
    print(find_star(records))
