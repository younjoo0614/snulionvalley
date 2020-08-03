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

// function filter(){

//     var f, fr, frn, i;

//     f = document.getElementsByName("friend-value").value.toUpperCase();
//     fr = document.getElementsByClassName("fr");

//     for(i=0; i<fr.length; i++){
//         frn = fr[i].getElementsByClassName("frn");
//         if(frn[0].innerHTML.toUpperCase.indexOf(f) > -1){
//             fr[i].style.display = "flex";
//         }else{
//             fr[i].style.display = "none";
//         }
//     }
// }

