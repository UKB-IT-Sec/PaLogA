from modules.parsing import parse_log_header, parse_log_data_line,\
    parse_log_data

TEST_LOG_LINES_INCLUDING_HEADER = ['First Value,Second Value,Third Value', '1,2,3', '1a,2a,3a']
PARSED_LOG_HEADER = ['First Value', 'Second Value', 'Third Value']


def test_parse_log_header():
    result = parse_log_header(TEST_LOG_LINES_INCLUDING_HEADER[0])
    assert result == PARSED_LOG_HEADER


def test_parse_log_data_line():
    result = parse_log_data_line('1,2,3', PARSED_LOG_HEADER)
    assert result['First Value'] == '1'
    assert result['Second Value'] == '2'
    assert result['Third Value'] == '3'


def test_parse_log_data():
    result = parse_log_data(TEST_LOG_LINES_INCLUDING_HEADER)
    assert type(result) == list
    assert len(result) == 2
    assert result[0]['First Value'] == '1'
    assert result[1]['Third Value'] == '3a'
