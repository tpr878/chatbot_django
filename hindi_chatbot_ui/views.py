from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from hindi_chatbot_ui.polarity import polarity
from random import choice  
import codecs
import statistics



# Create your views here.
choice_list = []
bot_list = []
user_list = []
emotion_list = [] 
 
def index(request):
    if request.method == "POST":
        message = request.POST['message']
        user_list.append(message)

        while message != "समाप्त":
            # if emotion not found in database 
            if polarity(message)[0] == None:
                if polarity(message)[1] > 0:
                    bot_list.append('POSITIVE')
                
                elif polarity(message)[1] < 0:
                    bot_list.append('NEGATIVE')
                
                elif polarity(message)[1] == 0:
                    bot_list.append('NEUTRAL')


            # if emotion found in database 
            else:
                emotion_list.append(polarity(message)[0][0])
                    
                # if polarity is positive 
                if polarity(message)[1] > 0: 
                    if polarity(message)[0][0] == 'joy':
                        
                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: JOY, Polarity: POSITIVE, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: JOY, Polarity: POSITIVE, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: JOY, Polarity: POSITIVE, Scale: HIGH''')
                    
                    
                    elif polarity(message)[0][0] == 'trust':
                        
                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: TRUST, Polarity: POSITIVE, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: TRUST, Polarity: POSITIVE, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: TRUST, Polarity: POSITIVE, Scale: HIGH''')
                    

                    elif polarity(message)[0][0] == 'surprise':
                        
                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: SURPRISE, Polarity: POSITIVE, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: SURPRISE, Polarity: POSITIVE, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: SURPRISE, Polarity: POSITIVE, Scale: HIGH''')
                    

                    elif polarity(message)[0][0] == 'interest':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: INTEREST, Polarity: POSITIVE, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: INTEREST, Polarity: POSITIVE, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: INTEREST, Polarity: POSITIVE, Scale: HIGH''')
                

                # if polarity is negative 
                elif polarity(message)[1] < 0:
                    
                    if polarity(message)[0][0] == 'fear':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: FEAR, Polarity: NEGATIVE, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: FEAR, Polarity: NEGATIVE, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: FEAR, Polarity: NEGATIVE, Scale: HIGH''')
                    

                    elif polarity(message)[0][0] == 'surprise':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: SURPRISE, Polarity: NEGATIVE, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: SURPRISE, Polarity: NEGATIVE, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: SURPRISE, Polarity: NEGATIVE, Scale: HIGH''')
                    

                    elif polarity(message)[0][0] == 'sadness':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: SADNESS, Polarity: NEGATIVE, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: SADNESS, Polarity: NEGATIVE, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: SADNESS, Polarity: NEGATIVE, Scale: HIGH''')
                        
                    
                    elif polarity(message)[0][0] == 'disgust':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: DISGUST, Polarity: NEGATIVE, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: DISGUST, Polarity: NEGATIVE, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: DISGUST, Polarity: NEGATIVE, Scale: HIGH''')

                    
                    elif polarity(message)[0][0] == 'anger':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: ANGER, Polarity: NEGATIVE, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: ANGER, Polarity: NEGATIVE, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: ANGER, Polarity: NEGATIVE, Scale: HIGH''')

                
                # if polarity is neutral 
                elif polarity(message)[1] == 0:
                    if polarity(message)[0][0] == 'joy':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: JOY, Polarity: NEUTRAL, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: JOY, Polarity: NEUTRAL, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: JOY, Polarity: NEUTRAL, Scale: HIGH''')
                    

                    elif polarity(message)[0][0] == 'trust':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: TRUST, Polarity: NEUTRAL, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: TRUST, Polarity: NEUTRAL, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: TRUST, Polarity: NEUTRAL, Scale: HIGH''')


                    elif polarity(message)[0][0] == 'fear':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: FEAR, Polarity: NEUTRAL, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: FEAR, Polarity: NEUTRAL, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: FEAR, Polarity: NEUTRAL, Scale: HIGH''')

                    
                    elif polarity(message)[0][0] == 'surprise':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: SURPRISE, Polarity: NEUTRAL, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: SURPRISE, Polarity: NEUTRAL, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: SURPRISE, Polarity: NEUTRAL, Scale: HIGH''')

                    
                    elif polarity(message)[0][0] == 'sadness':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: SADNESS, Polarity: NEUTRAL, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: SADNESS, Polarity: NEUTRAL, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: SADNESS, Polarity: NEUTRAL, Scale: HIGH''')

                    
                    elif polarity(message)[0][0] == 'disgust':
                        
                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: DISGUST, Polarity: NEUTRAL, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: DISGUST, Polarity: NEUTRAL, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: DISGUST, Polarity: NEUTRAL, Scale: HIGH''')
                    

                    elif polarity(message)[0][0] == 'anger':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: ANGER, Polarity: NEUTRAL, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: ANGER, Polarity: NEUTRAL, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: ANGER, Polarity: NEUTRAL, Scale: HIGH''')

                    
                    elif polarity(message)[0][0] == 'interest':

                        if polarity(message)[0][1] == 1:
                            bot_list.append('''Emotion: INTEREST, Polarity: NEUTRAL, Scale: LOW''')
                        
                        elif polarity(message)[0][1] == 2:
                            bot_list.append('''Emotion: INTEREST, Polarity: NEUTRAL, Scale: MEDIUM''')
                        
                        elif polarity(message)[0][1] == 3:
                            bot_list.append('''Emotion: INTEREST, Polarity: NEUTRAL, Scale: HIGH''')


                

                # bot_list.append(polarity(message)[0][0])


            mylist = zip(bot_list, user_list)
            return HttpResponseRedirect(reverse("index"))
        
        if len(emotion_list) > 0:
            alert = statistics.mode(emotion_list)
        else:
            alert = None
        
        bot_list.clear() 
        user_list.clear()

        return HttpResponseRedirect(reverse("index"))
    
    else:
        mylist = zip(bot_list, user_list)
        return render(request, "hindi_chatbot_ui/index.html", {
            "mylist": mylist,
            "alert": alert
        })       