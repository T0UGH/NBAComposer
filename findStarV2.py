def find_who_score(text, player_list):
    for player in player_list:
        if player in text:
            return player


def find_star(records, player_list):
    # player_list = generate_player_list(records)
    player_dict = {player: 0 for player in player_list}
    for record in records:
        text = record[4]
        if "三分球进" in text:
            # print(record)
            player_dict[find_who_score(text, player_list)] += 3
        elif "两分球进" in text:
            # print(record)
            print(text)
            print(player_list)
            player_dict[find_who_score(text, player_list)] += 2
        elif "罚球命中" in text:
            # print(record)
            player_dict[find_who_score(text, player_list)] += 1
        else:
            pass
    return find_max_score(player_dict)


def find_max_score(player_dict):
    player_list = [(key, value) for key, value in player_dict.items()]
    return max(*player_list, key=lambda item: item[1])

