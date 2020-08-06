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
        },
        dataType: "json",
        success(res) {
            console.log(res)
            const userbook = res.userbook;
            const memos = res.memos;
            let info_div=document.getElementById('info-div')
            let memo_div=document.getElementById('memo-div');
            
            info_div.innerHTML=`<p>책 제목 : ${userbook.title}</p>
            <p>작가 : ${userbook.author}</p>`;
            const memoTemplate=memos.map(memo=>`<div>${memo.page} ${memo.content}</div>`).join('');
            const submit_btn=document.getElementById('submit-memo');
            submit_btn.dataset.id=`${id}`;
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
    const id = $this.data('id');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
    console.log(id);
    $.ajax({
        url: `/bookshelf/${id}/memos/`,         
        method: 'POST',
        headers:{'X-CSRFToken':csrfmiddlewaretoken},
        data: {
            id:id,
            content: $(`textarea#review`).val(),
            page: $(`input#review_pages`).val(),
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: "json",
        success(res) {
            console.log(res);
            const new_page=res.page;
            const new_content=res.content;
            let memo_div=document.getElementById('memo-div');
            const newTemp=`<div>페이지: ${new_page}</div><div>메모: ${new_content}</div>`;
            memo_div.innerHTML+=newTemp;
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