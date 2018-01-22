$(document).ready(function() {
    $('#create_button').click(function(e) {
        if (!confirm('이동할까요?')) {
            return false;
        }
    });
});
