import testcode.dbUtil as dbUtil
from collections import namedtuple
import re

Player = namedtuple('Player', ('full_name', 'last_name', 'code'))


def get_home_player_name(match_id) -> list:
    # away_player_names = set()
    home_players = []
    home_data = dbUtil.get_home_player_data(match_id)
    for index in range(len(home_data)):
        full_name = home_data[index][1]
        last_name = get_last_name(full_name)
        home_players.append(Player(full_name, last_name, index))
    # print(home_players)
    return home_players


def get_away_player_name(match_id) -> list:
    away_players = []
    away_data = dbUtil.get_away_player_data(match_id)
    for index in range(len(away_data)):
        full_name = away_data[index][1]
        last_name = get_last_name(full_name)
        away_players.append(Player(full_name, last_name, index))
    # print(away_players)
    return away_players


def get_last_name(full_name: str):
    return full_name[full_name.find('-') + 1:]


def get_full_name_set(match_id):
    name_set = set()
    home_players = get_home_player_name(match_id)
    away_players = get_away_player_name(match_id)
    for player in home_players + away_players:
        name_set.add(player.full_name)
    return name_set


def get_last_name_set(match_id) -> set:
    name_set = set()
    home_players = get_home_player_name(match_id)
    away_players = get_away_player_name(match_id)
    for player in home_players + away_players:
        name_set.add(player.last_name)
    return name_set


def get_nick_name_set(match_id) -> set:
    name_set = set()
    home_players = get_home_player_name(match_id)
    away_players = get_away_player_name(match_id)
    for player in home_players + away_players:
        name_set.add('大'+player.last_name)
        name_set.add('小'+player.last_name)
    return name_set


def hide_all(record: str, team_name_set: set, full_name_set: set, last_name_set: set, nick_name_set: set = None):
    record = hide_team_name(record, team_name_set)
    record = hide_location(record)
    record = hide_player_name(record, full_name_set, last_name_set, nick_name_set)
    return record


def hide_team_name(record: str, team_name_set: set):
    for name in team_name_set:
        if name in record:
            record = record.replace(name, '<team_name>')
    return record


def hide_location(record: str):
    record = re.sub(r'(\d+)英尺外', "<location>", record)
    return record


def hide_player_name(record: str, full_name_set: set, last_name_set: set, nick_name_set: set = None):
    for name in full_name_set:
        if name in record:
            record = record.replace(name, '<player_name>')
    for name in nick_name_set:
        if name in record:
            record = record.replace(name, '<player_name>')
    for name in last_name_set:
        if name in record:
            record = record.replace(name, '<player_name>')
    return record


def get_record_text_after_hide_name(match_id) -> list:
    texts = []
    records = dbUtil.get_match_record(match_id)
    full_name_set = get_full_name_set(match_id)
    last_name_set = get_last_name_set(match_id)
    nick_name_set = get_nick_name_set(match_id)
    for record in records:
        text = record[4]
        texts.append(hide_all(text, {'国王', '灰熊'}, full_name_set, last_name_set, nick_name_set))
    return texts


def get_text_pattern_set(match_id) -> set:
    return set(get_record_text_after_hide_name(match_id))


if __name__ == '__main__':
    text_patterns = get_text_pattern_set(dbUtil.DEMO_MATCH_ID)
    for text_pattern in text_patterns:
        print(text_pattern)
