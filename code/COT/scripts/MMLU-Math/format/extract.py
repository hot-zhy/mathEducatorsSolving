import json
import re


def convert_jsonl_to_json(jsonl_file_path, json_file_path):
    result = {}
    with open(jsonl_file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                data = json.loads(line, strict=False)
                problem = data.get('problem')
                answer = data.get('answer')
                standard = data.get('standard-answer')
                options=data.get('options')
                # answer = str(answer)

                answer_match = re.search(r'Answer:\s*(.*)', answer)
                if answer_match:
                     answer = answer_match.group(1)
                # number_match = re.findall(
                #     r"[-+]?\d*\.\d+|[-+]?\d+", answer)
                # if number_match:
                #     answer = float(number_match[-1])
                #     result[queId] = answer
                # else:
                #     number_match = re.findall(
                #         r"[-+]?\d*\.\d+|[-+]?\d+", answer)
                #     if number_match:
                #         answer = float(number_match[-1])
                result[line_number] = {
                    'problem':problem,
                    'answer':answer,
                    'options':options,
                    'standard-answer':standard
                }
            except json.JSONDecodeError as e:
                print(e)

    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


for i in range(3):
    convert_jsonl_to_json(
    f'../results/few-shot/high/high_{i}_answers.jsonl', f'./calculate_accuracy/high/high_{i}.json')
