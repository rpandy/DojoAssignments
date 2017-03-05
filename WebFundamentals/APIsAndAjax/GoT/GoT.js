$(document).ready(function() {
    $('#houses').on('click','img',function() {
        var houseID = $(this).attr('id')
        console.log(houseID)
        $.get("http://anapioficeandfire.com/api/houses/" + houseID, function(res) {
            var houseTitles = []
            for(var i = 1; i < res.titles.length; i++){
                console.log(res.titles[i])
                houseTitles += res.titles[i]+","
            }
            var houseName = res.name
            var houseWords = res.words
            var string = '<h2>House Details</h2>'
            string += '<p>Name:</p>'+ houseName
            string += '<p>Words:</p>' + houseWords
            string += '<p>Titles:' + houseTitles +'</p>'

            console.log(string)
            console.log(res)
            console.log(res.name)
            console.log(res.words)

            $('#house_details').html(string)
        }, 'json');
    });
});
