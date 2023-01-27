from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRoutes(request):
  routes = [
    {
      'Endpoint': 'api/',
      'method': 'GET',
      'body': None,
      'description': 'Returns an urls to busstop location'
          
    },
    {
      'Endpoint': 'api/busroutes/',
      'method': 'GET',
      'body': None,
      'description': 'Returns an array of locations'
    },
    {
      'Endpoint': 'api/busroutes/id',
      'method': 'GET',
      'body': None,
      'description': 'Returns a single location object'
    },
    {
      'Endpoint': 'api/busroutes/create',
      'method': 'POST',           
      'description': 'Creates a new location with data sent in post request'
    },
    {
      'Endpoint': 'api/busroutes/id/update',
      'method': 'PUT',
      'description': 'Updates an existing location with data sent in the request'
    },
    {
      'Endpoint': 'api/busroutes/id/delete',
      'method': 'DELETE',
      'description': 'Deletes an existing location'
    },
  ]
  return Response(routes)