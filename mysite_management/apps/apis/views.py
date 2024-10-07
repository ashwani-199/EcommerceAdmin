from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from mysite_management.common_module.mainService import MainService
from apps.apis import setException, responseData
from apps.apis.UserApi.ApiMessages import CommonApiMessages, UserApiMessages
from apps.users.serializers import RegisterUserSerializer


@swagger_auto_schema(
    method='post',
    request_body=RegisterUserSerializer,
    responses=responseData
)
@api_view(['POST'])
def register(request):
    resData = dict()
    # Initialize register UserApi serializer to validate data
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Make response data success case
        resData['status'] = "SUCCESS"
        resData['data'] = None
        resData['message'] = "User is register successfully."
        resData['errors'] = []
        status_code = 200
    else:
        # Make response data fail case
        res = setException(serializer)
        resData['status'] = "Error"
        resData['data'] = {}
        resData['message'] = res.get('message')
        resData['errors'] = res.get('errors')
        status_code = 200
    return Response(resData, status=status_code)

    