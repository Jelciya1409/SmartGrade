from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():

    student_name = request.form.get("student_name")
    register_number = request.form.get("register_number")
    semester = request.form.get("semester")
    subjects = request.form.get("subjects")
    attendance = request.form.get("attendance")
    assignment_marks = request.form.get("assignment_marks")
    unit_test_1 = request.form.get("unit_test_1")
    unit_test_2 = request.form.get("unit_test_2")
    previous_gpa = request.form.get("previous_gpa")
    # Convert input values to numbers
    attendance = float(attendance)
    assignment_marks = float(assignment_marks)
    unit_test_1 = float(unit_test_1)
    unit_test_2 = float(unit_test_2)

    # Calculate overall score
    total_score = (
        attendance +
        assignment_marks +
        unit_test_1 +
        unit_test_2
    ) / 4

    # Calculate percentage
    percentage = total_score

    # Grade calculation
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return render_template(
        "result.html",
        student_name=student_name,
        register_number=register_number,
        semester=semester,
        subjects=subjects,
        attendance=attendance,
        assignment_marks=assignment_marks,
        unit_test_1=unit_test_1,
        unit_test_2=unit_test_2,
        previous_gpa=previous_gpa,
        total_score=total_score,
        percentage=percentage,
        grade=grade
    )

if __name__ == "__main__":
    app.run(debug=True)