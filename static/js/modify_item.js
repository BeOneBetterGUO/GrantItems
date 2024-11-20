window.onload = function () {
    $("#submit-btn").click(function (event) {
        // 阻止按钮的默认行为
        event.preventDefault();

        let name = $("input[name='name']").val();
        let price = $("input[name='price']").val();
        let type = $("#category-select").val();
        let status = $("#status-select").val();
        let description = $("#description").val();
        let csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();
        let img = $("input[name='image']")[0].files[0];
        let is_consumable = $("input[name='is_consumable']").is(":checked");
        let count = $("input[name='count']").val();
        let overdue = $("input[name='overdue']").val();
        let link = $("input[name='link']").val();

        // Create a FormData object
        let formData = new FormData();
        formData.append('name', name);
        formData.append('price', price);
        formData.append('description', description);
        formData.append('csrfmiddlewaretoken', csrfmiddlewaretoken);
        formData.append('type', type);
        formData.append('image', img); // Append the file object
        formData.append('status', status);
        formData.append('is_consumable', is_consumable);
        formData.append('count', count);
        formData.append('overdue', overdue);
        formData.append('link', link);

        console.log(name, price, description, csrfmiddlewaretoken, type, img, status, is_consumable, count, overdue, link);
        $.ajax({
            url: '',
            method: 'POST',
            data: formData,
            processData: false, // Prevent jQuery from automatically transforming the data into a query string
            contentType: false, // Prevent jQuery from setting the Content-Type header
            success: function (result) {
                if (result['code'] == 200) {
                    window.location.href='/items/show_detail/'+result['item_id'];
                } else {
                    alert(result['message']);
                }
            }
        });
    });
}
