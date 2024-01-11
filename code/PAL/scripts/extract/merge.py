import json


with open('../../../submission/TAL_SAQ6K_EN_prediction.json', 'r', encoding='utf-8') as file:
    test1_data = json.load(file)


with open('../scripts/eval_results/arithmetic_answer.json', 'r', encoding='utf-8') as file:
    test2_data = json.load(file)


for key, value in test2_data.items():
    if key in test1_data:
        test1_data[key] = value

with open('../scripts/eval_results/merge.json', 'w', encoding='utf-8') as file:
    json.dump(test1_data, file, indent=4)
