{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">
    <link rel="stylesheet" href="{% static 'hindi_chatbot_ui/styles.css' %}">
    <title>हिंदी चैटबॉट</title>
    <script>
        function emotion_alert()
        {

        if (document.getElementById("message").value == "समाप्त" ) {
            alert("the top emotion throughout the conversation was: {{alert}}");
            
        }
        }
    </script>
</head>

<body>
    <div class="wrapper">
        <div class="title">हिंदी चैटबॉट</div>
        <div class="box">
            <div class="item">
                <div class="icon">
                    <i class="fa fa-user"></i>
                </div>
                <div class="msg">
                    <p>कृपया अपनी समस्या बताएं। </p>
                </div>
            </div>

            {% for i, j in mylist %}
            <div class="item right">
                <div class="msg">
                    <p>{{ j }}</p>
                </div>
            </div>
            <br clear="both">
            <div class="item">
                <div class="icon">
                    <i class="fa fa-user"></i>
                </div>
                <div class="msg">
                    <p>{{ i }}</p>
                </div>
            </div>

            {% endfor %}
        </div>

        <form action="{% url 'index' %}" method="post">
            {% csrf_token %}
        <div class="typing-area">
                <div class="input-field">
                    <input type="text" id="message" placeholder="अपना उत्तर टाइप करें" required name="message">
                    <button onclick="emotion_alert()">भेजें</button>
                </div>
            </div>
        </form>
    </div>
   
</body>

</html>


