from django.shortcuts import render


def csrf_failure(request, reason=""):
    """Default view for CSRF failures."""
    return render(
        request,
        "404.html",
        {"reason": reason},
        status=403,
    )
