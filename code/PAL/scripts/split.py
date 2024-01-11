import json


def split_jsonl_file(input_file_path, output_file_base, num_files=5):
    # Count the total number of lines in the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        total_lines = sum(1 for _ in file)

    # Calculate the number of lines per file
    lines_per_file = total_lines // num_files
    extra_lines = total_lines % num_files

    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        for i in range(num_files):
            with open(f'{output_file_base}_{i+1}.jsonl', 'w', encoding='utf-8') as output_file:
                for j in range(lines_per_file):
                    line = input_file.readline()
                    if not line:
                        break
                    output_file.write(line)

                # Write extra line for the first 'extra_lines' files
                if i < extra_lines:
                    line = input_file.readline()
                    if line:
                        output_file.write(line)


# Example usage
# Replace with your actual input file path
input_file = './combined_filtered.jsonl'
output_file_base = 'output_file'  # Base name for output files
split_jsonl_file(input_file, output_file_base)
