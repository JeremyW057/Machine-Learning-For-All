from flask import Flask, render_template, request, jsonify, Response, make_response
import lin_model, io

app = Flask(__name__) ###References this file

##To run: Active venv - .\.venv\Scripts\activate
## cd into .venv
## run server - flask --app server.py run

## Main page
@app.route('/')
def index():
    return render_template("data_app.html")

## Info page
## Need to make_response with new page and all items for page.
@app.route('/sub',methods=['post'])
def info():
    iv = request.form.getlist('iv')
    dv = request.form.getlist('dv')
    csv= request.files.get('df_csv')
    
    iv = [x.strip() for x in iv]
    dv = [x.strip() for x in dv]

    try:
        tuple_ML = lin_model.build_model(csv, iv, dv)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    num_iv = len(iv)

    return render_template("display_app.html", tup = tuple_ML,num_iv=num_iv)
        
if __name__ == '__main__':
    app.run(debug=True)
    

  