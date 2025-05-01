from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import AllProject, DetailProject, Reivew, User
from django.template import loader
#    return HttpResponse("detail page")
# Create your views here.
# 🔹 프로젝트 리스트
def show_list(request):
    project_list = AllProject.objects.all().order_by('-projectName')

    context = {
        'project_list': project_list
    }
    return render(request, 'project_list.html', context)  # loader.get_template 생략 가능

def show_detail(request, project_id):
    submitted_rating = None
    userId = request.session.get('username')
    role = request.session.get('role')  # ✅ 사용자 권한 확인 ('admin' or 'user')

    # 프로젝트 정보 가져오기
    project = get_object_or_404(AllProject, id=project_id)

    try:
        project_detail = DetailProject.objects.get(projectId=project)
    except DetailProject.DoesNotExist:
        project_detail = None

    # 해당 프로젝트에 대한 모든 리뷰
    project_reviews = Reivew.objects.filter(projectId=project)

    if request.method == 'POST':
        submitted_rating = request.POST.get('rating')
        review_content = request.POST.get('content')

        if userId and role == 'user':  # ✅ 일반 사용자만 리뷰 작성 가능
            Reivew.objects.create(
                projectId=project,
                projectReviewStar=submitted_rating,
                projectReviewContent=review_content,
                userName=userId
            )
        else:
            submitted_rating = None  # 관리자거나 로그인 안 된 경우는 무시

    context = {
        'project_id': project_id,
        'submitted_rating': submitted_rating,
        'project_detail_list': project_detail,
        'project_review_list': project_reviews,
        'username': userId,
        'role': role  # ✅ 템플릿에서도 구분 가능
    }
    return render(request, 'project_detail.html', context)

def create_project(request):
    error = None
    if request.method == 'POST':
        name = request.POST.get('projectName')
        content = request.POST.get('projectContent')
        user_id = request.session.get('user_id')

        if not user_id:
            error = "로그인 후 등록할 수 있습니다."
        else:
            try:
                user = User.objects.get(userId=user_id)
                project = AllProject.objects.create(
                    projectName=name,
                    projectDate=timezone.now(),
                    projectUserName=user
                )
                DetailProject.objects.create(
                    projectId=project,
                    projectContent=content
                )
                return redirect('project_list')
            except User.DoesNotExist:
                error = "유효하지 않은 사용자입니다."

    return render(request, 'project_create.html', {'error': error})

def edit_project(request, project_id):
    user_id = request.session.get('user_id')
    project = get_object_or_404(AllProject, id=project_id)
    detail = get_object_or_404(DetailProject, projectId=project)

    # 권한 확인
    if project.projectUserName.userId != user_id:
        return HttpResponse("수정 권한이 없습니다.", status=403)

    if request.method == 'POST':
        project_name = request.POST.get('projectName')
        content = request.POST.get('projectContent')

        project.projectName = project_name
        detail.projectContent = content

        project.save()
        detail.save()

        return redirect('project_detail', project_id=project.id)

    context = {
        'project': project,
        'detail': detail
    }
    return render(request, 'project_edit.html', context)