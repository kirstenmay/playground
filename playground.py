from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def blue_boxes():
    return render_template("more_boxes_color.html", level=1)

@app.route("/play/<x>")
def more_blue_boxes(x):
    return render_template("more_boxes_color.html", level = 2, repeat = int(x))

@app.route("/play/<x>/<color>")
def more_color_boxes(x, color):
    return render_template("more_boxes_color.html", level = 3, repeat = int(x), color = str(color))

if __name__ == "__main__":
    app.run(debug=True)