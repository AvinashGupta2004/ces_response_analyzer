from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load CSV file
df = pd.read_csv('./CES Induction Form 2025.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    names = df['Your Full Name'].dropna().unique().tolist()
    columns = df.columns.tolist()
    result = ""

    if request.method == 'POST':
        selected_name = request.form.get('name')
        selected_column = request.form.get('column')

        # Filter the row for selected name
        filtered = df[df['Your Full Name'] == selected_name]

        if not filtered.empty and selected_column in filtered.columns:
            value = filtered[selected_column].values[0]
            result = f"{selected_column} for {selected_name}:\n\n{value}"
        else:
            result = "No data found or invalid column selected."

    return render_template('index.html', names=names, columns=columns, result=result)

if __name__ == '__main__':
    app.run(debug=True)
