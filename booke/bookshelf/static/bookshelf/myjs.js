$(document).ready(() => {
    $(".more-friendlist-btn").on('click', function(event) {
        $(this).toggleClass("showing-friend");

        if ($(this).hasClass("showing-friend")) {
            $(this).text("친구목록 펼치기");
            $(this).parent().find(".friend-list").show();
        } else {
            $(this).text("친구목록 닫기");
            $(this).parent().find(".friend-list").hide();
        }
        });
    }
)