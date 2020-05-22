import argparse
from google.cloud import vision


def main(image_file, verbose):
    content = image_file.read()

    client = vision.ImageAnnotatorClient()
    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:

        for block in page.blocks:

            if verbose:
                print('\nBlock confidence: {}\n'.format(block.confidence))

            if block.confidence < 0.8:
                if verbose:
                    print('Skipping block due to low confidence')
                continue

            for paragraph in block.paragraphs:
                paragraph_text = []
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    paragraph_text.append(word_text)
                    if verbose:
                        print(f'Word text: {word_text} '
                              f'(confidence: {word.confidence})')
                        for symbol in word.symbols:
                            print(f'\tSymbol: {symbol.text} '
                                  f'(confidence: {symbol.confidence})')

                print(' '.join(paragraph_text))

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
