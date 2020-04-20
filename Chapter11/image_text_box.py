import argparse
from google.cloud import vision


def main(image_file, verbose):
    content = image_file.read()

    client = vision.ImageAnnotatorClient()
    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)

    print('Texts:')
    for text in response.text_annotations:
        print('"{}"'.format(text.description))
        if verbose:
            points = ['({},{})'.format(p.x, p.y)
                      for p in text.bounding_poly.vertices]
            print('box: {}'.format(','.join(points)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input', type=argparse.FileType('rb'),
                        help='input image')
    parser.add_argument('-v', dest='verbose', help='Print more data',
                        action='store_true')
    args = parser.parse_args()
    main(args.input, args.verbose)
