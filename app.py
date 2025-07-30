from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from model import Student,db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Student.db'
db.init_app(app)

@app.route('/create',methods=['POST'])
def add_Student():
    data = request.get_json()
    name = data.get('name')
    subject = data.get('subject')
    grade = data.get('grade')
    new_Student = Student(name=name, subject=subject, grade=grade)
    db.session.add(new_Student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully!'}), 201

@app.route('/read', methods=['GET'])
def get_Students():
    students = Student.query.all()
    student_list =[]
    for student in students:
        student_list.append({
            "id" : student.id,
            "name" : student.name,
            "subject" : student.subject,
            "grade" : student.grade
        })
    return jsonify(student_list), 200

@app.route('/read/<int:id>', methods =['GET'])
def get(id):
    student_id = Student.query.get(id)
    if student_id:
        return jsonify({
                        "id": student_id.id,
                        "name": student_id.name,
                        "subject": student_id.subject,
                        "grade": student_id.grade})
    else:
        return jsonify("Student not found!"), 404
    
@app.route('/update/<int:id>',methods=['PUT'])
def update(id):
    data = request.get_json()
    student = Student.query.get(id)
    if not student:
        return jsonify({'message':'Student not Found!'}), 404

    student.name = data.get("name",student.name)
    student.subject = data.get("subject",student.subject)
    student.grade = data.get("grade",student.grade)
    db.session.commit()
    return jsonify({'message':'Student information updated!'}), 200
            
@app.route('/delete/<int:id>', methods=['DELETE'])
def del_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'message':'Student not Found!'}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message":"Student Information Deleted!"}), 200
    
if __name__ == '__main__':
    app.run()
    with app.app_context():
        db.create_all()
    print("Database created successfully!")
    

