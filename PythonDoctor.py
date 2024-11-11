import random as rand
import json
from enum import Enum as enum


class RowType(enum):
    Classic = "Classic"
    OneShot = "Oneshot"

class Category(enum):
    Sounds = "Sounds"
    Rows = "Rows"
    VFX = "VFX"
    Decorations = "Decorations"
    Rooms = "Rooms"


class EventType(enum): #This is a list of all the event types in the game. 1st value is the name, 2nd value is the category, 3rd value is the number of arguments. This is for ease of use.
    SetTheme = ("SetTheme", Category.VFX, 3)
    SetVFXPreset = ("SetVFXPreset", Category.VFX, 3)
    SetBackgroundColor = ("SetBackgroundColor", Category.VFX, 4)
    SetForeground = ("SetForeground", Category.VFX, 4)
    PlaySong = ("PlaySong", Category.Sounds, 3)
    PlaySound = ("PlaySound", Category.Sounds, 3)
    SetBeatsPerMinute = ("SetBeatsPerMinute", Category.Sounds, 1)
    SetClapSounds = ("SetClapSounds", Category.Sounds, 3)
    SetHeartExplodeVolume = ("SetHeartExplodeVolume", Category.Sounds, 1)
    SetHeartExplodeInterval = ("SetHeartExplodeInterval", Category.Sounds, 1)
    Flash = ("Flash", Category.VFX, 2)
    CustomFlash = ("CustomFlash", Category.VFX, 5)
    MoveCamera = ("MoveCamera", Category.VFX, 3)
    SetCrotchetsPerBar = ("SetCrotchetsPerBar", Category.Sounds, 2)
    SayReadyGetSetGo = ("SayReadyGetSetGo", Category.Sounds, 4)
    Move = ("Move", Category.Decorations, 5)
    ShowRooms = ("ShowRooms", Category.Rooms, 3)
    AddClassicBeat = ("AddClassicBeat", Category.Rows, 3)
    AddOneshotBeat = ("AddOneshotBeat", Category.Rows, 3)
    SetGameSound = ("SetGameSound", Category.Sounds, 2)
    SetBeatSound = ("SetBeatSound", Category.Sounds, 2)
    SetCountingSound = ("SetCountingSound", Category.Sounds, 5)
    HideRow = ("HideRow", Category.Rows, 3)
    MoveRow = ("MoveRow", Category.Rows, 4)
    PlayExpression = ("PlayExpression", Category.VFX, 3)
    TintRows = ("TintRows", Category.Rows, 5)
    BassDrop = ("BassDrop", Category.VFX, 2)
    ShakeScreen = ("ShakeScreen", Category.VFX, 2)
    FlipScreen = ("FlipScreen", Category.VFX, 2)
    InvertColors = ("InvertColors", Category.VFX, 1)
    Comment = ("Comment", Category.Decorations, 3)
    Tint = ("Tint", Category.Decorations, 4)
    MoveRoom = ("MoveRoom", Category.Rooms, 5)
    SetOneshotWave = ("SetOneshotWave", Category.Rows, 3)
    PulseCamera = ("PulseCamera", Category.VFX, 4)
    TextExplosion = ("TextExplosion", Category.VFX, 5)
    ShowDialogue = ("ShowDialogue", Category.Decorations, 5)
    ShowStatusSign = ("ShowStatusSign", Category.Decorations, 3)
    FloatingText = ("FloatingText", Category.Decorations, 7)
    ChangePlayersRows = ("ChangePlayersRows", Category.Rows, 4)
    FinishLevel = ("FinishLevel", Category.Decorations, 0)
    PlayAnimation = ("PlayAnimation", Category.VFX, 2)
    ReorderRooms = ("ReorderRooms", Category.Rooms, 1)
    Stutter = ("Stutter", Category.VFX, 5)
    ShowHands = ("ShowHands", Category.Decorations, 5)
    PaintHands = ("PaintHands", Category.Decorations, 4)
    SetHandOwner = ("SetHandOwner", Category.Decorations, 3)
    SetPlayStyle = ("SetPlayStyle", Category.Decorations, 3)
    TagAction = ("TagAction", Category.Decorations, 2)
    CallCustomMethod = ("CallCustomMethod", Category.Decorations, 3)
    NewWindowDance = ("NewWindowDance", Category.Decorations, 5)
    SetVisible = ("SetVisible", Category.Decorations, 2)
    SetRoomContentMode = ("SetRoomContentMode", Category.Rooms, 1)
    Tile = ("Tile", Category.Decorations, 5)
    MaskRoom = ("MaskRoom", Category.Rooms, 3)
    FadeRoom = ("FadeRoom", Category.Rooms, 2)
    SetRoomPerspective = ("SetRoomPerspective", Category.Rooms, 3)
    SetRowXs = ("SetRowXs", Category.Rows, 2)
    AddFreeTimeBeat = ("AddFreeTimeBeat", Category.Rows, 3)
    PulseFreeTimeBeat = ("PulseFreeTimeBeat", Category.Rows, 4)


