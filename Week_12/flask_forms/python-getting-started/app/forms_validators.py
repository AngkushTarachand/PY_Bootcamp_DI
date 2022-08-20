import wtforms


def my_length_check(max_value):
	def __my_length_check(form, field):
		if len(field.data) > max_value:
			raise wtforms.ValidationError(f'Field must be less than {max_value} characters')

	return __my_length_check


class MyLengthCheckV2:
	def __init__(self, max_value):
		self.max_value = max_value

	def __call__(self, form, field):
		if len(field.data) > self.max_value:
			raise wtforms.ValidationError(f'Field must be less than {self.max_value} characters (V2 validator)')
