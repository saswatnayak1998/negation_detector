from neg import make_negation
import json
with open("data.json") as json_file:
    json_data = json.load(json_file)
def test_index():
    truth=json_data.values()
    assert make_negation==truth