from django.shortcuts import render
from rest_framework  import generics
from apps.accounts.api.serializers import SignupSerializer, VerifyOTPSerializer,LoginSerializer, UserListSerializer
from apps.accounts.permissions import IsAdmin
from apps.accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken



class SignupAPIView(generics.CreateAPIView):
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Check your email for OTP"},
            status=status.HTTP_201_CREATED
        )

class VerifyOTPAPIView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.context['user']
        otp_obj = serializer.context['otp_obj']

        otp_obj.is_used = True
        otp_obj.save()

        user.is_active = True
        user.email_verified = True
        user.save()

        return Response(
            {"message": "Email verified successfully"},
            status=status.HTTP_200_OK
        )
    

class LoginAPIView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data,status=status.HTTP_200_OK)
    

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        return Response({
            'email' : user.email,
            'username' : user.username,
            'role' : user.role
        })
    
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message' : 'Logged out successfully'})
        except Exception:
            return Response({"error": "Invalid token"}, status=400)


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = User.objects.all()
    serializer_class = UserListSerializer