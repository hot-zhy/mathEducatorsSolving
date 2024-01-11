import json

# 读取 JSON 文件，这里假设文件名为 'data.json'
with open('./different_5_COT_PAL.json', 'r') as file:
    json_data = json.load(file)

# 获取 JSON 文件中的所有键
json_keys = json_data.keys()

# 初始化一个空列表用于存储匹配到的 JSONL 行
matched_lines = []

# 读取并处理 JSONL 文件，这里假设文件名为 'data.jsonl'
with open('../../cluster_answers/clusters_COT/cluster_5_answers.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        jsonl_data = json.loads(line)
        # 检查 JSONL 行中的 'queId' 是否在 JSON 文件的键中
        if jsonl_data['queId'] in json_keys:
            matched_lines.append(jsonl_data)

# 将匹配到的 JSONL 行保存到新的 JSONL 文件中，这里假设文件名为 'matched_data.jsonl'
with open('./different_5_COT_answers.jsonl', 'w') as file:
    for line in matched_lines:
        json.dump(line, file)
        file.write('\n')
