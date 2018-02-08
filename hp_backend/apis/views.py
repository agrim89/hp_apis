from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, BaseUser, NoteBook, WorkStation, BusinessPC
from .serializers import BaseUserSerializer, CompanySerializer
import json, datetime

class UserDetail(APIView):

    def get(self, request):
        snippets = BaseUser.objects.all()
        serializer = BaseUserSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BaseUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            user = BaseUser.objects.get(username=request.data['username'])
            user.first_name = request.data['first_name'] if request.data['first_name'] else user.first_name
            user.last_name = request.data['last_name'] if request.data['last_name'] else user.last_name
            user.username = request.data['username'] if request.data['username'] else user.username
            user.dealer_name = request.data['dealer_name'] if request.data['dealer_name'] else user.dealer_name
            user.mobile = request.data['mobile'] if request.data['mobile'] else user.mobile
            user.email = request.data['email'] if request.data['email'] else user.email
            user.address = request.data['address'] if request.data['address'] else user.address
            user.gender = request.data['gender'] if request.data['gender'] else user.gender

            user.save()
            return Response(BaseUserSerializer(user).data, status=status.HTTP_202_ACCEPTED )
        except Exception:
            return Response(status='User Not Found')


class CompanyDetail(APIView):

    def get(self, request, format=None):
        snippets = Company.objects.all()
        serializer = CompanySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            user = Company.objects.get(company_namer=request.data['company_name'])
            user.company_name = request.data['company_name'] if request.data['company_name'] else user.company_name
            user.domain_name = request.data['domain_name'] if request.data['domain_name'] else user.domain_name
            user.partner_id = request.data['partner_id'] if request.data['partner_id'] else user.partner_id
            user.region = request.data['region'] if request.data['region'] else user.region
            user.location = request.data['location'] if request.data['location'] else user.location
            user.dedicated_person = request.data['dedicated_person'] if request.data['dedicated_person'] else user.dedicated_person
            user.email_id = request.data['email_id'] if request.data['email_id'] else user.email_id
            user.mobile = request.data['mobile'] if request.data['mobile'] else user.mobile

            user.save()
            return Response(BaseUserSerializer(user).data, status=status.HTTP_202_ACCEPTED )
        except Exception:
            return Response(status='User Not Found')


class ListDetail(APIView):
    def post(self, request):
        try:
            date = request.data["date"]
            mod_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            payload = dict()
            if date:
                bpc = BusinessPC.objects.filter(modified=mod_date).values('product', 'part_no', "specification_details",
                                                                             "processor", "screen_size", "warranty", "ram",
                                                                             "hard_disk", "operating_system", "screen",
                                                                             "price")
                work = WorkStation.objects.filter(modified=mod_date).values('product', 'part_no',
                                                                               "specification_details", "processor",
                                                                               'graphics', "warranty", "ram", "hard_disk",
                                                                               "odd", "price")
                note = NoteBook.objects.filter(modified=mod_date).values('product', 'part_no', "specification_details",
                                                                            "processor", "screen_size", "warranty", "ram",
                                                                            "hard_disk", "operating_system", "screen",
                                                                            "price")
                payload['business'] = bpc
                payload['notebook'] = note
                payload['workbook'] = work

                return Response(dict(payload=payload, status=status.HTTP_200_OK, time=datetime.datetime.now(), message='success'))
            else:
                return Response(
                    dict(payload={}, status=status.HTTP_204_NO_CONTENT, time=datetime.datetime.now(), message="Please select a date"))
        except KeyError:
            return Response(
                dict(payload={}, status=status.HTTP_204_NO_CONTENT, time=datetime.datetime.now(),
                     message="Please select a date"))