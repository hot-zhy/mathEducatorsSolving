import json


def extract_difficulty_one(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
            open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            try:
                data = json.loads(line)
                # Check if 'difficulty' is 1
                if data.get('difficulty') == "3":
                    json.dump(data, output_file, ensure_ascii=False)
                    output_file.write('\n')
            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e}")


# Example usage
# Replace with your actual input file path
input_file = '../all.jsonl'
output_file = '../difficulty_3.jsonl'  # Output file path
extract_difficulty_one(input_file, output_file)
