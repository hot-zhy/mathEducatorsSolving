import json

jsonl_input_file = '../../../PAL/results/no_answer_problems_answers.jsonl'
json_data = {}

with open(jsonl_input_file, 'r', encoding='utf-8') as jsonl_file:
    for line in jsonl_file:
        try:
            json_object = json.loads(line)
            que_id = json_object['queId']
            answer = json_object['answer']
            if que_id is not None and answer is not None:
                json_data[que_id] = answer
        except json.JSONDecodeError as e:
            print(que_id)

json_file_path = '../../../COT/results/no_answer_problems_answers_extract.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)
