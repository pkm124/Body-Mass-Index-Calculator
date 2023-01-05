from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calc_formula")
def calc_formula():
    height = float(request.args.get('height'))
    weight = float(request.args.get('weight'))
    bmi = weight/(height*height)
    if bmi>30 and bmi<34.9 :
        level = "Low"
    elif bmi>35 and bmi<39.9 :
        level = "Normal"
    else :
        level = "High"
    return render_template("index.html", bmi=bmi, level=level)

if __name__=="__main__":
    app.run(debug=True)