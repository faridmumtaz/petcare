from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from services.models import Adoption, User
from services.models import Pet
from services.models import Volunteer
from services.models import Feedback

def indexPage(request):
    feedbackData = Feedback.objects.filter(enable = 1)
    # print(request.session['user_logged_in'])
    # print(request.session['volunteer_logged_in'])
    return render(request,"index.html",{'feedbackData':feedbackData})
def about(request):
    return render(request,"about.html")
def contacts(request):
    if request.method == "POST":
        name = request.POST['nmtb']
        email = request.POST['emailtb']
        message = request.POST['feedtb']
        feedback_data = Feedback(name = name, email = email, message = message)
        feedback_data.save()
        return render(request,"index.html")
    else:
        return render(request,"contacts.html")
def user(request):
    if 'user_logged_in' in request.session:
        return render(request,"user.html")
    else:
        return render(request,"login.html",{'logged_in': False})
def volunteer(request):
    if request.method == "POST":
        fnm= request.POST['fnmtb']
        lnm = request.POST['lnmtb']
        unm = User.objects.get(unm = request.session['user_logged_in'])
        email = request.POST['emailtb']
        pno = request.POST['pnotb']
        address = request.POST['addtb']

        new_volunteer = Volunteer(fnm = fnm, lnm = lnm, unm = unm, email = email, pno = pno, address = address)
        new_volunteer.save()

        return render(request,"index.html")

    if 'user_logged_in' in request.session:
        return render(request,"volunteer.html")
    else:
        return render(request,"login.html",{'logged_in':False})
def login(request):
    if request.method == "POST":#validating the user
        unm = request.POST['unmtb']
        password = request.POST['passtb']
        
        try:
            userData = User.objects.filter(unm = unm).get(password = password)
        except ObjectDoesNotExist:
            userData = False

        if userData is not False:
            try:
                volunteerData = Volunteer.objects.get(email = userData.email)
            except ObjectDoesNotExist:
                volunteerData = False

            if volunteerData:
                request.session['volunteer_logged_in'] = volunteerData.email

        if userData:
            request.session['user_logged_in'] = userData.unm #setting session
            request.session['email_logged_in'] = userData.email
            request.session['phone_logged_in'] = userData.pno
            request.session['password_logged_in'] = userData.password
            return render(request,"index.html")
        else:
            return render(request,"login.html",{'valid':False})
    else:
        return render(request,"login.html")
def consult(request):
    return render(request,"consult.html")
def adoption(request):
    petData = Pet.objects.all()
    paginator = Paginator(petData,2)
    page_number = request.GET.get('page')
    pageData = paginator.get_page(page_number)
    totalPages = pageData.paginator.num_pages
    return render(request,"adoption.html",{'pageData':pageData,'pages':[str(n+1) for n in range(totalPages)],'totalPages':totalPages})
def behaviour(request):
    return render(request,"behaviour.html")
def care(request):
    return render(request,"care.html")
def signup(request):
    if request.method == "POST":
        unm = request.POST['unmtb']
        fnm = request.POST['fnmtb']
        lnm = request.POST['lnmtb']
        email = request.POST['emailtb']
        pno = request.POST['pnotb']
        password = request.POST['passtb']
        
        new_user = User(fnm = fnm,lnm = lnm,unm = unm, email = email, pno = pno, password = password)
        new_user.save()

        return render(request,"login.html")
    else:
        return render(request,"signup.html")
def logout(request):
    try:
        del request.session['user_logged_in']
        del request.session['volunteer_logged_in']
    except KeyError:
        pass
    return render(request,"index.html")
def updateDetails(request):
    #updating user name
    uunmtb = request.POST.get('uunmtb',False)
    if uunmtb is not False:
        User.objects.filter(unm = request.session['user_logged_in']).update(unm = uunmtb)
        request.session['user_logged_in'] = uunmtb
    #updating email
    uemailtb = request.POST.get('uemailtb',False)
    if uemailtb is not False:
        User.objects.filter(unm = request.session['user_logged_in']).update(email = uemailtb)
        request.session['email_logged_in'] = uemailtb
    #updating password
    upasstb = request.POST.get('upasstb',False)
    if upasstb is not False:
        User.objects.filter(unm = request.session['user_logged_in']).update(password = upasstb)
        request.session['password_logged_in'] = upasstb
    return render(request,"user.html")
def confirmation(request,petid):
    if request.method == "POST":
        unm = User.objects.get(unm = request.POST['unmtb'])
        pid = Pet.objects.get(id = petid)
        email = request.POST['emailtb']
        pno = request.POST['pnotb']
        address = request.POST['addtb']
        adoptionData = Adoption(unm = unm,pid = pid, email = email, pno = pno, address = address)
        adoptionData.save()
        return render(request,"index.html")
    if 'user_logged_in' not in request.session:
        return render(request,"login.html",{'logged_in':False})
    else:
        petData = Pet.objects.get(id = petid)
        return render(request,"confirmation.html",{'petData':petData})
# def admin(request):
#     add = request.POST.get('add',False)
#     if request.method == "POST":
#         print(add)
#         if add is not False:
#             pass
#             # Feedback.objects.filter()
#     remove = request.POST.get('remove',False)    
#     if request.method == "POST":
#         print(remove)
#         if remove is not False:
#             pass
#     userData = User.objects.filter(role = 'admin')
#     volunteerData = Volunteer.objects.all()
#     feedbackData = Feedback.objects.all()
#     return render(request,"admin.html",{'userData':userData,'volunteerData':volunteerData,'feedbackData':feedbackData})