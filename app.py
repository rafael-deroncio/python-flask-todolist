from flask import Flask, render_template, request, redirect, url_for, render_template_string

app = Flask(__name__, template_folder='./')

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("index"))


@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    if 0 <= id < len(tasks):
        tasks.pop(id)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
