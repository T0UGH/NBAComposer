from grabMatchInfo import grab_record
from collections import namedtuple
from DataDef import Piece


total_time = []  # 所有播报时间集合
total_difference_score = []  # 所有分数集合
total_derivative = []  # 导数
total_host_score = []  # 客队得分
total_guest_score = []  # 主队得分
total_slice_set = []  # 片总集合
final_total_slice_set = []  # 最终片总集合
total_piece = []  # 总片输出
threshold = 7  # 阈值
anxious_value = 5  # 焦灼值


# 得到两个列表
def mysql_query(results):
    section_number = 1
    time = []  # 每节时间集合
    difference_score = []  # 每节分数差集合
    host_score = []  # 每节客队分数集合
    guest_score = []  # 每节主队分数集合
    for row in results:
        if row.section_num == section_number + 1:
            total_time.append(time)
            total_difference_score.append(difference_score)
            total_guest_score.append(guest_score)
            total_host_score.append(host_score)
            section_number = section_number + 1
            time = []  # 每节时间集合
            difference_score = []  # 每节分数差集合
            host_score = []  # 每节客队分数集合
            guest_score = []  # 每节主队分数集合
        if row.section_num == section_number:
            temp_time_to_end = row.time_to_end  # 到这节结束时间
            difference = int(row.score.split('-')[0]) - int(row.score.split('-')[1])  # 分数差，客队减去主队的
            host_s = int(row.score.split('-')[0])
            guest_s = int(row.score.split('-')[1])
            # # 打印结果
            # print("time=%s,name=%s" % (temp_time_to_end, difference))
            # 放入列表中
            # 若时间相同，取该时间的最大分数，即最后一个时间的分数
            if len(time) != 0 and int(temp_time_to_end) == time[-1]:
                time.pop()
                difference_score.pop()
                host_score.pop()
                guest_score.pop()
            time.append(int(temp_time_to_end))
            difference_score.append(difference)
            host_score.append(host_s)
            guest_score.append(guest_s)
    total_time.append(time)
    total_difference_score.append(difference_score)
    total_guest_score.append(guest_score)
    total_host_score.append(host_score)
    # 若每一节第一次直播文本时间开始不为720，或结尾不为0，手动插入
    for i in range(0, len(total_time)):
        if total_time[i][0] != 720:
            total_time[i].insert(0, 720)
            if i == 0:
                total_difference_score[i].insert(0, 0)
                total_host_score[i].insert(0, 0)
                total_guest_score[i].insert(0, 0)
            else:
                total_difference_score[i].insert(0, total_difference_score[i - 1][-1])
                total_host_score[i].insert(0, total_host_score[i - 1][-1])
                total_guest_score[i].insert(0, total_guest_score[i - 1][-1])
        if total_time[i][-1] != 0:
            total_time[i].append(0)
            total_difference_score[i].append(total_difference_score[i][-1])
            total_host_score[i].append(total_host_score[i][-1])
            total_guest_score[i].append(total_guest_score[i][-1])


# 获得导数
def get_derivative():
    for i in range(0, len(total_time)):
        derivative = []
        for n in range(0, len(total_time[i])-1):  # 最后一点无导数
            der = (total_difference_score[i][n+1]-total_difference_score[i][n])/(total_time[i][n]-total_time[i][n+1])
            derivative.append(der)
        # derivative.append(0)
        total_derivative.append(derivative)
    # print(total_derivative)


Slice = namedtuple('Slice', ['begin_time', 'end_time', 'state', 'begin_guest_score', 'end_guest_score', 'begin_host_score', 'end_host_score'])


def data_fragmentation():
    for i in range(0, len(total_derivative)):  # 在第i节中
        slice_set = []  # 片集合
        begin_time = 720
        if i > 3:
            begin_time = 300
        state = 0
        begin_guest_s = total_guest_score[i][0]
        begin_host_s = total_host_score[i][0]
        # 只有开头会出现片开始导数为0 的情况，只需判断开头即可
        for b in range(0, len(total_derivative[i])):
            if judge_symbol(total_derivative[i][b]) != 0:
                # state为1，该分片为增区间，为-1为减区间
                state = judge_symbol(total_derivative[i][b])
                break

        for k in range(0, len(total_derivative[i])):
            if judge_symbol(total_derivative[i][k]) == -state:
                end_time = total_time[i][k]
                end_guest_s = total_guest_score[i][k]
                end_host_s = total_host_score[i][k]
                # 赋值
                s = Slice(begin_time, end_time, state, begin_guest_s, end_guest_s, begin_host_s, end_host_s)
                slice_set.append(s)

                begin_time = total_time[i][k]
                begin_host_s = total_host_score[i][k]
                begin_guest_s = total_guest_score[i][k]
                state = judge_symbol(total_derivative[i][k])
        # 若最后end_time不为0，则加入
        if slice_set[-1].end_time != 0:
            s = Slice(slice_set[-1][1], 0, state, slice_set[-1].end_guest_score, total_guest_score[i][-1], slice_set[-1].end_host_score, total_host_score[i][-1])
            slice_set.append(s)
        total_slice_set.append(slice_set)


