import json
from typing import List

def validate_answers_and_save_results(json_file_paths: List[str], results_file_path: str):
    total_count = 0
    correct_count = 0

    # Process each JSON file
    for json_file_path in json_file_paths:
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            for item in data.values():
                total_count += 1
                if item["answer"] == item["standard-answer"]:
                    correct_count += 1

        except json.JSONDecodeError as e:
            print(f"Error parsing JSON in {json_file_path}: {e}")
        except FileNotFoundError:
            print(f"File {json_file_path} not found.")
        except Exception as e:
            print(f"An unexpected error occurred in {json_file_path}: {e}")

    correct_rate = correct_count / total_count * 100 if total_count > 0 else 0

    # Write aggregated results to the results file
    try:
        with open(results_file_path, 'w', encoding='utf-8') as results_file:
            results_file.write(f"Total questions: {total_count}\n")
            results_file.write(f"Correct answers: {correct_count}\n")
            results_file.write(f"Accuracy rate: {correct_rate:.2f}%\n")

        print(f"Results have been saved to {results_file_path}")

    except Exception as e:
        print(f"An unexpected error occurred while writing results: {e}")

# List of JSON file paths
json_file_paths = [
    './calculate_accuracy/high/high_0.json',
    './calculate_accuracy/high/high_1.json',
    './calculate_accuracy/high/high_2.json'
]
# Specify the path for the results file
results_file_path = './calculate_accuracy/high/high_few_shot.txt'
validate_answers_and_save_results(json_file_paths, results_file_path)
