from flask import Flask, render_template, request
from backend_folder.db_model import insert_measurement, init_db
from backend_folder.utility import calculate_real_size

app = Flask(__name__,

template_folder="Web_part/Web_template", 
    static_folder="Web_part/Web_template/Static"   )

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        try:
            username = request.form["username"]
            microscope_size = float(request.form["size"])
            magnification = float(request.form["magnification"])

            actual_size = calculate_real_size(microscope_size, magnification)

            # Save to database
            insert_measurement(username, microscope_size, actual_size)

            result = f"Actual size is {actual_size:.2f} units"

        except ValueError as ve:
            result = f"Error: {ve}"
        except Exception as e:
            result = f"Something went wrong: {e}"

    return render_template("main.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port)
