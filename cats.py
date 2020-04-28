from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import csv

app = Flask(__name__)
Bootstrap(app)
application = app


def convert_to_dict(filename):
    """
    Convert a CSV file to a list of Python dictionaries
    """
    # open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')

    # create DictReader object
    my_reader = csv.DictReader(datafile)

    # create a regular Python list containing dicts
    list_of_dicts = list(my_reader)

    # close original csv file
    datafile.close()

    # return the list
    return list_of_dicts

# create a list of dicts from a CSV
cats_list = convert_to_dict("cats.csv")

# create a list of tuples in which the first item is the number
# (Presidency) and the second item is the name (President)
pairs_list = []
for c in cats_list:
    pairs_list.append( (c['ID'], c['Breed']) )

# first route

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="The Alley")

# second route

@app.route('/breed/<num>')
def detail(num):
    try:
        cats_dict = cats_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for ID: {num}</h1>"
    # a little bonus function, imported on line 2 above
    #ord = make_ordinal( int(num) )
    return render_template('cats.html', cats=cats_dict, the_title=cats_dict['Breed'])


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)