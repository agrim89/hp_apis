from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Partner, PartnerSalesTeam, Product, Category
from .serializers import BaseUserSerializer, CompanySerializer
import datetime, os
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .report_api import ReportGenerator, CSVReportGenerator
from django.conf import settings

class UserDetail(APIView):

    def get(self, request):
        snippets = PartnerSalesTeam.objects.all()
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
            user = PartnerSalesTeam.objects.get(username=request.data['username'])
            user.first_name = request.data['first_name'] if request.data['first_name'] else user.first_name
            user.last_name = request.data['last_name'] if request.data['last_name'] else user.last_name
            user.username = request.data['username'] if request.data['username'] else user.username
            user.dealer_name = request.data['dealer_name'] if request.data['dealer_name'] else user.dealer_name
            user.mobile = request.data['mobile'] if request.data['mobile'] else user.mobile
            user.email = request.data['email'] if request.data['email'] else user.email
            user.address = request.data['address'] if request.data['address'] else user.address
            user.gender = request.data['gender'] if request.data['gender'] else user.gender

            user.save()
            return Response(BaseUserSerializer(user).data, status=status.HTTP_202_ACCEPTED)
        except Exception:
            return Response(status='User Not Found')


class CompanyDetail(APIView):

    def get(self, request, format=None):
        snippets = Partner.objects.all()
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
            user = Partner.objects.get(company_namer=request.data['company_name'])
            user.company_name = request.data['company_name'] if request.data['company_name'] else user.company_name
            user.domain_name = request.data['domain_name'] if request.data['domain_name'] else user.domain_name
            user.partner_id = request.data['partner_id'] if request.data['partner_id'] else user.partner_id
            user.region = request.data['region'] if request.data['region'] else user.region
            user.location = request.data['location'] if request.data['location'] else user.location
            user.dedicated_person = request.data['dedicated_person'] if request.data['dedicated_person'] \
                else user.dedicated_person
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
            if request.data['api_key'] == 'kzvXN896YE':
                date = request.data["date"]
                payload = dict()
                if date:
                    bpc = Product.objects.filter(modified__gte=date).values('id', 'category', 'category__name','product'
                                                                            , 'part_no',"specification_details", "processor",
                                                                            "screen_size", "warranty", "ram", "hard_disk",
                                                                            "operating_system", "screen", "odd", "graphics",
                                                                            "price", "data_sheet", "image_url", "status")
                    category = Category.objects.filter(modified__gte=date).values('id', 'name', 'status')
                    payload['product'] = bpc
                    payload['category'] = category

                    return Response(dict(payload=payload, status=status.HTTP_200_OK,
                                         time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message='success'))
                else:
                    bpc = Product.objects.all().values('id', 'category', 'category__name', 'product', 'part_no',
                                                                            "specification_details", "processor",
                                                                            "screen_size", "warranty", "ram", "hard_disk",
                                                                            "operating_system", "screen", "odd", "graphics",
                                                                            "price", "data_sheet", "image_url", "status")
                    category = Category.objects.all().values('id', 'name', 'status')
                    payload['product'] = bpc
                    payload['category'] = category
                    return Response(
                        dict(payload=payload, status=status.HTTP_200_OK,
                             time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message="Please select a date"),
                        status=status.HTTP_200_OK)
            else:
                return Response(
                    dict(payload={}
                         , message="Please provide correct API KEY"), status=status.HTTP_401_UNAUTHORIZED)
        except KeyError:
            return Response(
                dict(payload={}, status=status.HTTP_204_NO_CONTENT, time=datetime.datetime.now(),
                     message="Please select a date"), status=status.HTTP_204_NO_CONTENT)


class LoginVerify(APIView):
    def post(self, request):

        try:
            payload = dict()
            username = request.data["username"]
            password = request.data["password"]
            user = PartnerSalesTeam.objects.get(email=username, is_active=True)
            if user.password == password:
                payload['id'] = user.id
                payload['name'] = user.get_full_name()
                payload['username'] = user.username
                payload['email'] = user.email
                payload['dealer_name'] = user.dealer_name.company_name
                payload['mobile'] = user.mobile
                payload['address'] = user.address
                payload['gender'] = user.gender

                user.last_login = datetime.datetime.now()
                user.login_count += 1
                user.save()
                return Response(dict(payload=payload, message="User Found", status=status.HTTP_200_OK))
            elif user.check_password(password):
                payload['id'] = user.id
                payload['name'] = user.get_full_name()
                payload['username'] = user.username
                payload['email'] = user.email
                payload['dealer_name'] = user.dealer_name.company_name
                payload['mobile'] = user.mobile
                payload['address'] = user.address
                payload['gender'] = user.gender

                user.last_login = datetime.datetime.now()
                user.login_count += 1
                user.save()
                return Response(dict(payload=payload, message="User Found", status=status.HTTP_200_OK))
            else:
                return Response(dict(payload={}, message="Please check password", status=status.HTTP_204_NO_CONTENT))
        except Exception:
            return Response(dict(payload={}, message="User Not Found", status=status.HTTP_205_RESET_CONTENT))


