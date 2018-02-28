from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Partner, PartnerSalesTeam, Product, Category
from .serializers import BaseUserSerializer, CompanySerializer
import datetime, json
from django.core.mail import EmailMessage
from django.contrib.auth.models import User


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
    import io, csv
    now = datetime.datetime.now().date()
    last = now - datetime.timedelta(days=30)
    col_heads = ['SNo', 'Name', 'Email', 'Dealer Name', 'Logged Times', 'Last Login']
    buffer = io.StringIO()
    wr = csv.writer(buffer, quoting=csv.QUOTE_ALL)
    wr.writerows([[]])
    wr.writerows([["Daily Analysis Report"]])
    yest = now - datetime.timedelta(days=1)
    dyes = now - datetime.timedelta(days=2)
    login_yest = PartnerSalesTeam.objects.filter(last_login=yest).count()
    login_dyest = PartnerSalesTeam.objects.filter(last_login=dyes).count()
    unique_yes = PartnerSalesTeam.objects.filter(login_count=1, last_login=yest).count()
    unique_dyes = PartnerSalesTeam.objects.filter(login_count=1, last_login=dyes).count()
    wr.writerows([["Date", "No. of Session", "Percentage Change", "Unique Sessions", "Percentage Change"]])
    row = [dyes, login_dyest, '', unique_dyes, '']
    wr.writerows([row])
    if login_yest > 0 and unique_yes > 0:
        row = [yest, login_yest, (login_dyest/login_yest) * 100, unique_dyes, (unique_dyes/unique_yes) * 100]
    else:
        row = [yest, login_yest, (login_dyest / 1) * 100, unique_dyes, (unique_dyes / 1) * 100]
    wr.writerows([row])
    wr.writerows([[]])
    wr.writerows([[]])
    wr.writerows([['Active User Data']])
    wr.writerows([col_heads])
    wr.writerows([[]])

    active_user = PartnerSalesTeam.objects.filter(last_login__gt=last, last_login__lt=now)
    active = user_data(active_user)
    wr.writerows(active)
    wr.writerows([[]])
    wr.writerows([[]])
    wr.writerows([['Deactive User Data']])
    wr.writerows([col_heads])
    deactive_user = PartnerSalesTeam.objects.filter(last_login__lt=last)
    deactive = user_data(deactive_user)
    wr.writerows(deactive)

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=user_login_data_{}.csv'.format(datetime.datetime.now().date())

    return response


def user_data(user):
    data = []
    i = 1
    for a in user:
        name = a.get_full_name()
        email = a.email
        dealer_name = a.dealer_name.company_name
        login_count = a.login_count
        last_login = datetime.datetime.strftime(a.last_login, "%Y-%m-%d")
        data.append([i, name, email, dealer_name, login_count, last_login])
        i += 1
    return data


def send_email(request):
    from django.template.loader import render_to_string
    from django.utils.html import strip_tags
    from django.core.mail import EmailMultiAlternatives

    try:
        now = datetime.datetime.now().date()
        yest = now - datetime.timedelta(days=1)
        dyes = now - datetime.timedelta(days=2)
        login_yest = PartnerSalesTeam.objects.filter(last_login=yest).count()
        login_dyest = PartnerSalesTeam.objects.filter(last_login=dyes).count()
        unique_yes = PartnerSalesTeam.objects.filter(login_count=1, last_login=yest).count()
        unique_dyes = PartnerSalesTeam.objects.filter(login_count=1, last_login=dyes).count()
        pchn = (login_yest/login_dyest)*100 if login_dyest > 0 else 0
        pcn = (unique_yes/unique_dyes)*100 if unique_dyes > 0 else 0
        html_content = render_to_string('mail_template.html', {"yest": yest,
                                                               "dyest": dyes,
                                                               "nosdyes": login_dyest,
                                                               "uns_dyes": unique_dyes,
                                                               "nosyes": login_yest,
                                                               "pcn": pcn,
                                                               "pchn": pchn,
                                                               "uns_yes": unique_yes
                                                               })
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives('Test', text_content, 'agrim.sharma@sirez.com', ['agrim.sharma@sirez.com'])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return HttpResponse(json.dumps(dict(payload={}, message="Email Sent.",
                                            status=status.HTTP_200_OK))
                            )
    except Exception:
        return HttpResponse(json.dumps(dict(payload={}, message="Email not Sent.",
                                            status=status.HTTP_206_PARTIAL_CONTENT))
                            )
