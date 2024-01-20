import pandas as pd
import copy

data_total = pd.read_excel('./各区分段统计1.xlsx', sheet_name='Sheet1')
data_die = pd.read_excel('./各区死亡率统计1.xlsx', sheet_name='Sheet1')
data_born = pd.read_excel('./生育率1.xlsx', sheet_name='Sheet1')
data_total.fillna(0)
data_die.fillna(0)
data_born.fillna(0)

TIME_GAP = 5

t_year_list = {}
m_year_list = {}
w_year_list = {}

col_total_l = data_total.columns.tolist()

for area_index in range(0, 17):
    for col_index in range(1, 64):
        if (col_index - 1) % 3 == 0:
            if 2020 not in t_year_list:
                t_year_list[2020] = {}
            if data_total.iat[area_index, 0].strip() not in t_year_list[2020]:
                t_year_list[2020][data_total.iat[area_index, 0].strip()] = {}
            t_year_list[2020][data_total.iat[area_index, 0].strip()][col_total_l[col_index]] = data_total.iat[
                area_index, col_index]
        elif (col_index - 1) % 3 == 1:
            if 2020 not in m_year_list:
                m_year_list[2020] = {}
            if data_total.iat[area_index, 0].strip() not in m_year_list[2020]:
                m_year_list[2020][data_total.iat[area_index, 0].strip()] = {}
            m_year_list[2020][data_total.iat[area_index, 0].strip()][col_total_l[col_index - 1]] = data_total.iat[
                area_index, col_index]
        elif (col_index - 1) % 3 == 2:
            if 2020 not in w_year_list:
                w_year_list[2020] = {}
            if data_total.iat[area_index, 0].strip() not in w_year_list[2020]:
                w_year_list[2020][data_total.iat[area_index, 0].strip()] = {}
            w_year_list[2020][data_total.iat[area_index, 0].strip()][col_total_l[col_index - 2]] = data_total.iat[
                area_index, col_index]
# print(t_year_list)
# print(m_year_list)
# print(w_year_list)

t_die = {}
m_die = {}
w_die = {}
col_die_l = data_die.columns.tolist()
# print(col_die_l)
for area_index in range(0, 17):
    for col_index in range(1, 64):
        if (col_index - 1) % 3 == 0:
            if data_die.iat[area_index, 0].strip() not in t_die:
                t_die[data_die.iat[area_index, 0].strip()] = {}
            t_die[data_die.iat[area_index, 0].strip()][col_die_l[col_index]] = data_die.iat[area_index, col_index]/1000
        elif (col_index - 1) % 3 == 1:
            if data_die.iat[area_index, 0].strip() not in m_die:
                m_die[data_die.iat[area_index, 0].strip()] = {}
            m_die[data_die.iat[area_index, 0].strip()][col_die_l[col_index - 1]] = data_die.iat[area_index, col_index]/1000
        elif (col_index - 1) % 3 == 2:
            if data_die.iat[area_index, 0].strip() not in w_die:
                w_die[data_die.iat[area_index, 0].strip()] = {}
            w_die[data_die.iat[area_index, 0].strip()][col_die_l[col_index - 2]] = data_die.iat[area_index, col_index]/1000
# print(t_die)
# print(m_die)
# print(w_die)


born_rate_dict = {}
col_born_l = data_born.columns.tolist()
for area_index in range(0, 17):
    for col_index in range(1, 8):
        if data_born.iat[area_index, 0].strip() not in born_rate_dict:
            born_rate_dict[data_born.iat[area_index, 0].strip()] = {}
        born_rate_dict[data_born.iat[area_index, 0].strip()][col_born_l[col_index]] = data_born.iat[
            area_index, col_index] / 1000
# print(born_rate_dict)


def this5year_num(last_num, last_die_rate, this_die_rate):
    this_num = 0
    per_year_num = last_num/5
    this_num += per_year_num * ((1 - last_die_rate) ** 1) * ((1 - this_die_rate) ** 4)
    this_num += per_year_num * ((1 - last_die_rate) ** 2) * ((1 - this_die_rate) ** 3)
    this_num += per_year_num * ((1 - last_die_rate) ** 3) * ((1 - this_die_rate) ** 2)
    this_num += per_year_num * ((1 - last_die_rate) ** 4) * ((1 - this_die_rate) ** 1)
    this_num += per_year_num * ((1 - last_die_rate) ** 5) * ((1 - this_die_rate) ** 0)
    return this_num


def make_new_num(year):
    for area, w_area_datas in w_year_list[year].items():
        last_born_per5year = -1
        last_born_rate = -1
        girl_rate = 100 / (100 + sex_rate[area])
        boy_rate = sex_rate[area] / (100 + sex_rate[area])
        new_t_num = 0
        new_w_num = 0
        new_m_num = 0
        for born_per5year, born_rate in born_rate_dict[area].items():  # born_per5year:育龄的每一段(eg:15-19岁)
            if born_per5year == '15-19岁':
                pass
            elif born_per5year == '45-49岁':
                last_peryear_num = w_area_datas[last_born_per5year] / 5.0
                new_t_num += last_peryear_num * (last_born_rate * 15)
                new_w_num += last_peryear_num * (last_born_rate * 15) * girl_rate
                new_m_num += last_peryear_num * (last_born_rate * 15) * boy_rate
            else:
                last_peryear_num = w_area_datas[last_born_per5year] / 5.0
                new_t_num += last_peryear_num * (last_born_rate * 15 + born_rate * 10)
                new_w_num += last_peryear_num * (last_born_rate * 15 + born_rate * 10) * girl_rate
                new_m_num += last_peryear_num * (last_born_rate * 15 + born_rate * 10) * boy_rate
            last_born_per5year = born_per5year
            last_born_rate = born_rate
        t_year_list[year][area]['0-4岁'] = new_t_num
        m_year_list[year][area]['0-4岁'] = new_m_num
        w_year_list[year][area]['0-4岁'] = new_w_num
