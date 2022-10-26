from flask_wtf import FlaskForm
from wtforms import StringField,validators,IntegerField,SelectField,SubmitField,ValidationError,DateField
from .models import Position

class PostionForm(FlaskForm):
    name = StringField(label='Name',validators=[validators.DataRequired()])
    wage = IntegerField(label='Wage ',validators=[validators.DataRequired()])
    department = StringField(label='department')
    submit = SubmitField(label='Ok')


    def validate_wage(self,wage):
        if wage.data <= 0:
            raise ValidationError('Nelzya vvodit otricatelnye chisla')


class EmployeeForm(FlaskForm):
    name = StringField(label='Name',validators=[validators.DataRequired()])
    birth_date = DateField(label='birth date',validators=[validators.DataRequired()])
    position_id = SelectField(label='postion',validators=[validators.DataRequired()])
    submit = SubmitField(label='Ok')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for p in Position.query.all():
            result.append((p.id, p.name))
        self.position_id.choices = result
