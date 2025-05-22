from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            role = serializer.validated_data['role']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email, role=role)
                if not user.is_active:
                    return Response({"error": "Account is disabled"}, status=status.HTTP_403_FORBIDDEN)

                if user.check_password(password):
                    return Response({
                        "email": user.email,
                        "username": user.username,
                        "role": user.role,
                        "message": "Login successful"
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

            except User.DoesNotExist:
                return Response({"error": "Invalid email or role"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