sex_rate = {
    '总计': 109.12,
    '黄浦区': 108.14,
    '徐汇区': 116.81,
    '长宁区': 124.82,
    '静安区': 103.55,
    '普陀区': 116.02,
    '虹口区': 119.29,
    '杨浦区': 120.41,
    '闵行区': 110.94,
    '宝山区': 106.46,
    '嘉定区': 109.52,
    '浦东新区': 110.96,
    '金山区': 96.58,
    '松江区': 107.59,
    '青浦区': 97.79,
    '奉贤区': 110.31,
    '崇明区': 83.18
}
for year in range(2020, 2051, 5):
    # 女
    last_w_year_list = copy.deepcopy(w_year_list)
    if year in last_w_year_list:
        continue
    last_year = year - 5
    last_year_data = last_w_year_list[last_year]
    new_year_data = {}
    for area, area_datas in last_year_data.items():
        last_per5year_num = -1
        last_die_rate = -1
        new_year_data[area] = {}
        new_num = 0  # 新增人口
        for per5year, num in area_datas.items():
            die_rate = w_die[area][per5year]
            if last_per5year_num == -1:  # 0~4岁
               new_year_data[area][per5year] = 0
            else:
                new_year_data[area][per5year] = this5year_num(last_per5year_num, last_die_rate, die_rate)
            last_per5year_num = num
            last_die_rate = die_rate
    w_year_list.update({year: new_year_data})

    # 总共
    last_t_year_list = copy.deepcopy(t_year_list)
    if year in last_t_year_list:
        continue
    last_year = year - 5
    last_year_data = last_t_year_list[last_year]
    new_year_data = {}
    for area, area_datas in last_year_data.items():
        last_per5year_num = -1
        last_die_rate = -1
        new_year_data[area] = {}
        for per5year, num in area_datas.items():

            die_rate = t_die[area][per5year]
            if last_per5year_num == -1:  # 0~4岁
                new_year_data[area][per5year] = 0
            else:
                new_year_data[area][per5year] = this5year_num(last_per5year_num, last_die_rate, die_rate)
            last_per5year_num = num
            last_die_rate = die_rate
    t_year_list.update({year: new_year_data})

    # 男
    last_m_year_list = copy.deepcopy(m_year_list)
    if year in last_m_year_list:
        continue
    last_year = year - 5
    last_year_data = last_m_year_list[last_year]
    new_year_data = {}
    for area, area_datas in last_year_data.items():
        last_per5year_num = -1
        last_die_rate = -1
        boy_rate = sex_rate[area] / (100 + sex_rate[area])
        new_year_data[area] = {}
        for per5year, num in area_datas.items():
            die_rate = m_die[area][per5year]
            if last_per5year_num == -1:  # 0~4岁
                new_year_data[area][per5year] = 0
            else:
                new_year_data[area][per5year] = this5year_num(last_per5year_num, last_die_rate, die_rate)
            last_per5year_num = num
            last_die_rate = die_rate
    m_year_list.update({year: new_year_data})

    #计算男、女、总0~4岁人数（新生儿人数）
    make_new_num(year)

def to_int(year_list):
    new_year_list = copy.deepcopy(year_list)
    for year, year_data in year_list.items():
        for area, area_data in year_data.items():
            for per5year,num in area_data.items():
                new_year_list[year][area][per5year] = int(num)
    return new_year_list
print("2025年总：" + str(to_int(t_year_list)[2025]))
print("2025年男：" + str(to_int(m_year_list)[2025]))
print("2025年女：" + str(to_int(w_year_list)[2025]))
print("2030年总：" + str(to_int(t_year_list)[2030]))
print("2030年男：" + str(to_int(m_year_list)[2030]))
print("2030年女：" + str(to_int(w_year_list)[2030]))
print("2035年总：" + str(to_int(t_year_list)[2035]))
print("2035年男：" + str(to_int(m_year_list)[2035]))
print("2035年女：" + str(to_int(w_year_list)[2035]))
print("2040年总：" + str(to_int(t_year_list)[2040]))
print("2040年男：" + str(to_int(m_year_list)[2040]))
print("2040年女：" + str(to_int(w_year_list)[2040]))
print("2045年总：" + str(to_int(t_year_list)[2045]))
print("2045年男：" + str(to_int(m_year_list)[2045]))
print("2045年女：" + str(to_int(w_year_list)[2045]))
print("2050年总：" + str(to_int(t_year_list)[2050]))
print("2050年男：" + str(to_int(m_year_list)[2050]))
print("2050年女：" + str(to_int(w_year_list)[2050]))


