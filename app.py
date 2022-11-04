import time

import redis

from crypt import methods
from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/populares')
def populares():
    url_pop = "https://api.themoviedb.org/3//discover/movie?sort_by=popularity.desc&api_key=96275fcac06ba8cbe9d9d4e246f32038"
    
    resposta_pop = urllib.request.urlopen(url_pop)      ##urlopen
    
    dados_pop = resposta_pop.read()                     ##variável para read
    
    jsondata_pop = json.loads(dados_pop)                ##transformar em json
    
    return render_template("populares.html", pops=jsondata_pop['results'])

@app.route('/acao')
def acao():
    url_acao = "https://api.themoviedb.org/3///discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=96275fcac06ba8cbe9d9d4e246f32038"
    
    resposta_ação = urllib.request.urlopen(url_acao)    ##urlopen
    
    dados_ação = resposta_ação.read()                   ##variável para read
    
    jsondata_ação = json.loads(dados_ação)              ##transformar em json
    
    return render_template("acao.html", acoes=jsondata_ação['results'])

#aclamados
@app.route('/aclamados')
def aclamados():
    url_acla = "https://api.themoviedb.org/3///discover/movie?with_genres=18&primary_release_year=2014&api_key=96275fcac06ba8cbe9d9d4e246f32038"
    
    resposta_acla = urllib.request.urlopen(url_acla)    ##urlopen
    
    dados_acla = resposta_acla.read()                   ##variável para read
    
    jsondata_acla = json.loads(dados_acla)              ##transformar em json
    
    return render_template("aclamados.html", aclamados=jsondata_acla['results'])

#dramas
@app.route('/dramas')
def dramas():
    url_dramas = "https://api.themoviedb.org/3///discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=96275fcac06ba8cbe9d9d4e246f32038"
    
    resposta_dramas = urllib.request.urlopen(url_dramas)    ##urlopen
    
    dados_dramas = resposta_dramas.read()                   ##variável para read
    
    jsondata_dramas = json.loads(dados_dramas)              ##transformar em json
    
    return render_template("dramas.html", dramas=jsondata_dramas['results'])

#classicos
@app.route('/classicos')
def classicos():
    url_class = "https://api.themoviedb.org/3///discover/movie?primary_release_date.gte=2014-09-15&primary_release_date.lte=2014-10-22&api_key=96275fcac06ba8cbe9d9d4e246f32038"
    
    resposta_class = urllib.request.urlopen(url_class)    ##urlopen
    
    dados_class = resposta_class.read()                   ##variável para read
    
    jsondata_class = json.loads(dados_class)              ##transformar em json
    
    return render_template("classicos.html", classicos=jsondata_class['results'])

#ficção cientifica
@app.route('/cientifica')
def cientifica():
    url_cientifica = "https://api.themoviedb.org/3///discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=96275fcac06ba8cbe9d9d4e246f32038"
    
    resposta_cientifica = urllib.request.urlopen(url_cientifica)    ##urlopen
    
    dados_cientifica = resposta_cientifica.read()                   ##variável para read
    
    jsondata_cientifica = json.loads(dados_cientifica)              ##transformar em json
    
    return render_template("ficcao.html", cientificas=jsondata_cientifica['results'])

@app.route('/melhores')
def melhores():
    url_melhores = "https://api.themoviedb.org/3///discover/movie?certification_country=US&certification=R&sort_by=revenue.desc&with_cast=3896&api_key=96275fcac06ba8cbe9d9d4e246f32038"
    
    resposta_melhores = urllib.request.urlopen(url_melhores)    ##urlopen
    
    dados_melhores = resposta_melhores.read()                   ##variável para read
    
    jsondata_melhores = json.loads(dados_melhores)              ##transformar em json
    
    return render_template("melhores.html", melhores=jsondata_melhores['results'])

@app.route('/familia')
def familia():
    url_familia = "https://api.themoviedb.org/3///discover/movie?with_genres=35&with_cast=23659&sort_by=revenue.desc&api_key=96275fcac06ba8cbe9d9d4e246f32038"
    
    resposta_familia = urllib.request.urlopen(url_familia)    ##urlopen
    
    dados_familia = resposta_familia.read()                   ##variável para read
    
    jsondata_familia = json.loads(dados_familia)              ##transformar em json
    
    return render_template("familia.html", familias=jsondata_familia['results'])


if __name__ =="__main__":
    app.run(debug=True)