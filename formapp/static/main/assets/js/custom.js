$(document).ready(function () {
    var currentTime = new Date();
    var hours = currentTime.getHours();
    var greeting = "";

    if (hours >= 5 && hours < 12) {
        greeting = "Good Morning";
    } else if (hours >= 12 && hours < 18) {
        greeting = "Good Afternoon";
    } else {
        greeting = "Good Evening";
    }

    greeting += ", Admin !";

    $(".g-msg").text(greeting);



    function updateDateButton() {
        var currentDate = new Date();
        var formattedDate = currentDate.toLocaleString(); 
        $(".date-button").text(formattedDate);
    }
    updateDateButton();
    setInterval(updateDateButton, 1000);

     
     function copyData() {
        var sourceData = $(".source-data").text(); 
        $(".destination-data").text(sourceData); 
    }
    copyData();
}); 







