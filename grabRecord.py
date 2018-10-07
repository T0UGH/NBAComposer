import requests
from bs4 import BeautifulSoup
from collections import namedtuple

Record = namedtuple("Record", ['match_id', 'section_num', 'time_to_end', 'team', 'event', 'score'])


def grab_team_name(match_id):
    # 爬取数据统计
    url_record = 'https://nba.hupu.com/games/boxscore/' + str(match_id)
    req_data = requests.get(url_record)
    soup_data = BeautifulSoup(req_data.text, "html.parser")
    soup2_score = soup_data.find("table", class_="itinerary_table")
    section_score = []
    team = []
    aggregate_score = ""
    # 抓取比分
    score = ""
    # score存储了section_score

    for tags_score in soup2_score.find_all("tr"):
        for tags2_score in tags_score.find_all("td"):
            if (tags2_score.string != None):
                section_score.append(tags2_score.string.strip())
        if '一' not in section_score[0]:
            team.append(section_score.pop(0))
            score += "["
            for i in section_score:
                score += " " + i
            score += " ]"
            aggregate_score += section_score[-1] + "-"
        section_score.clear()
    return team[0], team[1]


def grab_record(match_id):
    """
    根据比赛的id爬取比赛的文字实录
    :param match_id: 比赛的id
    :return: list -> Record类型的列表
    """

    # 首先定义一个时间转换函数
    def translate_time(time_to_end):
        time = 0
        if ':' in time_to_end:
            time = int(time_to_end.split(':')[0]) * 60 + int(time_to_end.split(':')[1])
        elif '.' in time_to_end:
            time = int(time_to_end.split('.')[0])
        else:
            pass
        return time
    # 找到文字实录链接
    url_record = 'https://nba.hupu.com/games/playbyplay/' + str(match_id)
    req = requests.get(url_record)
    soup = BeautifulSoup(req.text, "html.parser")
    soup2 = soup.find("div", "table_list_live playbyplay_td table_overflow")
    records = []

    # 爬取文字实录

    section = 1
    for tags in soup2.find_all("tr"):

        record = []
        for tags2 in tags.find_all("td"):
            record.append(tags2.string.strip('\n'))

        # 判断当前的节数
        flag = "结束"
        if flag in record[0]:
            section = section + 1
        record.append(section)

        if len(record) == 5:
            records.append(Record(match_id, section, translate_time(record[0]), record[1], record[2], record[3]))
            pass

    return records


if __name__ == '__main__':
    records = grab_team_name(157292)
    print(records)








