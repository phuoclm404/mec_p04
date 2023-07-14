$(document).ready(function() {
    $('#upload-form').on('submit', function(event) {
        event.preventDefault();

        $('#upload-button').prop('disabled', true);
        $('#process-button').hide();

        var form = $(this);
        var url = form.attr('action');
        var formData = new FormData(this);

        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            processData: false,
            contentType: false,
            beforeSend: function() {
                $('#status').text('Đang tải lên...');
            },
            success: function(response) {
                $('#status').text('Tải lên thành công');
                $('#process-button').show();
            },
            error: function(xhr, status, error) {
                $('#status').text('Lỗi khi tải lên: ' + error);
                $('#upload-button').prop('disabled', false);
            }
        });
    });
});