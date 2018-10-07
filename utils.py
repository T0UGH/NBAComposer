def get_record_from_section_num(section_num, records):
    """
    根据比赛的节数和正常比赛的文字实录选出指定节的文字实录,如果返回结果为None说明没有这一节
    :param section_num:
    :param records:
    :return:
    """
    section_records = []
    for record in records:
        if record.section_num == section_num:
            section_records.append(record)
    # for section_record in section_records:
    #     print(section_record)
    return section_records if section_records != [] else None


def get_record(start_time, end_time, section_num, team, records):
    return_records = []
    for record in records:
        if section_num == record.section_num and end_time <= record.time_to_end <= start_time and record.team == team:
            return_records.append(record)
    return return_records


def generate_player_list(records, team):

    def analysis_change_text(change_team_text):
        left_index = change_team_text.find("(") + 1
        right_index = change_team_text.find(")")
        pieces = change_team_text[left_index:right_index].split("; ")
        return pieces

    player_list = []
    for record in records:
        text = record[4]
        if "阵容调整" in text and record.team == team:
            player_sub_list = analysis_change_text(text)
            player_list += player_sub_list
    return list(set(player_list))


