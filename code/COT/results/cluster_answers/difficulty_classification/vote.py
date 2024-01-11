import json


def count_votes(file_paths):
    votes = {}

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for key, value in data.items():
                if key not in votes:
                    votes[key] = {}
                if value not in votes[key]:
                    votes[key][value] = 0
                votes[key][value] += 1

    winners = {}
    for key, value in votes.items():
        max_votes = max(value.values())
        winners[key] = [option for option,
                        count in value.items() if count == max_votes][0]

    return winners


# 三个json文件的路径
file_paths = ["./difficulty_submission/different_3_COT_PAL/cluster_11_difficulty_3_COT_PAL_answers_simply.json", "./problems_difficulty_3_PAL_enhanced_simpy.json",
              "./difficulty_submission/problems_difficulty_3_PAL.json", "./difficulty_submission/problems_difficulty_3_COT.json"]

# 统计投票结果
result = count_votes(file_paths)

output_path = './cluster_1_vote.json'
with open(output_path, 'w') as output_file:
    json.dump(result, output_file, indent=4)
