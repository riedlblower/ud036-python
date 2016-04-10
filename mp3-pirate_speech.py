import urllib

def get_pirate_speech():
    text = raw_input("Enter the text you'd like to convert into pirate speech: ")
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text)
    translated_text = connection.read()
    connection.close()
    print "In pirate speech this is: " + translated_text
    return translated_text 

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=+" + text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print "Profanity Alert!!!"
    elif "false" in output:
        print "This document has no curse words"
    else:
        print "Could not scan the document properly"
    return

pirate_speech = get_pirate_speech()
check_profanity(pirate_speech)
