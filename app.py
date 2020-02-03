import os
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    firstname = request.form.get('firstname')
    lastname = request.form['lastname']

    return '''
              <div>
                <h2>Submitted data:</h2>
                <table>
                 <tr>
                   <td>Firstname</td>
                   <td>Lastname</td>
                 </tr>
                 <tr>
                   <td>{}</td>
                   <td>{}<td>
                 </tr>
              </table>
           </div>'''.format(firstname, lastname)

  return render_template("index.html", message="Toggle Switch Example", title="Tony Flask Example");


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)
