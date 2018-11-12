import utils


def find_who_score(text, player_list):
    """
    根据records中某一条record的text,找到这次得分的是哪位球员
    """
    for player in player_list:
        if player in text:
            return player


def find_max_score(player_dict):
    player_list = [(key, value) for key, value in player_dict.items()]
    return max(*player_list, key=lambda item: item[1])


def find_star(records, player_list):
    """
    通过给定一个records来得到这段records中表现最好的球员
    """
    # player_list = generate_player_list(records)
    player_dict = {player: 0 for player in player_list}
    for record in records:
        text = record.event
        if "三分球进" in text:
            # print(record)
            player_dict[find_who_score(text, player_list)] += 3
        elif "两分球进" in text:
            # print(record)
            player_dict[find_who_score(text, player_list)] += 2
        elif "罚球命中" in text:
            # print(record)
            player_dict[find_who_score(text, player_list)] += 1
        else:
            pass
    # 返回得分最高的球员和他的得分
    return find_max_score(player_dict)


def fill_star_to_pieces(total_pieces, records, home_team_name, away_team_name):
    """
    给切好的所有比赛片段填充上对应片段中发挥最好的球员和他的得分
    """
    # 获取主队的球员列表和客队的球员列表
    home_player_list = utils.generate_player_list(records, home_team_name)
    away_player_list = utils.generate_player_list(records, away_team_name)
    # 填充球星
    for index, quarter_pieces in enumerate(total_pieces):
        quarter_num = index + 1
        for piece in quarter_pieces:
            temp_record = utils.get_record(piece.start_time, piece.end_time, quarter_num, home_team_name, records)
            (piece.home_star_name, piece.home_star_score) = find_star(temp_record, home_player_list)
            temp_record = utils.get_record(piece.start_time, piece.end_time, quarter_num, away_team_name, records)
            (piece.away_star_name, piece.away_star_score) = find_star(temp_record, away_player_list)