from flask import Flask, render_template, request
import jinja2
import uuid

app = Flask(__name__, template_folder="./templates", static_folder="./static")

def gen_template_string(name:str, surname: str, gender: int, age: int):
    template_string = render_template(
        "card.html",
        firstName = name,
        lastName = surname,
        gender = gender,
        age = age
    )
    return template_string


@app.get("/")
def return_index():
    return render_template("index.html")

@app.post("/generate_card")
def gen_card():
    name = request.form["firstName"]
    surname = request.form["lastName"]
    gender = request.form["gender"]
    age = int(request.form["age"])

    uniq_data = """
        <p><strong>Уникальный id:</strong> {{uniq_id}}</p>
    </div>
</body>
</html>
    """
    final_template_string = gen_template_string(name, surname, gender, age) + uniq_data
    return jinja2.Template(final_template_string).render(
        uniq_id = uuid.uuid4()
    )

if __name__ == "__main__":
    app.run("0.0.0.0", 9000)
