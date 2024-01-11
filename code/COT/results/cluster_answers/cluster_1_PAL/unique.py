import json


def deduplicate_jsonl_by_queid(jsonl_path, output_jsonl_path):
    seen_que_ids = set()
    unique_lines = []

    # 读取 JSONL 文件
    with open(jsonl_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                data = json.loads(line)
                que_id = data.get('queId')
                if que_id not in seen_que_ids:
                    seen_que_ids.add(que_id)
                    unique_lines.append(line)
            except json.JSONDecodeError:
                print(f"Error decoding JSON on line: {line}")
                continue

    # 将去重后的行写入新的 JSONL 文件
    with open(output_jsonl_path, 'w', encoding='utf-8') as output_file:
        for line in unique_lines:
            output_file.write(line)


# 调用函数进行去重
jsonl_path = './matched_lines.jsonl'
output_jsonl_path = './cluster_1_vote.jsonl'
deduplicate_jsonl_by_queid(jsonl_path, output_jsonl_path)
