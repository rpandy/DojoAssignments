$(document).ready(function() {
    $('form').submit(function() {
        // your code here (build up your url)
        $.get(url, function(res) {
            // your code here
        }, 'json');
        // don't forget to return false so the page doesn't refresh
        return false;
    });
});
