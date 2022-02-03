from flask import Flask, url_for

app = Flask(__name__)

STATIC_PATH = 'static'


@app.route('/')
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """
    <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Человечество вырастает из детства.</h1><br>
                    <h1>Человечеству мала одна планета.</h1><br>
                    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1><br>
                    <h1>И начнем с Марса!</h1><br>
                    <h1>Присоединяйся!</h1>
                  </body>
                </html>"""


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <img src="{url_for(STATIC_PATH, filename='images/mars.jpg')}" 
                alt="красивое, марсистое">
                    <br>
                    <h1>Присоединяйся!</h1>
                  </body>
                </html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="{url_for(STATIC_PATH, filename='css/style.css')}">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>
                     Жди нас, Марс!
                    </h1>
                    <img src="{url_for(STATIC_PATH, filename='images/mars.jpg')}" 
                alt="красивое, марсистое">
                    <br>
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-info" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/choice/')
@app.route('/choice/<planet_name>')
def planet_choice(planet_name=None):
    planet_texts = {
        "unknown_planet": {
            "name": "Неизвестная нам планета",
            "distance": "Мы не знаем про расстояние до этой планеты",
            "resources": "Мы не знаем сколько на ней ресурсов",
            "atmosphere": "Мы не знаем про атмосферу данной планеты",
            "magnetic_field": "Мы не знаем про магнитное поле данной планеты",
            "beautifulness": "Но наверняка, эта планета очень красивая"
        },
        "venerus": {
            "name": "Венера",
            "distance": "Находится относительно недалеко от земли",
            "resources": "На ней достаточно необходимых ресурсов",
            "atmosphere": "Атмосфера данной планеты безжизненна",
            "magnetic_field": "Магнитное поле данной планеты слабое",
            "beautifulness": "Венера завораживающе красива"
        },
        "mars": {
            "name": "Марс",
            "distance": "Данная планета близка к Земле",
            "resources": "На ней предостаточно ресурсво",
            "atmosphere": "На ней есть атмосфера почти схожая с земной",
            "magnetic_field": "На ней присутствует слабое магнитное поле",
            "beautifulness": "Марс завораживает своими пейзажами"
        },
        "earth": {
            "name": "Земля",
            "distance": "Эта планета и есть земля",
            "resources": "На ней достатотчно ресурсов для того что бы человечество процветало",
            "atmosphere": "Атмосфера данной планеты позволяет нам жить",
            "magnetic_field": "Магнитное поле достаточно сильное что бы защитить нас от солнца",
            "beautifulness": "Земля очень красива"
        }
    }
    if planet_name:
        planet_name = planet_name.lower()
    if planet_name not in planet_texts.keys():
        planet_name = 'unknown_planet'

    text = planet_texts[planet_name]
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="{url_for(STATIC_PATH, filename="css/style.css")}">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>
                     Мое предложение: {text["name"]}
                    </h1>
                    <div class="alert alert-primary" role="alert">
                      {text["distance"]}
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      {text["resources"]}
                    </div>
                    <div class="alert alert-success" role="alert">
                      {text["atmosphere"]}
                    </div>
                    <div class="alert alert-danger" role="alert">
                     {text["magnetic_field"]}
                    </div>
                    <div class="alert alert-info" role="alert">
                      {text["beautifulness"]}
                    </div>
                  </body>
                </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname="{nickname}", level=0, rating=0.0):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="{url_for(STATIC_PATH, filename="css/style.css")}">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результат</title>
                  </head>
                  <body>
                    <h1>
                     Результаты отбора
                    </h1>
                    <br>
                    <h2>
                     Претендента на участие в миссии {nickname}:
                    </h2>
                    <div class="alert alert-primary" role="alert">
                      Поздравляем ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      составляет {rating}!
                    </div>
                    <div class="alert alert-success" role="alert">
                      Удачи!
                    </div>
                  </body>
                </html>"""


@app.route('/carousel')
def carousel():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="{url_for(STATIC_PATH, filename="css/style.css")}">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
                    <title>Результат</title>
                  </head>
                  <body>
                   <center><h1>Пейзажи Марса</h1></center>
                   <div id="carouselMars" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-indicators">
                     <button type="button" data-bs-target="#carouselMars" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                     <button type="button" data-bs-target="#carouselMars" data-bs-slide-to="1" aria-label="Slide 2"></button>
                     <button type="button" data-bs-target="#carouselMars" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img src="{url_for(STATIC_PATH, filename="images/image_1.jpg")}" class="d-block w-100" alt="misfortune">
                        </div>
                        <div class="carousel-item">
                          <img src="{url_for(STATIC_PATH, filename="images/image_2.jpg")}" class="d-block w-100" alt="misfortune">
                        </div>
                        <div class="carousel-item">
                          <img src="{url_for(STATIC_PATH, filename="images/image_3.jpg")}" class="d-block w-100" alt="misfortune">
                        </div>
                      </div>
                      <button class="carousel-control-prev" type="button" data-bs-target="#carouselMars" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                      </button>
                      <button class="carousel-control-next" type="button" data-bs-target="#carouselMars" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                      </button>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
