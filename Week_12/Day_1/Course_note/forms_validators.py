import wrtforms

class LengthCheck2:
    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, *args, **kwargs):
        if len(field.data) > self.max_value:
            raise wrforms.ValidationError(f"Field must be less than {self.max_value} characters")

