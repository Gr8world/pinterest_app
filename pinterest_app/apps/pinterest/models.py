# pinterest_app/models.py

from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    """
    Stores the authenticated user’s basic Pinterest profile info.
    """
    pinterest_id      = models.CharField(max_length=64, unique=True)
    username          = models.CharField(max_length=128)
    bio               = models.TextField(blank=True)
    profile_image     = models.URLField(blank=True)
    followers_count   = models.IntegerField(null=True, blank=True)
    following_count   = models.IntegerField(null=True, blank=True)
    last_synced       = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username} ({self.pinterest_id})"


class Board(models.Model):
    """
    Represents a Pinterest board belonging to a UserProfile.
    """
    pinterest_id      = models.CharField(max_length=64, unique=True)
    name              = models.CharField(max_length=255)
    description       = models.TextField(blank=True)
    follower_count    = models.IntegerField(null=True, blank=True)
    cover_image       = models.URLField(blank=True)
    user_profile      = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='boards')
    last_synced       = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.pinterest_id})"


class Pin(models.Model):
    """
    Represents a Pin under a specific Board.
    """
    pinterest_id      = models.CharField(max_length=64, unique=True)
    title             = models.CharField(max_length=255, blank=True)
    description       = models.TextField(blank=True)
    image_url         = models.URLField(blank=True)
    link              = models.URLField(blank=True)
    media_type        = models.CharField(max_length=16, blank=True)  # e.g. "image" or "video"
    created_at        = models.DateTimeField(null=True, blank=True)
    board             = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='pins')
    save_count        = models.IntegerField(default=0)
    last_synced       = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title or '(No Title)'} ({self.pinterest_id})"


class PinAnalytics(models.Model):
    """
    Stores analytics metrics for a single Pin.
    One-to-one with Pin.
    """
    pin               = models.OneToOneField(Pin, on_delete=models.CASCADE, related_name='analytics')
    impression_count  = models.IntegerField(default=0)
    save_count        = models.IntegerField(default=0)
    outbound_clicks   = models.IntegerField(default=0)
    engagement_count  = models.IntegerField(default=0)
    last_fetched      = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Analytics for {self.pin.pinterest_id}"
