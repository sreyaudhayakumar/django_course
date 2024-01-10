from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect
from.models import Course,UserProfile
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('base_new')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'login.html')

def dashborad(request):
    return render(request,'header.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def account(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        adduser = UserProfile(firstname=firstname, lastname=lastname,  phone=phone, email=email,
                          username=username, password=password)

        auth_user = User(username=username, first_name=firstname, last_name=lastname, email=email)
        auth_user.set_password(password)
        auth_user.save()
        adduser.save()
        return redirect('login') 

    return render(request,'registration.html')

# def add_course(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         description = request.POST['description']
#         new_product = Course(title=title,description=description)
#         new_product.save()

#         return HttpResponse("course successfully added.")

#     return render(request, 'courses_add.html')
def add_course(request):
    if request.method == 'POST':
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        description = request.POST['description']
        amount = request.POST['amount']
        additional_info = request.POST['additional_info']
        status = request.POST['status']
        image = request.FILES['image']
        
        if not title or not amount or not image:
         return HttpResponse("Please provide all required fields.")

        new_course = Course(
            title=title,
            subtitle=subtitle,
            description=description,
            amount=amount,
            additional_info=additional_info,
            status=status
        )
        new_course.save()
        return HttpResponse("Course successfully added.")

    return render(request, 'short-course-create.html')


# def courses_list(request):
#     courses_list = Course.objects.all()
#     paginator = Paginator(all_courses, 10)  

#     page = request.GET.get('page')
#     try:
#         courses = paginator.page(page)
#     except PageNotAnInteger:
#         courses = paginator.page(1)
#     except EmptyPage:
#         courses = paginator.page(paginator.num_pages)
    
#     return render(request, 'course_view.html', {'courses': courses_list})
def courses_list(request):
    all_courses = Course.objects.all()
    all_user_profiles = UserProfile.objects.all()

    paginator = Paginator(all_courses, 10)  

    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    return render(request, 'course_view.html', {'courses': courses, 'user_profiles': all_user_profiles})

def edit_course(request, product_id):
    try:
        edit_course = get_object_or_404(Course, id=product_id)
    except Course.DoesNotExist:
        return HttpResponse('Product not found')

    if request.method == 'POST':
        edit_course.title = request.POST['title']
        edit_course.subtitle = request.POST['subtitle']
        edit_course.description = request.POST['description']
        edit_course.amount = request.POST['amount']
        edit_course.additional_info = request.POST['additional_info']  
        edit_course.status = request.POST['status']

        edit_course.save()

        return HttpResponse('Course edited successfully')

    return render(request, 'edit_course.html', {'edit_courses': edit_course})
 
def edit_password(request, user_id):
    try:
        edit_password = get_object_or_404(UserProfile, id=user_id)
    except UserProfile.DoesNotExist:
        return HttpResponse('User not found')

    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        user = authenticate(username=edit_password.username, password=old_password)
        if user is not None:
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                messages.success(request, 'Password updated successfully')
                return redirect('success_page_name')

            else:
                return HttpResponse('New passwords do not match')
        else:
            messages.error(request, 'Password update failed. Please check your information and try again.')
            
    return render(request, 'edit_password.html', {'user': edit_password})




def delete_course(request, product_id):
    del_course = get_object_or_404(Course, id=product_id)
    if request.method == 'POST':
        del_course.delete()
        return redirect('courses_list')
    return HttpResponse('Invalid request for product deletion')

def courses_list(request):#search
    query = request.GET.get('q')

    if query:
        courses_list = Course.objects.filter(title__icontains=query)
    else:
        courses_list = Course.objects.all()
        
        

    return render(request, 'course_view.html', {'courses': courses_list, 'query': query})

def profile(request):
    return render(request,'profile.html')

def short_course_create(request):
    return render(request,'short-course-create.html')


def footer(request):
    return render(request,'footer.html')