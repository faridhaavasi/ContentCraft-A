from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from apps.authentication.api.v1.serializers.register_serializer import SteponeRegisterSerializer

class SteponeRegisterView(CreateAPIView):
    serializer_class = SteponeRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = serializer.create_user(email=email, password=password)
            token = AccessToken.for_user(user)
            return Response({'token': str(token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
