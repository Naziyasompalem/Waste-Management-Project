def user_email(request):
    if request.user.is_authenticated:
        return {'user_email': request.user.email}
    return {user_email: 'Please login into your account'}

def is_user(request):
    print(str(request.user))
    return {'user': None if str(request.user)=="AnonymousUser" else request.user}