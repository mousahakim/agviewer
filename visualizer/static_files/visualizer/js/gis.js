//crsf handler 
$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});

//glabals

//ajax
function ajax_request(callback, data, url) {
    var request = $.ajax({
          method: "POST",
          url: url,
          data: JSON.stringify(data), 
          dataType: 'json'
        }).done(function(data) {
            callback(data);
        }).fail(function(msg){
            alert('failed');
        });
};

function list_files(data){
    console.log(data);
    var file_list = '';
    for(i=0;i<data.length;i++){
        str = data[i].split('/');
        file_list += "<option value="+data[i]+">"+str[str.length-1]+"</option>";
    }; 
    $('select.file-select').html(file_list);
};

$(function(){

    ajax_request(list_files, {}, urlListFiles);

});

$(function() {
    $('#file-upload-form').submit(function (event) {
        event.preventDefault();
        var data = new FormData($('#file-upload-form').get(0));
        console.log('uploading ...');
        var request = $.ajax({
            method: 'POST',
            url: $('#file-upload-form').attr('action'),
            data: data,
            processData: false,
            contentType: false
            }).done(function(data) {
               ajax_request(list_files, {}, urlListFiles);
            }).fail(function(msg){
                alert('failed');
        });
    });

    $('#delete-btn').on('click', function(e){
        e.stopImmediatePropagation();
        delete_files();
    });
    $('#download-btn').on('click', function(e){
        e.stopImmediatePropagation();
        download_file();
    });
    $('#add-btn').on('click', function(e){
        e.stopImmediatePropagation();
        get_url();
    })
});

$("#ms-main-sensors option:selected")

function get_selected(element){
    var $files;
    
    $files = $.map(element, function (el, i) {
        return $(el).val();
    });

    return $files  
};


function delete_files(){
    var $element = $('select.file-select')
    var $files = get_selected($element);
    console.log('to be deleted: ', $files);
    var request = $.ajax({
          method: "POST",
          url: urlDeleteFiles,
          data: JSON.stringify($files), 
          dataType: 'json'
        }).done(function(data) {
            console.log('files deleted.');
            ajax_request(list_files, {}, urlListFiles);
        }).fail(function(msg){
            alert('failed');
    });

};


function download_file() {
    var $element = $('select.file-select');
    var $files = get_selected($element);
    if($files.length > 1){
        alert('Please select a single file to download.');
        return
    };
    console.log('Downloading ...');

    dynamic_form(urlDownloadFile, 'post', {
        name: $files[0]
    });
    
}


function dynamic_form(action, method, input) {
    'use strict';
    var form;
    form = $('<form />', {
        action: action,
        method: method,
        style: 'display: none;'
    });
    $(token, {}).appendTo(form);
    if (typeof input !== 'undefined' && input !== null) {
        $.each(input, function (name, value) {
            $('<input />', {
                type: 'hidden',
                name: name,
                value: value
            }).appendTo(form);
        });
    }
    form.appendTo('body').submit();
}

function get_url() {
    var $element = $('select.file-select');
    var $files = get_selected($element);
    if ($files.length > 1){
        alert('Please select a single file to download.');
        return
    };
    var url;
    var request = $.ajax({
          method: "POST",
          url: urlGetUrl,
          data: JSON.stringify($files), 
          dataType: 'json'
        }).done(function(data) {
            console.log('url received.');
            add_layer('kml', data.url);
        }).fail(function(msg){
            alert('failed');
    });

    return url;
};

function add_layer(type, data){
    console.log('adding layer ...');
    var vector_layer = new ol.layer.Vector({
        source: new ol.source.Vector({
            url: 'http://192.168.8.102:8000/'+data, 
            format: new ol.format.KML()
        })
    });
    console.log(data);
    map.addLayer(vector_layer);
};