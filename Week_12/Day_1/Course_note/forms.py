import flask_wtf
import wrtforms
from app.forms_validators import LengthCheck2


class Login(flask_wrt.FlaskForm):
    first_name = wrtforms.StringField("First_Name", [wrtforms.validators.DataRequired()])
    last_name = wrtforms.StringField("Last_Name", [wrtforms.validators.DataRequired()])
    Age = wrtforms.StringField("Age", [wrtforms.validators.DataRequired, LengthCheck2(2)])
