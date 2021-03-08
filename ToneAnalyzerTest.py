import json #json module
import re #regex module
from ibm_watson import ToneAnalyzerV3 #imports tone analyzer from watson module
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator #authentication command

authenticator = IAMAuthenticator('maeMiifGGFeGzuqkvf24d-MbZvJVUybEpGQ_oV74joUd')#auth info
tone_analyzer = ToneAnalyzerV3(
    version='2021-01-12', #change date to previous release dates for different version
    authenticator=authenticator)
tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/792102c8-7d97-4918-83c8-e27a044493e7') #auth info


text1 = input("enter a sentence: ")
#text1 = 'i hate you' #target string to be analysed

tone_analysis = tone_analyzer.tone(
    {'text': text1},
    content_type='application/json'
    ).get_result()#sends text to TA and returns in json dictionary format




##print(json.dumps(tone_analysis, indent=2)) #prints returned analysis dictionary, indentation for formatting purposes
out1 = json.dumps(tone_analysis, indent=2) #sets variable with analyzed tones
##print(out1) #prints full tone analysis 
##test1 = re.search(".*tone_id.*\n", out1) #regex search to find all lines beginning with "tone_id"
##print((test1).group()) #prints test1 regex search
##test2 = re.findall("anger""score", out1)
#print(test2, "test 2")

for m in re.finditer(".*tone_id.*", out1):
    toneList = m.group()
    print (toneList)


##
##if out1.find("Anger") != -1:
##    print("text 1 has anger")
##else:
##    print("no anger")

