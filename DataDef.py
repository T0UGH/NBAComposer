from collections import namedtuple

# 比赛分段
MatchPiece = namedtuple('MatchPiece', ['start_time', 'end_time', 'type', 'start_home_score', 'start_away_score',
                                       'end_home_score', 'end_away_score', 'player_name', 'player_score'])
# 一些其他的比赛信息
MatchInfo = namedtuple('MatchInfo', ['home_name', 'away_name'])


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


if __name__ == '__main__':
    piece = Piece(1, 1, 2, 3, 4, 5, 6, "he", 5)
    print(piece)

