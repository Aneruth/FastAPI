$( document ).ready(function() {
    $("#add_user_block").hide();
    $("#list_user_block").hide();
    $("#delete_user_block").hide();
    $("#get_user_by_city_block").hide();
    $("#view_user_by_city").hide();
    $(".add_user").on("click", () => {
        $("#list_user_block").hide();
        $("#add_user_block").show();
        $("#delete_user_block").hide();
        $("#get_user_by_city_block").hide();
        $("#view_user_by_city").hide();
        console.log('Hello world 2');
    } );
    $("#submit").on("click", () => {
        var bodyFormData = new FormData();
        bodyFormData.append('name',$("#username").val());
        bodyFormData.append('age',$("#age").val());
        bodyFormData.append('others',$("#other").val());
        axios({
            method: "post",
            url: "/users/",
            data: bodyFormData,
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
          })
            .then(function (response) {
              //handle success
              console.log(response);
              $("#username").val('');
              $("#age").val('');
              $("#other").val('');
              alert("Success :)")
            })
            .catch(function (response) {
              //handle error
              console.log(response);
            });
    }); // add user and submit method conclusion

    // List User starts
    $("#list_user").on("click", () =>{
        $("#add_user_block").hide();
        $("#delete_user_block").hide();
        $("#list_user_block").show();
        $("#view_user_by_city").hide();
        $("#get_user_by_city_block").hide();
        axios({
            method: 'get',
            url: '/users/',
            responseType: 'text',
            }).then(function (response) {
                if ($.fn.DataTable.isDataTable("#example")) {
                    $('#example').DataTable().clear().destroy();
                }                  
                $('#example').DataTable( {
                    "aaData": response.data['data'],
                    "columns": [
                        { 'data': "age" },
                        { 'data': "created" },
                        { 'data': "id" },
                        { 'data': "name" },
                        { 'data': "others" }
                    ]
                } );
              });   
    }); // list user method conclusion

    // Delete User starts
    $("#delete_user").on("click", () =>{
        $("#add_user_block").hide();
        $("#list_user_block").hide();
        $("#delete_user_block").show();
        $("#get_user_by_city_block").hide();
        $("#view_user_by_city").hide();
        $("#delete_submit").on("click", () => {
            var path = "/users/"+String($("#user_id").val()).trim()+"/"
            console.log(path);
            axios.delete(path)
                .then(function (response) {
                  //handle success
                  console.log(response);
                  alert("Success :)")
                  $("#user_id").val('');
                })
                .catch(function (response) {
                  //handle error
                  console.log(response);
                });
        });

    }); // delete user method conclusion


    // List user by city starts
    $("#user_by_city").on("click", () =>{
        $("#add_user_block").hide();
        $("#list_user_block").hide();
        $("#delete_user_block").hide();
        $("#get_user_by_city_block").show();
        $("#view_user_by_city").hide();
    }); 
    $("#city_submit").on("click", ()=>{
        $("#view_user_by_city").show();
        axios({
            method: 'get',
            url: "/users/city/"+String($("#city").val()).trim()+"/",
            responseType: 'text',
            }).then(function (response) {
                if ($.fn.DataTable.isDataTable("#spcific_user_by_city")) {
                    $('#spcific_user_by_city').DataTable().clear().destroy();
                }                  
                $('#spcific_user_by_city').DataTable( {
                    "aaData": response.data['data'],
                    "columns": [
                        { 'data': "age" },
                        { 'data': "created" },
                        { 'data': "id" },
                        { 'data': "name" },
                        { 'data': "others" }
                    ]
                });
              });   
    });// list city user method conclusion

});