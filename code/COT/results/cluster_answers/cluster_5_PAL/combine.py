import json

# 读取2.jsonl的内容，建立一个字典，以queId作为键，存储对应的answer和generation
pal_data = {}
with open('./different_5_PAL_answers.jsonl', 'r', encoding='utf-8') as f2:
    for line in f2:
        try:
            data = json.loads(line)
            queId = data.get('queId')
            if queId:
                pal_data[queId] = {
                    'pal_answer': data.get('answer'),
                    'pal_generation': data.get('generation')
                }
        except json.JSONDecodeError as e:
            print(e)
            print(queId)

# 遍历1.jsonl的内容，修改数据并写入3.jsonl
with open('./different_5_COT_answers.jsonl', 'r', encoding='utf-8') as f1, open('./cluster_5_COT_PAL_combine_answers.jsonl', 'w', encoding='utf-8') as f3:
    for line in f1:
        data = json.loads(line)
        queId = data.get('queId')
        if queId in pal_data:
            data['cot_answer'] = data.get('answer')
            data['cot_generation'] = data.get('generation')
            data['pal_answer'] = pal_data[queId]['pal_answer']
            data['pal_generation'] = pal_data[queId]['pal_generation']
            data.pop('answer', None)
            data.pop('generation', None)
        # 写入修改后的数据到3.jsonl
        f3.write(json.dumps(data, ensure_ascii=False) + '\n')
