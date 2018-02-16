from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, BaseUser, ProductDetails
from .serializers import BaseUserSerializer, CompanySerializer
import datetime
from django.core.mail import EmailMessage


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
    now = datetime.datetime.now()

    def post(self, request):
        try:
            date = request.data["date"]
            payload = dict()
            if date:
                bpc = ProductDetails.objects.filter(modified__gte=date).values('id', 'category','product', 'part_no', "specification_details",
                                                                             "processor", "screen_size", "warranty", "ram",
                                                                             "hard_disk", "operating_system", "screen",
                                                                             "price")
                payload['product'] = bpc

                return Response(dict(payload=payload, status=status.HTTP_200_OK, time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message='success'))
            else:
                bpc = ProductDetails.objects.all().values('id','category','product', 'part_no', "specification_details", "processor",
                                                      "screen_size", "warranty", "ram", "hard_disk", "operating_system",
                                                      "screen", "price")
                payload['product'] = bpc

                return Response(
                    dict(payload=payload, status=status.HTTP_200_OK, time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message="Please select a date"))
        except KeyError:
            return Response(
                dict(payload={}, status=status.HTTP_204_NO_CONTENT, time=datetime.datetime.now(),
                     message="Please select a date"))


class LoginVerify(APIView):
    def post(self, request):
        try:
            payload = dict()
            username = request.data["username"]
            password = request.data["password"]
            user = BaseUser.objects.get(email=username, password=password)
            payload['id'] = user.id
            payload['name'] = user.get_full_name()
            payload['username'] = user.username
            payload['email'] = user.email
            payload['dealer_name'] = user.dealer_name
            payload['mobile'] = user.mobile
            payload['address'] = user.address
            payload['gender'] = user.gender

            return Response(dict(payload=payload, message="User Found", status=status.HTTP_200_OK))
        except Exception:
            return Response(dict(payload={}, message="User Not Found", status=status.HTTP_404_NOT_FOUND))

    def put(self, request):
        try:
            payload = dict()
            username = request.data["username"]
            password = request.data["password"]
            change_password = request.data["new_password"]
            user = BaseUser.objects.get(id=int(username))
            if user.check_password(password):
                user.set_password(change_password)
                user.save()
                return Response(dict(payload=payload, message="Password Reset Successful", status=status.HTTP_200_OK))
            else:
                return Response(dict(payload=payload, message="Check Password again", status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION))

        except Exception:
            return Response(dict(payload={}, message="Password Reset Failed", status=status.HTTP_404_NOT_FOUND))


class ForgotPassword(APIView):
    def post(self, request):
        try:
            username = request.data["username"]
            user = BaseUser.objects.get(email=username)
            email = EmailMessage('HP Password Request',
                                 'Please find the below password for {username} and password is {password}'\
                                 .format(username=user.username,password=user.password), to=[user.email])
            email.send()

            return Response(dict(payload={}, message="Email Sent", status=status.HTTP_200_OK))
        except Exception:
            return Response(dict(payload={}, message="User Not Found", status=status.HTTP_404_NOT_FOUND))