import random as rand
import json
import enum
import colour as col


class EventType(enum):
        SetTheme = "SetTheme"
        SetVFXPreset = "SetVFXPreset"
        SetBackgroundColor = "SetBackgroundColor"
        SetForeground = "SetForeground"


class PythonDoctor:

    


    def newLevel():
        return({
            "settings":{
    "version": 61, 
    "artist": "Fizzd", 
    "song": "Intimate", 
    "specialArtistType": "None", 
    "artistPermission": "", 
    "artistLinks": "e.g. soundcloud.com/fizzd", 
    "author": "Miner", 
    "difficulty": "Medium", 
    "seizureWarning": False, 
    "previewImage": "", 
    "syringeIcon": "", 
    "previewSong": "", 
    "previewSongStartTime": 0, 
    "previewSongDuration": 10, 
    "songNameHue": 0, 
    "songLabelGrayscale": False, 
    "description": "This is a cool level!", 
    "tags": "slow, guitar, 2p", 
    "separate2PLevelFilename": "", 
    "canBePlayedOn": "OnePlayerOnly", 
    "firstBeatBehavior": "RunNormally", 
    "multiplayerAppearance": "HorizontalStrips", 
    "levelVolume": 1, 
    "rankMaxMistakes": [20, 15, 10, 5], 

    "rankDescription":
    [
        "Better call 911, now!",
        "Ugh, you can do better",
        "Not bad I guess...",
        "We make a good team!",
        "You are really good!",
        "Wow! That's awesome!!"
    ]
},
            "rows":[],
            "events":[],
            "decorations":[],
            "conditionals":[],
            "bookmarks":[],
            "colorPallete":[]
        })

    def newEvent(Bar:int,Beat:int,Type:EventType):
        
        return({"bar":Bar,"beat":Beat,"type":Type})
    



            
