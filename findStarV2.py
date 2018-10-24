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
    通过给定一个records来得到这段records中表现最好的秋燕
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


def fill_star_to_pieces(total_pieces, records, team_name):
    """
    给切好的所有比赛片段填充上对应片段中发挥最好的球员和他的得分
    """
    # 获取主队的球员列表和客队的球员列表
    home_player_list = utils.generate_player_list(records, team_name[0])
    away_player_list = utils.generate_player_list(records, team_name[1])

    # 填充球星
    for index, quarter_pieces in enumerate(total_pieces):
        quarter_num = index + 1
        for piece in quarter_pieces:
            temp_team = team_name[0] if piece.type < 4 else team_name[1]
            temp_player_list = home_player_list if piece.type < 4 else away_player_list
            temp_record = utils.get_record(piece.start_time, piece.end_time, quarter_num, temp_team, records)
            (piece.player_name, piece.player_score) = find_star(temp_record, temp_player_list)
