#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name':'Kampala'}, {'name':'Mbarara'}, {'name':'Jinja'},
        {'name':'Mbale'}, {'name':'Mukono'}, {'name':'Wakiso'},
        {'name':'Gulu'}, {'name':'Fort Portal'}, {'name':'Kasese'}, 
        {'name':'Arua'},{'name':'Hoima'}, {'name':'Kabale'}, {'name':'Butaleja'},
        {'name':'Bushenyi'}, {'name':'Soroti'}, {'name':'Tororo'},
        {'name':'Iganga'}, {'name':'Kamuli'}, {'name':'Mayuge'}, 
        {'name':'Budaka'},{'name':'Kumi'}, {'name':'Kalangala'}, {'name':'Kayunga'},
        {'name':'Masaka'}, {'name':'Mityana'}, {'name':'Mpigi'},
        {'name':'Nakaseke'}, {'name':'Nakasongola'}, {'name':'Rakai'}, 
        {'name':'Sembabule'},{'name':'Bududa'}, {'name':'Bugiri'}, {'name':'Busia'},
        {'name':'Kaberamaido'}, {'name':'Kaliro'}, {'name':'Kapchorwa'},
        {'name':'Katakwi'}, {'name':'Kibuku'}, {'name':'Manafwa'}, 
        {'name':'Namayingo'},{'name':'Namutumba'}, {'name':'Pallisa'}, {'name':'Serere'},
        {'name':'Sironko'}, {'name':'Katakwi'}, {'name':'Adjumani'},
        {'name':'Apac'}, {'name':'Dokolo'}, {'name':'Kitgum'}, 
        {'name':'Koboko'},{'name':'Kotido'}, {'name':'Lira'}, {'name':'Moroto'},
        {'name':'Napak'}, {'name':'Nebbi'}, {'name':'Rukunjiri'},
        {'name':'Ntungamo'}, {'name':'Masindi'}, {'name':'Kyenjojo'}, 
        {'name':'Kyegegwa'},{'name':'Kisoro'}, {'name':'Kiryandongo'}, {'name':'Kiruhura'},
        {'name':'Kanungu'}, {'name':'Kamwenge'}, {'name':'Kabarole'},
        {'name':'Isingiro'}, {'name':'Ibanda'}, {'name':'Bundibugyo'}, 
        {'name':'Bulisa'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)

if __name__=='__main__':
    app.run(debug=True)