# from django.shortcuts import render
# from .models import Person
# # Create your views here.
# from django.shortcuts import render, redirect
# from .models import Person   # model nomingizga moslang
# def main(request):
#     if request.POST:
#         model = Person()
#         model.first_name = request.POST.get('first_name','')
#         model.last_name = request.POST.get('last_name','')
#         model.company = request.POST.get('company', '')
#         model.email = request.POST.get('email', '')
#         model.phone = request.POST.get('area_code', '') + request.POST.get('phone', '')
#         model.course_type = request.POST.get('course_type', '')
#         model.subject = request.POST.get('subject', '')
#         model.exist = request.POST.get('exist', '')
#         model.save()
#         print(request.POST)
#     return render(request,'index.html')
#
#
# # def register(request):
# #     if request.POST:
# #
# #         print(request.POST)
# #     return render(request,'register.html')
# from django.shortcuts import render
# from .models import Person  # bu sizning model nomingiz bo'lishi kerak
#
# from django.shortcuts import render
#
# def home(request):
#     return render(request, 'home.html')   # bu sahifa templates ichida bo'lishi kerak
#
# def register(request):
#     return render(request, 'register.html')
#
# def panel(request):
#     users = Person.objects.all()
#     return render(request, 'panel.html', {'users': users})
#
#
#
# def register(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         company = request.POST.get('company')
#         email = request.POST.get('email')
#         area_code = request.POST.get('area_code')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#
#         # Ma'lumotlarni bazaga saqlash
#         Person.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             company=company,
#             email=email,
#             area_code=area_code,
#             phone=phone,
#             subject=subject
#         )
#
#         # ✅ Ma'lumot saqlangandan keyin panelga yo‘naltirish
#         return redirect('panel')   # bu yerda 'panel' url nomi bilan mos bo‘lishi kerak
#
#     return render(request, 'register.html')


































# def orm_list(request):
#     queryset = Employees.objects.values("job_id").annotate(xodim_soni=Count("job_id"))
#
#     for i in queryset:
#         print(i)
#     return HttpResponse("ok")

    # emp_list = ""
    # for c in queryset:
    #     emp_list += f"<li>{c.first_name} {c.last_name}</li>"
    # return HttpResponse(f"<ol>{emp_list}</ol")


from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        company = request.POST.get('company')
        phone = request.POST.get('phone')
        familya = request.POST.get('familya')

        # Ma'lumotlarni boshqa sahifaga uzatamiz
        context = {
            'name': name,
            'age': age,
            'email': email,
            'company': company,
            'phone': phone,
            'familya': familya
        }
        return render(request, 'panel.html', context)

    return render(request, 'index.html')