# 判断数的正负，正数返回1 ，负数返回-1,0返回0
def judge_symbol(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


Compose = namedtuple('Slice', ['begin_time', 'end_time', 'state', 'begin_guest_score', 'end_guest_score', 'begin_host_score', 'end_host_score'])


def data_compose():
    for i in range(0, len(total_slice_set)):  # 在每一节中
        final_slice_set = []
        begin_time = 720
        if i > 3:
            begin_time = 300
        state = total_slice_set[i][0].state  # 增减区间
        max_difference = total_slice_set[i][0].end_host_score - total_slice_set[i][0].end_guest_score
        begin_guest_s = total_slice_set[i][0].begin_guest_score
        begin_host_s = total_slice_set[i][0].begin_host_score
        for k in range(0, len(total_slice_set[i])):
            if total_slice_set[i][k].state != state:
                continue
            else:
                # 该if为下一区间加入分片的情况
                if (state == 1 and total_slice_set[i][k].end_host_score - total_slice_set[i][k].end_guest_score >= max_difference) or (state == -1 and total_slice_set[i][k].end_host_score - total_slice_set[i][k].end_guest_score <= max_difference):  # 增函数区间
                    max_difference = total_slice_set[i][k].end_host_score - total_slice_set[i][k].end_guest_score
                    end_time = total_slice_set[i][k].end_time
                    end_guest_s = total_slice_set[i][k].end_guest_score
                    end_host_s = total_slice_set[i][k].end_host_score
                # 该为到达该总分片终点
                else:
                    c = Compose(begin_time, end_time, state, begin_guest_s, end_guest_s, begin_host_s, end_host_s)
                    # 加入列表中
                    final_slice_set.append(c)

                    begin_time = end_time
                    end_time = total_slice_set[i][k].begin_time
                    state = -state
                    begin_host_s = end_host_s
                    begin_guest_s = end_guest_s
                    end_guest_s = total_slice_set[i][k].begin_guest_score
                    end_host_s = total_slice_set[i][k].begin_host_score
        # 若该节一直处于增或减状态
        if len(final_slice_set) == 0:
            c = Compose(720, 0, state, total_guest_score[i][0],
                        total_guest_score[i][-1], total_host_score[i][0], total_host_score[i][-1])
            final_slice_set.append(c)
        # 若最后分片没有把末尾加入，则手动加入至末尾
        if final_slice_set[-1].end_time != 0:
            c = Compose(final_slice_set[-1].end_time, 0, state, final_slice_set[-1].end_guest_score, total_guest_score[i][-1], final_slice_set[-1].end_host_score, total_host_score[i][-1])
            # 加入列表中
            final_slice_set.append(c)
        final_total_slice_set.append(final_slice_set)
    for i in range(0, len(final_total_slice_set)):  # 第i节
        for n in range(0, len(final_total_slice_set[i])):
            if state == 1 and final_total_slice_set[i][n].begin_host_score - final_total_slice_set[i][n].begin_guest_score < -threshold and final_total_slice_set[i][n].end_host_score - final_total_slice_set[i][n].end_guest_score > threshold:
                for m in range(0, len(total_time[i])):
                    if (total_time[i][m] < final_total_slice_set[i][n].begin_time) and (total_time[i][m] > final_total_slice_set[i][n].end_time) and (total_host_score[i][m] - total_guest_score[i][m] <= 0) and (total_host_score[i][m+1] - total_guest_score[i][m+1] > 0):
                        c = Compose(total_time[i][m], final_total_slice_set[i][n].end_time, final_total_slice_set[i][n].state, total_guest_score[i][m], final_total_slice_set[i][n].end_guest_s, total_host_score[i][m], final_total_slice_set[i][n].end_host_s)
                        final_total_slice_set[i].insert(n+1, c)
                        c = Compose(final_total_slice_set[i][n].begin_time, total_time[i][m],
                                    final_total_slice_set[i][n].state, final_total_slice_set[i][n].begin_guest_score,
                                    total_guest_score[i][m], final_total_slice_set[i][n].begin_host_score,
                                    total_host_score[i][m])
                        final_total_slice_set[i].insert(n + 1, c)
                        del final_total_slice_set[i][n]
                        break
            elif state == -1 and final_total_slice_set[i][n].begin_host_score - final_total_slice_set[i][n].begin_guest_score > threshold and final_total_slice_set[i][n].end_host_score - final_total_slice_set[i][n].end_guest_score < -threshold:
                for m in range(0, len(total_time[i])):
                    if (total_time[i][m] < final_total_slice_set[i][n].begin_time) and (total_time[i][m] > final_total_slice_set[i][n].end_time) and (total_host_score[i][m] - total_guest_score[i][m] >= 0) and (total_host_score[i][m+1] - total_guest_score[i][m+1] < 0):
                        c = Compose(total_time[i][m], final_total_slice_set[i][n].end_time, final_total_slice_set[i][n].state, total_guest_score[i][m], final_total_slice_set[i][n].end_guest_score, total_host_score[i][m], final_total_slice_set[i][n].end_host_score)
                        final_total_slice_set[i].insert(n + 1, c)
                        c = Compose(final_total_slice_set[i][n].begin_time, total_time[i][m], final_total_slice_set[i][n].state, final_total_slice_set[i][n].begin_guest_score, total_guest_score[i][m], final_total_slice_set[i][n].begin_host_score, total_host_score[i][m])
                        final_total_slice_set[i].insert(n + 1, c)
                        del final_total_slice_set[i][n]
                        break


def get_type():
    for i in range(0, len(final_total_slice_set)):
        piece = []  # 分片
        for k in range(0, len(final_total_slice_set[i])):
            t_type = -1
            state = final_total_slice_set[i][k].state
            # 焦灼
            if abs((final_total_slice_set[i][k].begin_host_score - final_total_slice_set[i][k].begin_guest_score) - (final_total_slice_set[i][k].end_host_score - final_total_slice_set[i][k].end_guest_score)) < anxious_value:
                t_type = 3
            elif state == 1:
                # 客队领先并扩大优势
                if final_total_slice_set[i][k].begin_host_score - final_total_slice_set[i][k].begin_guest_score >= threshold:
                    t_type = 0
                # 客队建立优势
                elif threshold >= final_total_slice_set[i][k].begin_host_score - final_total_slice_set[i][k].begin_guest_score > -threshold:
                    t_type = 1
                # 客队落后但缩小分差
                elif final_total_slice_set[i][k].begin_host_score - final_total_slice_set[i][k].begin_guest_score < -threshold:# and final_total_slice_set[i][k].end_host_score - final_total_slice_set[i][k].end_guest_score < threshold:
                    t_type = 2
            elif state == -1:
                # 主队领先并扩大优势
                if final_total_slice_set[i][k].begin_host_score - final_total_slice_set[i][k].begin_guest_score <= -threshold:
                    t_type = 4
                # 主队建立优势
                elif threshold >= final_total_slice_set[i][k].begin_host_score - final_total_slice_set[i][k].begin_guest_score > -threshold:
                    t_type = 5
                # 主队落后但缩小分差
                elif final_total_slice_set[i][k].begin_host_score - final_total_slice_set[i][k].begin_guest_score > threshold:# and final_total_slice_set[i][k].end_host_score - final_total_slice_set[i][k].end_guest_score >= 0:
                    t_type = 6
            match_piece = Piece(final_total_slice_set[i][k].begin_time, final_total_slice_set[i][k].end_time, t_type, final_total_slice_set[i][k].begin_host_score, final_total_slice_set[i][k].begin_guest_score, final_total_slice_set[i][k].end_host_score, final_total_slice_set[i][k].end_guest_score)
            piece.append(match_piece)
        total_piece.append(piece)


def divide_piece(records):
    mysql_query(records)
    get_derivative()
    data_fragmentation()
    data_compose()
    get_type()
    return total_piece


if __name__ == '__main__':
    records = grab_record(151595)
    total_piece = divide_piece(records)
    for q in total_piece:
        for p in q:
            print(p)
