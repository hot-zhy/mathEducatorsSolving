import json


def filter_jsonl_files(input_file_paths, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for input_file_path in input_file_paths:
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                for line_number, line in enumerate(input_file, start=1):
                    try:
                        data = json.loads(line, strict=False)
                        answer = data.get('answer', '')

                        # Write the line to the output file if it does not contain 'Final answer:'
                        if "Final answer:" not in answer:
                            output_file.write(line)
                    except json.JSONDecodeError as e:
                        print(
                            f"JSON decoding error in file {input_file_path} at line {line_number}: {e}")


# List of input JSONL files
# Replace with your actual file paths
input_files = ['./chinese-1-answers.jsonl',
               './chinese-2-answers.jsonl',
               './chinese-3-answers.jsonl',
               './chinese-4-answers.jsonl',
               './chinese-5-answers.jsonl',
               './chinese-6-answers.jsonl',
               './chinese-7-answers.jsonl',
               './chinese-8-answers.jsonl',
               './chinese-9-answers.jsonl',
               './chinese-10-answers.jsonl',
               './chinese-11-answers.jsonl',
               './chinese-answers.jsonl',

               ]

# Output JSONL file
output_file = './combined_filtered.jsonl'

# Call the function
filter_jsonl_files(input_files, output_file)
