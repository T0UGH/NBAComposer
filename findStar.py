import testcode.pointDict as pd
from collections import namedtuple
import re
import testcode.dbUtil as dbUtil
import testcode.dataAnalysis as da

"""Removed"""
ExtractedRecord = namedtuple('ExtractedRecord', ['text_pattern', 'player_score_dict'])


def get_point_dict():
    return pd.point_dict


def find_player_from_name(player_list, name):
    for player in player_list:
        if name in (player.full_name, player.another_last_name, player.last_name):
            return player.full_name
    return None


def hide_all(record: str, team_name_list: list, player_name_list: list):
    record = hide_team_name(record, team_name_list)
    record = hide_location(record)
    record = hide_player_name(record, player_name_list)
    return record


def hide_team_name(record: str, team_name_list: list):
    for name in team_name_list:
        if name in record:
            record = record.replace(name, '<team_name>')
    return record


def hide_location(record: str):
    record = re.sub(r'(\d+)英尺外', "<location>", record)
    return record


def hide_player_name(record: str, name_list: list):
    name_list = list(name_list)
    name_list = sorted(name_list, key=len, reverse=True)
    for name in name_list:
        if name in record:
            record = record.replace(name, '<player_name>')
    return record


def extract_players(record, text_pattern):
    pieces = text_pattern.split('<player_name>')
    # print(pieces)
    record_pieces = []
    for record_piece in pieces:
        if record_piece != '':
            record_pieces.append(record_piece)
    for piece in record_pieces:
        record = record.replace(piece, '+')
    record_pieces = record.split('+')
    players = []
    for record_piece in record_pieces:
        if record_piece != '':
            players.append(record_piece)
    return players


def extract_record(record: str, team_name_list, player_name_list, point_dict: dict):
    text_pattern = hide_all(record, team_name_list, player_name_list)
    players = extract_players(record, text_pattern)
    points = point_dict.get(text_pattern)
    if points is None:
        point_score_dict = {player: 0 for player in players}
    else:
        point_score_dict = {player: point for player, point in zip(players, points)}
    return point_score_dict


def get_player_name_list(player_list):
    name_list = list()
    for player in player_list:
        name_list.append(player.full_name)
        name_list.append(player.last_name)
        name_list.append(player.another_last_name)
        name_list.append('大' + player.another_last_name)
        name_list.append('小' + player.another_last_name)
    name_list += ['迈卡威', '麦卡杜', '慈世平', '德隆', '科比', '费弗斯', '恩瓦巴']
    return name_list


def find_star(record_list: list, player_list: list, point_dict: dict, team_name_list) -> str:
    player_name_list = get_player_name_list(player_list)
    player_dict = {player.full_name: 0 for player in player_list}
    for record in record_list:
        point_score_dict = extract_record(record, team_name_list, player_name_list, point_dict)
        for player_name in point_score_dict.keys():
            full_name = find_player_from_name(player_list, player_name)
            if full_name is not None:
                player_dict[full_name] += point_score_dict[player_name]
    return player_dict


if __name__ == '__main__':
    team_name_list = list(da.get_team_name_set(dbUtil.DEMO_MATCH_ID))
    player_list = list(da.get_away_players(dbUtil.DEMO_MATCH_ID)) + list(da.get_home_players(dbUtil.DEMO_MATCH_ID))
    origin_records = dbUtil.get_match_record(dbUtil.DEMO_MATCH_ID)
    record_list = []
    for origin_record in origin_records:
        record_list.append(origin_record[4])
    player_dict = find_star(record_list, player_list, get_point_dict(), team_name_list)
    for player in da.get_away_players(dbUtil.DEMO_MATCH_ID):
        print(player.full_name, " : ", player_dict[player.full_name])
