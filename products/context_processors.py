def user_email(request):
    if request.user.is_authenticated:
        return {'user_email': request.user.email}
    return {user_email: 'Please login into your account'}
