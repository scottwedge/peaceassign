from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "company_name", "city", "state", "zip", "website", "email", "age")
