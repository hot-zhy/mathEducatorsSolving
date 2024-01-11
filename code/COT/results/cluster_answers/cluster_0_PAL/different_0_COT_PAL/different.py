import json

# 读取第一个 JSON 文件
with open('../cluster_0_PAL_answers_simply.json', 'r') as file:
    cot_data = json.load(file)

# 读取第二个 JSON 文件
with open('../../cluster_submission/cluster_0_submission.json', 'r') as file:
    pal_data = json.load(file)

# 找出不同的条目
differences = {}
for key in cot_data:
    # 将两个文件中的值都转换为字符串进行比较
    cot_value = str(cot_data[key])
    pal_value = str(pal_data.get(key, ""))  # 使用 get() 方法处理缺失的键

    # 比较并记录不同的条目
    if cot_value != pal_value:
        differences[key] = {"COT": cot_value, "PAL": pal_value}

# 将不同的条目保存到新的 JSON 文件
differences_file_path = './different_0_COT_PAL.json'
with open(differences_file_path, 'w') as file:
    json.dump(differences, file, indent=4)
