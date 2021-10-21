import unittest 
from unittest import TestCase 
from unittest.mock import patch

import bitcoin_app
from bitcoin_app import BitCoinError


class TestBitCoin(TestCase):

    @patch('bitcoin_app.get_result_from_api')
    def test_convert(self, mock_api_call):
        # Example response. rate_float is 8735.44
        example_rate_float = 8735.44
        mock_response = {"time":{"updated":"Mar 3, 2020 16:14:00 UTC","updatedISO":"2020-03-03T16:14:00+00:00","updateduk":"Mar 3, 2020 at 16:14 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"8,735.4400","description":"United States Dollar","rate_float": example_rate_float},"GBP":{"code":"GBP","symbol":"&pound;","rate":"6,815.3466","description":"British Pound Sterling","rate_float":6815.3466},"EUR":{"code":"EUR","symbol":"&euro;","rate":"7,813.8161","description":"Euro","rate_float":7813.8161}}}
        # if it's reasonable to always expect the same return value, 
        # you can set the return_value instead of side_effect. 
        mock_api_call.return_value = mock_response 
        example_dollars = 99.99
        expected_conversion = example_rate_float * example_dollars
        actual_conversion = bitcoin_app.convert_dollars_to_bitcoin(example_dollars, 'example url') 
        self.assertEqual(expected_conversion, actual_conversion)


    @patch('bitcoin_app.get_result_from_api')
    def test_convert_different_json_format(self, mock_api_call):
        # not the expected JSON
        mock_response = {"cat": "hello kitty", "pizza_count": 1000000}
        mock_api_call.return_value = mock_response 
        with self.assertRaises(BitCoinError):             
             bitcoin_app.convert_dollars_to_bitcoin(100, 'example url')


    # Mock an error thrown from the api_call function, again, avoid calling real API
    @patch('bitcoin_app.get_result_from_api', side_effect=BitCoinError)
    def test_bad_response_from_server(self, mock_api_call):
        with self.assertRaises(BitCoinError):             
            bitcoin_app.convert_dollars_to_bitcoin(100, 'example url')


if __name__ == '__main__':
    unittest.main()