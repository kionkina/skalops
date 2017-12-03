from flask import Flask, render_template, json
import requests
import twitter
import Executer3
import sys




app = Flask(__name__)

def analyze_tone(text, username, password):
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-18'
    headers = {"content-type": "text/plain"}
    data = text
    try:
        r = requests.post(watsonUrl, auth=(username, password),
                          headers=headers, data=data)
        return r.text
    except Exception as e:
        print e
        return False





def tone(boop):
 json.loads(analyze_tone( boop, 'b438b590-ddfc-4cd7-a19a-79658f87f4e6', 'pZ3ObmB3jdkt'))['document_tone']['tone_categories'][0]['tones'][0]['tone_name']



    
'''
patrick = test()
"LEN OF PATRICK: ---------------------"
for item in patrick:
    print item
    print "\n"
'''



@app.route("/")
def home():
    test = []
    for i in range(10):
        k = Executer3.makeTweets()
        test.append(k[0])
        test.append(k[1])
        reload(sys)  
        sys.setdefaultencoding('utf8')

    return render_template("index.html", test=test, len=range(len(test)))



if __name__ == "__main__":
    app.debug = True
    app.run()

