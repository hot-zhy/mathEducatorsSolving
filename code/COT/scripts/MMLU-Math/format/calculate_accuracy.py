import json

def validate_answers_and_save_results(json_file_path, results_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        total_count = 0
        correct_count = 0

        for item in data.values():
            total_count += 1
            if item["answer"] == item["standard-answer"]:
                correct_count += 1

        correct_rate = correct_count / total_count * 100

        with open(results_file_path, 'w', encoding='utf-8') as results_file:
            results_file.write(f"Total questions: {total_count}\n")
            results_file.write(f"Correct answers: {correct_count}\n")
            results_file.write(f"Accuracy rate: {correct_rate:.2f}%\n")

        print(f"Results have been saved to {results_file_path}")

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except FileNotFoundError:
        print(f"File {json_file_path} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Replace 'data.json' with the path to your actual JSON file
json_file_path = './calculate_accuracy/high_school_mathematics_test.json'
# Specify the path for the results file
results_file_path = './calculate_accuracy/high_school.txt'
validate_answers_and_save_results(json_file_path, results_file_path)
