from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
import csv
from pinterest_app.apps.pinterest.services import board_service, analytics_service

@require_GET
def get_boards_api(request):
    token = request.session.get('access_token')
    data = board_service.get_user_boards(token)
    return JsonResponse(data)

@require_GET
def get_board_pins_api(request, board_id):
    token = request.session.get('access_token')
    data = board_service.get_pins_for_board(token, board_id)
    return JsonResponse(data)

@require_GET
def get_pin_analytics_api(request, pin_id):
    token = request.session.get('access_token')
    data = analytics_service.get_pin_analytics(token, pin_id)
    return JsonResponse(data)

@require_GET
def audience_insights_view(request):
    token = request.session.get('access_token')
    data = analytics_service.get_audience_insights(token)
    return JsonResponse(data)

@require_GET
def export_analytics_csv(request):
    token = request.session.get("access_token")
    board_id = request.GET.get("board_id")
    pins_data = board_service.get_pins_for_board(token, board_id).get("items", [])

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="analytics.csv"'
    writer = csv.writer(response)
    writer.writerow(["Pin ID", "Title", "Impressions", "Saves", "Outbound Clicks", "Engagements"])

    for pin in pins_data:
        pin_id = pin.get("id")
        analytics = analytics_service.get_pin_analytics(token, pin_id).get("metrics", {})
        writer.writerow([
            pin_id,
            pin.get("title", ""),
            analytics.get("impression", {}).get("value", 0),
            analytics.get("save", {}).get("value", 0),
            analytics.get("outbound_click", {}).get("value", 0),
            analytics.get("engagement", {}).get("value", 0),
        ])
    return response
