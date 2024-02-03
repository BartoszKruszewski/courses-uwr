import unittest
from unittest.mock import patch, MagicMock
from client.client import get, create, API_URL


class TestGet(unittest.TestCase):
    @patch('client.client.req_get')
    def test_get_success(self, mock_req_get):
        model_name = "example_model"
        expected_response = {"key": "value"}

        mock_response = MagicMock()
        mock_response.json.return_value = expected_response
        mock_req_get.return_value = mock_response

        result = get(model_name)

        mock_req_get.assert_called_once_with(
            API_URL, json={"model": model_name})
        self.assertEqual(result, expected_response)

    @patch('client.client.req_get')
    def test_get_empty_response(self, mock_req_get):
        model_name = "example_model"

        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_req_get.return_value = mock_response

        result = get(model_name)

        mock_req_get.assert_called_once_with(
            API_URL, json={"model": model_name})
        self.assertEqual(result, {})

    @patch('client.client.req_get')
    def test_get_network_error(self, mock_req_get):
        model_name = "example_model"

        mock_req_get.side_effect = Exception("Network error")

        with self.assertRaises(Exception):
            get(model_name)


class TestCreate(unittest.TestCase):
    @patch('client.client.req_post')
    def test_create_success(self, mock_req_post):
        model_name = "example_model"
        properties = {"key": "value"}
        expected_response = {"key": "created"}

        mock_response = MagicMock()
        mock_response.json.return_value = expected_response
        mock_req_post.return_value = mock_response

        result = create(model_name, properties)

        mock_req_post.assert_called_once_with(
            API_URL, json={"model": model_name, "properties": properties})
        self.assertEqual(result, expected_response)

    @patch('client.client.req_post')
    def test_create_duplicate_entry(self, mock_req_post):
        model_name = "example_model"
        properties = {"key": "value"}

        mock_response = MagicMock()
        mock_response.json.return_value = {"error": "Duplicate entry"}
        mock_req_post.return_value = mock_response

        result = create(model_name, properties)

        mock_req_post.assert_called_once_with(
            API_URL, json={"model": model_name, "properties": properties})
        self.assertEqual(result, {"error": "Duplicate entry"})

    @patch('client.client.req_post')
    def test_create_invalid_properties(self, mock_req_post):
        model_name = "example_model"
        properties = {"invalid_key": "value"}

        mock_response = MagicMock()
        mock_response.json.return_value = {"error": "Invalid properties"}
        mock_req_post.return_value = mock_response

        result = create(model_name, properties)

        mock_req_post.assert_called_once_with(
            API_URL, json={"model": model_name, "properties": properties})
        self.assertEqual(result, {"error": "Invalid properties"})


if __name__ == '__main__':
    unittest.main()
