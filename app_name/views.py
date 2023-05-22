from urllib.parse import quote_plus, urlencode

from django.conf import settings
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect("profile")
    else:
        return render(request, "index.html")


@login_required
def profile(request):
    user = request.user

    auth0_user = user.social_auth.get(provider='auth0', uid=user.uid)
    # print(request.user.social_auth.values_list('provider'))

    # print(dir(user))
    # print(dir(auth0_user))

    context = {
        'uid': auth0_user.uid,
        'user_id': auth0_user.user_id,
        'user': auth0_user.user,
        'picture': auth0_user.extra_data['picture'],
    }

    # request.user.save()
    # auth0_user.save()

    return render(request, 'profile.html', context=context)


def logout_view(request):
    django_logout(request)

    return redirect(
        f"https://{settings.SOCIAL_AUTH_AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.SOCIAL_AUTH_AUTH0_KEY,
            },
            quote_via=quote_plus,
        ),
    )
