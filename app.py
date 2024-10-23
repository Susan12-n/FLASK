from flask import Flask
app = Flask(__name__)
# Flask(__name__) -creates a flask instance and __name__ helps the flask to find resoursces
@app.route("/")
#the above defines the route for homepage
def Home():
    return("This is my homepage")
#  about us route 
@app.route("/about")
def About():
    return("this is about page")

#route page
@app.route("/service")
def services():
    return("this is the service page") 

#contact
@app.route("/contact")
def contact():
    return("this is the contact page")



@app.route("/signup")
def signup ():
    return("this is the sign up page")




@app.route("/testimonials")
def testimonials():
    return("this is the testimonial  page")



@app.route("/blog")
def blog():
    return("this is the blog page")
if __name__=="__main__":
    app.run (port=4001, debug=True)