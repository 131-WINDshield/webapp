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
    carlist[i] = {'Name': request.form['name'].strip(), 'Brand': request.form['brand'].strip(), 'mileage': int(request.form['mileage']), 'mpg': int(request.form['mpg'])}

    return redirect(url_for('printing'))

@app.route('/front')
def front():
    return render_template('front.html')


@app.route('/print')
def printing():
    return render_template('print.html', carlist=carlist)


@app.route('/print', methods=['POST'])
def sorting():
    qsort(request.form['type'], carlist, 0, len(carlist)-1)
    return render_template("print.html", carlist=carlist)


@app.route('/search')
def search():
    return render_template('search.html', carlist=carlist)


@app.route('/search', methods=['POST'])
def find():
    type = request.form['type']
    searchlist = []
    print(searchlist)
    searched = request.form['searched']
    if searched == "":
        searchlist = "Please type in something to search"
        return render_template('search.html', Searched=searchlist)
    if type == "mpg" or type == "mileage":
        if searched.isdigit():
            rangelow = round(float(searched) * 0.95)
            rangehigh = round(float(searched) *1.05)
            for i in range(len(carlist)):
                if rangehigh > carlist[i][type] > rangelow:
                    searchlist.append(carlist[i])
        else:
            searchlist = "Please type in a number for MPG pr Mileage searches"
    if type == "Brand":
        for i in range(len(carlist)):
            if carlist[i][type] == searched:
                searchlist.append(carlist[i])
    if searched == "":
        searchlist = "Please type in something to search"
    elif not searchlist:
        searchlist = "Sorry no results"
    return render_template('search.html', Searched=searchlist)



if __name__ == '__main__':
    app.run()