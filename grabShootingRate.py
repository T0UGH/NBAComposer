import requests
from bs4 import BeautifulSoup


def grab_shooting_rate(team_name_1, team_name_2):
    url = 'https://nba.hupu.com/stats/teams'
    req_data = requests.get(url)
    soup = BeautifulSoup(req_data.text, 'html.parser')
    statistic_table = soup.find('table', id='data_js_sort')
    shooting_rate_amount = 0
    for tr in statistic_table.find_all('tr', class_=False):
        tds = tr.find_all('td')
        temp_team_shooting_rate = float(tds[2].get_text()[:-1])
        shooting_rate_amount += temp_team_shooting_rate
        temp_team_name = tds[1].get_text()
        if team_name_1 == temp_team_name:
            team_shooting_rate_1 = temp_team_shooting_rate
        elif team_name_2 == temp_team_name:
            team_shooting_rate_2 = temp_team_shooting_rate
    league_shooting_rate = shooting_rate_amount / 30
    return league_shooting_rate, team_shooting_rate_1, team_shooting_rate_2


print(grab_shooting_rate('火箭', '步行者'))
