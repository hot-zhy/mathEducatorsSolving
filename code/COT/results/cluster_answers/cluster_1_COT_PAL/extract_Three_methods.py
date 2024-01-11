import json
import re

# 读取原始 JSONL 文件
with open('./cluster_1_COT_PAL_choose.jsonl', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 处理数据
processed_data = []
for line in lines:
    try:
        # 解析 JSON 数据
        data = json.loads(line)

        # 这里进行数据提取或变换操作
        # 例如: processed_data.append({'new_key': data['old_key']})
        cot_answer = data['cot_answer']
        number_match = re.findall(
            r"[-+]?\d*\.\d+|[-+]?\d+", cot_answer)
        cot_answer = float(number_match[-1])
        choose_answer = data['choose-answer']
        number2_match = re.findall(
            r"[-+]?\d*\.\d+|[-+]?\d+", choose_answer)
        choose_answer = float(number2_match[-1])

        if data['pal_answer'] == "":
            pal_answer = str(data['pal_generation'])
            number3_match = re.findall(
                r"[-+]?\d*\.\d+|[-+]?\d+", pal_answer)
            if number3_match:
                pal_answer = float(number3_match[-1])
        else:
            pal_answer = data['pal_answer']

        data = {
            'queId': data['queId'],
            'problem': data['problem'],
            'pal_answer': pal_answer,
            'cot_answer': cot_answer,
            'choose_answer': choose_answer
        }
        processed_data.append(data)  # 示例中只是简单地复制数据
    except ValueError:
        print('error')

# 写入新的 JSONL 文件
with open('new.jsonl', 'w') as file:
    for item in processed_data:
        file.write(json.dumps(item) + '\n')
