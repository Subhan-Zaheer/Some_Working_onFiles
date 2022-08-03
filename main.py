import os


def parse_header(header_line):
    header = header_line.strip().split(',')
    return header


def parse_values(values):
    parsed_val = values.strip().split(',')
    return parsed_val


def creating_dict(values, headers):
    dict1 = {}
    for v, h in zip(values, headers):
        zip(values, headers)
        if v != '':
            dict1[h] = float(v)
        else:
            dict1[h] = 0.0
    return dict1


def read_csv_file(path):
    # Opening file with given path in read mode.
    file = open(path, 'r')
    # Reading lines from files from readlines() to parse them later.
    file_lines = file.readlines()
    # Parsing header
    header = parse_header(file_lines[0])
    # A list for having all records of dictionary.
    result = []
    # Loop for parsing values except header as we have parsed it above.
    for items in file_lines:
        # If statement for header
        if items == file_lines[0]:
            continue
        # Parsing values
        value = parse_values(items)
        # Creating dict of values and headers
        f_dict = creating_dict(value, header)
        # Appending all dictionaries in a list.
        result.append(f_dict)
    for items in result:
        print(items)


if __name__ == '__main__':
    read_csv_file(os.getcwd()+"\\file.txt")

