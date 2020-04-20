'''
This file will read a log file and produce an CSV file with the data
'''
import csv
import argparse
from datetime import datetime, timezone


def american_format(timestamp):
    '''
    Transform from MM-DD-YYYY HH:MM:SS to iso 8601
    '''
    FORMAT = '%m-%d-%Y %H:%M:%S'

    parsed_tmp = datetime.strptime(timestamp, FORMAT)
    time_with_tz = parsed_tmp.astimezone(timezone.utc)
    isotimestamp = time_with_tz.isoformat()

    return isotimestamp


def add_std_timestamp(row):
    country = row['COUNTRY']
    if country == 'USA':
        # No change
        row['STD_TIMESTAMP'] = american_format(row['TIMESTAMP'])
    elif country == 'CANADA':
        # No change
        row['STD_TIMESTAMP'] = row['TIMESTAMP']
    else:
        raise Exception('Country not found')

    return row


def main(input_file, output_file):
    reader = csv.DictReader(input_file)
    result = [add_std_timestamp(row) for row in reader]

    # Save into csv format
    header = result[0].keys()
    writer = csv.DictWriter(output_file, fieldnames=header)
    writer.writeheader()
    writer.writerows(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input', type=argparse.FileType('r'),
                        help='input file')
    parser.add_argument(dest='output', type=argparse.FileType('w'),
                        help='output file')
    args = parser.parse_args()
    main(args.input, args.output)
