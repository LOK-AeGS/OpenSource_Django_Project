document.addEventListener("DOMContentLoaded", function () {
    const projectId = "{{ project_id }}";  // 이건 작동 안 함 – JS는 템플릿 렌더링 후 동작함
  
    // 대안: 서버에서 HTML 렌더링 시 데이터 속성으로 전달
    const container = document.querySelector("#project-info");
    container.innerHTML = `<p>이곳에 프로젝트 <b>#${container.dataset.projectId}</b>의 정보가 표시됩니다.</p>`;
  });
  