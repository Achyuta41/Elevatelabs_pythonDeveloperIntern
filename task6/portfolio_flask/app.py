from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/download-resume')
def download_resume():
    return send_from_directory('static', 'Achyuta_resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
