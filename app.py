from flask import Flask, render_template_string, request, session, redirect, url_for
import random
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How vexingly quick daft zebras jump!",
    "Sphinx of black quartz, judge my vow.",
    "Waltz, nymph, for quick jigs vex Bud."
]

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Typing Speed Test</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; }
        .container { max-width: 600px; margin: 40px auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px #ccc; }
        .sample { color: #1a73e8; font-size: 1.2em; margin-bottom: 20px; }
        textarea { width: 100%; height: 100px; font-size: 1.1em; }
        .result { font-size: 1.2em; margin-top: 20px; }
        button { padding: 10px 20px; font-size: 1em; margin-top: 10px; }
        .footer { text-align: center; margin-top: 40px; color: #888; font-size: 1em; }
        .footer a { color: #1a73e8; text-decoration: none; }
        .footer a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Typing Speed Test</h2>
        <form method="post" action="/">
            <div class="sample">{{ sample_text }}</div>
            <input type="hidden" name="start_time" value="{{ start_time }}">
            <input type="hidden" name="sample_text" value="{{ sample_text }}">
            <textarea name="user_input" placeholder="Start typing here..." required autofocus></textarea><br>
            <button type="submit">Submit</button>
        </form>
        {% if result %}
        <div class="result">{{ result }}</div>
        <form method="get" action="/">
            <button type="submit">Try Again</button>
        </form>
        {% endif %}
    </div>
    <div class="footer">
        Made by <a href="https://github.com/mallocode300" target="_blank">Mallory Antomarchi</a>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input'].strip()
        sample_text = request.form['sample_text']
        start_time = float(request.form['start_time'])
        end_time = time.time()
        elapsed = end_time - start_time
        word_count = len(user_input.split())
        wpm = (word_count / elapsed) * 60 if elapsed > 0 else 0
        correct = user_input == sample_text
        if correct:
            result = f"Correct! Your speed: {wpm:.2f} WPM"
        else:
            result = f"Text does not match. Your speed: {wpm:.2f} WPM"
        return render_template_string(HTML_TEMPLATE, sample_text=sample_text, start_time=start_time, result=result)
    else:
        sample_text = random.choice(SAMPLE_TEXTS)
        start_time = time.time()
        return render_template_string(HTML_TEMPLATE, sample_text=sample_text, start_time=start_time, result=None)

if __name__ == '__main__':
    app.run(debug=True) 