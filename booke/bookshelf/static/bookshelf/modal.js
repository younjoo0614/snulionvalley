$( document ).ready(function() {
});

$('#signup-form').submit((event) => {
    event.preventDefault()
    $.ajax({
        url: '/accounts/signup/',
        method: 'POST',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: $(event.currentTarget).data('csrfmiddlewaretoken'),
            username: $(`input#username`).val(),
            password1: $(`input#password1`).val(),
            password2: $(`input#password2`).val(),
            goal: $(`#goal option:selected`).val(),
            taste: $(`#taste option:selected`).val(),
        },
        success(response) {
            console.log(response)
            window.location.href='/bookshelf/'
        },
        error(response, status, error) {
            console.log(response, status, error);
        }
    })

    
})

$('#login-form').submit((event) => {
    event.preventDefault()
    $.ajax({
        url: '/accounts/login/',
        method: 'POST',
        data: {
            login: $(`input#login-username`).val(),
            password: $(`input#password`).val(),
            csrfmiddlewaretoken: $(event.currentTarget).data('csrfmiddlewaretoken')
        },
        dataType: "json",
        success(res) {
            console.log(res)
            window.location.href='/bookshelf/'
        },
        error(response, status, error) {
            console.log(response, status, error);
        }
    })
})

$('#book-create').submit((event) => {
    event.preventDefault()
    var colors = document.getElementsByName('color');
        var color_value;
        for(var i = 0; i < colors.length; i++){
            if(colors[i].checked){
                color_value = colors[i].value;
                // console.log(color_value)
            }
            // return color_value;
        }

    $.ajax({
        url: '/bookshelf/',
        method: 'POST',
        data: {
            title: $(`input#title`).val(),
            // author: $(`input#author`).val(),
            // page: $(`input#page`).val(),
            author: $(`input#author`).val(),
            color: color_value,
            csrfmiddlewaretoken: $(event.currentTarget).data('csrfmiddlewaretoken')
        },
        dataType: "json",
        success(res) {
            console.log(res);
            window.location.href='/bookshelf/'
        },
        error(response, status, error) {
            console.log(response, status, error);
        }
    })
    // .then(res => {
       
    //     var colors = document.getElementsByName('color');
    //     var color_value;
    //     for(var i = 0; i < colors.length; i++){
    //         if(colors[i].checked){
    //             color_value = colors[i].value;
    //             // console.log(color_value)
    //         }
    //         // return color_value;
    //     }
    //     console.log(color_value);
    //     console.log(`${res.id}`);
    //     console.log($(`#${res.id}`));
    //     // document.getElementById(`${res.id}`).classList.add(`btn-${color_value}`);
    //     $(`#${res.id}`).addClass(`book-${color_value}`);
    // })         
})

$('.showmodal').click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const id = $this.data('id');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

    $.ajax({
        type: 'GET',

        url: `/bookshelf/${id}`, 
        data: { 
            id: id,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            //content: $(`input#${id}[name=content]`).val(),
        },
        dataType: "json",
        success(res) {
            console.log(res)
            //window.location.href=`/bookshelf/${id}/`
            const userbook = data.userbook;
            const memos = data.memos;

            let info_div=document.getElementById('info-div')
            let memo_div=document.getElementById('memo-div');
            let str=``
            for (let i=0; i<memos.length; i++){
                str+=`<p> ${memos.i.page}, ${memos.i.created_at},${memos.content}</p>`;
            }
            info_div.innerHTML=`<p>책 제목 : ${userbook.title}</p>
            <p>작가 : ${userbook.author}</p>`;
            const memos=data.memos;
            const memoTemplate=memos.map(memo=>`<div>${memo.id} ${memo.content}</div>`).join('');
            memo_div.innerHTML=memoTemplate;
            },
        error(response, status, error) {
            console.log(response, status, error);
        }

    })
})

$('#submit-memo').click( (e) => {
    e.preventDefault()
    const $this = $(e.currentTarget);
    const id = document.getElementById('submit-memo').value; //이게 제일 문제 userbook의 id를 어떻게 받아와야 할지...
    
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
    console.log(id);
    $.ajax({
        url: `/bookshelf/${id}/memos/`,         
        method: 'POST',
        data: {
            id:id,
            content: $(`textarea#review`).val(),
            page: $(`input#review_page`).val(),
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: "json",
        success(data) {
            console.log(data)
            //window.location.href=`/bookshelf/${id}/`
            const userbook = data.userbook;
            const memos = data.memos;

            let info_div=document.getElementById('info-div')
            info_div.innerHTML=`<p>책 제목 : ${userbook.title}</p>
            <p>작가 : ${userbook.author}</p>`;
            let memo_div=document.getElementById('memo-div');
            const memos=data.memos;
            const memoTemplate=memos.map(memo=>`<div>${memo.id} ${memo.content}</div>`).join('');
            memo_div.innerHTML=memoTemplate;
        },
        error(response, status, error) {
            console.log(response, status, error);
        }
    })
})

$(document).ready(() => {
    $(".more-comment-btn").on('click', function(event) {
        $(this).toggleClass("showing-comment");
    
        if ($(this).hasClass("showing-comment")) {
            $(this).text("HIDE COMMENTS");
            $(this).parent().find(".toggle-comment").not(".last-comment").show();
        } else {
            $(this).text("MORE COMMENTS");
            $(this).parent().find(".toggle-comment").not(".last-comment").hide();
        }
    });
}
)