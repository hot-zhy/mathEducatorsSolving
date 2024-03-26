import csv
import json

# 输入CSV文件名
input_csv_file = '../../../../dataset/data/test/elementary_mathematics_test.csv'

# 输出JSON文件名
output_json_file = '../../../../dataset/data/elementary_mathematics_test.json'

# 初始化一个空列表，用于存储转换后的数据
data = []

# 打开CSV文件并读取数据
with open(input_csv_file, mode='r', encoding='utf-8') as csv_file:
    # CSV阅读器，这里我们直接按行读取，因为列的含义是固定的
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        # 解析每行的数据，并构建相应的字典
        question_data = {
            "problem": row[0],
            "options": row[1:5],  # 选项是从第二个到第五个元素
            "answer": row[5]      # 正确答案的索引
        }
        # 将问题数据添加到列表中
        data.append(question_data)

# 将数据转换为JSON格式，并写入文件
with open(output_json_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"CSV数据已成功转换为JSON，并保存至'{output_json_file}'。")