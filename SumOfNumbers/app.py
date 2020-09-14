from flask import Flask
import json

app = Flask(__name__)

@app.route("/total")

def sum_of_numbers():
    # Please add code here to fetch the list from Database
    numbers_to_add = list(range(10000001))
    max_number = max(numbers_to_add)
    total = int(max_number * (max_number + 1) / 2)

    response = '{' + ('\"total\": {}').format(total) + '}'

    return json.loads(response)

if __name__ == '__main__':
    app.run(debug=True)
