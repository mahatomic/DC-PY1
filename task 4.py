import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter=",") -> list[dict]:
    with open(file) as f:
        headlines_str = f.readline()
        headlines_list = headlines_str.rstrip().split(delimiter)

        list_dict = []
        for string in f:
            val = string.rstrip().split(delimiter)
            dict_ = {key: value for key, value in zip(headlines_list, val)}
            list_dict.append(dict_)

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
