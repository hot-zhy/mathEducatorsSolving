import json

# 读取第一个 JSON 文件
with open('./cluster_5_PAL_answers_simpy.json', 'r') as file:
    cot_data = json.load(file)

# 读取第二个 JSON 文件
with open('../cluster_submission/cluster_5_submission.json', 'r') as file:
    pal_data = json.load(file)

# 找出不同的条目
differences = {}
for key in cot_data:
    # 尝试将值转换为浮点数，如果不成功，则保留原始字符串形式
    try:
        cot_value = float(str(cot_data[key]))
    except ValueError:
        cot_value = str(cot_data[key])

    try:
        pal_value = float(str(pal_data.get(key, "")))
    except ValueError:
        pal_value = str(pal_data.get(key, ""))

    # 比较并记录不同的条目
    if cot_value != pal_value:
        differences[key] = {"COT": str(cot_value), "PAL": str(pal_value)}


# 将不同的条目保存到新的 JSON 文件
differences_file_path = './different_5_COT_PAL.json'
with open(differences_file_path, 'w') as file:
    json.dump(differences, file, indent=4)
