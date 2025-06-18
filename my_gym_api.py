from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database
gym_members = [
    {
        "member_id": 1,
        "member_name": "Aman Gupta",
        "trainers": ["jeet", "akhilesh"]
    },
    {
        "member_id": 2,
        "member_name": "Diya",
        "trainers": ["Aman"]
    }
]

# Get all members
@app.route('/api/members', methods=['GET'])
def get_members():
    return jsonify(gym_members), 200

# Get single member by ID
@app.route('/api/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = next((m for m in gym_members if m["member_id"] == member_id), None)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "member not found"}), 404

# Add a new member
@app.route('/api/members', methods=['POST'])
def add_member():
    trainer = request.args.get('trainer')
    data = request.get_json()
    if not data or "member_id" not in data or "member_name" not in data or "trainers" not in data:
        return jsonify({"error": "invalid input"}), 400
    gym_members.append(data)
    return jsonify({"message": "member added", "member": data}), 201

# Delete member by ID
@app.route('/api/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global gym_members
    gym_members = [m for m in gym_members if m["member_id"] != member_id]
    return jsonify({"message": f"Member with ID {member_id} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
