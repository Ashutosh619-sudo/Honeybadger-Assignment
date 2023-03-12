from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import send_slack_alert
from .enums import NotificationType


# Create your views here.

class Alert(APIView):

    def post(self,request):

        request_data = request.data

        if request_data.get("Email") == None or request_data["Email"] == "":
            return Response(data={"data":"the slack alert payload must have a email address"}, status=status.HTTP_400_BAD_REQUEST)

        if request_data["Type"] != NotificationType.spam_notification.value:
            return Response(data={"data":"only sends slack alert if the payload has a Type SpamNotification"}, status=status.HTTP_400_BAD_REQUEST)

        send_slack_alert(request_data)

        return Response(data={"data":"succesfully sent the alert"}, status=status.HTTP_200_OK)

