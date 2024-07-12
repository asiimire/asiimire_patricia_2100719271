from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# species list
species_list = [
    {'name': 'Lion', 'habitat': 'Savannah'},
    {'name': 'Tiger', 'habitat': 'Jungle'},
    {'name': 'Elephant', 'habitat': 'Africa'},
    {'name': 'Giraffe', 'habitat': 'Mountain'},
    {'name': 'Panda', 'habitat': 'Forest'},
    {'name': 'Bird', 'habitat': 'Grassland'},
    {'name': 'Fish', 'habitat': 'Water'},
    {'name': 'Whale', 'habitat': 'Ocean'},
    {'name': 'Snail', 'habitat': 'Earth'},
    {'name': 'Ant', 'habitat': 'Antennae'},
    {'name': 'Spider', 'habitat': 'Web'},
    {'name': 'Octopus', 'habitat': 'Sea'},
    {'name': 'Squirrel', 'habitat': 'Forest'},
    {'name': 'Turtle', 'habitat': 'Water'},
    {'name': 'Dolphin', 'habitat': 'Ocean'},
    {'name': 'Goose', 'habitat': 'Grassland'},
    {'name': 'Bat', 'habitat': 'Antennae'},
    {'name': 'Hippopotamus', 'habitat': 'Mountain'},
    {'name': 'Bear', 'habitat': 'Savannah'},
    {'name': 'Kangaroo', 'habitat': 'Africa'},
    {'name': 'Giraffe', 'habitat': 'Mountain'}
]

@app.route('/')
def index():
    return render_template('index.html', species_list=species_list)

@app.route('/add', methods=['GET','POST'])
def add_species():
    if request.method == 'POST':
        name = request.form['name']
        habitat = request.form['habitat']
        species_list.append({'name': name, 'habitat': habitat})
        return redirect(url_for('index'))
    return render_template('add_species.html')

if __name__ == '__main__':
    app.run(debug=True)