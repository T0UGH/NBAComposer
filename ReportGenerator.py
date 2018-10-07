from Template import choice_template


def generate_quarter_head(quarter_num):
    if quarter_num > 3:
        return "第%d个加时赛:" % quarter_num - 3
    else:
        return ['首节比赛:', '次节比赛:', '易边再战:', '最后一节:'][quarter_num]


def fill_template(match_piece, match_info):
    piece_type = match_piece.type
    team_name = match_info[0]
    other_team_name = match_info[1]
    team_score = match_piece.end_home_score - match_piece.start_home_score
    other_team_score = match_piece.end_away_score - match_piece.start_away_score
    player_score = match_piece.player_score
    player_name = match_piece.player_name
    time = parse_time(match_piece.start_time)

    template = choice_template(piece_type)

    if piece_type >= 4:
        team_name, other_team_name = other_team_name, team_name
        team_score, other_team_score = other_team_score, team_score

    score_gap = abs(team_score - other_team_score)

    if '<time>' in template:
        template = template.replace('<time>', time)
    if '<team_name>' in template:
        template = template.replace('<team_name>', team_name)
    if '<team_score>' in template:
        template = template.replace('<team_score>', str(team_score))
    if '<other_team_name>' in template:
        template = template.replace('<other_team_name>', other_team_name)
    if '<other_team_score>' in template:
        template = template.replace('<other_team_score>', str(other_team_score))
    if '<score_gap>' in template:
        template = template.replace('<score_gap>', str(score_gap))
    if '<player_name>' in template:
        template = template.replace('<player_name>', player_name)
    if '<player_score>' in template:
        template = template.replace('<player_score>', str(player_score))

    return template


def parse_time(time, is_add_quarter=False):
    if is_add_quarter:
        time_length = 300
    else:
        time_length = 720
    if time == time_length:
        return "本节开场"
    elif time <= 120:
        return "本节末段"
    else:
        return "本节第%d分钟" % caculate_minutes(time, time_length)


def caculate_minutes(time, time_length):
    reverse_time = time_length - time
    return int(reverse_time/60)


def generate_report(match_pieces, team_names):
    for index in range(len(match_pieces)):
        print(generate_quarter_head(index), end='')
        for match_piece in match_pieces[index]:
            print(fill_template(match_piece, team_names), end='.')
