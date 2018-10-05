import random


def choice_template(template_type: int) -> str:

    type_0_templates = ["<time>,<team_name>队手感火热，多点开花，打出一波<team_score>:<other_team_score>的进攻波，成功扩大优势",
                        "<time>,<team_name>队的<player_name>表现神勇，连突带投，帮助球队扩大优势"]

    type_1_templates = ["<time>,<team_name>队表现出色，建立起<score_gap>分的领先优势",
                        "<time>,<team_name>队在<player_name>的带领下，打出一波<team_score>:<other_team_score>的进攻波，逐渐确立优势",
                        "<time>,<team_name>队的<player_name>连得<player_score>分，帮助球队建立起领先优势"]

    type_2_templates = ["<time>,<team_name>不甘示弱，在<player_name>的带领下不断追赶比分，缩小分差",
                        "<time>,<team_name>手感回暖，其中<player_name>连续得分，打出一波<team_score>:<other_team_score>的进攻波，缩小落后"]

    type_3_templates = ["<time>,双方打得难解难分，均有亮眼发挥",
                        "<time>,双方交替领先，比赛逐渐白热化",
                        "<time>,双方展开了对攻大战，<team_name>得到<team_score>分,<other_team_name>也有<other_team_score>分进账"]

    templates = [type_0_templates, type_1_templates, type_2_templates, type_3_templates]

    if template_type >= 4:
        template_type = template_type % 4

    return random.choice(templates[template_type])
