# custom_filters.py

from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def calculate_days_hours_since(value):
    print(value)
    if value:
        now = timezone.now()  # Use timezone.now() to ensure a timezone-aware datetime
        duration = now - value
        days = duration.days
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        return f"{days} days, {hours} hours, {minutes} minutes ago"
    return ""
