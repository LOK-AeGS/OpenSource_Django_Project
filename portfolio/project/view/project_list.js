const projects = [
    {
      title: "웹사이트 리디자인",
      description: "기존 기업 웹사이트의 UX/UI 개선 프로젝트",
      date: "2025-03-15"
    },
    {
      title: "모바일 앱 개발",
      description: "iOS와 Android 앱 동시 출시를 위한 크로스플랫폼 개발",
      date: "2025-01-05"
    },
    {
      title: "AI 챗봇 구축",
      description: "고객 서비스 자동화를 위한 AI 기반 챗봇 시스템",
      date: "2025-02-20"
    }
  ];
  
  const projectList = document.getElementById("project-list");
  
  projects.forEach(project => {
    const card = document.createElement("div");
    card.className = "project-card";
    card.innerHTML = `
      <div class="project-title">${project.title}</div>
      <div class="project-desc">${project.description}</div>
      <div class="project-date">📅 ${project.date}</div>
    `;
    projectList.appendChild(card);
  });
  