dict_data = {
    "1": {"id": 2, "value": "value 2"},
    "2": {"id": 5, "value": "value 5"},
    "3": {"id": 1, "value": "value 1"},
    "4": {"id": 3, "value": "value 3"},
}

sorted_dict = sorted(dict_data.items(), key=lambda pair: pair[1]["id"])

for entry in sorted_dict:
    print(entry)
# ('3', {'id': 1, 'value': 'value 1'})
# ('1', {'id': 2, 'value': 'value 2'})
# ('4', {'id': 3, 'value': 'value 3'})
# ('2', {'id': 5, 'value': 'value 5'})    