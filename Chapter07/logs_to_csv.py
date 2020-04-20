'''
This file will read a log file and produce an CSV file with the data
'''
import csv
import argparse
from price_log import PriceLog


def log_to_csv(input_file, output_file, location):
    logs = [PriceLog.parse(location, line) for line in input_file]

    # Save into csv format
    writer = csv.writer(output_file)
    writer.writerow(PriceLog.header())
    writer.writerows(l.row() for l in logs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input', type=argparse.FileType('r'),
                        help='input file')
    parser.add_argument(dest='output', type=argparse.FileType('w'),
                        help='output file')
    parser.add_argument('-l', dest='location', type=str,
                        help='Location of the logs. Default US', default='US')

    args = parser.parse_args()
    log_to_csv(args.input, args.output, args.location)
