def parse_log_header(log_file_lines, seperator=','):
    return log_file_lines[0].split(seperator)


def parse_log_data_line(input_string, header_fields, seperator=','):
    result = dict()
    values = input_string.split(seperator)
    for index in range(len(header_fields)):
        result[header_fields[index]] = values[index]
    return result
