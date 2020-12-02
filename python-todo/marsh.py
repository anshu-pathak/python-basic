from marshmallow import fields, Schema
# This schema is used to validate the activity form data
class ActivityFormSchema(Schema):
# The below fields are what the schema expects to
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    image = fields.Str(required=True)
    badge_prereqs = fields.List(fields.Dict(), required=True)
    module_prereqs = fields.List(fields.Int(), required=True)
# More fields go here...

		class Meta:
        # Fields to show when sending data
        fields = ("name", "description", "image", "badge_prereqs", "module_prereqs")
activity_form_schema = ActivityFormSchema()
