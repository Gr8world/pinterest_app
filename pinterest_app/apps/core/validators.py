from django.core.exceptions import ValidationError

def validate_date_format(date_str):
    # Ensure YYYY-MM-DD format
    import re
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        raise ValidationError('Date must be in YYYY-MM-DD format')
