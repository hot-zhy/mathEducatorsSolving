import json

for i in range(14):
    # 读取1.json
    with open('../../submission/TAL_SAQ6K_EN_prediction.json', 'r') as file:
        data1 = json.load(file)

    # 读取2.jsonl
    with open(f'../extracted_answers/cluster_{i}_answers_temp.json', 'r') as file:
        data2 = json.load(file)

    # 处理和组合数据
    combined_data = {}
    for queId in data2:
        if queId in data1:
            # 组合数据，以 queId 作为键
            combined_data[queId] = data1[queId]  # 获取对应的answer

    # 将组合后的数据保存到3.json
    with open(f'cluster_{i}_submission.json', 'w') as file:
        json.dump(combined_data, file, indent=4)
