
$("#tab-test").on("click", "li", function () {
    $(this).addClass("am-active").siblings("li").removeClass("am-active");
    var target = $(this).children("a").attr("data-target");
    $(target).addClass("am-active").siblings(".am-tab-panel").removeClass("am-active");
}).find("li").eq(0).trigger("click");


$('#belong_case_id').on('change', function () {
    if ($('#belong_case_id').val() !== '请选择') {
        case_id = $('#belong_case_id').val();
        case_name = $('#belong_case_id option:selected').text();
        var href = "<li id=" + case_id + "><a href='/api/edit_case/" + case_id + "/' id = " + case_id + ">" + case_name + "" +
            "</a><i class=\"js-remove\" onclick=remove_self('#" + case_id + "')>✖</i></li>";
        $("#pre_case").append(href);
    }
});

function remove_self(id) {
    $(id).remove();
}

$(function () {
    $('#add_data').text('add ' + $('#DataType').val());
    $('#del_data').text('del ' + $('#DataType').val());
});

//
function run_case(){
    var url;
    var method;

    url = $('#url').val();
    method = $('#method option:selected').val();

    $('#select_env').modal({
        relatedTarget: this,
        onConfirm: function () {
            alert($('#env_name option:selected').text());
            post('/runcase/', {
                'url': url,
                'method': method,
                'base_url':$('#env_name option:selected').text()
            })
        },
        onCancel: function () {
        }
    });
}


function post(url, params) {
    var temp = document.createElement("form");
    temp.action = url;
    temp.method = "post";
    temp.style.display = "none";
    for (var x in params) {
        var opt = document.createElement("input");
        opt.name = x;
        opt.value = params[x];
        temp.appendChild(opt);
    }
    document.body.appendChild(temp);
    temp.submit();
    return temp;
}

function case_ajax(type, editor) {
    var caseInfo = $("#form_message").serializeJSON();
    alert("ok");
}