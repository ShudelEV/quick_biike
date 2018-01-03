function prev_order(form, url) {
    $.ajax({
        type: 'POST',
        url: url,
        data: { context: form },
        dataType: 'json',
        success: prev_order_confirm,
        error: function () {alert('AJAX error.');}
    });
}

function prev_order_confirm(response) {
    var response_data = JSON.parse(response);
    alert('Good! 1');
}