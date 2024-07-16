from flask import Flask

app = Flask(__name__)
#main
@app.route('/home')
def home():
    return '''<html> 

    <h1> WELLCOME TO THE WEBSITE!</h1> 
    <h2><Click this link!/h2>
    <a href="/food1">food1</a>
    <a href="/food3">food3</a>
    <a href="/pet2">pet2</a>
    <a href="/space1">space1</a>

    </html>'''

#food pictures
@app.route('/food1')
def food1():
    return '''<html> 

    <h1> WELLCOME TO THE food1 WEBSITE!</h1> 
    <a href="/home">home</a>
    <a href="/food2">food2</a>
    <img src="https://t3.ftcdn.net/jpg/02/52/38/80/360_F_252388016_KjPnB9vglSCuUJAumCDNbmMzGdzPAucK.jpg">

    </html>'''

@app.route('/food2')
def food2():
    return '''<html> 

    <h1> WELLCOME TO THE food2 WEBSITE!</h1> 
    <a href="/food1">food1</a>
    <a href="/food3">food3</a>
    <img src="https://news.mit.edu/sites/default/files/styles/news_article__image_gallery/public/images/202312/MIT_Food-Diabetes-01_0.jpg?itok=Mp8FVJkC">

    </html>'''   

@app.route('/food3')
def food3():
    return '''<html> 

    <h1> WELLCOME TO THE food3 WEBSITE!</h1>
    <a href="/food2">food2</a> 
    <a href="/home">home</a>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLvk2v9KKSMy93OkaOX5WTkKjDH2kAyTfOoQ&s">

    </html>''' 

#pet picturs
@app.route('/pet1')
def pet1():
    return '''<html> 

    <h1> WELLCOME TO THE pet1 WEBSITE!</h1> 
    <a href="/pet2">pet2</a>
    <img src="https://brunswick.ces.ncsu.edu/wp-content/uploads/2022/05/pets-g6fa575878_1920.jpg">

    </html>'''  

@app.route('/pet2')
def pet2():
    return '''<html> 

    <h1> WELLCOME TO THE pet2 WEBSITE!</h1> 
    <a href="/home">home</a>
    <a href="/pet1">pet1</a>
    <a href="/pet3">pet3</a>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVL9tfVWVWLX8jiKGmbm4PhI8VGIqpM0GVxQ&s">

    </html>'''  

@app.route('/pet3')
def pet3():
    return '''<html> 

    <h1> WELLCOME TO THE pet3 WEBSITE!</h1> 
    <a href="/home">home</a>
    <a href="/pet2">pet2</a>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwvAPSnUrBg9QnZDHhlV_dDD-cUFM-sovWGA&s">

    </html>''' 

    #space picturs
@app.route('/space1')
def space1():
    return '''<html> 

    <h1> WELLCOME TO THE space1 WEBSITE!</h1>
    <a href="/home">home</a> 
    <a href="/space2">space2</a>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJpaWTviBwKxlBCAQujz_Jr3Fb2baDw7eRrg&s">

    </html>'''  

@app.route('/space2')
def space2():
    return '''<html> 

    <h1> WELLCOME TO THE space2 WEBSITE!</h1> 
    <a href="/space1">space1</a>
    <a href="/space3">space3</a>
    <img src="https://c02.purpledshub.com/uploads/sites/48/2020/04/Things-never-knew-astronomy-e454e5d.jpg">

    </html>'''  

@app.route('/space3')
def space3():
    return '''<html> 

    <h1> WELLCOME TO THE space3 WEBSITE!</h1> 
    <a href="/space1">space1</a>
    <a href="/space2">space2</a>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRu2fTlZBOzWrf4NuOQuIbgV9hg_kVjl9aavA&s">

    </html>'''  



if __name__ == '__main__':
    app.run(debug=True)