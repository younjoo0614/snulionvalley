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
            goal: $(`input#goal`).val(),
            taste: $(`input#taste`).val()
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
    $.ajax({
        url: '/bookshelf/new/',
        method: 'POST',
        data: {
            title: $(`input#title`).val(),
            author: $(`input#author`).val(),
            page: $(`input#page`).val(),
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

$('#memo-create').submit(async (e) => {
    event.preventDefault()
    const $this = $(e.currentTarget);
    const id = $this.data('id');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

    $.ajax({
        url: `/bookshelf/${id}/`,  
        method: 'GET'
      })

    await $.ajax({
        url: `/bookshelf/${id}/memos/`, 
        // 서버가 처리할 url. create_memo를 백에서 불러야 db에 추가되기 때문
        method: 'POST',
        data: {
            content: $(`input#review`).val(),
            page: $(`input#review_page`).val(),
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: "json",
        success(res) {
            console.log(res)
            window.location.href=`/bookshelf/${id}/`
        },
        error(response, status, error) {
            console.log(response, status, error);
        }
    })

})