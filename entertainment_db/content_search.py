from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def search_bar(request):
    activitie_id = request.GET.get('activitie_id', None)
    data = {'price': Activities.objects.get(id=int(activitie_id)).price}
    return JsonResponse(data)