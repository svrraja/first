from flask import Flask, render_template

app = Flask(__name__)

@app.route('/india_map')
def india_map():
    return render_template('india_map.html')

if __name__ == '__main__':
    app.run(debug=True)