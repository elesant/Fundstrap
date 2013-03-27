from django.utils import simplejson
from django.http import HttpResponse


# Status Codes: http://en.wikipedia.org/wiki/List_of_HTTP_status_codes
def build_response(response, mimetype='application/json', status=200):
    return HttpResponse(simplejson.dumps(response), mimetype=mimetype, status=status)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    return client_ip


def prepare_response(request):
    response = {}
    meta_data = {}
    meta_data['request_uri'] = request.build_absolute_uri()
    meta_data['get'] = request.GET
    meta_data['post'] = request.POST
    meta_data['ip'] = get_client_ip(request)
    if 'sessionid' in request.COOKIES:
        meta_data['session_id'] = request.COOKIES['sessionid']
    if 'csrftoken' in request.COOKIES:
        meta_data['csrf_token'] = request.COOKIES['csrftoken']
    meta_data['user_agent'] = request.META['HTTP_USER_AGENT']
    if request.user.is_authenticated():
        meta_data['current_user_id'] = request.user.id
    response['meta'] = meta_data
    return response
