editor = null;

$('#DataType').on('change', function () {
    if ($('#DataType').val() === 'json') {
        $('#add_data').attr('disabled', true);
        $('#del_data').attr('disabled', true);
        $('#data').remove();
        var json_text = "<span style=\"font-size:10px;\" id=\"json-text\">\n" +
            "                                <div style=\"margin-left: 0px; margin-top: 5px; height: 200px\">" +
            "<pre id=\"code\" class=\"ace_editor\" style=\"margin-top: 0px; margin-bottom: 0px; min-height: 200px;\">\n" +
            "    <textarea>{\"key\":\"value\"}</textarea>\n" +
            "</pre></div></span>";
        $('#form_request_data').append(json_text);
        editor = ace.edit("code");
        init_acs('json', 'github', editor);
    } else {
        var table = '<table class="table table-hover table-condensed table-bordered table-striped" id="data">\n' +
            '                                <caption>' + $('#DataType').val() + ':</caption>\n' +
            '                                <thead>\n' +
            '                                <tr class="active text-success">\n' +
            '                                    <th width="5%" align="center">Option</th>\n' +
            '                                    <th width="30%" align="center">Key</th>\n' +
            '                                    <th width="5%" align="center">Type</th>\n' +
            '                                    <th width="60%" align="center">Value</th>\n' +
            '                                </tr>\n' +
            '                                </thead>\n' +
            '                                <tbody>\n' +
            '                                </tbody>\n' +
            '                            </table>';

        $('#add_data').text('add ' + $('#DataType').val());
        $('#del_data').text('del ' + $('#DataType').val());

        $('#add_data').removeAttr("disabled");
        $('#del_data').removeAttr("disabled");
        $('#data').remove();
        $('#json-text').remove();
        $('#form_request_data').append(table);
    }
});

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