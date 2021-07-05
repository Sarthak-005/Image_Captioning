from flask import Flask, request, render_template, redirect
import Caption

app = Flask(__name__)
friends = ["Abc","BCS","SDD"]

@app.route('/')
def hello():
    return render_template("index.html", my_friends=friends)

"""@app.route('/about')
def about():
    return "ABout page "

@app.route('/Home')
def home():
    return redirect('/')"""

@app.route('/', methods = ['POST'])
def submit():
    if request.method == "POST":
        f = request.files['userfile']
        path = "./static/images/{}".format(f.filename)
        f.save(path)
        caption=Caption.caption_this_img(path)
        res_dict={
            'image': path,
            'caption': caption
        }
        print(caption)
    return render_template("index.html" , ur_cap=res_dict)
    



if __name__==    '__main__':
    #app.debug = True
    app.run(debug = True)