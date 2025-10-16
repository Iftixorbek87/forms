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
