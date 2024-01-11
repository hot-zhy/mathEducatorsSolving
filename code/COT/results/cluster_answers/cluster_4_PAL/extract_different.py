import json

# Load the JSON file
with open('./cluster_4_COT_PAL/different_4_COT_PAL.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract queIDs
que_ids = set(data.keys())

# Initialize a list to store the corresponding lines
selected_lines = []

# Open and read the JSONL file
with open('./cluster_4_COT_PAL_combine_answers.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        line_data = json.loads(line)
        # Assuming each line in JSONL has an ID field
        if line_data['queId'] in que_ids:
            selected_lines.append(line_data)

# Write the selected lines to a new JSONL file
with open('./cluster_4_COT_PAL/different_cluster_4_COT_PAL.jsonl', 'w', encoding='utf-8') as file:
    for line in selected_lines:
        json.dump(line, file)
        file.write('\n')  # Write a newline character after each JSON object

# The selected lines are now saved in 'output_jsonl_file.jsonl'
