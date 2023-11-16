from .models import Profile, Relationship
from django.db.models import Q


def request_received(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        request_available = Relationship.objects.filter(
            Q(receiver=profile) & Q(status="send"))
        return {'request_count': len(request_available)}
    return {}
