from collections import namedtuple

# 比赛分段
MatchPiece = namedtuple('MatchPiece', ['start_time', 'end_time', 'type', 'start_home_score',
                                       'end_home_score', 'start_away_score, end_away_score'])
# 一些其他的比赛信息
MatchInfo = namedtuple('MatchInfo', ['home_name', 'away_name'])


def daizhi_do(match_id):
    """请照着这个格式返回数据"""
    return [[MatchPiece(720, 650, 1, 0, 0, 10, 12), MatchPiece(650, 320, 2, 10, 12, 30, 15), MatchPiece(320, 0, 2, 30, 15, 40, 25)],
            [MatchPiece(720, 650, 1, 0, 0, 10, 12), MatchPiece(650, 320, 2, 10, 12, 30, 15), MatchPiece(320, 0, 2, 30, 15, 40, 25)],
            [MatchPiece(720, 650, 1, 0, 0, 10, 12), MatchPiece(650, 320, 2, 10, 12, 30, 15), MatchPiece(320, 0, 2, 30, 15, 40, 25)],
            [MatchPiece(720, 650, 1, 0, 0, 10, 12), MatchPiece(650, 320, 2, 10, 12, 30, 15), MatchPiece(320, 0, 2, 30, 15, 40, 25)]],\
           MatchInfo('猛龙', '魔术')