class Character(enum):
    ADOG = "Adog"
    ALLISON = "Allison"
    ATHLETE = "Athlete"
    ATHLETE_PHYSIO = "AthletePhysio"
    BARISTA = "Barista"
    BEAT = "Beat"
    BODYBUILDER = "Bodybuilder"
    BOY = "Boy"
    BOY_RAYA = "BoyRaya"
    BOY_TANGZHUANG = "BoyTangzhuang"
    BURO = "Buro"
    CLEF = "Clef"
    COCKATIEL = "Cockatiel"
    COLE_GUITAR = "ColeGuitar"
    COLE_SYNTH = "ColeSynth"
    CONTROLLER = "Controller"
    DANCING_COUPLE = "DancingCouple"
    EDEGA = "Edega"
    FARMER = "Farmer"
    FARMER_ALTERNATE = "FarmerAlternate"
    GIRL = "Girl"
    GIRL_CNY = "GirlCNY"
    HOODIE_BOY = "HoodieBoy"
    HOODIE_BOY_ALTERNATE = "HoodieBoyAlternate"
    HOODIE_BOY_BLUE = "HoodieBoyBlue"
    IAN = "Ian"
    IAN_BUBBLE = "IanBubble"
    JANITOR = "Janitor"
    LUCIA = "Lucia"
    LUCKY_BASEBALL = "LuckyBaseball"
    LUCKY_ICE = "LuckyIce"
    LUCKY_BAG = "LuckyBag"
    MARIJA = "Marija"
    MINER = "Miner"
    MRS_STEVENDOG = "MrsStevendog"
    MRS_STEVENSON = "MrsStevenson"
    MR_STEVENDOG = "MrStevendog"
    MR_STEVENSON = "MrStevenson"
    NICOLE_CIGS = "NicoleCigs"
    NICOLE_COFFEE = "NicoleCoffee"
    NICOLE_MINTS = "NicoleMints"
    NONE = "None"
    ORIOLE = "Oriole"
    OWL = "Owl"
    PAIGE = "Paige"
    PARROT = "Parrot"
    PLAYER = "Player"
    POLITICIAN = "Politician"
    PURRITICIAN = "Purritician"
    QUAVER = "Quaver"
    RIN = "Rin"
    RODNEY = "Rodney"
    SAMURAI = "Samurai"
    SAMURAI_BASEBALL = "SamuraiBaseball"
    SAMURAI_BLUE = "SamuraiBlue"
    SAMURAI_BOSS = "SamuraiBoss"
    SAMURAI_BOSS_ALT = "SamuraiBossAlt"
    SAMURAI_GIRL = "SamuraiGirl"
    SAMURAI_GREEN = "SamuraiGreen"
    SAMURAI_PIRATE = "SamuraiPirate"
    SAMURAI_YELLOW = "SamuraiYellow"
    SATURDAY = "Saturday"
    SMOKIN_BARISTA = "SmokinBarista"
    TENTACLE = "Tentacle"
    TREBLE = "Treble"
    
    # Aliases
    LOGAN = BOY
    HAILEY = GIRL
    LUCKY = ATHLETE
    NICOLE_TING = SMOKIN_BARISTA
    COLE_BREW = HOODIE_BOY
    COLE_BREW_BLUE = HOODIE_BOY_BLUE

