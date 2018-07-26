function info_ajax(id,url){
    var data = $(id).serializeJSON();
    $.ajax({
        type: 'post',
        url: url,
        data: JSON.stringify(data),
        // contentType: "application/json",
        contentType: "application/x-www-form-urlencoded",
        success: function (data) {
            if (data == 'OK') {
                window.location.href = "/project_list/";
            }
            else{
               alert(data);
            }
        }
        ,
        error: function () {
            alert('Sorry，服务器可能开小差啦, 请重试!');
        }
    });
}