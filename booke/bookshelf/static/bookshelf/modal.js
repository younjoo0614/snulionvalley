$(document).ready(function () {});

$("#signup-form").submit((event) => {
  event.preventDefault();
  $.ajax({
    url: "/accounts/signup/",
    method: "POST",
    dataType: "json",
    data: {
      csrfmiddlewaretoken: $(event.currentTarget).data("csrfmiddlewaretoken"),
      username: $(`input#username`).val(),
      password1: $(`input#password1`).val(),
      password2: $(`input#password2`).val(),
      goal: $(`#goal option:selected`).val(),
      taste: $(`#taste option:selected`).val(),
    },
    success(response) {
      console.log(response);
      window.location.href = "/bookshelf/";
    },
    error(response, status, error) {
      console.log(response, status, error);
    },
  });

});

$("#login-form").submit((event) => {
  event.preventDefault();
  $.ajax({
    url: "/accounts/login/",
    method: "POST",
    data: {
      login: $(`input#login-username`).val(),
      password: $(`input#password`).val(),
      csrfmiddlewaretoken: $(event.currentTarget).data("csrfmiddlewaretoken"),
    },
    dataType: "json",
    success(res) {
      console.log(res);
      window.location.href = "/bookshelf/";
    },
    error(response, status, error) {
      console.log(response, status, error);
    },
  });
});


$("#book-create").submit((event) => {
  event.preventDefault();
  var colors = document.getElementsByName("color");
  var color_value;
  for (var i = 0; i < colors.length; i++) {
    if (colors[i].checked) {
      color_value = colors[i].value;
      // console.log(color_value)
    }
    // return color_value;
  }

  $.ajax({
    url: "/bookshelf/",
    method: "POST",
    data: {
      title: $(`input#title`).val(),
      // author: $(`input#author`).val(),
      // page: $(`input#page`).val(),
      author: $(`input#author`).val(),
      color: color_value,
      csrfmiddlewaretoken: $(event.currentTarget).data("csrfmiddlewaretoken"),
    },
    dataType: "json",
    success(res) {
      console.log(res);
      window.location.href = "/bookshelf/";
    },
    error(response, status, error) {
      console.log(response, status, error);
    },
  });
});


$(".showmodal").click((e) => {
  e.preventDefault();
  const $this = $(e.currentTarget);
  const id = $this.data("id");
  const csrfmiddlewaretoken = $this.data("csrfmiddlewaretoken");

  $.ajax({
    type: "GET",
    url: `/bookshelf/${id}`,
    data: {
      id: id,
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },
    dataType: "json",
    success(res) {
      console.log(res);
      const userbook = res.userbook;
      const memos = res.memos;
      const csrftoken=csrfmiddlewaretoken;
      let info_div = document.getElementById("info-div");
      let memo_div = document.getElementById("memo-div");

      info_div.innerHTML = `<p>책 제목 : ${userbook.title}</p>
            <p>작가 : ${userbook.author}</p>
            <p>메모:</p>`;

      const memoTemplate = memos.map((memo) => `<div><div>${memo.content}  (p.${memo.page}) (날짜: ${memo.created_at})</div>
      <button type="submit" class="delete-memo" data-bid =${id} data-mid=${memo.id} >삭제</button></div>`)
        .join("");
      const submit_btn = document.getElementById("submit-memo");
      submit_btn.dataset.id = `${id}`;
      const delete_btn=document.getElementById("delete-book");
      delete_btn.dataset.id = `${id}`;
      memo_div.innerHTML = memoTemplate;

      document.getElementById("submit-memo").setAttribute("data-id", `${id}`);
    },
    error(response, status, error) {
      console.log(response, status, error);
    },
  });
});

$("#submit-memo").click((e) => {
  e.preventDefault();
  const $this = $(e.currentTarget);
  const id = $this.data("id");
  const csrfmiddlewaretoken = $this.data("csrfmiddlewaretoken");
  console.log(id);
  $.ajax({
    url: `/bookshelf/${id}/memos/`,
    method: "POST",
    headers: { "X-CSRFToken": csrfmiddlewaretoken },
    data: {
      id: id,
      content: $(`textarea#review`).val(),
      page: $(`input#review_pages`).val(),
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },
    dataType: "json",
    success(res) {
      console.log(res);
      const new_page = res.page;
      const new_content = res.content;
      const created_at = res.created_at;
      
      let memo_div = document.getElementById("memo-div");
      // const newTemp = `<div>페이지: ${new_page}</div><div>메모: ${new_content}</div>`;
      const newTemp = `<div><div>${new_content}  (p.${new_page}) ${created_at}</div>
      <button data-bid="${res.id}" data-mid="${res.new_memo_id}" >삭제</button></div>`;
      memo_div.innerHTML += newTemp;
    },
    error(response, status, error) {
      console.log(response, status, error);
    },
  });
});

$("#delete-book").click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const id =$this.data("id");
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

    $.ajax({
        type: 'POST',
        url: `/bookshelf/${id}/delete/`,
        data: {
            id:id,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: 'json',
        success: function(response) {
            console.log(response);

            window.location.href="/bookshelf/";
        },
        error: function(response, status, error) {
            console.log(response, status, error);
        },
        complete: function(response) {
            console.log(response);
        },
    })
})

$(".showfriendmodal").click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const id = $this.data("id");
    const csrfmiddlewaretoken = $this.data("csrfmiddlewaretoken");
  
    $.ajax({
      type: "GET",
      url: `/bookshelf/${id}`,
      data: {
        id: id,
        csrfmiddlewaretoken: csrfmiddlewaretoken,
      },
      dataType: "json",
      success(res) {
        console.log(res);
        const userbook = res.userbook;
        const memos = res.memos;
        let info_div_friend = document.getElementById("info-div-friend");
        let memo_div_friend = document.getElementById("memo-div-friend");
  
        info_div_friend.innerHTML = `<p>책 제목 : ${userbook.title}</p>
              <p>작가 : ${userbook.author}</p>
              <p>메모:</p>`;
  
        const memoTemplate = memos
          .map(
            (memo) => `<div>${memo.content}  (p.${memo.page})</div>`
          ).join("");
        memo_div_friend.innerHTML = memoTemplate;
  
        // document.getElementById("submit-memo").setAttribute("data-id", `${id}`);
      },
      error(response, status, error) {
        console.log(response, status, error);
      },
    });
  });

$(".delete-memo").click((e)=> {
  e.preventDefault();
    const $this = $(e.currentTarget);
    const bid =$this.data("bid");
    const mid=$this.data("mid");
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

    $.ajax({
        type: 'POST',
        url: `/bookshelf/${bid}/memos/${mid}/delete/`,
        data: {
            bid:bid,
            mid:mid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: 'json',
        success: function(response) {
            console.log(response);
            $(this).parent().remove();
        },
        error: function(response, status, error) {
            console.log(response, status, error);
        },
        complete: function(response) {
            console.log(response);
        },
    })
});
      
$(document).ready(() => {
  $(".more-comment-btn").on("click", function (event) {
    $(this).toggleClass("showing-comment");

    if ($(this).hasClass("showing-comment")) {
      $(this).text("HIDE COMMENTS");
      $(this).parent().find(".toggle-comment").not(".last-comment").show();
    } else {
      $(this).text("MORE COMMENTS");
      $(this).parent().find(".toggle-comment").not(".last-comment").hide();
    }
  });
});
