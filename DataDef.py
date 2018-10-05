from collections import namedtuple

# 比赛分段
MatchPiece = namedtuple('MatchPiece', ['start_time', 'end_time', 'type', 'start_home_score', 'start_away_score',
                                       'end_home_score', 'end_away_score', 'player_name', 'player_score'])
# 一些其他的比赛信息
MatchInfo = namedtuple('MatchInfo', ['home_name', 'away_name'])


def daizhi_do():
    """请照着这个格式返回数据"""
    return [[MatchPiece(720, 450, 1, 0, 0, 15, 3, '德玛尔 德罗赞', 7),
             MatchPiece(450, 220, 6, 15, 3, 26, 22, '阿龙 戈登', 6),
             MatchPiece(220, 0, 3, 26, 22, 30, 28, '凯尔 罗瑞', 4)],

            [MatchPiece(720, 550, 1, 30, 28, 45, 32, '德玛尔 德罗赞', 6),
             MatchPiece(550, 320, 0, 45, 32, 56, 40, '塞尔吉 伊巴卡', 8),
             MatchPiece(320, 0, 6, 56, 40, 62, 48, '乔纳森 西蒙斯', 4)],

            [MatchPiece(720, 400, 3, 62, 48, 70, 56, '德玛尔 德罗赞', 4),
             MatchPiece(400, 200, 6, 70, 56, 80, 70, '阿龙 戈登', 9),
             MatchPiece(200, 0, 3, 80, 70, 85, 75, '德玛尔 德罗赞', 4)],

            [MatchPiece(720, 450, 3, 85, 75, 92, 88, '德玛尔 德罗赞', 4),
             MatchPiece(450, 220, 4, 92, 88, 100, 106, '阿龙 戈登', 4),
             MatchPiece(220, 0, 4, 100, 106, 106, 115, '武切维奇', 5)]], MatchInfo('猛龙', '魔术')

