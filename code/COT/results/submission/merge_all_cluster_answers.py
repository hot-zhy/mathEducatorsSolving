import json


file_names = ["../cluster_0_answers_temp.json",
              "../cluster_1_answers_temp.json",
              "../cluster_2_answers_temp.json",
              "../cluster_3_answers_temp.json",
              "../cluster_4_answers_temp.json",
              "../cluster_5_answers_temp.json",
              "../cluster_6_answers_temp.json",
              "../cluster_7_answers_temp.json",
              "../cluster_8_answers_temp.json",
              "../cluster_9_answers_temp.json",
              "../cluster_10_answers_temp.json",
              "../cluster_11_answers_temp.json",
              "../cluster_12_answers_temp.json",
              "../cluster_13_answers_temp.json",
              ]

merged_data = {}

for file_name in file_names:
    with open(file_name, 'r') as file:
        data = json.load(file)
        merged_data.update(data)  # 后来的文件覆盖之前的键值对


with open('../submission/TAL_SAQ6K_EN_prediction.json', 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=4)
