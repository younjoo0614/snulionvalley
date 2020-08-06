// $(document).ready(() => {
//     $(".friendlist_btn").on('click', function(event) {
//         $(this).toggleClass("showing-friend");
    
//         if ($(this).hasClass("showing-friend")) {
//             $(this).text("친구목록 닫기");
//             $(this).parent().find(".friend_list").show();
//         } else {
//             $(this).text("친구목록 펼치기");
//             $(this).parent().find(".friend_list").hide();
//         }
//         });
//         }
//     )

    $('.friendlist_btn').click((e) => {
        e.preventDefault();
        const $this = $(e.currentTarget);
        const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

        $.ajax({
            type: 'GET',
            url: '/bookshelf/list/', 
            data: { 
                csrfmiddlewaretoken: csrfmiddlewaretoken,
            },
            dataType: "json",
            success(res) {
                console.log(res)
                const follows = res.follows;
                let friend_list=document.getElementById('friend_list')
                
                const friendTemplate=follows.map( profile=> `<div class="friend_list" data-id='${profile.id}'>${profile.nickname}</div>`)
                
                friend_list.innerHTML=friendTemplate;
                
                $(this).toggleClass("showing-friend");
    
                if ($(this).hasClass("showing-friend")) {
                    $(this).text("친구목록 닫기");
                    $(this).parent().find(".friend_list").show();
                } else {
                    $(this).text("친구목록 펼치기");
                    $(this).parent().find(".friend_list").hide();
                }

                },
                
            error(response, status, error) {
                console.log(response, status, error);
            }
        })
    })