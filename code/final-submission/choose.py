import json
import re

# 读取 JSON 文件
with open('./TAL_SAQ6K_EN_prediction_________________6_9_11_2_3_1_COT_1_vote_11_3_vote_11_2_vote_11_1_vote_4_vote_13_5_choose.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 遍历 JSONL 文件
jsonl_files = ['../cluster_answers/cluster_0_PAL/different_0_COT_PAL/different_0_COT_PAL_answers.jsonl', '../cluster_answers/cluster_0_PAL/cluster_0_PAL_answers.jsonl', '../cluster_answers/cluster_0_PAL/cluster_0_PAL_answers_enhanced.jsonl', '../cluster_answers/clusters_COT/cluster_0_answers.jsonl', '../cluster_answers/cluster_1_COT_PAL/cluster_1_COT_PAL_choose.jsonl', '../cluster_answers/cluster_1_PAL/cluster_1_PAL_answers_enhanced.jsonl', '../cluster_answers/cluster_1_PAL/cluster_1_PAL_answers.jsonl', '../cluster_answers/clusters_COT/cluster_1_answers.jsonl', '../cluster_answers/clusters_COT/cluster_2_answers.jsonl', '../cluster_answers/clusters_COT/cluster_3_answers.jsonl', '../cluster_answers/clusters_COT/cluster_4_answers.jsonl', '../cluster_answers/cluster_4_PAL/cluster_4_COT_PAL_choose.jsonl', '../cluster_answers/cluster_4_PAL/cluster_4_PAL_answers.jsonl', '../cluster_answers/cluster_5_PAL/cluster_5_COT_PAL_combine_choose.jsonl', '../cluster_answers/cluster_5_PAL/cluster_5_PAL_answers.jsonl', '../cluster_answers/clusters_COT/cluster_5_answers.jsonl', '../cluster_answers/clusters_COT/cluster_6_answers.jsonl', '../cluster_answers/cluster_6_COT_PAL/cluster_6_COT_PAL_choose.jsonl', '../cluster_answers/cluster_6_COT_PAL/cluster_6_PAL_answers.jsonl', '../cluster_answers/cluster_6_COT_PAL/cluster_6_PAL_answers_enhanced.jsonl', '../cluster_answers/clusters_COT/cluster_7_answers.jsonl',
               '../cluster_answers/clusters_COT/cluster_8_answers.jsonl', '../cluster_answers/clusters_COT/cluster_9_answers.jsonl', '../cluster_answers/cluster_9_PAL/cluster_9_PAL_answers.jsonl', '../cluster_answers/clusters_COT/cluster_10_answers.jsonl', '../cluster_answers/cluster_10_PAL/cluster_10_PAL_answers.jsonl', '../cluster_answers/clusters_COT/cluster_11_answers.jsonl', '../cluster_answers/difficulty_classification/problems_difficulty_2_PAL_enhanced.jsonl', '../cluster_answers/difficulty_classification/problems_difficulty_3_PAL_enhanced.jsonl', '../cluster_answers/difficulty_classification/problems_difficulty_2_PAL.jsonl', '../cluster_answers/difficulty_classification/problems_difficulty_3_PAL.jsonl', '../cluster_answers/cluster_11_1_COT_PAL/combine_11_1_COT_PAL.jsonl', '../cluster_answers/cluster_11_2_COT_PAL/cluster_11_2_COT_PAL.jsonl', '../cluster_answers/difficulty_classification/difficulty_submission/different_3_COT_PAL/cluster_11_difficulty_3_COT_PAL_answers.jsonl', '../cluster_answers/cluster_12_COT_PAL/cluster_12_COT_PAL.jsonl', '../cluster_answers/clusters_COT/cluster_12_answers.jsonl', '../cluster_answers/cluster_12_more_examples/cluster_12_more_examples_PAL.jsonl', '../cluster_answers/cluster_12_more_examples/cluster_12_more_examples_PAL_plus.jsonl', '../cluster_answers/cluster_13_PAL/cluster_13_PAL_answers.jsonl', '../cluster_answers/clusters_COT/cluster_13_answers.jsonl']  # JSONL 文件列表
# 打开文件以写入匹配的行和记录错误或未找到的 queId
with open('matched_lines.jsonl', 'w', encoding='utf-8') as output_file, \
        open('error_queIds.txt', 'w', encoding='utf-8') as error_file, \
        open('not_found_queIds.txt', 'w', encoding='utf-8') as not_found_file:

    for jsonl_file in jsonl_files:
        found_que_ids = set()  # 记录在当前文件中找到的 queId
        with open(jsonl_file, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    line_data = json.loads(line)
                    que_id = line_data.get('queId')
                    answer = str(line_data.get('answer'))

                    if que_id in data:
                        found_que_ids.add(que_id)  # 标记为找到的 queId
                        number_match = re.findall(
                            r"[-+]?\d*\.\d+|[-+]?\d+", answer)
                        if number_match:
                            try:
                                last_number = float(number_match[-1])
                                if last_number == float(data[que_id]):
                                    json.dump(line_data, output_file,
                                              ensure_ascii=False)
                                    output_file.write('\n')
                            except ValueError:
                                # 无法将字符串转换为浮点数时，记录该行的 queId
                                error_file.write(que_id + '\n')
                except json.JSONDecodeError:
                    # 解析 JSON 时发生错误，记录该行的 queId
                    if que_id:
                        error_file.write(que_id + '\n')

        # 检查哪些 queId 没有在当前文件中找到
        not_found_ids = set(data.keys()) - found_que_ids
        for que_id in not_found_ids:
            not_found_file.write(que_id + '\n')
