from grabMatchInfo import grab_match_info
from dividePiece import divide_piece
from findStar import fill_star_to_pieces
from generateReport import generate_report


def compose_nba(match_id):
    """
    通过传入一场比赛对应的id,来生成对应的比赛战报
    :param match_id:
    :return: 直接将战报打印到控制台
    """

    # 获取数据
    match_info = grab_match_info(match_id)

    # 获取正常比赛的片段
    total_pieces = divide_piece(match_info.records)

    # 获取这场比赛的对阵双方,以元组形式返回 (主队,客队)

    # 为每个数据片段补充发挥好的球员和这个球员得到的分数
    fill_star_to_pieces(total_pieces, match_info.records, (match_info.basic_match_info.home_team_name, match_info.basic_match_info.away_team_name))

    # 生成战报
    generate_report(total_pieces, match_info)


if __name__ == '__main__':
    compose_nba(156175)
