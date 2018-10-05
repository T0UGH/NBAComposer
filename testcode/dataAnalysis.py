import testcode.dbUtil as dbUtil
from collections import namedtuple
import re

Player = namedtuple('Player', ('full_name', 'last_name', 'another_last_name', 'full_name_without_line', 'code'))


def remove_line_from_full_name(full_name):
    full_name_without_line = full_name.replace('-', ' ', 1)
    return full_name_without_line


def get_home_players(match_id) -> list:
    # away_player_names = set()
    home_players = []
    home_data = dbUtil.get_home_player_data(match_id)
    for index in range(len(home_data)):
        full_name = home_data[index][1]
        last_name = get_last_name(full_name)
        another_last_name = get_another_last_name(full_name)
        home_players.append(Player(full_name, last_name, another_last_name,remove_line_from_full_name(full_name), index))
    # print(home_players)
    return home_players


def get_away_players(match_id) -> list:
    away_players = []
    away_data = dbUtil.get_away_player_data(match_id)
    for index in range(len(away_data)):
        full_name = away_data[index][1]
        last_name = get_last_name(full_name)
        another_last_name = get_another_last_name(full_name)
        away_players.append(Player(full_name, last_name, another_last_name, remove_line_from_full_name(full_name), index))
    # print(away_players)
    return away_players


def get_another_last_name(full_name: str):
    return full_name[full_name.rfind('-') + 1:]


def get_last_name(full_name: str):
    return full_name[full_name.find('-') + 1:]


def get_player_name_set(match_id):
    name_set = set()
    home_players = get_home_players(match_id)
    away_players = get_away_players(match_id)
    for player in home_players + away_players:
        name_set.add(player.full_name)
        name_set.add(player.last_name)
        name_set.add(player.another_last_name)
        name_set.add(player.full_name_without_line)
        name_set.add('大' + player.another_last_name)
        name_set.add('小' + player.another_last_name)
    name_set.update(('迈卡威', '麦卡杜', '慈世平', '德隆', '科比', '费弗斯', '恩瓦巴'))
    return name_set


def hide_all(record: str, team_name_set: set, player_name_set: set):
    record = hide_team_name(record, team_name_set)
    record = hide_location(record)
    record = hide_player_name(record, player_name_set)
    return record


def hide_team_name(record: str, team_name_set: set):
    for name in team_name_set:
        if name in record:
            record = record.replace(name, '<team_name>')
    return record


def hide_location(record: str):
    record = re.sub(r'(\d+)英尺外', "<location>", record)
    return record


def hide_player_name(record: str, name_set: set):
    name_list = list(name_set)
    name_list = sorted(name_list, key=len, reverse=True)
    for name in name_list:
        if name in record:
            record = record.replace(name, '<player_name>')
    return record


def get_team_name_set(match_id):
    team_name_set = set()
    team_name_tuple = dbUtil.get_match_team_names(match_id)
    for team_name in team_name_tuple:
        team_name_set.add(team_name)
        team_name_set.add(team_name + '队')
        if team_name == '独行侠':
            team_name_set.add('小牛')
            team_name_set.add('小牛队')
    return team_name_set


def get_record_text_after_hide_name(match_id) -> list:
    texts = []
    records = dbUtil.get_match_record(match_id)
    player_name_set = get_player_name_set(match_id)
    team_name_set = get_team_name_set(match_id)
    for record in records:
        text = record[4]
        texts.append(hide_all(text, team_name_set, player_name_set))
    return texts


def get_text_pattern_set(match_id) -> set:
    text_patterns = list(set(get_record_text_after_hide_name(match_id)))
    for text_pattern in text_patterns:
        if '<player_name>' not in text_pattern:
            text_patterns.remove(text_pattern)
    return set(text_patterns)


if __name__ == '__main__':
    match_ids = dbUtil.get_match_ids()
    text_patterns = set()
    for match_id in match_ids:
        text_patterns |= get_text_pattern_set(match_id)
    for text_pattern in text_patterns:
        print('\'' + text_pattern + '\': [],')
