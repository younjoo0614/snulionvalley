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
            major: $(`input#major`).val(),
            ordinal: $(`input#ordinal`).val()
        },
        success(response) {
            console.log(response)
            window.location.href='/pages/'
        },
        error(response, status, error) {
            console.log(response, status, error)
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
            window.location.href='/pages/'
        },
        error(response, status, error) {
            console.log(response, status, error)
        }
    })
})