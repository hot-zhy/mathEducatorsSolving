"""
找到生成的答案中末尾是@的，即这道题更适合用PAL的
"""
import json

# 创建一个列表来保存符合条件的 JSON 对象
filtered_json_objects = []

# 循环处理从 cluster_0 到 cluster_13 的文件
for i in range(14):
    file_name = f'../cluster_{i}_answers.jsonl'
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                json_obj = json.loads(line)
                queId = json_obj.get('queId')
                answer = json_obj.get('answer')
                # 检查 JSON 对象中是否有至少一个符合条件的键值对
                if queId is not None and answer is not None and any(isinstance(value, str) and value.rstrip().endswith('@') for value in json_obj.values()):
                    filtered_json_objects.append(json_obj)  # 保存整个 JSON 对象
            except json.JSONDecodeError as e:
                print("Error in file:", file_name, "Error:", e)
                print(queId)

# 将筛选后的数据写入新的 JSONL 文件
with open('../filtered_data.jsonl', 'w', encoding='utf-8') as new_file:
    for json_obj in filtered_json_objects:
        json.dump(json_obj, new_file, ensure_ascii=False)
        new_file.write('\n')
