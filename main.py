
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

carlist = {0: {'Name': 'Pat', 'Brand': 'Ford', 'mileage': 10000, 'mpg': 12},
           1: {'Name': 'Dean', 'Brand': 'Ford', 'mileage': 600, 'mpg': 55},
           2: {'Name': 'Sam', 'Brand': 'Lexus', 'mileage': 234156, 'mpg': 33},
           3: {'Name': 'Dude', 'Brand': 'Acura', 'mileage': 35, 'mpg': 5}}


def partition(types, carlist, l, h):
    pivot = carlist[h][types]
    i = l - 1

    for j in range(l,h):
        if carlist[j][types] < pivot:
            i += 1
            carlist[i],carlist[j] =carlist[j],carlist[i]
    carlist[i+1], carlist[h] = carlist[h], carlist[i+1]
    return i+1


def qsort(types,carlist, l, h):
    if l < h:
        part = partition(types, carlist, l, h)
        qsort(types,carlist, l, part-1)
        qsort(types, carlist, part+1, h)


@app.route('/')
def my_form():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def login():
    i = len(carlist)
    carlist[i] = {'HASH': 0, 'Name': request.form['name'], 'Brand': request.form['brand'], 'mileage': request.form['mileage'], 'mpg': request.form['mpg']}

    return redirect(url_for('printing'))


@app.route('/print')
def printing():
    return render_template('print.html', carlist=carlist)


@app.route('/print', methods=['POST'])
def sorting():
    qsort(request.form['type'], carlist, 0, len(carlist)-1)
    return render_template("print.html", carlist=carlist)


if __name__ == '__main__':
    app.run()