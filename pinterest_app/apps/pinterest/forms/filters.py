from django import forms

class AnalyticsFilterForm(forms.Form):
    board_id = forms.CharField(required=False, widget=forms.HiddenInput())
    date_range = forms.ChoiceField(choices=[
        ('7d', 'Last 7 Days'),
        ('30d', 'Last 30 Days'),
        ('90d', 'Last 90 Days'),
    ], required=False)
