import json
import pytest
from app import get_response

with open("test/test_data.json", "r") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("test_case", test_data["tests"])
def test_chatbot_responses(test_case):
    input_text = test_case["input"]
    expected_output = test_case["expected_output"]

    bot_output = get_response(input_text)

    assert bot_output == expected_output, f"Failed on input: {input_text}"
