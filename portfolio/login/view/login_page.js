document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", function (e) {
      const username = document.getElementById("username").value.trim();
      const password = document.getElementById("password").value.trim();
  
      if (!username || !password) {
        alert("아이디와 비밀번호를 모두 입력해주세요.");
        e.preventDefault();
      }
    });
  });
  