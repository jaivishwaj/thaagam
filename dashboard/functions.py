def is_superuser(user):
    return user.is_superuser  # or any other logic to determine an admin


def is_administrator(user):
    return user.groups.filter(name="Administrator").exists() or is_superuser(user)


def superuser_or_administrator(user):
    return is_superuser(user) or is_administrator(user)


def is_staff(user):
    return (
        is_superuser(user)
        or is_administrator(user)
    )