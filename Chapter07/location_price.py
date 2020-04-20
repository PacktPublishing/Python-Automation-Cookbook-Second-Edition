'''
This file will read a log file and produce an CSV file with the data
'''
import csv
import argparse
from decimal import Decimal, getcontext

# Set precission to two digital positions
getcontext().prec = 2

US_LOCATIONS = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
                'DC']
CAD_LOCATIONS = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK',
                 'NT', 'NU', 'YT']
CAD_TO_USD = Decimal(0.76)


def add_price_by_location(row):
    location = row['LOCATION']
    if location in US_LOCATIONS:
        row['COUNTRY'] = 'USA'
        row['CURRENCY'] = 'USD'
        row['USD'] = Decimal(row['PRICE'])
    elif location in CAD_LOCATIONS:
        row['COUNTRY'] = 'CANADA'
        row['CURRENCY'] = 'CAD'
        row['USD'] = Decimal(row['PRICE']) * CAD_TO_USD
    else:
        raise Exception('Location not found')

    return row


def main(input_file, output_file):
    reader = csv.DictReader(input_file)
    result = [add_price_by_location(row) for row in reader]

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