class ForgotPassword(APIView):
    def post(self, request):
        try:
            username = request.data["username"]
            user = PartnerSalesTeam.objects.get(email=username)
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            email = EmailMessage('HP Password Request',
                                 'Please find the below password for {username} and password is {password}'\
                                 .format(username=user.username, password=password), to=[user.email])
            email.send()

            return Response(dict(payload={}, message="Your password has been sent to your registered email.",
                                 status=status.HTTP_200_OK))
        except Exception:
            return Response(dict(payload={}, message="User Not Found", status=status.HTTP_404_NOT_FOUND))


class ChangePassword(APIView):

    def post(self, request):
        try:
            payload = dict()
            id = request.data["id"]
            password = request.data["password"]
            change_password = request.data["new_password"]
            user = User.objects.get(id=int(id))
            if user.check_password(password):
                user.set_password(change_password)
                user.save()
                return Response(dict(payload=payload, message="Password Reset Successful", status=status.HTTP_200_OK))
            elif user.password == password:
                user.set_password(change_password)
                user.save()
                return Response(dict(payload=payload, message="Password Reset Successful", status=status.HTTP_200_OK))
            else:
                return Response(dict(payload=payload, message="Check Password again",
                                     status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION))

        except Exception:
            return Response(dict(payload={}, message="Password Reset Failed", status=status.HTTP_204_NO_CONTENT))


def report_api(request):
    col_heads = ['SNo', 'Name', 'Email', 'Dealer Name', 'Logged Times', 'Last Login']
    report_active = ReportGenerator('active_user_report_{}.xlsx'.format(datetime.datetime.now().date()))
    report_deactive = ReportGenerator('deactive_user_report_{}.xlsx'.format(datetime.datetime.now().date()))
    now = datetime.datetime.now().date()
    last = now - datetime.timedelta(days=30)
    active_user = PartnerSalesTeam.objects.filter(last_login__gte=last).values_list('first_name', 'email',
                                                                               'dealer_name__company_name',
                                                                               'login_count', 'last_login')
    deactive_user = PartnerSalesTeam.objects.filter(last_login__lte=last).values_list('first_name', 'email',
                                                                               'dealer_name__company_name',
                                                                               'login_count', 'last_login')
    # active = user_data(active_user)
    # deactive = user_data(deactive_user)
    report_active.write_header(col_heads)
    report_deactive.write_header(col_heads)
    report_active.write_body(active_user)
    report_deactive.write_body(deactive_user)
    mail = EmailMessage('subject', 'text', 'agrim.sharma@sirez.com', ["agrim.sharma@sirez.com"])
    mail.attach_file(os.path.join(settings.STATIC_ROOT, 'active_user_report_{}.xlsx'.\
                                  format(datetime.datetime.now().date())))
    mail.attach_file(os.path.join(settings.STATIC_ROOT, 'deactive_user_report_{}.xlsx'.\
                                  format(datetime.datetime.now().date())))
    mail.send()
    return HttpResponse('Success')

    # response = HttpResponse(content_type="text/csv")
    # response['Content-Disposition'] = "attachment; filename='report.csv'"
    # with open('reports/report_{}.csv'.format(datetime.datetime.now()), 'w+') as writer:
    #     writer = csv.writer(response)
    #     writer.writerow(['Active Users last login with in a month'])
    #     now = datetime.datetime.now().date()
    #     last = now - datetime.timedelta(days=30)
    #     writer.writerow(fields)
    #     active = PartnerSalesTeam.objects.filter(last_login__gte=last)
    #     deactive = PartnerSalesTeam.objects.filter(last_login__lte=last)
    #     for i in range(len(active)):
    #         writer.writerow([i+1, active[i].get_full_name(), active[i].email, active[i].dealer_name,
    #                          active[i].login_count, active[i].last_login])
    #
    #         writer.writerow(['Deactive users last login greater than a month'])
    #     for i in range(len(deactive)):
    #         writer.writerow([i+1, deactive[i].get_full_name(), deactive[i].email, deactive[i].dealer_name,
    #                          deactive[i].login_count, deactive[i].last_login])
    #     mail = EmailMessage('subject', 'text', ['agrim.sharma@sirez.com'], ['agrim.sharma@sirez.com'])
    #     mail.attach_file()
    # return response


def user_data(user):
    data = []
    for a in user:
        i = 1
        name = a.get_full_name()
        email = a.email
        dealer_name = a.dealer_name.company_name
        login_count = a.login_count
        last_login = datetime.datetime.strftime(a.last_login, "%Y-%m-%d")
        data.append([i, name, email, dealer_name, login_count, last_login])
        i += 1
    return data
