import json

# 读取 unique_queIds.txt 文件，将 queId 存储到集合中
unique_que_ids = set()
with open('unique_queIds.txt', 'r', encoding='utf-8') as file:
    for line in file:
        unique_que_ids.add(line.strip())

# JSONL 文件路径
jsonl_file_path = '../../../../dataset/AAAI/TAL-SAQ6K-EN.jsonl'

# 读取 JSONL 文件，并检查每一行
with open(jsonl_file_path, 'r', encoding='utf-8') as input_file, open('../cluster_answers/possible_no_answer/possible_no_answer.jsonl', 'w', encoding='utf-8') as output_file:
    for line in input_file:
        try:
            line_data = json.loads(line)
            que_id = line_data.get('queId')
            if que_id in unique_que_ids:
                json.dump(line_data, output_file)
                output_file.write('\n')
        except json.JSONDecodeError:
            continue
