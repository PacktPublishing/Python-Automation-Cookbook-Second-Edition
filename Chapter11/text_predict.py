import argparse

from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1


def main(input_file, model_name):
    content = input_file.read()
    options = ClientOptions(api_endpoint='automl.googleapis.com')
    prediction_client = automl_v1.PredictionServiceClient(
        client_options=options
    )
    payload = {'text_snippet': {'content': content, 'mime_type': 'text/plain'}}
    params = {}
    request = prediction_client.predict(model_name, payload, params)
    for result in request.payload:
        label = result.display_name
        match = result.classification.score
        print(f'Label: {label} : {match:.5f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input', type=argparse.FileType('r'),
                        help='input text')
    parser.add_argument('-m', dest='model', type=str, help='model ref')
    args = parser.parse_args()

    main(args.input, args.model)
