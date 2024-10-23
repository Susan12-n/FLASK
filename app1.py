# madaraka with flask 
from flask import Flask
from flask import render_template
app= Flask(__name__)

@app.route("/home")
def Home():
      return render_template("index.html")

@app.route("/about")
def About():
      return render_template("about.html")

@app.route("/service")
def service():
      return render_template("service.html")

@app.route("/gallery")
def gallery():
      return render_template("gallery.html")

@app.route("/contact")
def contact():
      return render_template("contact.html")

@app.route("/faqs")
def faqs():
      return render_template("faqs.html")


if __name__== "__main__":
      app.run(debug=True,port=7000)