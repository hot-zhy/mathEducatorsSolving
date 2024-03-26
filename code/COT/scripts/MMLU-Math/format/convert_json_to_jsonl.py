import json

# JSON 文件路径
json_file_path = '../../../../dataset/data/abstract_algebra_test.json'
# JSONL 文件的目标路径
jsonl_file_path = '../../../../dataset/data/abstract_algebra_test.jsonl'

try:
    # 读取 JSON 文件
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)  # 假设 JSON 文件中是一个对象数组

    # 写入 JSONL 文件
    with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
        for item in data:
            json_line = json.dumps(item,ensure_ascii=False)  # 将对象转换为 JSON 字符串
            jsonl_file.write(json_line + '\n')  # 写入一行

    print(f"JSON 文件已成功转换为 JSONL，并保存至 '{jsonl_file_path}'。")
except json.JSONDecodeError as e:
    print(f"解析 JSON 时出错：{e}")
except FileNotFoundError:
    print(f"找不到文件：{json_file_path}")
except Exception as e:
    print(f"发生了未预期的错误：{e}")
