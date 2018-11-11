from Template import choice_template


def generate_report_head(match_info):
    templete = "北京时间<time>,<home_team_name>队坐镇主场迎战<away_team_name>队。"
    time_str = match_info.basic_match_info.time_str
    home_team_name = match_info.basic_match_info.home_team_name
    away_team_name = match_info.basic_match_info.away_team_name
    templete = templete.replace('<time>', time_str)
    templete = templete.replace('<home_team_name>', home_team_name)
    templete = templete.replace('<away_team_name>', away_team_name)
    return templete


def generate_quarter_head(quarter_num):
    quarter_num = int(quarter_num)
    if quarter_num > 3:
        return "第%d个加时赛阶段:" % (quarter_num - 3)
    else:
        return ['首节比赛:', '次节比赛:', '易边再战:', '最后一节:'][quarter_num]


def add_scores(quarter_scores, quarter_num):
    amount = 0
    for i in range(0, quarter_num + 1):
        amount += quarter_scores[i]
    return amount


def generate_quarter_tail(match_info, quarter_num):
    quarter_tail_templete = "本节结束，<home_team_name>队以<home_score>分比<away_score>分<decorator>于<away_team_name>队。"
    report_tail_templete = "最终，<home_team_name>队以<home_score>分比<away_score>分<decorator>了<away_team_name>队。"
    quarter_tail_decorators = ["领先", "落后", "打平"]
    report_tail_decorators = ["战胜", "输给"]
    home_quarter_scores = match_info.basic_match_info.home_quarter_scores
    away_quarter_scores = match_info.basic_match_info.away_quarter_scores
    home_score = add_scores(home_quarter_scores, quarter_num)
    away_score = add_scores(away_quarter_scores, quarter_num)
    total_quarter = len(home_quarter_scores)
    home_team_name = match_info.basic_match_info.home_team_name
    away_team_name = match_info.basic_match_info.away_team_name

    if quarter_num == total_quarter - 1:
        report_tail_templete = report_tail_templete.replace('<home_team_name>', home_team_name)
        report_tail_templete = report_tail_templete.replace('<away_team_name>', away_team_name)
        report_tail_templete = report_tail_templete.replace('<home_score>', str(home_score))
        report_tail_templete = report_tail_templete.replace('<away_score>', str(away_score))
        if home_score > away_score:
            report_tail_templete = report_tail_templete.replace('<decorator>', report_tail_decorators[0])
        else:
            report_tail_templete = report_tail_templete.replace('<decorator>', report_tail_decorators[1])
        return report_tail_templete
    else:
        quarter_tail_templete = quarter_tail_templete.replace('<home_team_name>', home_team_name)
        quarter_tail_templete = quarter_tail_templete.replace('<away_team_name>', away_team_name)
        quarter_tail_templete = quarter_tail_templete.replace('<home_score>', str(home_score))
        quarter_tail_templete = quarter_tail_templete.replace('<away_score>', str(away_score))
        if home_score > away_score:
            quarter_tail_templete = quarter_tail_templete.replace('<decorator>', quarter_tail_decorators[0])
        elif home_score < away_score:
            quarter_tail_templete = quarter_tail_templete.replace('<decorator>', quarter_tail_decorators[1])
        else:
            quarter_tail_templete = quarter_tail_templete.replace('<decorator>', quarter_tail_decorators[2])
        return quarter_tail_templete


def fill_template(match_piece, team_names, is_add_quarter=False):
    piece_type = match_piece.type
    team_name = team_names[0]
    other_team_name = team_names[1]
    team_score = match_piece.end_home_score - match_piece.start_home_score
    other_team_score = match_piece.end_away_score - match_piece.start_away_score
    player_score = match_piece.player_score
    player_name = match_piece.player_name
    time = parse_time(match_piece.start_time, is_add_quarter)

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


def generate_report(match_pieces, match_info):
    print(generate_report_head(match_info))
    team_names = (match_info.basic_match_info.home_team_name, match_info.basic_match_info.away_team_name)
    for index in range(len(match_pieces)):
        print(generate_quarter_head(index), end='')
        for match_piece in match_pieces[index]:
            print(fill_template(match_piece, team_names, is_add_quarter=(index > 3)), end='.')
        print(generate_quarter_tail(match_info, index), end='')
