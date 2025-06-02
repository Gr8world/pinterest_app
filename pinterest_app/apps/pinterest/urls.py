from django.urls import path
from pinterest_app.apps.pinterest.views.oauth_views import login_view, callback_view
from pinterest_app.apps.pinterest.views.dashboard_views import dashboard_view
from pinterest_app.apps.pinterest.views.api_views import (
    get_boards_api, get_board_pins_api, get_pin_analytics_api,
    audience_insights_view, export_analytics_csv
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('callback/', callback_view, name='callback'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('api/boards/', get_boards_api, name='api_boards'),
    path('api/boards/<str:board_id>/pins/', get_board_pins_api, name='api_board_pins'),
    path('api/pins/<str:pin_id>/analytics/', get_pin_analytics_api, name='api_pin_analytics'),
    path('api/audience-insights/', audience_insights_view, name='api_audience_insights'),
    path('api/export/csv/', export_analytics_csv, name='api_export_csv'),
]







"""# pinterest_app/urls.py
from django.urls import path
from pinterest_app.views.home_views import root_redirect
from pinterest_app.views.oauth_views import login_view, callback_view, set_dummy_token
from pinterest_app.views.dashboard_views import dashboard_view
from pinterest_app.views.api_views import (
    get_boards_api, get_board_pins_api, get_pin_analytics_api,
    audience_insights_view, export_analytics_csv
)
from pinterest_app.views.sync_views import (
    sync_profile, sync_boards, sync_pins, sync_all_pins, sync_analytics
)

urlpatterns = [
    # ← This line handles “GET /” and redirects appropriately
    path('', root_redirect, name='root_redirect'),

    path('login/', login_view, name='login'),
    path('callback/', callback_view, name='callback'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('set-fake-token/', set_dummy_token, name='set_dummy_token'),

    path('api/boards/', get_boards_api, name='api_boards'),
    path('api/boards/<str:board_id>/pins/', get_board_pins_api, name='api_board_pins'),
    path('api/pins/<str:pin_id>/analytics/', get_pin_analytics_api, name='api_pin_analytics'),
    path('api/audience-insights/', audience_insights_view, name='api_audience_insights'),
    path('api/export/csv/', export_analytics_csv, name='api_export_csv'),

    path('sync/profile/', sync_profile, name='sync_profile'),
    path('sync/boards/', sync_boards, name='sync_boards'),
    path('sync/boards/<str:board_id>/pins/', sync_pins, name='sync_pins'),
    path('sync/all-pins/', sync_all_pins, name='sync_all_pins'),
    path('sync/analytics/', sync_analytics, name='sync_analytics'),
]
"""