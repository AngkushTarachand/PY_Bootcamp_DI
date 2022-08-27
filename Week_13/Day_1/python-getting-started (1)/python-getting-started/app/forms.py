import flask_wtf
import wtforms
from app.forms_validators import my_length_check
from app.forms_validators import MyLengthCheckV2


class Login(flask_wtf.FlaskForm):
	username = wtforms.StringField("Email", [wtforms.validators.DataRequired(),
	                                         wtforms.validators.Email(message="Please enter a valid Email")])
	password = wtforms.PasswordField("Password",
	                                 [wtforms.validators.DataRequired(),
	                                  MyLengthCheckV2(max_value=10)
	                                  # my_length_check(max_value=10),
	                                  # wtforms.validators.Length(min=4, max=10)
	                                  ])

	age_grater_than_18 = wtforms.BooleanField("is your age is grater the 18")
	hoppyies = wtforms.RadioField(choices=["coding", "reading", "sleeping"])

	hoppyies_select = wtforms.SelectField(choices=["coding", "reading", "sleeping"])


	cv = wtforms.MultipleFileField()

	submit = wtforms.SubmitField("Submit")


class Register(flask_wtf.FlaskForm):
	username = wtforms.StringField("Email")
	password = wtforms.PasswordField("Password")

	submit = wtforms.SubmitField("Submit")
