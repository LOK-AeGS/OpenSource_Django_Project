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

        # 일반 사용자 체크
        try:
            user = User.objects.get(userId=userid)
            if user.userPassword == password:
                request.session['user_id'] = user.userId
                request.session['username'] = user.userName
                request.session['role'] = 'user'  # 역할 저장
                return redirect('project_list')
            else:
                error = "비밀번호가 일치하지 않습니다."
        except User.DoesNotExist:
            # 관리자 사용자 체크
            try:
                admin = AdminUser.objects.get(userId=userid)
                if admin.userPassword == password:
                    request.session['user_id'] = admin.userId
                    request.session['username'] = admin.userName
                    request.session['role'] = 'admin'  # 역할 저장
                    return redirect('project_list')  # 필요 시 관리자 전용 페이지로 변경
                else:
                    error = "비밀번호가 일치하지 않습니다."
            except AdminUser.DoesNotExist:
                error = "존재하지 않는 사용자입니다."

    return render(request, "login_page.html", {'error': error})

# 회원가입 처리
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
            User.objects.create(
                userId=userid,
                userPassword=pw1,
                userName=name
            )
            return redirect('login_page')

    return render(request, "singup.html", {'error': error})

def logout_view(request):
    # 세션 전체 삭제
    request.session.flush()
    # 로그아웃 후, 로그인 페이지로 이동(혹은 홈으로)
    return redirect('project_list')