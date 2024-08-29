from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Simulated in-memory data
    matches = [
        {"team1": "India", "team2": "Australia", "score": "250/7", "status": "In Progress"},
        {"team1": "England", "team2": "New Zealand", "score": "180/3", "status": "In Progress"}
    ]
    return render_template('index.html', matches=matches)
