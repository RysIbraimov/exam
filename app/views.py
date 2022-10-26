from flask import render_template,request,flash,redirect,url_for
from . import app,db
from .models import Position,Employee
from .forms import PostionForm,EmployeeForm

def index():
    employee = Employee.query.all()
    return render_template('index.html',employees=employee)

def position_create():
    form = PostionForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            position = Position()
            form.populate_obj(position)
            db.session.add(position)
            db.session.commit()
            flash(f'{position.name} dobavlen',category='success')
            return redirect(url_for('index'))
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(f'{error} in field {field}',category='danger')

    return render_template('position_form.html',form=form)

def position_delete(position_id):
    position = Position.query.filter_by(id=position_id).first()
    if request.method == 'GET':
        return render_template('position_delete.html',position=position)
    if request.method == 'POST':
        db.session.delete(position)
        db.session.commit()
        flash(f'{position.name} deleted')
        return redirect(url_for('index'))

def position_update(position_id):
    position = Position.query.filter_by(id=position_id).first()
    form = PostionForm(request.form, obj=position)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(position)
            db.session.commit()
            flash(f'{position.name} obnavlen',category='success')
            return redirect(url_for('index'))
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(f'{error} in field {field}',category='danger')

    return render_template('position_form.html',form=form)

def employee_create():
    form = EmployeeForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            employee = Employee()
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            flash(f'{employee.name} created')
            return redirect(url_for('index'))
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(f'{error} in field {field}')

    return render_template('employee_form.html',form=form)

def employee_detail(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    return render_template('employee_detail.html', employee=employee)

def employee_delete(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    if request.method == 'GET':
        return render_template('employee_delete.html',employee=employee)
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        flash(f'{employee.name} deleted')
        return redirect(url_for('index'))

def employee_update(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    form = EmployeeForm(request.form, obj=employee)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(employee)
            db.session.commit()
            flash(f'{employee.name} obnavlen',category='success')
            return redirect(url_for('index'))
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(f'{error} in field {field}',category='danger')

    return render_template('employee_form.html',form=form)