class BeatSounds(enum):
    SHAKER = "Shaker"
    NONE = "None"
    SHAKER_HIGH = "Shaker High"
    STICK = "Stick"
    STICK_OLD = "Stick Old"
    SIDESTICK = "Sidestick"
    PUNCH = "Punch"
    RIDE2 = "Ride2"
    KICK = "Kick"
    KICK_CHROMA = "Kick Chroma"
    KICK_CLEAN = "Kick Clean"
    KICK_TIGHT = "Kick Tight"
    KICK_HOUSE = "Kick House"
    KICK_RUPTURE = "Kick Rupture"
    KICK_ECHO = "Kick Echo"
    HAMMER = "Hammer"
    CHUCK = "Chuck"
    CLOSED_HAT = "Closed Hat"
    TIGHTLY_CLOSED_HAT = "Tightly Closed Hat"
    HAT_HOUSE = "Hat House"
    SIZZLE = "Sizzle"
    CLAVES_LOW = "Claves Low"
    CLAVES_HIGH = "Claves High"
    TOM_LOW_E = "Tom Low E"
    TOM_MID_G = "Tom Mid G"
    TOM_MID_B = "Tom Mid B"
    TOM_HIGH_D = "Tom High D"
    WOOD_BLOCK_HIGH = "Wood Block High"
    WOOD_BLOCK_LOW = "Wood Block Low"
    TRIANGLE_MUTE = "Triangle Mute"
    COWBELL = "Cowbell"
    TIMBALE_HIGH = "Timbale High"
    TIMBALE_LOW = "Timbale Low"

class ClapSounds(enum):
    CLAP_HIT = "Clap Hit"
    REVERB_CLAP = "Reverb Clap"
    CLAP_HIT_2 = "Clap Hit 2"
    CLAP_HIT_MASSIVE_PRE_ECHO = "Clap Hit Massive Pre Echo"
    CLAP_HIT_ECHO = "Clap Hit Echo"
    SNARE_ACOUSTIC_2 = "Snare Acoustic 2"
    SNARE_ACOUSTIC_4 = "Snare Acoustic 4"
    SNARE_HOUSE = "Snare House"
    SNARE_VAPOR = "Snare Vapor"
    CLAP_HIT_CPU = "Clap Hit CPU"


class PythonDoctor():

    


    def newLevel():
        return({
            "settings":{
    "version": 61, 
    "artist": "Fizzd", 
    "song": "Intimate", 
    "specialArtistType": "None", 
    "artistPermission": "", 
    "artistLinks": "soundcloud.com/fizzd", 
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
            "colorPalette":[
                "000000ff",
		        "ffffffff",
		        "7f7f7fff",
		        "c3c3c3ff",
		        "880015ff",
		        "b97a57ff",
		        "ff0000ff",
		        "ffaec9ff",
		        "ff7f27ff",
		        "ffc90eff",
		        "fff200ff",
		        "efe4b0ff",
		        "22b14cff",
		        "b5e61dff",
		        "00a2e8ff",
		        "99d9eaff",
		        "3f48ccff",
		        "7092beff",
		        "a349a4ff",
		        "c8bfe7ff",
		        "00000000"
                ]
        })

    def newEvent(Bar:int,Beat:int,Type:EventType,*Params:json):  
        output = {"bar":Bar,"beat":Beat,"type":Type.value[0]}
        for x in Params:
            output = output | x

        
        return(output)
    

    def addEventToLevel(Level:json,*Event:json):
        output = Level
        for x in Event:
            output["events"].append(x)

        return(output)
    

    def newRow(Room:int,Row:int,Rowtype:RowType,Character:str,Beatsound:str):
        return({"rooms":[Room],"row":Row,"rowType":Rowtype.value,"player": "P1", "character": Character, "pulseSound": Beatsound})
    

    def addRowtoLevel(Level:json,Row:json):
        output = Level
        output["rows"].append(Row)
        return(output)