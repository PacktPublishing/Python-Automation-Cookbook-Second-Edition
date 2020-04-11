import argparse
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def main(image_file):
    content = image_file.read()
    print(f'Text: {content}')
    document = types.Document(content=content,
                              type=enums.Document.Type.PLAIN_TEXT)

    client = language.LanguageServiceClient()

    print('Categories')
    response = client.classify_text(document=document)
    if not response.categories:
        print('No categories detected')

    for category in response.categories:
        print(f'Category: {category.name}')
        print(f'Confidence: {category.confidence}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input', type=argparse.FileType('r'),
                        help='input text')
    args = parser.parse_args()
    main(args.input)
