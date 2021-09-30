# from apps.users.models import User
#
#
# def register_user(data):
#
#     # user registration logic goes here
#     name = data['first_name'] +' '+ data['last_name']
#     user = User(
#         username=data['email'],
#         first_name=data['first_name'],
#         last_name=data['last_name'],
#         name=name,
#         nic=data['nic'],
#         email=data['email'],
#         contact_no=data['contact_no'],
#     )
#     user.set_password(data['password'])
#     user.save()
#     return user
#
