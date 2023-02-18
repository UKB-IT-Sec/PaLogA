import pytest
from modules.pseudomize import delete_data_in_fields, pseudomize_ip


def test_delete_data_in_fileds():
    test_list = ['a', 'b', 'c']
    result = delete_data_in_fields(test_list, [0, 2])
    assert result[0] == ''
    assert result[1] == 'b'
    assert result[2] == ''


@pytest.mark.parametrize('input_data, salt, expected', [
    ('1.1.1.1', 0, '1.1.1.1'),
    ('2.2.2.2', 1, '2.2.3.3'),
    ('192.168.254.254', 3, '192.168.1.1')
])
def test_pseudomize_ip(input_data, salt, expected):
    assert pseudomize_ip(input_data, salt) == expected
