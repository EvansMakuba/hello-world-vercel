from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load the queue of comments from our JSON file
with open('queue.json','r') as f:
    comment_queue = json.load(f)

# Keep track of our position in the queue
current_index = 0

@app.route('/get-next-item', methods=['GET'])
def get_next_item():
    """Provide the next submission URL and comment."""
    global current_index
    if current_index < len(comment_queue):
        item = comment_queue[current_index]
        return jsonify(item)

    else:
        return jsonify({"submission_url": "No more items in the queue!", "comment_to_place": ""})

@app.route('/item-published', methods=['POST'])
def item_published():
    """Moves to the next item after the user confirms the published the previous one."""
    global current_index
    current_index +=1
    return jsonify({"status":"success", "next_index":current_index})

if __name__ == '__main__':
    #Runs the server on localhost port 5000
    app.run(debug=True, port=5000)