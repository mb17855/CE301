import time #time module
import datetime #date time module
bridgeip = "100.71.223.6"  #sets bridge ip
import json #json module
import re #regex module
import speech_recognition as sr
from ibm_watson import ToneAnalyzerV3 #imports tone analyzer from watson module
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator #authentication command
from phue import Bridge  #imports bridge settings from library

authenticator = IAMAuthenticator('maeMiifGGFeGzuqkvf24d-MbZvJVUybEpGQ_oV74joUd')#auth info
tone_analyzer = ToneAnalyzerV3(
    version='2021-01-12', #change date to previous release dates for different version
    authenticator=authenticator)
tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/792102c8-7d97-4918-83c8-e27a044493e7') #auth info

def light_access(bridgeip): #function to connect to lights
    b = Bridge(bridgeip) #sets bridge ip
    b.connect()
    light_list = b.get_light_objects("name") #sets variable with all lights
    return light_list #returns the list of lights

def spRecog():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        global said #sets as global variable // access availiable outside function
        said = ""
        try:
            said = r.recognize_google(audio)
            print("Microphone input: ", said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

def emergencyLight(): #function for emergency lights
    lights = light_access(bridgeip)
    while True: #basic test loop
        time.sleep(0.5) #sleep time to flash lights
        for light in lights:
            lights[light].on = True
            lights[light].hue = 180
            lights[light].saturation = 200
        time.sleep(0.5)
        for light in lights:
            lights[light].on = True
            lights[light].hue = 7000
            lights[light].saturation = 100
            
def redLight():
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = True
        lights[light].xy = [0.7, 0.2986]
        lights[light].saturation = 255
def yellowLight():
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = True
        lights[light].xy = [0.4432, 0.5154]
        lights[light].saturation = 255
def orangeLight():
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = True
        lights[light].xy = [0.5614, 0.4156]
        lights[light].saturation = 255
def greenLight():
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = True
        lights[light].xy = [0.214, 0.709]
        lights[light].saturation = 255
def blueLight():
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = True
        lights[light].xy = [0.139, 0.081]
        lights[light].saturation = 255
def purpleLight():
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = True
        lights[light].xy = [0.139, 0.081]
        lights[light].saturation = 210
def pinkLight():
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = True
        lights[light].xy = [0.2651, 0.1291]
        lights[light].saturation = 180
def brownLight():
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = True
        lights[light].xy = [0.6399, 0.3041]
        lights[light].saturation = 147
            
def normalLight(): #function for normal light
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 120
        lights[light].saturation = 100
def lightOff():
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = False

def moodLight():
    print("Please talk into the mic and wait")
    spRecog()
    print("speech recognition finished")
    text1 = said
    tone_analysis = tone_analyzer.tone(
    {'text': text1},
    content_type='application/json'
    ).get_result()#sends text to TA and returns in json dictionary format
    out1 = json.dumps(tone_analysis, indent=2)
    
    for m in re.finditer(".*tone_id.*", out1):
        toneList = m.group()
        print (toneList)
    if "anger" in toneList:
        redLight()
    elif "fear" in toneList:
        yellowLight()
    elif "joy" in toneList:
        orangeLight()
    elif "sadness" in toneList:
        blueLight()
    elif "analytical" in toneList:
        purpleLight()
    elif "confident" in toneList:
        greenLight()
    elif "tentative" in toneList:
        pinkLight()
    else:
        brownLight()
        
picker = int(input("1) Light off, 2) Normal Light, 3) Mood Light: "))

if __name__ == "__main__":
    if picker == 1:
        lightOff()
    elif picker == 2:
        normalLight()
    elif picker == 3:
        moodLight()

            
    
