from flask import Flask, render_template, request
import random as rd

app = Flask(__name__)

boys = list(range(1, 20))
girls = list(range(20, 39))

@app.route('/', methods=['GET', 'POST'])
def home():
    global boys, girls
    if request.method == 'POST':
        if 'shuffle' in request.form:
            boys = list(range(1, 20))
            girls = list(range(20, 39))
            listp = []
            while boys and girls:
                b = rd.choice(boys)
                d = boys.index(b)
                boys.pop(d)
                g = rd.choice(girls)
                e = girls.index(g)
                girls.pop(e)
                c = list((b, g))
                listp.append(c)
            row_1 = listp[0:4]
            row_2 = listp[4:9]
            row_3 = listp[9:14]
            row_4 = listp[14:23]
            return render_template('home.html', row_1=row_1, row_2=row_2, row_3=row_3, row_4=row_4)
        elif 'reshuffle' in request.form:
            listp = []
            while boys and girls:
                b = rd.choice(boys)
                d = boys.index(b)
                boys.pop(d)
                g = rd.choice(girls)
                e = girls.index(g)
                girls.pop(e)
                c = list((b, g))
                listp.append(c)
            row_1 = listp[0:4]
            row_2 = listp[4:9]
            row_3 = listp[9:14]
            row_4 = listp[14:23]
            return render_template('home.html', row_1=row_1, row_2=row_2, row_3=row_3, row_4=row_4)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
