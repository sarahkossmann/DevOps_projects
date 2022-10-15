from flask import Flask, render_template
from main_game import *

app = Flask(__name__)

@app.route('/')
def score_server():
    with open("scores.txt", 'r') as f:
        lines = f.readlines()
        total_score = lines[-1]
        current_score = lines[-2]
        f.close()
    return render_template('index.html', total_score=total_score, current_score=current_score)



if __name__ == "__main__":
    app.run()