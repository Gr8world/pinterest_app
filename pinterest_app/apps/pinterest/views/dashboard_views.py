from django.shortcuts import render, redirect

from pinterest_app.apps.pinterest.forms.filters import AnalyticsFilterForm

# pinterest_app/views/home_views.py
# from django.shortcuts import redirect

# def root_redirect(request):
#     if request.session.get('access_token'):
#         return redirect('dashboard')
#     return redirect('login')


# def dashboard_view(request):
#     if not request.session.get('access_token'):
#         return redirect('login')
#     form = AnalyticsFilterForm(request.GET or None)
#     return render(request, 'pinterest_app/dashboard.html', {'filter_form': form})


# pinterest_app/views/dashboard_views.py

from django.contrib import messages
from pinterest_app.apps.pinterest.models import UserProfile

def dashboard_view(request):
    """
    Renders the dashboard.html template. 
    - If there’s no access_token in session, redirect to login.
    - Otherwise, fetch the most recently synced UserProfile and attach it to request.
    - Pass the filter_form and request into the template context.
    """
    if not request.session.get('access_token'):
        return redirect('login')

    try:
        user_profile = UserProfile.objects.latest('last_synced')
    except UserProfile.DoesNotExist:
        messages.info(request, "No Pinterest profile found. Click “Sync Profile” to begin.")
        user_profile = None

    # Attach to request so the template’s `{% with userp = request.user_profile %}` works
    request.user_profile = user_profile

    form = AnalyticsFilterForm(request.GET or None)
    return render(request, 'pinterest_app/dashboard.html', {
        'filter_form': form,
        'request': request,
    })
