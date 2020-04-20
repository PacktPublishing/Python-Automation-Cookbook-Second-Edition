import argparse
from google.cloud import vision


def landmark(client, image):
    print('Landmark detected')
    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    for landmark in landmarks:
        print(f'  {landmark.description}')
        for location in landmark.locations:
            coord = location.lat_lng
            print(f'  Latitude {coord.latitude}')
            print(f'  Longitude {coord.longitude}')

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


def main(image_file):
    content = image_file.read()

    client = vision.ImageAnnotatorClient()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels for the image and score:')

    for label in labels:
        print(label.description, label.score)
        if(label.description == 'Landmark'):
            landmark(client, image)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input', type=argparse.FileType('rb'),
                        help='input image')
    args = parser.parse_args()
    main(args.input)
