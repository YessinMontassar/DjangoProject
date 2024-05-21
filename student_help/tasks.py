from celery import shared_task
from .models import Post
from datetime import datetime, timedelta

@shared_task
def cleanup_old_posts():
    threshold_date = datetime.now() - timedelta(days=30)
    Post.objects.filter(date_posted__lt=threshold_date).delete()
