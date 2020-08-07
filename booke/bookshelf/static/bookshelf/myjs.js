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

// $(".to-friend-btn").click((e) => {
//   e.preventDefault();
//   const $this = $(e.currentTarget);
//   const id = $this.data("id");
//   const csrfmiddlewaretoken = $this.data("csrfmiddlewaretoken");

//   $.ajax({
//     type: "GET",
//     url: `/bookshelf/friend/${id}`,
//     data: {
//       id: id,
//       csrfmiddlewaretoken: csrfmiddlewaretoken,
//     },
//     dataType: "json",
//     success(res) {
//       console.log(res);
//     },
//     error(response, status, error) {
//       console.log(response, status, error);
//     },
//   });
// });

// $("#friend-value").autocomplete({
//     source : function(request, response) {
//         $.ajax({
//             url : "accounts/result/"
//             , type : "GET"
//             , data : {keyWord : $("#friend-value").val()}
//             , success : function(data){
//                 response(
//                     $.map(data, function(item) {
//                         return {
//                             label : item.nickname
//                             , value : item.nickname
//                             , idx : item.testIdx
//                         };
//                     })
//                 );    //response
//             }
//             ,
//             error : function(){ //실패
//                 alert("통신에 실패했습니다.");
//             }
//         });
//     }
//     , minLength : 1
//     , autoFocus : false
//     , select : function(evt, ui) {
//         console.log("전체 data: " + JSON.stringify(ui));
//         console.log("db Index : " + ui.item.idx);
//         console.log("검색 데이터 : " + ui.item.value);
//     }
//     , focus : function(evt, ui) {
//         return false;
//     }
//     , close : function(evt) {
//     }
// });
