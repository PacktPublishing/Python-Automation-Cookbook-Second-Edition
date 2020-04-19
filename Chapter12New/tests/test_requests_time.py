import responses
import urllib.parse
from freezegun import freeze_time
from code.code_requests import order_pizza


@responses.activate
@freeze_time("2020-03-17T19:34")
def test_order_time():
    body = {
        'form': {
            'size': 'small',
            'topping': ['bacon', 'onion']
        }
    }
    responses.add(responses.POST, 'https://httpbin.org/post',
                  json=body, status=200)

    order_pizza()
    # Decode the sent data
    encoded_body = responses.calls[0].request.body
    sent_data = urllib.parse.parse_qs(encoded_body)
    assert sent_data['delivery'] == ['20:34']
