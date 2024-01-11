import json


file_names = ["./chinese-1-answers-submission.json",
              "./chinese-2-answers-submission.json",
              "./chinese-3-answers-submission.json",
              "./chinese-4-answers-submission.json",
              "./chinese-5-answers-submission.json",
              "./chinese-6-answers-submission.json",
              "./chinese-7-answers-submission.json",
              "./chinese-8-answers-submission.json",
              "./chinese-9-answers-submission.json",
              "./chinese-10-answers-submission.json",
              "./chinese-11-answers-submission.json",
              "./chinese-answers-submission.json",
              ]

merged_data = {}

for file_name in file_names:
    with open(file_name, 'r') as file:
        data = json.load(file)
        merged_data.update(data)  # 后来的文件覆盖之前的键值对


with open('../submission/TAL_SAQ7K_CN_prediction.json', 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=4)
