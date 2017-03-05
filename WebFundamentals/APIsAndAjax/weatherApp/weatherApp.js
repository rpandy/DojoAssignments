$(document).ready(function() {
    $('form').submit(function() {
        var myInput = $('#city').val();
        var apiID = 'a1cc4be94d1d1a27d66229af9a1fb034'
        var string = 'http://api.openweathermap.org/data/2.5/weather?q='
        string+=myInput
        string+='&&appid='
        string+=apiID

        // console.log(myInput)
        // console.log(string)

        $.get(string, function(res) {
            console.log(res.main.temp)
            var tempF = Math.floor((res.main.temp*(9/5)-459.67))
            console.log(tempF)

            $('#weatherData').html("<h2>" + "The current temperature in " + myInput + " is " + tempF + " degrees Fahrenheit.</h2>")
        }, 'json');
        // don't forget to return false so the page doesn't refresh
        return false;
    });
});
