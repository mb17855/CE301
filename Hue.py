from phue import Bridge  #imports bridge settings from library
import time #time module
import datetime #date time module
bridgeip = "100.71.232.10"  #sets bridge ip

def light_access(bridgeip): #function to connect to lights
    b = Bridge(bridgeip) #sets bridge ip
    b.connect()
    light_list = b.get_light_objects("name") #sets variable with all lights
    return light_list #returns the list of lights

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
            
def timeLight(): #function for light dependant on time
    lights = light_access(bridgeip)

    now = datetime.datetime.now()
##    if now.hour > 0 and now.hour < 5:
##        for light in lights:
##            lights[light].on = True
##            lights[light].hue = 7000
##            lights[light].saturation = 100
##            lights[light].brightness = 30
##           
    if now.hour > 4 and now.hour < 12:
        for light in lights:
            lights[light].on = True
            lights[light].hue = 7000
            lights[light].saturation = 100
            lights[light].brightness = 130
    elif now.hour > 12 and now.hour < 18:
        for light in lights:
            lights[light].on = True
            lights[light].hue = 7000
            lights[light].saturation = 100
            lights[light].brightness = 200
    elif now.hour > 18 and now.hour < 24:
        for light in lights:
            lights[light].on = True
            lights[light].hue = 7000
            lights[light].saturation = 100
            lights[light].brightness = 70
            
            
def normalLight(): #function for emergency lights
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 7080
        lights[light].saturation = 100
def lightOff():
    lights = light_access(bridgeip)
    for light in lights:
        lights[light].on = False

##aaa =int(input("Type 1 for emergency, 2 for Light on: "))
##if aaa == "1":
##    emergencyLight()
##else:
##    normalLight()
##
##
##
if __name__ == "__main__":
    #lightOff()
    #emergencyLight()
    #normalLight()
    timeLight()

            
    
