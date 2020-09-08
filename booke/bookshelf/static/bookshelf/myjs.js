$(document).ready(() => {});

$(".more-friendlist-btn").on("click", function (event) {
  $(this).toggleClass("showing-friend");

  if ($(this).hasClass("showing-friend")) {
    $(this).text("친구목록 닫기");
    $(".friend_list").show();
  } else {
    $(this).text("친구목록 펼치기");
    $(".friend_list").hide();
  }
});

// 원래 post 요청을 js로 보내려 했어서 만들어놓음.. 살펴보시와요
// $(".to-friend-btn").on("click", function (e) {
//   e.preventDefault();
//   const $this = $(e.currentTarget);
//   const fid = $this.data("fid");
//   const csrfmiddlewaretoken = $this.data("csrfmiddlewaretoken");
//   $.ajax({
//     url: "/bookshelf/friends/",
//     method: "POST",
//     dataType: "json",
//     data: {
//       fid: fid,
//       csrfmiddlewaretoken: csrfmiddlewaretoken,
//     },
//     success(response) {
//       console.log(response);
//       return render(jsonObj, (mimetype = "application/json"));
//     },
//     error(response, status, error) {
//       console.log(response, status, error);
//     },
//   });
// });
