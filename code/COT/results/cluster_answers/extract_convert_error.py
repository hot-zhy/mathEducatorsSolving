import json


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def is_float(value):
    # 如果值是列表，直接返回False
    if isinstance(value, list):
        return False
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def filter_non_floats(json_data):
    non_floats = {}
    for key, value in json_data.items():
        if not isinstance(value, float) and not is_float(value):
            non_floats[key] = value
    return non_floats


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    for i in range(14):
        input_file = f'../cluster_answers/cluster_submission/cluster_{i}_submission.json'
        output_file = f'../cluster_answers/cluster_convert_error/cluster_{i}_convert_error.json'
        json_data = read_json(input_file)
        non_floats = filter_non_floats(json_data)
        save_json(non_floats, output_file)


if __name__ == "__main__":
    main()
