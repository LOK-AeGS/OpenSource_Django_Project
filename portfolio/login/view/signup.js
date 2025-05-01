document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const pw1 = document.getElementById("password1");
    const pw2 = document.getElementById("password2");
  
    form.addEventListener("submit", function (e) {
      if (pw1.value !== pw2.value) {
        e.preventDefault();
        alert("비밀번호가 일치하지 않습니다.");
      }
    });
  });
  