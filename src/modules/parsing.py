def parse_log_header(log_header_line: list, seperator: str = ','):
    return log_header_line.split(seperator)


def parse_log_data_line(input_data: str, header_fields: list, seperator: str = ',') -> str:
    result = dict()
    values = input_data.split(seperator)
    for index in range(len(header_fields)):
        result[header_fields[index]] = values[index]
    return result


def parse_log_data(input_data: list, seperator: str = ',') -> list:
    header_fields = parse_log_header(input_data[0], seperator=seperator)
    result = list()
    for log_data_line in input_data[1:]:
        result.append(parse_log_data_line(log_data_line, header_fields, seperator=seperator))
    return result
