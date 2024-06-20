from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView

from user_profile.serializers import UserSerializer


class RetrieveUserOwnProfileView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
