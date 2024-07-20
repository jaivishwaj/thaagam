def superuser(user):
    return user.is_superuser

def staff(user):
    return user.is_staff