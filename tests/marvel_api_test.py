import unittest
from unittest.mock import patch, MagicMock
import json
from marvel_api import fetch_characters_batch

class TestMarvelAPI(unittest.TestCase):

    @patch("urllib.request.urlopen")
    def test_fetch_characters_batch(self, mock_urlopen):
        """Test fetching a batch of characters with a mocked API response."""
        
        # Create a mock response object
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "data": {
                "results": [
                    {"name": "Spider-Man", "comics": {"available": 100}}
                ]
            }
        }).encode("utf-8")

        # Ensure the mock is returned within a 'with' statement
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = fetch_characters_batch(0)
        self.assertEqual(result, [("Spider-Man", 100)])

    @patch("urllib.request.urlopen", side_effect=Exception("API Error"))
    def test_fetch_characters_batch_failure(self, mock_urlopen):
        """Test error handling when API request fails."""
        result = fetch_characters_batch(0)
        self.assertEqual(result, [])  # Should return an empty list on failure

if __name__ == "__main__":
    unittest.main()
