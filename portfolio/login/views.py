from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User,AdminUser

def show_page(request):
    error = None

    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')

        try:
            user = User.objects.get(userId=userid)
            if user.userPassword == password:  # 실제로는 check_password() 사용 권장
                request.session['user_id'] = user.userId
                request.session['username'] = user.userName
                return redirect('project_list')  # 로그인 후 이동
            else:
                error = "비밀번호가 일치하지 않습니다."
        except User.DoesNotExist:
            error = "존재하지 않는 사용자입니다."

    return render(request, "login_page.html", {'error': error})
# ✅ 회원가입 처리
def signup(request):
    error = None

    if request.method == 'POST':
        userid = request.POST.get('userid')
        name = request.POST.get('name')
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password2')

        if pw1 != pw2:
            error = "비밀번호가 일치하지 않습니다."
        elif User.objects.filter(userId=userid).exists():
            error = "이미 존재하는 아이디입니다."
        else:
            # 사용자 생성
            user = User.objects.create(
                userId=userid,
                userPassword=pw1,
                userName=name  # 만약 모델에 name 필드가 있다면
            )
            return redirect('login_page')  # 로그인 페이지로 이동

    return render(request, "singup.html", {'error': error})