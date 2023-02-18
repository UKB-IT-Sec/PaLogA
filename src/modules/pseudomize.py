import logging


LOG_FILTER = [5, 9, 10, 11, 12, 13, 17, 20]


def delete_data_in_fields(data_list, list_of_fields):
    for index in list_of_fields:
        data_list[index] = ''
    return data_list


def pseudomize_ip(original_ip, salt):
    ip_segements = original_ip.split('.')
    ip_segements[2] = str((int(ip_segements[2]) + salt) % 256)
    ip_segements[3] = str((int(ip_segements[3]) + salt) % 256)
    pseudomized_ip = '.'.join(ip_segements)
    logging.debug('ip-pseudomized {} -> {}'.format(original_ip, pseudomized_ip))
    return pseudomized_ip
