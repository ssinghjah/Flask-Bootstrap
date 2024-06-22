$(document).ready(function() {

    function callBackEnd(api, data) {
        $.ajax({
            url: '/' + api,
            contentType: 'application/json',
            data: JSON.stringify(data),
            type: 'POST',
            success: function(response) {
                // Update the message paragraph with the response from Flask
                console.log("success");
                //$('#message').text(response.message);
            },
            error: function(xhr, status, error) {
                // Handle errors if any
                console.error('Error:', error);
            }
        });

    }

    console.log("ready.")
    $("#startSession").click(function(){
        console.log("start session called.")
        data = {"session_name":"for-demo"}
        $.ajax({
            url: '/start-session',
            contentType: 'application/json',
            data: JSON.stringify(data),
            type: 'POST',
            success: function(response) {
                // Update the message paragraph with the response from Flask
                console.log("success");
                //$('#message').text(response.message);
            },
            error: function(xhr, status, error) {
                // Handle errors if any
                console.error('Error:', error);
            }
        });
    })

    $("#stopSession").click(function(){
        console.log("stop session called.")
        data = {"session_name":"for-demo"}
        callBackEnd("end-session", data)
    })

    $("#validateSession").click(function(){
        console.log("validate session called.")
        data = {"session_name":"test", "metadata_url": "1M8vAA-dUf_ZbSRW74vw_E1peNWKwxtxY"}
        $.ajax({
            url: '/end-session',
            data: JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',
            type: 'POST',
            success: function(response) {
                // Update the message paragraph with the response from Flask
                console.log("success");
                //$('#message').text(response.message);
            },
            error: function(xhr, status, error) {
                // Handle errors if any
                console.error('Error:', error);
            }
        });
    })
    
    $("#submitSession").click(function(){
        console.log("submit session called.")
            $.ajax({
            url: '/submit-ticket',
            type: 'POST',
            success: function(response) {
                // Update the message paragraph with the response from Flask
                console.log("success");
                //$('#message').text(response.message);
            },
            error: function(xhr, status, error) {
                // Handle errors if any
                console.error('Error:', error);
            }
        });
    })
    // When the document is ready, make an AJAX request to Flask backend
   
});