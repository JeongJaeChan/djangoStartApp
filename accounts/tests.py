# from django.test import TestCase
# from rest_framework.views import APIView
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi


# # Create your tests here.

# class Test(APIView):
#     bstopId = openapi.Parameter('stationId', openapi.IN_QUERY, description='정류소 고유번호', required=True, default=165000381, type=openapi.TYPE_NUMBER)
    
#     @swagger_auto_schema(manual_parameters=[bstopId], responses={200: "Success"})
#     def get(self, request):
#         bstopId = request.GET.get("stationId", None)