import pytest
import requests
import responses
import urllib.parse
from code.code_requests import order_pizza


@responses.activate
def test_order_pizza():
    body = {
        'form': {
            'size': 'small',
            'topping': ['bacon', 'onion']
        }
    }
    responses.add(responses.POST, 'https://httpbin.org/post',
                  json=body, status=200)

    result = order_pizza()
    assert result['size'] == 'small'
    # Decode the sent data
    encoded_body = responses.calls[0].request.body
    sent_data = urllib.parse.parse_qs(encoded_body)
    assert sent_data['size'] == ['small']


@responses.activate
def test_order_pizza_timeout():
    responses.add(responses.POST, 'https://httpbin.org/post',
                  body=requests.exceptions.Timeout())

    with pytest.raises(requests.exceptions.Timeout):
        order_pizza()
