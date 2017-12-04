
    $(document).ready(function(){
        $("#tutorBtn").click(function(){
            $("#tutorDetails").show();
            $("#carpoolDetails").hide();
            $("#bookDetails").hide();
            $("#activityDetails").hide();
        });
    });




    $(document).ready(function(){
        $("#bookBtn").click(function(){
            $("#tutorDetails").hide();
            $("#carpoolDetails").hide();
            $("#bookDetails").show();
            $("#activityDetails").hide();
        });
    });




    $(document).ready(function(){
        $("#carpoolBtn").click(function(){
            $("#tutorDetails").hide();
            $("#carpoolDetails").show();
            $("#bookDetails").hide();
            $("#activityDetails").hide();
        });
    });



    $(document).ready(function(){
        $("#actBtn").click(function(){
            $("#tutorDetails").hide();
            $("#carpoolDetails").hide();
            $("#bookDetails").hide();
            $("#activityDetails").show();
        });
    });


