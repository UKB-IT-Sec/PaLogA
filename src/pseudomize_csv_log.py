#! /usr/bin/env python3
'''
    PaLogA
    Copyright (C) 2023 Universitaetsklinikum Bonn AoeR

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import argparse
import logging
import sys
from modules.pseudomize import pseudomize_ip, delete_data_in_fields, LOG_FILTER

PROGRAM_NAME = 'PaLogA CSV Log Pseudomizer'
PROGRAM_VERSION = '0.1'
PROGRAM_DESCRIPTION = 'Pseudomize a csv log export'


def _setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('-s', '--salt', default='3', help='salt for pseudomize algorithm')
    parser.add_argument('input_file', help='input csv log file')
    parser.add_argument('output_file', help='output file')
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages')
    return parser.parse_args()


def _setup_logging(args):
    log_format = logging.Formatter(fmt='[%(asctime)s][%(module)s][%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger('')
    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    console_logger = logging.StreamHandler()
    console_logger.setFormatter(log_format)
    logger.addHandler(console_logger)


def pseudomize_line(log_line, salt):
    log_segments = log_line.split(',')
    log_segments = delete_data_in_fields(log_segments, LOG_FILTER)
    log_segments[7] = pseudomize_ip(log_segments[7], salt)
    return ';'.join(log_segments)


if __name__ == '__main__':
    args = _setup_argparser()
    _setup_logging(args)
    try:
        salt = int(args.salt)
    except ValueError:
        sys.exit('salt must be int')

    log_file = open(args.input_file, 'r')
    censored_log_file = open(args.output_file, 'w')

    header_line = log_file.readline()
    censored_log_file.writelines(';'.join(header_line.split(',')))

    while True:
        log_line = log_file.readline()
        try:
            log_line = pseudomize_line(log_line, salt)
        except IndexError:
            logging.debug('EOF')
        censored_log_file.writelines(log_line)
        if not log_line:
            break

    log_file.close()
    censored_log_file.close()

    sys.exit()
