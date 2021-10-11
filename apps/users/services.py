from apps.users.models import Company, User


def register_user(data):

    # user registration logic goes here
    user = User(
        username=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],

    )
    user.set_password(data['password'])
    user.save()

    # create company for registered user
    company = Company(type=data['company_type'])
    company.name = data.get('company_name', None)
    company.save()

    # Set company owner
    company.owner = user
    company.save()

    return user


def delete_user(user_id):
    user: User = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()

    return user
