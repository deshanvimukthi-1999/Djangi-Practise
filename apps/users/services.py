from apps.users.models import User


def register_user(data):

    # user registration logic goes here
    name = data['first_name'] + ' ' + data['last_name']
    user = User(
        username=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        name=name,
        email=data['email'],
    )
    user.set_password(data['password'])
    user.save()
    return user


def delete_user(user_id):
    user: User = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()

    return user

