import json


def filter_jsonl_by_difficulty(input_file, output_file, difficulty_level):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # 将行转换为JSON对象
            data = json.loads(line)
            # 检查difficulty的值
            if data.get('difficulty') == difficulty_level:
                # 将符合条件的行写入新文件
                json.dump(data, outfile)
                outfile.write('\n')


# 使用函数
input_file = '../../../../classification/KMeans/KMeanscluster_11.jsonl'  # 替换为你的原始文件路径
output_file = './problems_difficulty_0.jsonl'  # 替换为你想保存的新文件路径
filter_jsonl_by_difficulty(input_file, output_file, "0")
