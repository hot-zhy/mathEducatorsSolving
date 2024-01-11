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
file_paths = ["./cluster_13_PAL_answers_simpy.json", "../cluster_submission/cluster_13_submission.json",
              "../../pal/better_pal_questions_PAL.json"]

# 统计投票结果
result = count_votes(file_paths)

output_path = './cluster_13_vote.json'
with open(output_path, 'w') as output_file:
    json.dump(result, output_file, indent=4)
