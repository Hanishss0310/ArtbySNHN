from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Artworks page route
@app.route('/artworks')
def artworks():
    return render_template('artworks.html')

# Order now redirect
@app.route('/order')
def order():
    return redirect("https://forms.gle/eJHHyjJ9CjvqyWc16", code=302)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
