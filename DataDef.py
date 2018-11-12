

# 比赛分段
class Piece:

    def __init__(self, start_time, end_time, _type, start_home_score, start_away_score,
                 end_home_score, end_away_score, home_star_name=None, home_star_score=None,
                 away_star_name=None, away_star_score=None, home_shoot=None, home_shoot_attemp=None, home_efficiency_type=None,
                 away_shoot=None, away_shoot_attemp=None, away_efficiency_type=None):
        self.start_time = start_time
        self.end_time = end_time
        self.type = _type
        self.start_home_score = start_home_score
        self.start_away_score = start_away_score
        self.end_home_score = end_home_score
        self.end_away_score = end_away_score
        self.home_star_name = home_star_name
        self.home_star_score = home_star_score
        self.away_star_name = away_star_name
        self.away_star_score = away_star_score
        self.home_shoot = home_shoot
        self.home_shoot_attemp = home_shoot_attemp
        self.home_efficiency_type = home_efficiency_type
        self.away_shoot = away_shoot
        self.away_shoot_attemp = away_shoot_attemp
        self.away_efficiency_type = away_efficiency_type

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<" + str(self.start_time) + ", " + str(self.end_time) + ", " + str(self.type) \
               + ", " + str(self.start_home_score) + ", " + str(self.start_away_score) + ", " \
               + str(self.end_home_score) + ", " + str(self.end_away_score) + ", " \
               + str(self.home_star_name) + ", " + str(self.home_star_score) + ", " \
               + str(self.away_star_name) + ", " + str(self.away_star_score) + ", " \
               + str(self.home_shoot) + ", " + str(self.home_shoot_attemp) + ", " + str(self.home_efficiency_type) + ", " \
               + str(self.away_shoot) + ", " + str(self.away_shoot_attemp) + ", " + str(self.away_efficiency_type) + ">"


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

    def shooting_rate(self):
        return self.shoot_num / self.shoot_attemp_num * 100


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

