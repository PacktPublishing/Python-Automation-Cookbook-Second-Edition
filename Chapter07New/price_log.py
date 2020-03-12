import parse
from decimal import Decimal


class PriceLog(object):

    def __init__(self, location, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price
        self.location = location

    @classmethod
    def parse(cls, location, text_log):
        '''
        Parse from a text log with the format
        [<Timestamp>] - SALE - PRODUCT: <product id> - PRICE: <price>
        to a PriceLog object

        It requires a location
        '''
        def price(string):
            return Decimal(string)

        FORMAT = ('[{timestamp}] - SALE - PRODUCT: {product:d} - '
                  'PRICE: {price:price}')

        formats = {'price': price}
        result = parse.parse(FORMAT, text_log, formats)

        return cls(location=location, timestamp=result['timestamp'],
                   product_id=result['product'], price=result['price'])

    @classmethod
    def header(cls):
        return ['LOCATION', 'TIMESTAMP', 'PRODUCT', 'PRICE']

    def row(self):
        return [self.location, self.timestamp, self.product_id, self.price]
