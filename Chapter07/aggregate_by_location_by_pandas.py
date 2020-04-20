'''
This file will read a CSV file and produce another with aggregated data
'''
import csv
import argparse
import pandas as pd


def pandas_format(row):
    row['DATE'] = pd.to_datetime(row['STD_TIMESTAMP'])
    row['USD'] = pd.to_numeric(row['USD'])

    return row


def calculate_results(reader):
    # Load the data, formatting
    data = pd.DataFrame(pandas_format(r) for r in reader)
    by_usd = data.groupby(data['DATE'].dt.date)['USD']
    result = by_usd.agg(['sum', 'count', 'mean'])

    # Round to 2 digital places
    result = result.round(2)

    # Rename colums
    result = result.rename(columns={
        'sum': 'TOTAL USD',
        'count': 'NUMBER',
        'mean': 'AVERAGE',
    })

    return result


def main(input_file, output_file):
    reader = csv.DictReader(input_file)
    result = calculate_results(reader)

    # Save into csv format
    output_file.write(result.to_csv())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input', type=argparse.FileType('r'),
                        help='input file')
    parser.add_argument(dest='output', type=argparse.FileType('w'),
                        help='output file')
    args = parser.parse_args()
    main(args.input, args.output)
