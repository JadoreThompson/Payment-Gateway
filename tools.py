from functools import wraps

from django.shortcuts import redirect

STRIPE_MICROSERVICE = 'http://127.0.0.1:4242'


# Custom wrapper for blocking logged-in users
def logout_required(function, redirect_url="/accounts/login"):
    """
    :param function:
    :param redirect_url:
    :return: Redirect to the login page if the user is logged in
    - In theory to be used for the onboarding page, looking for a specific marker
        to indicate they aren't fully onboarded, for example having an onboarding column with True / False.
        If false they can access. To be done in production. For now concept can be seen here
    """
    def decorator(func):
        @wraps(func)
        def function_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)
            return func(*args, **kwargs)
        return function_wrapper

    if function:
        return decorator(function)
    return decorator
