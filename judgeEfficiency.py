from grabMatchInfo import grab_match_info
from dividePiece import divide_piece
from grabShootingRate import grab_shooting_rate
import utils

MATCH_SHOOTING_RATE_WEIGHT = 0.7
TEAM_SHOOTING_RATE_WEIGHT = 0.2
LEAGUE_SHOOTING_RATE_WEIGHT = 0.1
SHOOTING_RATE_TOLERANCE = 5
HIGH_EFFICIENCY = 0
MID_EFFICIENCY = 1
LOW_EFFICIENCY = 2


def calculate_avg_shooting_rate(home_team_name, away_team_name, home_match_shooting_rate, away_match_shooting_rate):
    print(home_match_shooting_rate, away_match_shooting_rate)
    league_shooting_rate, home_team_shooting_rate, away_team_shooting_rate = grab_shooting_rate(home_team_name, away_team_name)
    home_avg_shooting_rate = home_match_shooting_rate * MATCH_SHOOTING_RATE_WEIGHT \
                         + home_team_shooting_rate * TEAM_SHOOTING_RATE_WEIGHT \
                         + league_shooting_rate * LEAGUE_SHOOTING_RATE_WEIGHT
    away_avg_shooting_rate = away_match_shooting_rate * MATCH_SHOOTING_RATE_WEIGHT \
                               + away_team_shooting_rate * TEAM_SHOOTING_RATE_WEIGHT \
                               + league_shooting_rate * LEAGUE_SHOOTING_RATE_WEIGHT
    return home_avg_shooting_rate, away_avg_shooting_rate


def calculate_shooting_rate(shoot, shoot_attemp, default=0):
    try:
        piece_home_shooting_rate = shoot / shoot_attemp * 100
    except ZeroDivisionError:
        piece_home_shooting_rate = default
    return piece_home_shooting_rate


def judge_efficiency(shooting_rate, avg_shooting_rate, shooting_rate_tolerance = SHOOTING_RATE_TOLERANCE):
    sub = abs(shooting_rate - avg_shooting_rate)
    if sub < shooting_rate_tolerance:
        return MID_EFFICIENCY
    elif shooting_rate > avg_shooting_rate:
        return HIGH_EFFICIENCY
    else:
        return LOW_EFFICIENCY


def fill_shooting_rate_to_pieces(total_pieces, records, match_info):

    home_team_name = match_info.basic_match_info.home_team_name
    away_team_name = match_info.basic_match_info.away_team_name
    home_shooting_rate = match_info.home_team_statistic.shooting_rate()
    away_shooting_rate = match_info.away_team_statistic.shooting_rate()

    # 为主队填充命中率
    home_avg_shooting_rate, away_avg_shooting_rate = \
        calculate_avg_shooting_rate(home_team_name, away_team_name, home_shooting_rate, away_shooting_rate)

    for index, quarter_pieces in enumerate(total_pieces):

        quarter_num = index + 1
        for piece in quarter_pieces:

            home_temp_record = utils.get_record(piece.start_time, piece.end_time, quarter_num, home_team_name, records)
            (home_shoot, home_shoot_attemp) = count_shoot_and_shoot_attemp(home_temp_record)
            piece_home_shooting_rate = calculate_shooting_rate(home_shoot, home_shoot_attemp, default=home_avg_shooting_rate)
            home_efficency = judge_efficiency(piece_home_shooting_rate,home_avg_shooting_rate)
            piece.home_shoot, piece.home_shoot_attemp, piece.home_efficiency_type = home_shoot, home_shoot_attemp, home_efficency

            away_temp_record = utils.get_record(piece.start_time, piece.end_time, quarter_num, away_team_name, records)
            (away_shoot, away_shoot_attemp) = count_shoot_and_shoot_attemp(away_temp_record)
            piece_away_shooting_rate = calculate_shooting_rate(away_shoot, away_shoot_attemp, default=away_avg_shooting_rate)
            away_efficency = judge_efficiency(piece_away_shooting_rate, away_avg_shooting_rate)
            piece.away_shoot, piece.away_shoot_attemp, piece.away_efficiency_type = away_shoot, away_shoot_attemp, away_efficency


def count_shoot_and_shoot_attemp(records):
    shoot_attemp = 0
    shoot = 0
    for record in records:
        if "分不中" in record.event:
            shoot_attemp += 1
        elif "分球进" in record.event:
            shoot += 1
            shoot_attemp += 1
    return shoot, shoot_attemp


if __name__ == '__main__':
    # 获取数据
    match_info = grab_match_info(156150)
    # 获取正常比赛的片段
    total_pieces = divide_piece(match_info.records)

    fill_shooting_rate_to_pieces(total_pieces, match_info.records, match_info)
