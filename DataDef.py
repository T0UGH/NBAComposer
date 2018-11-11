from collections import namedtuple

# 比赛分段
MatchPiece = namedtuple('MatchPiece', ['start_time', 'end_time', 'type', 'start_home_score', 'start_away_score',
                                       'end_home_score', 'end_away_score', 'player_name', 'player_score'])


# 比赛分段
class Piece:

    def __init__(self, start_time, end_time, _type, start_home_score, start_away_score,
                 end_home_score, end_away_score, player_name=None, player_score=None):
        self.start_time = start_time
        self.end_time = end_time
        self.type = _type
        self.start_home_score = start_home_score
        self.start_away_score = start_away_score
        self.end_home_score = end_home_score
        self.end_away_score = end_away_score
        self.player_name = player_name
        self.player_score = player_score

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<" + str(self.start_time) + ", " + str(self.end_time) + ", " + str(self.type) \
               + ", " + str(self.start_home_score) + ", " + str(self.start_away_score) + ", " + str(self.end_home_score) \
               + ", " + str(self.end_away_score) + ", " + str(self.player_name) + ", " + str(self.player_score) + ">"


# 单条比赛记录
class Record:

    def __init__(self, match_id, section_num, time_to_end, team, event, score):
        self.match_id = match_id
        self.section_num = section_num
        self.time_to_end = time_to_end
        self.team = team
        self.event = event
        self.score = score

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<" + str(self.match_id) + ", " + str(self.section_num) + ", " + str(self.time_to_end) \
               + ", " + str(self.team) + ", " + str(self.event) + ", " + str(self.score)  + ">"


class BasicMatchInfo:

    def __init__(self, home_team_name, away_team_name, home_score, away_score, home_quarter_scores, away_quarter_scores, time_str):
        self.home_team_name = home_team_name
        self.away_team_name = away_team_name
        self.home_score = home_score
        self.away_score = away_score
        self.home_quarter_scores = home_quarter_scores
        self.away_quarter_scores = away_quarter_scores
        self.time_str = time_str

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<" + str(self.home_team_name) + ", " + str(self.away_team_name) + ", " + str(self.home_score) \
               + ", " + str(self.away_score) + ", " + str(self.home_quarter_scores) + ", " + str(self.away_quarter_scores) \
               + ", " + str(self.time_str) + ">"


class TeamStatistic:

    def __init__(self, shoot_num, shoot_attemp_num, three_points_num,
                 three_points_attemp_num, free_throw_num, free_throw_attemp_num,
                 offensive_rebound_num, defensive_rebound_num, rebound_num,
                 assist_num, fool_num, steal_num, turnover_num, block_num, score):
        self.shoot_num = shoot_num
        self.shoot_attemp_num = shoot_attemp_num
        self.three_points_num = three_points_num
        self.three_points_attemp_num = three_points_attemp_num
        self.free_throw_num = free_throw_num
        self.free_throw_attemp_num = free_throw_attemp_num
        self.offensive_rebound_num = offensive_rebound_num
        self.defensive_rebound_num = defensive_rebound_num
        self.rebound_num = rebound_num
        self.assist_num = assist_num
        self.fool_num = fool_num
        self.steal_num = steal_num
        self.turnover_num = turnover_num
        self.block_num = block_num
        self.score = score

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<" + str(self.shoot_num) + ", " + str(self.shoot_attemp_num) \
               + ", " + str(self.three_points_num) + ", " + str(self.three_points_attemp_num) + ", " + str(self.free_throw_num) \
               + ", " + str(self.free_throw_attemp_num) + ", " + str(self.offensive_rebound_num) + ", " + str(self.defensive_rebound_num) \
               + ", " + str(self.rebound_num) + ", " + str(self.assist_num) + ", " + str(self.fool_num) \
               + ", " + str(self.steal_num) + ", " + str(self.turnover_num) + ", " + str(self.block_num) + ", " + str(self.score) \
               + ", " + ">"


class PlayerStatistic:

    def __init__(self, player_name, playing_time, shoot_num, shoot_attemp_num, three_points_num,
                 three_points_attemp_num, free_throw_num, free_throw_attemp_num,
                 offensive_rebound_num, defensive_rebound_num, rebound_num,
                 assist_num, fool_num, steal_num, turnover_num, block_num, score, add_sub_num):
        self.player_name = player_name
        self.playing_time = playing_time
        self.shoot_num = shoot_num
        self.shoot_attemp_num = shoot_attemp_num
        self.three_points_num = three_points_num
        self.three_points_attemp_num = three_points_attemp_num
        self.free_throw_num = free_throw_num
        self.free_throw_attemp_num = free_throw_attemp_num
        self.offensive_rebound_num = offensive_rebound_num
        self.defensive_rebound_num = defensive_rebound_num
        self.rebound_num = rebound_num
        self.assist_num = assist_num
        self.fool_num = fool_num
        self.steal_num = steal_num
        self.turnover_num = turnover_num
        self.block_num = block_num
        self.score = score
        self.add_sub_num = add_sub_num

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<" + str(self.player_name) + ", " + str(self.playing_time) + ", " + str(self.shoot_num) + ", " + str(self.shoot_attemp_num) \
               + ", " + str(self.three_points_num) + ", " + str(self.three_points_attemp_num) + ", " + str(self.free_throw_num) \
               + ", " + str(self.free_throw_attemp_num) + ", " + str(self.offensive_rebound_num) + ", " + str(self.defensive_rebound_num) \
               + ", " + str(self.rebound_num) + ", " + str(self.assist_num) + ", " + str(self.fool_num) \
               + ", " + str(self.steal_num) + ", " + str(self.turnover_num) + ", " + str(self.block_num) + ", " + str(self.score) \
               + ", " + str(self.add_sub_num) + ">"


class MatchInfo:

    def __init__(self, basic_match_info, records, home_team_statistic, away_team_statistic, home_player_statistics, away_player_statistics):
        self.basic_match_info = basic_match_info
        self.records = records
        self.home_team_statistic = home_team_statistic
        self.away_team_statistic = away_team_statistic
        self.home_player_statistics = home_player_statistics
        self.away_player_statistics = away_player_statistics

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<" + str(self.basic_match_info) + ", " + str(self.records) + ", " + str(self.home_team_statistic) \
               + ", " + str(self.away_team_statistic) + ", " + str(self.home_player_statistics) + ", "\
               + str(self.away_player_statistics) + ">"


if __name__ == '__main__':
    piece = Piece(1, 1, 2, 3, 4, 5, 6, "he", 5)
    print(piece)

