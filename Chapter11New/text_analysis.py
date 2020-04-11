import argparse
from google.cloud import language
from google.cloud import translate_v2 as translate
from google.cloud.language import enums
from google.cloud.language import types


def main(image_file):
    content = image_file.read()
    print(f'Text: {content}')
    document = types.Document(content=content,
                              type=enums.Document.Type.PLAIN_TEXT)

    client = language.LanguageServiceClient()

    response = client.analyze_sentiment(document=document)
    lang = response.language
    print(f'Language: {lang}')
    sentiment = response.document_sentiment
    score = sentiment.score
    magnitude = sentiment.magnitude
    print(f'Sentiment Score (how positive the sentiment is): {score}')
    print(f'Sentiment Magnitude (how strong it is): {magnitude}')
    if lang != 'en':
        # Translate into English
        translate_client = translate.Client()
        response = translate_client.translate(content, target_language='en')
        print('IN ENGLISH')
        print(response['translatedText'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input', type=argparse.FileType('r'),
                        help='input text')
    args = parser.parse_args()
    main(args.input)
