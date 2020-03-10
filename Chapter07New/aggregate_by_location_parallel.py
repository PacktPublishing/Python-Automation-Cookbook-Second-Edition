'''
This file will read a list of matched CSV file
and produce one with aggregated data for each
'''
import glob
import re
import argparse
import concurrent.futures
from aggregate_by_location import main as main_by_file


def aggregate_filename(filename):
    try:
        print(f'Processing {filename}')
        # Obtain the location
        match = re.match(r'output_3_(.*).csv', filename)
        location = match.group(1)
        output_file = f'aggregate_{location}.csv'

        with open(filename) as in_file, open(output_file, 'w') as out_file:
            main_by_file(in_file, out_file)

        print(f'Done with {filename} => {output_file}', flush=True)
    except Exception as exc:
        print(f'Unexpected exception {exc}')


def main(input_glob):
    input_files = [filename for filename in glob.glob(input_glob)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(aggregate_filename, filename)
                   for filename in input_files]
        concurrent.futures.wait(futures)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input', type=str, help='input glob')
    args = parser.parse_args()
    main(args.input)
