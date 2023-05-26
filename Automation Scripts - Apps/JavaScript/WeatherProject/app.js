const { log } = require("console");
const express = require("express");
const https = require("https");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.urlencoded({extended:true}))

app.get("/", function (req, res){
    res.sendFile(__dirname + "/index.html")
})

app.post("/", function(req, res) {
    const query = req.body.city;
    const apiKey = "095f93974230f7d857fbadc0582404e7"
    const unit = "metric"
    const weatherUrl = "https://api.openweathermap.org/data/2.5/weather?q=" + query + "&appid=" + apiKey + "&units=" + unit +""

    https.get(weatherUrl, function (response){
        console.log(response.statusCode);

        response.on("data", function(data){
            const weatherData = JSON.parse(data);
            const temp = weatherData.main.temp;
            const description = weatherData.weather[0].description;
            const icon = weatherData.weather[0].icon;
            const imgUrl = "https://openweathermap.org/img/wn/" + icon +"@2x.png";


            res.write("<h1>The temprature in " + query + " is " + temp + "C</h1>")
            res.write("<h3> The weather now in " + query + " is " + description + "</h3>")
            res.write("<img src=" + imgUrl + ">")

            res.send()

        })
    });
})



app.listen(3000, function() {
    console.log("Server is runnig now on port 3000.");
});