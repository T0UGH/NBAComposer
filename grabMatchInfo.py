import requests
from bs4 import BeautifulSoup
from DataDef import Record, BasicMatchInfo, TeamStatistic, PlayerStatistic, MatchInfo


def grab_match_info(match_id):
    basic = grab_basic_match_info(match_id)
    records = grab_record(match_id)
    home_team_statistic, away_team_statistic, home_player_statistics, away_player_statistics = grab_statistic(match_id)
    return MatchInfo(basic, records, home_team_statistic, away_team_statistic, home_player_statistics, away_player_statistics)


def grab_basic_match_info(match_id):
    url = 'https://nba.hupu.com/games/boxscore/' + str(match_id)
    req_data = requests.get(url)
    soup = BeautifulSoup(req_data.text, 'html.parser')

    team_vs_box = soup.find(class_='team_vs')
    time_str = team_vs_box.find('p', class_='time_f').string[3:]

    quarter_score_table = soup.find('table', class_='itinerary_table')

    away_quarter_scores = []
    away_data = quarter_score_table.find('tr', class_='away_score').find_all('td')
    for index, td in enumerate(away_data):
        if index == 0:
            away_team_name = td.string
        elif index == len(away_data) - 1:
            away_score = int(td.string)
        else:
            away_quarter_scores.append(int(td.string))

    home_quarter_scores = []
    home_data = quarter_score_table.find('tr', class_='home_score').find_all('td')
    for index, td in enumerate(home_data):
        if index == 0:
            home_team_name = td.string
        elif index == len(away_data) - 1:
            home_score = int(td.string)
        else:
            home_quarter_scores.append(int(td.string))
    basic_match_info = BasicMatchInfo(home_team_name, away_team_name, home_score, away_score,
                                      home_quarter_scores, away_quarter_scores, time_str)
    return basic_match_info


def grab_statistic(match_id):
    url = 'https://nba.hupu.com/games/boxscore/' + str(match_id)
    req_data = requests.get(url)
    soup = BeautifulSoup(req_data.text, 'html.parser')
    away_statistic_box = soup.find("table", id='J_away_content')
    home_statistic_box = soup.find("table", id='J_home_content')
    away_statistic_data = away_statistic_box.find_all('tr')
    home_statistic_data = home_statistic_box.find_all('tr')

    away_player_statistics = []
    for i, tr in enumerate(away_statistic_data):
        tds = tr.find_all('td')
        if tds[0].get_text() in ('首发', '替补') or i == len(away_statistic_data) - 1:
            continue
        elif i == len(away_statistic_data) - 2:
            away_team_statistic = generate_team_statistic(tr)
        else:
            temp = generate_player_statistic(tr)
            away_player_statistics.append(temp)

    home_player_statistics = []
    for i, tr in enumerate(home_statistic_data):
        tds = tr.find_all('td')
        if tds[0].get_text() in ('首发', '替补') or i == len(home_statistic_data) - 1:
            continue
        elif i == len(home_statistic_data) - 2:
            home_team_statistic = generate_team_statistic(tr)
        else:
            temp = generate_player_statistic(tr)
            home_player_statistics.append(temp)

    return home_team_statistic, away_team_statistic, home_player_statistics, away_player_statistics


def generate_player_statistic(tr):
    tds = tr.find_all('td')
    player_name = tds[0].get_text()
    playing_time = int(tds[2].get_text())
    shoot_num, shoot_attemp_num = extract_number_data(tds[3].get_text())
    three_points_num, three_points_attemp_num = extract_number_data(tds[4].get_text())
    free_throw_num, free_throw_attemp_num = extract_number_data(tds[5].get_text())
    offensive_rebound_num = int(tds[6].get_text())
    defensive_rebound_num = int(tds[7].get_text())
    rebound_num = int(tds[8].get_text())
    assist_num = int(tds[9].get_text())
    fool_num = int(tds[10].get_text())
    steal_num = int(tds[11].get_text())
    turnover_num = int(tds[12].get_text())
    block_num = int(tds[13].get_text())
    score = int(tds[14].get_text())
    add_sub_num = int(tds[15].get_text())
    return PlayerStatistic(player_name, playing_time, shoot_num, shoot_attemp_num, three_points_num, three_points_attemp_num, free_throw_num,
                         free_throw_attemp_num, offensive_rebound_num, defensive_rebound_num, rebound_num, assist_num,
                         fool_num, steal_num, turnover_num, block_num, score, add_sub_num)


def generate_team_statistic(tr):
    tds = tr.find_all('td')
    shoot_num, shoot_attemp_num = extract_number_data(tds[3].get_text())
    three_points_num, three_points_attemp_num = extract_number_data(tds[4].get_text())
    free_throw_num, free_throw_attemp_num = extract_number_data(tds[5].get_text())
    offensive_rebound_num = int(tds[6].get_text())
    defensive_rebound_num = int(tds[7].get_text())
    rebound_num = int(tds[8].get_text())
    assist_num = int(tds[9].get_text())
    fool_num = int(tds[10].get_text())
    steal_num = int(tds[11].get_text())
    turnover_num = int(tds[12].get_text())
    block_num = int(tds[13].get_text())
    score = int(tds[14].get_text())
    return TeamStatistic(shoot_num, shoot_attemp_num, three_points_num, three_points_attemp_num, free_throw_num,
                         free_throw_attemp_num, offensive_rebound_num,defensive_rebound_num, rebound_num, assist_num,
                         fool_num, steal_num, turnover_num, block_num, score)


def extract_number_data(number_data_with_split):
    number_data_with_split = str(number_data_with_split)
    splits = number_data_with_split.split('-')
    return int(splits[0]), int(splits[1])


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
    match_id = 156175
    print(grab_match_info(156175))












