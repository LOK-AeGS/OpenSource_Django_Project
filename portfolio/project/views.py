from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AllProject, DetailProject, Reivew
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


# 🔹 프로젝트 상세
def show_detail(request, project_id):
    submitted_rating = None
    username = request.session.get('username')  # ✅ 로그인 사용자 정보 불러오기

    # 프로젝트 객체
    project = get_object_or_404(AllProject, id=project_id)

    # 상세 내용
    try:
        project_detail = DetailProject.objects.get(projectId=project)
    except DetailProject.DoesNotExist:
        project_detail = None

    # 리뷰 리스트
    project_reviews = Reivew.objects.filter(projectId=project)

    if request.method == 'POST':
        submitted_rating = request.POST.get('rating')
        review_content = request.POST.get('content')  # ✅ 리뷰 내용도 함께 저장

        if username:
            Reivew.objects.create(
                projectId=project,
                projectReviewStar=submitted_rating,
                projectReviewContent=review_content,
                userName=username
            )
        else:
            submitted_rating = None  # 비회원의 제출 무효화

    context = {
        'project_id': project_id,
        'submitted_rating': submitted_rating,
        'project_detail_list': project_detail,
        'project_review_list': project_reviews,
        'username': username  # ✅ 템플릿에서 조건 분기용
    }
    return render(request, 'project_detail.html', context)