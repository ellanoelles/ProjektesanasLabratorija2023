from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('jauns.html')


    import cx_Oracle
    connection = cx_Oracle.connect("SYSTEM/Kaskurkad7@localhost:1521/ORCLSS")
    cursor = connection.cursor()

    cursor.execute("SELECT PEĻŅA FROM PASŪTIJUMI")
    data = cursor.fetchall()

    cursor.close()
    connection.close()
    print(data)



def calculate_average_profit(book, cover, volume, cursor=None):
    cursor.execute("SELECT peļņa FROM PASUTIJUMI WHERE grāmata = :1 AND tips = :2 AND apjoms = :3",
                   (book, cover, volume))
    profits = cursor.fetchall()
    total_profit = sum(profit[0] for profit in profits)
    return total_profit / len(profits) if len(profits) > 0 else 0


@app.route('/')
def index():
    return render_template('jauns.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    book = request.form['book']
    cover = request.form['cover']
    volume = request.form['volume']

    average_profit = calculate_average_profit(book, cover, volume)
    return f'Vidējā peļņa grāmatai {book}, ar {cover} vāku un apjomu {volume} ir: {average_profit}'


if __name__ == "__main__":
    app.run(debug=True)