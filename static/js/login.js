function login(){
        email = document.getElementById("login-email").value;
        password = document.getElementById("login-password").value;
        csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        $("#errorlogin").html("");
        $.ajax({
            type:"POST",
            url:'/user/log_in/',
            data:{
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
                'email':email,
                'password':password,
            },
            success : function(data){
                console.log(data);
                if(data['result'] == "success"){
                    location.reload();
                }
                else if(data['result'] == "inactive"){
                    $("#errorlogin").html("Please verify this E-mail address.");
                }
                else{
                    $("#errorlogin").html("Проверьте введеные данные!");
                }
            }
        });
    }

function signup(){
            email = document.getElementById("reg_email").value;
            password1 = document.getElementById("reg_pass1").value;
            password2 = document.getElementById("reg_pass2").value;
            n1 = $('#reg_n1').data('n1');
            n2 = $('#reg_n2').data('n2');
            answer = $('#reg_answer').val();
            csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
            $("#erroremail").html("");
            $("#errorpass").html("");

            $.ajax({
            type:"POST",
            url:'/user/signup/',
            data:{
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
              'email':email,
              'password1':password1,
              'password2':password2,
                'n1':n1,
                'n2':n2,
                'answer':answer,
            },
            success : function(data){
                console.log(data['result']);
                if (data['result'] == "bad"){
                    $("#errorother").html("Неверный ответ");
                    return;
                }

                if(data['result'] == "success"){
                    // $('#reg_text1').css('display','none');
                    // $('#reg_text2').css('display','block');
                    location.reload();

                }
                else{
                    if("email" in data['result'])
                        $("#erroremail").html(data['result']['email'][0]);
                    if("password2" in data['result'])
                        $("#errorpass").html(data['result']['password2'][0]);
                }
            }
        })

      }