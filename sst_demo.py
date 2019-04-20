"""
+++ Main SSTRDX +++

-imports                                    [I]
-lists                                      [II]
-map/reset/display                          [III]
-playerObject                               [IV]
-classes                                    [V]
-generators inc. ships & gridPop            [VI]
-other functions inc. bresenham & help      [VII]
-initialisation                             [VIII]
-main game loop                             [IX]
-notes                                      [X]

Main improvements:
- Energy costs to (some) movement & sensors
- Target feature
- User Interface, screens and screen switching, last screen feature
- Speech function
- Star objects
- Derelict civilians
- Board function, Capture Enemy
- Preliminary Trade and Salvage functions

"""
import random
import time, sys

mineral_ore = ["Dilithium","Jevonite","Trillium","Mizinite","Tritanium","Duridium","Diamagnetic Ore","Fortanium","Kelbonite"]
kli_names = ["BortaS'tej","B'rel","Ehhak","Fragh'ka","T'Kora","Ti'voh","YoHwl'","Zan'zi","RoghvaH","Qu'Vat","noH'pach","Nav'Don"]
kli_house = ["House D'Ghor","House Duras","House Martok","House Kor","House K'toh-maag","House Mo'Kai","House Korath"]
kli_cargo = ["Gagh","Racht","Targ","Bloodwine","Chech'tluth","Armour","Munitions","Plasma Weapons","Medical Supplies","Phaser Rifles","Disruptor Rifles","Heavy Machinery"]
k_crew_names = ["Hur'agha","ghawran","qeyLis","Korax","'atroum","'a'Setbur","tlha'a","ruq'e'vet","Qen","Qa'taq","paq","ml'LLn","qoreQ","be'etor"]
exp_names = ["Midnight","USS Hubris","Orca","Nebechanezzer","HMS Celeste","NuDrive","Excelsior"]
civ_names = ["Cobra MkIII","Stellar Breeze"]
cgo_names = ["Planet Express","Ol' faithful","Steamboat Willy","RS EverSteen","StarCrawler","MassLifter","Big Boy"]
sci_names = ["Midnight","Surveyor 12","technoCore Inc","BFRX2K","Star Gaze 42"]
tpt_names = ["Stagecoach","Starliner","GreyStar","Nexus Spaceway"]
mil_cargo = ["Munitions","Heavy Weapons","Medical Supplies","Rifles","Explosives","Rockets","Heavy Machinery"]
sci_cargo = ["Delta Generator","Ion Charger","Chemical Sampler","Quaser Tuner","High Emission Radar","Deep Field Probes","Quantum Furnace","Full Spectral Scanners","Biomedical Equipment","Long Range Scanners"]
tpt_cargo = ["Luggage","Food Provisions","Medical Equipment","Neck Pillows","In-Flight Magazines","Headphones With Obscure Jacks"]
materials = ["Anidium","Ditrillium","Deandrite","Vulcan Steel","Vibranium"]
crew_names = ["Philip J. Fry","Dr. Zoidberg","Alfonzo","Rodriguez","Juarez","Carter","Ace","Spencer","Jeff","Deejay","Lucas","Kit","Matt","Nathan","Tino","Vicki","Teddy","Hannah","Dan"]
cargo_type = ["Plumbus","Clothes","Munitions","Medical Supplies","Corporate Data","Marijuana","Coffee","Food","Luxury Goods","Machinery","Scientific Equipment"]
captain_names = ["Deej RaEl","Gilgamesh","Antoine Roquentin","B Real","Arthur Eagle","Nikola Tesla","Elon Musk"]
birthplace = ["Iain M. Banks","Dean Bowie","Margaret Thatcher","Venus Williams"]
atmospheres = ["Helium","Oxygen","Hydrogen","Nitrogen"]
ship_salvage = ["Reaction Matrix","Duranium Couplers","Sub-Processing Units","Power Unit","Relays","Nitrium Casing","Iso-Linear Circuits","Qubit Register","Computational Matrix"]
base_material = ["Corundium","Duritanium Polyalloy","Duranium","Dentarium"]
base_essential = ["Noranium","Talgonite"]
ship_material = ["Duranium", "Dentarium", "Polyduranium", "Transparent Aluminium"]
ship_essential = ["Tritanium","Nitrium"]
planet_gas = ["Hydrogen","Helium","Chlorine","Methane","Ammonia","Fluorine"]
fun_num = ["1","2","3","4","5","6","7","8","9"]
random_seeds = ["1111YMY","0210YMY","5000N-N","0100N-Y","0010YVY","0001YMN"]

planet_names = ["Talos","Vulcan","Earth","Idir","Azad"]
classes = ["H","J","K","L","N","R","T","Y"]


""" Map, Reset, Display etc """


sector = [["N01210N-B19","N30000N-N29","N00000YMN39","N00000N-N49","N00000N-N59","N00000N-N69","N00000N-N79","N00000N-N89","N00000N-N99"],
          ["N00000YJN18","N00000S-N28","N00000YLN38","N00000N-N48","N00000N-N58","N00000N-N68","N00000N-N78","N00000N-N88","N00000N-N98"],
          ["N00000N-N17","N01110YVB27","N00000N-N37","N00000N-N47","N30000N-N57","N00000N-N67","N00000N-N77","N00000N-N87","N00000N-N97"],
          ["N00000N-N16","N00000N-N26","N00000N-N36","N00000N-N46","N20000N-N56","N00000N-N66","N00000N-N76","N00000N-N86","N00000N-N96"],
          ["N00000N-N15","N00000N-N25","N00000N-N35","N00000N-N45","Y02100YMB55","N10000YLN65","N00000S-N75","N00000N-N85","N00000N-N95"],
          ["N00000N-N14","N00000N-N24","N00000N-N34","N00000YMN44","N00000S-N54","N00000N-N64","N00000N-N74","N00000N-N84","N00000N-N94"],
          ["N01020N-N13","N00000N-N23","N00000N-N33","N00000N-N43","N00000YLN53","N00000N-N63","N00000N-N73","N00000N-N83","N00000N-N93"],
          ["N00000N-N12","N00000N-N22","N00000N-N32","N00000N-N42","N00000N-N52","N00000N-N62","N00000N-N72","N00000N-N82","N01210YEB92"],
          ["N00000N-N11","N00000N-N21","N00000N-N31","N00000N-N41","N00000N-N51","N00000N-N61","N00000N-N71","N00000YJN81","N00000S-N91"]]

sectorScanned = [["...","...","...","...","...","...","...","...","..."],
                 ["...","***","...","...","...","...","...","...","..."],
                 ["...","...","...","...","...","...","...","...","..."],
                 ["...","...","...","...","...","...","...","...","..."],
                 ["...","...","...","...","...","...","***","...","..."],
                 ["...","...","...","...","...","...","...","...","..."],
                 ["...","...","...","...","...","...","...","...","..."],
                 ["...","...","...","...","...","...","...","...","..."],
                 ["...","...","...","...","...","...","...","...","***"]]

class map():
    def __init__(self):
        self.grid = [[".",".",".",".",".",".",".",".","."],  #0 Y
                     [".",".",".",".",".",".",".",".","."],  #1
                     [".",".",".",".",".",".",".",".","."],  #2
                     [".",".",".",".",".",".",".",".","."],  #3
                     [".",".",".",".",".",".",".",".","."],  #4
                     [".",".",".",".",".",".",".",".","."],  #5
                     [".",".",".",".",".",".",".",".","."],  #6
                     [".",".",".",".",".",".",".",".","."],  #7
                     [".",".",".",".",".",".",".",".","."]]  #8 Y

def resetGrid():
    map.grid = []
    map.grid = [[".",".",".",".",".",".",".",".","."],  #0 Y
                [".",".",".",".",".",".",".",".","."],  #1
                [".",".",".",".",".",".",".",".","."],  #2
                [".",".",".",".",".",".",".",".","."],  #3
                [".",".",".",".",".",".",".",".","."],  #4
                [".",".",".",".",".",".",".",".","."],  #5
                [".",".",".",".",".",".",".",".","."],  #6
                [".",".",".",".",".",".",".",".","."],  #7
                [".",".",".",".",".",".",".",".","."]]  #8 Y

def lrsDisplay():
    game.currentScreen = "lrs"
    neighbour()
    print("9 |" + codeToLrs(sectorScanned[0][0]) + "|" + codeToLrs(sectorScanned[0][1]) + "|" + codeToLrs(sectorScanned[0][2]) + "|" + codeToLrs(sectorScanned[0][3]) + "|" + codeToLrs(sectorScanned[0][4]) + "|" + codeToLrs(sectorScanned[0][5]) + "|" + codeToLrs(sectorScanned[0][6]) + "|" + codeToLrs(sectorScanned[0][7]) + "|" + codeToLrs(sectorScanned[0][8]) + "|")
    print("8 |" + codeToLrs(sectorScanned[1][0]) + "|" + codeToLrs(sectorScanned[1][1]) + "|" + codeToLrs(sectorScanned[1][2]) + "|" + codeToLrs(sectorScanned[1][3]) + "|" + codeToLrs(sectorScanned[1][4]) + "|" + codeToLrs(sectorScanned[1][5]) + "|" + codeToLrs(sectorScanned[1][6]) + "|" + codeToLrs(sectorScanned[1][7]) + "|" + codeToLrs(sectorScanned[1][8]) + "|")
    print("7 |" + codeToLrs(sectorScanned[2][0]) + "|" + codeToLrs(sectorScanned[2][1]) + "|" + codeToLrs(sectorScanned[2][2]) + "|" + codeToLrs(sectorScanned[2][3]) + "|" + codeToLrs(sectorScanned[2][4]) + "|" + codeToLrs(sectorScanned[2][5]) + "|" + codeToLrs(sectorScanned[2][6]) + "|" + codeToLrs(sectorScanned[2][7]) + "|" + codeToLrs(sectorScanned[2][8]) + "|")
    print("6 |" + codeToLrs(sectorScanned[3][0]) + "|" + codeToLrs(sectorScanned[3][1]) + "|" + codeToLrs(sectorScanned[3][2]) + "|" + codeToLrs(sectorScanned[3][3]) + "|" + codeToLrs(sectorScanned[3][4]) + "|" + codeToLrs(sectorScanned[3][5]) + "|" + codeToLrs(sectorScanned[3][6]) + "|" + codeToLrs(sectorScanned[3][7]) + "|" + codeToLrs(sectorScanned[3][8]) + "|")
    print("5 |" + codeToLrs(sectorScanned[4][0]) + "|" + codeToLrs(sectorScanned[4][1]) + "|" + codeToLrs(sectorScanned[4][2]) + "|" + codeToLrs(sectorScanned[4][3]) + "|" + codeToLrs(sectorScanned[4][4]) + "|" + codeToLrs(sectorScanned[4][5]) + "|" + codeToLrs(sectorScanned[4][6]) + "|" + codeToLrs(sectorScanned[4][7]) + "|" + codeToLrs(sectorScanned[4][8]) + "|")
    print("4 |" + codeToLrs(sectorScanned[5][0]) + "|" + codeToLrs(sectorScanned[5][1]) + "|" + codeToLrs(sectorScanned[5][2]) + "|" + codeToLrs(sectorScanned[5][3]) + "|" + codeToLrs(sectorScanned[5][4]) + "|" + codeToLrs(sectorScanned[5][5]) + "|" + codeToLrs(sectorScanned[5][6]) + "|" + codeToLrs(sectorScanned[5][7]) + "|" + codeToLrs(sectorScanned[5][8]) + "|")
    print("3 |" + codeToLrs(sectorScanned[6][0]) + "|" + codeToLrs(sectorScanned[6][1]) + "|" + codeToLrs(sectorScanned[6][2]) + "|" + codeToLrs(sectorScanned[6][3]) + "|" + codeToLrs(sectorScanned[6][4]) + "|" + codeToLrs(sectorScanned[6][5]) + "|" + codeToLrs(sectorScanned[6][6]) + "|" + codeToLrs(sectorScanned[6][7]) + "|" + codeToLrs(sectorScanned[6][8]) + "|")
    print("2 |" + codeToLrs(sectorScanned[7][0]) + "|" + codeToLrs(sectorScanned[7][1]) + "|" + codeToLrs(sectorScanned[7][2]) + "|" + codeToLrs(sectorScanned[7][3]) + "|" + codeToLrs(sectorScanned[7][4]) + "|" + codeToLrs(sectorScanned[7][5]) + "|" + codeToLrs(sectorScanned[7][6]) + "|" + codeToLrs(sectorScanned[7][7]) + "|" + codeToLrs(sectorScanned[7][8]) + "|")
    print("1 |" + codeToLrs(sectorScanned[8][0]) + "|" + codeToLrs(sectorScanned[8][1]) + "|" + codeToLrs(sectorScanned[8][2]) + "|" + codeToLrs(sectorScanned[8][3]) + "|" + codeToLrs(sectorScanned[8][4]) + "|" + codeToLrs(sectorScanned[8][5]) + "|" + codeToLrs(sectorScanned[8][6]) + "|" + codeToLrs(sectorScanned[8][7]) + "|" + codeToLrs(sectorScanned[8][8]) + "|")
    print("    1   2   3   4   5   6   7   8   9")
    print("\nCurrent Zone:",game.currentZone)

def codeToLrs(zone):

    if zone == "...":
        return zone
    if zone == "***":
        return zone
    if zone[6] == "S":
        return "***"
    else:
        num = int(zone[2]) + int(zone[3]) + int(zone[4])
        if int(zone[1]) > 0:
            kli = zone[1]
        else:
            kli = " "
        if num > 0:
            civ = str(num)
        else:
            civ = " "
        if zone[6] == "Y":
            planet = "P"
        else:
            planet = " "
        if zone[8] == "B":
            base = "B"
        else:
            base = " "
        code = kli + planet + base
        return code

def discoDisplay():

    game.currentScreen = "disco"
    if disco.shldSt == True:
        shieldScreen = "Online"
        if disco.shldUp == True:
            shldUp = "Up"
        else:
            shldUp = "Down"
    else:
        shieldScreen = "Offline"
        shldUp = "Down"
    if disco.helmSt == True:
        helmScreen = "Online"
    else:
        helmScreen = "Offline"
    if disco.lifeSt == True:
        lifeScreen = "Operational"
    else:
        lifeScreen = "Critically Damaged"
    if disco.shldUp == False:
        shldScrn = 0
    else:
        shldScrn = disco.shields * 10
    speech(game.lastTitle,game.lastMsg)
    print("______________________Discovery :\n")
    print("9",map.grid[0][0],map.grid[0][1],map.grid[0][2],map.grid[0][3],map.grid[0][4],map.grid[0][5],map.grid[0][6],map.grid[0][7],map.grid[0][8],"| Hull Integrity:",disco.hull)
    print("8",map.grid[1][0],map.grid[1][1],map.grid[1][2],map.grid[1][3],map.grid[1][4],map.grid[1][5],map.grid[1][6],map.grid[1][7],map.grid[1][8],"| Current Zone:",game.currentZone)
    print("7",map.grid[2][0],map.grid[2][1],map.grid[2][2],map.grid[2][3],map.grid[2][4],map.grid[2][5],map.grid[2][6],map.grid[2][7],map.grid[2][8],"| Current Coordinates:",disco.hOld)
    print("6",map.grid[3][0],map.grid[3][1],map.grid[3][2],map.grid[3][3],map.grid[3][4],map.grid[3][5],map.grid[3][6],map.grid[3][7],map.grid[3][8],"| Crew:",disco.crewNo)
    print("5",map.grid[4][0],map.grid[4][1],map.grid[4][2],map.grid[4][3],map.grid[4][4],map.grid[4][5],map.grid[4][6],map.grid[4][7],map.grid[4][8],"| Energy -",disco.energy)
    print("4",map.grid[5][0],map.grid[5][1],map.grid[5][2],map.grid[5][3],map.grid[5][4],map.grid[5][5],map.grid[5][6],map.grid[5][7],map.grid[5][8],"| Shields -",shieldScreen,"-",shldUp,"-",shldScrn,"%")
    print("3",map.grid[6][0],map.grid[6][1],map.grid[6][2],map.grid[6][3],map.grid[6][4],map.grid[6][5],map.grid[6][6],map.grid[6][7],map.grid[6][8],"| Photon Torpedoes -",disco.photonNum)
    print("2",map.grid[7][0],map.grid[7][1],map.grid[7][2],map.grid[7][3],map.grid[7][4],map.grid[7][5],map.grid[7][6],map.grid[7][7],map.grid[7][8],"| Away Team:",disco.team)
    print("1",map.grid[8][0],map.grid[8][1],map.grid[8][2],map.grid[8][3],map.grid[8][4],map.grid[8][5],map.grid[8][6],map.grid[8][7],map.grid[8][8],"| Life Support -",lifeScreen)
    print("  1 2 3 4 5 6 7 8 9")

def objDisplay():

    game.currentScreen = "obj"
    speech(game.lastTitle,game.lastMsg)
    print("______________________Short Range Scanners :\n")
    print("9",map.grid[0][0],map.grid[0][1],map.grid[0][2],map.grid[0][3],map.grid[0][4],map.grid[0][5],map.grid[0][6],map.grid[0][7],map.grid[0][8],"|",objDis(0),disHull(0),objHull(0))
    print("8",map.grid[1][0],map.grid[1][1],map.grid[1][2],map.grid[1][3],map.grid[1][4],map.grid[1][5],map.grid[1][6],map.grid[1][7],map.grid[1][8],"|",objDis(1),disHull(1),objHull(1))
    print("7",map.grid[2][0],map.grid[2][1],map.grid[2][2],map.grid[2][3],map.grid[2][4],map.grid[2][5],map.grid[2][6],map.grid[2][7],map.grid[2][8],"|",objDis(2),disHull(2),objHull(2))
    print("6",map.grid[3][0],map.grid[3][1],map.grid[3][2],map.grid[3][3],map.grid[3][4],map.grid[3][5],map.grid[3][6],map.grid[3][7],map.grid[3][8],"|",objDis(3),disHull(3),objHull(3))
    print("5",map.grid[4][0],map.grid[4][1],map.grid[4][2],map.grid[4][3],map.grid[4][4],map.grid[4][5],map.grid[4][6],map.grid[4][7],map.grid[4][8],"|",objDis(4),disHull(4),objHull(4))
    print("4",map.grid[5][0],map.grid[5][1],map.grid[5][2],map.grid[5][3],map.grid[5][4],map.grid[5][5],map.grid[5][6],map.grid[5][7],map.grid[5][8],"|",objDis(5),disHull(5),objHull(5))
    print("3",map.grid[6][0],map.grid[6][1],map.grid[6][2],map.grid[6][3],map.grid[6][4],map.grid[6][5],map.grid[6][6],map.grid[6][7],map.grid[6][8],"|",objDis(6),disHull(6),objHull(6))
    print("2",map.grid[7][0],map.grid[7][1],map.grid[7][2],map.grid[7][3],map.grid[7][4],map.grid[7][5],map.grid[7][6],map.grid[7][7],map.grid[7][8],"|",objDis(7),disHull(7),objHull(7))
    print("1",map.grid[8][0],map.grid[8][1],map.grid[8][2],map.grid[8][3],map.grid[8][4],map.grid[8][5],map.grid[8][6],map.grid[8][7],map.grid[8][8],"|",objDis(8),disHull(8),objHull(8))
    print("  1 2 3 4 5 6 7 8 9")

def mainScreen():

    game.currentScreen = "main"
    target = game.target[0]
    if target.objType == "civilian" or target.objType == "klingon":

        speech(game.lastTitle,game.lastMsg)
        print("______________________" + target.name, end = '')
        for i in range(30 - len(target.name)):
            print("_", end = '')
        print("\n")
        print("9",map.grid[0][0],map.grid[0][1],map.grid[0][2],map.grid[0][3],map.grid[0][4],map.grid[0][5],map.grid[0][6],map.grid[0][7],map.grid[0][8],"| Class",target.desc)
        print("8",map.grid[1][0],map.grid[1][1],map.grid[1][2],map.grid[1][3],map.grid[1][4],map.grid[1][5],map.grid[1][6],map.grid[1][7],map.grid[1][8],"| Coordinates",target.hXY)
        print("7",map.grid[2][0],map.grid[2][1],map.grid[2][2],map.grid[2][3],map.grid[2][4],map.grid[2][5],map.grid[2][6],map.grid[2][7],map.grid[2][8],"|_______________________________")
        print("6",map.grid[3][0],map.grid[3][1],map.grid[3][2],map.grid[3][3],map.grid[3][4],map.grid[3][5],map.grid[3][6],map.grid[3][7],map.grid[3][8],"|")
        print("5",map.grid[4][0],map.grid[4][1],map.grid[4][2],map.grid[4][3],map.grid[4][4],map.grid[4][5],map.grid[4][6],map.grid[4][7],map.grid[4][8],"| Captain:",tgtMCap(target))
        print("4",map.grid[5][0],map.grid[5][1],map.grid[5][2],map.grid[5][3],map.grid[5][4],map.grid[5][5],map.grid[5][6],map.grid[5][7],map.grid[5][8],"| Lifesigns:",tgtMCrew(target))
        print("3",map.grid[6][0],map.grid[6][1],map.grid[6][2],map.grid[6][3],map.grid[6][4],map.grid[6][5],map.grid[6][6],map.grid[6][7],map.grid[6][8],"| Composition:",tgtMComp(target))
        print("2",map.grid[7][0],map.grid[7][1],map.grid[7][2],map.grid[7][3],map.grid[7][4],map.grid[7][5],map.grid[7][6],map.grid[7][7],map.grid[7][8],"| Cargo:", tgtMCargo(target))
        print("1",map.grid[8][0],map.grid[8][1],map.grid[8][2],map.grid[8][3],map.grid[8][4],map.grid[8][5],map.grid[8][6],map.grid[8][7],map.grid[8][8],"| ")
        print("  1 2 3 4 5 6 7 8 9")

    elif target.objType == "planet":

        speech(game.lastTitle,game.lastMsg)
        print("______________________" + target.name, end = '')
        for i in range(30 - len(target.name)):
            print("_", end = '')
        print("\n")
        print("9",map.grid[0][0],map.grid[0][1],map.grid[0][2],map.grid[0][3],map.grid[0][4],map.grid[0][5],map.grid[0][6],map.grid[0][7],map.grid[0][8],"|",target.pClass,"Class Planet -",target.desc2)
        print("8",map.grid[1][0],map.grid[1][1],map.grid[1][2],map.grid[1][3],map.grid[1][4],map.grid[1][5],map.grid[1][6],map.grid[1][7],map.grid[1][8],"|_______________________________")
        print("7",map.grid[2][0],map.grid[2][1],map.grid[2][2],map.grid[2][3],map.grid[2][4],map.grid[2][5],map.grid[2][6],map.grid[2][7],map.grid[2][8],"| ")
        print("6",map.grid[3][0],map.grid[3][1],map.grid[3][2],map.grid[3][3],map.grid[3][4],map.grid[3][5],map.grid[3][6],map.grid[3][7],map.grid[3][8],"| Biology:",tgtMBio(target))
        print("5",map.grid[4][0],map.grid[4][1],map.grid[4][2],map.grid[4][3],map.grid[4][4],map.grid[4][5],map.grid[4][6],map.grid[4][7],map.grid[4][8],"| Population:",tgtMPop(target))
        print("4",map.grid[5][0],map.grid[5][1],map.grid[5][2],map.grid[5][3],map.grid[5][4],map.grid[5][5],map.grid[5][6],map.grid[5][7],map.grid[5][8],"| Atmosphere:",tgtMAtmos(target))
        print("3",map.grid[6][0],map.grid[6][1],map.grid[6][2],map.grid[6][3],map.grid[6][4],map.grid[6][5],map.grid[6][6],map.grid[6][7],map.grid[6][8],"| Year:",tgtMYear(target))
        print("2",map.grid[7][0],map.grid[7][1],map.grid[7][2],map.grid[7][3],map.grid[7][4],map.grid[7][5],map.grid[7][6],map.grid[7][7],map.grid[7][8],"| Day:",tgtMDay(target))
        print("1",map.grid[8][0],map.grid[8][1],map.grid[8][2],map.grid[8][3],map.grid[8][4],map.grid[8][5],map.grid[8][6],map.grid[8][7],map.grid[8][8],"| ")
        print("  1 2 3 4 5 6 7 8 9")

    else:

        speech(game.lastTitle,game.lastMsg)
        print("______________________" + target.name, end = '')
        for i in range(30 - len(target.name)):
            print("_", end = '')
        print("\n")
        print("9",map.grid[0][0],map.grid[0][1],map.grid[0][2],map.grid[0][3],map.grid[0][4],map.grid[0][5],map.grid[0][6],map.grid[0][7],map.grid[0][8],"|",target.affiliation,"Space Station")
        print("8",map.grid[1][0],map.grid[1][1],map.grid[1][2],map.grid[1][3],map.grid[1][4],map.grid[1][5],map.grid[1][6],map.grid[1][7],map.grid[1][8],"|_______________________________")
        print("7",map.grid[2][0],map.grid[2][1],map.grid[2][2],map.grid[2][3],map.grid[2][4],map.grid[2][5],map.grid[2][6],map.grid[2][7],map.grid[2][8],"| ")
        print("6",map.grid[3][0],map.grid[3][1],map.grid[3][2],map.grid[3][3],map.grid[3][4],map.grid[3][5],map.grid[3][6],map.grid[3][7],map.grid[3][8],"| Population:",tgtMPop(target))
        print("5",map.grid[4][0],map.grid[4][1],map.grid[4][2],map.grid[4][3],map.grid[4][4],map.grid[4][5],map.grid[4][6],map.grid[4][7],map.grid[4][8],"| Status: Green")
        print("4",map.grid[5][0],map.grid[5][1],map.grid[5][2],map.grid[5][3],map.grid[5][4],map.grid[5][5],map.grid[5][6],map.grid[5][7],map.grid[5][8],"| System: This One")
        print("3",map.grid[6][0],map.grid[6][1],map.grid[6][2],map.grid[6][3],map.grid[6][4],map.grid[6][5],map.grid[6][6],map.grid[6][7],map.grid[6][8],"| ")
        print("2",map.grid[7][0],map.grid[7][1],map.grid[7][2],map.grid[7][3],map.grid[7][4],map.grid[7][5],map.grid[7][6],map.grid[7][7],map.grid[7][8],"| ")
        print("1",map.grid[8][0],map.grid[8][1],map.grid[8][2],map.grid[8][3],map.grid[8][4],map.grid[8][5],map.grid[8][6],map.grid[8][7],map.grid[8][8],"| ")
        print("  1 2 3 4 5 6 7 8 9")

def tacticalContactScreen():

    game.currentScreen = "tac"
    target = game.target[0]
    if target.objType == "civilian" or target.objType == "klingon":

        if target.zeta == True:
            if target.shieldSt == True:
                shld = "Online: " + str(target.shieldLvl) + " %"
            else:
                shld = "Offline"
        else:
            shld = "-"

        if target.zeta == True:
            if target.phaserSt == True:
                phsr = "Online: " + str(target.phaserLvl) + " %"
            else:
                phsr = "Offline"
        else:
            phsr = "-"

        if target.zeta == True:
            if target.photonSt == True:
                phtn = "Online: " + str(target.photonLvl) + " %"
            else:
                phtn = "Offline"
        else:
            phtn = "-"

        if target.zeta == True:
            if target.engineSt == True:
                eng = "Online: " + str(target.engineLvl) + " %"
            else:
                eng = "Offline"
        else:
            eng = "-"

        if target.zeta == True:
            if target.lifeSt == True:
                life = "Online"
            else:
                life = "Offline"
        else:
            life = "-"

        speech(game.lastTitle,game.lastMsg)
        print("______________________Tactical: " + target.name, end = '')
        for i in range(20 - len(target.name)):
            print("_", end = '')
        print("\n")
        print("9",map.grid[0][0],map.grid[0][1],map.grid[0][2],map.grid[0][3],map.grid[0][4],map.grid[0][5],map.grid[0][6],map.grid[0][7],map.grid[0][8],"| Coordinates",target.hXY)
        print("8",map.grid[1][0],map.grid[1][1],map.grid[1][2],map.grid[1][3],map.grid[1][4],map.grid[1][5],map.grid[1][6],map.grid[1][7],map.grid[1][8],"| Hull:",str(target.hull))
        print("7",map.grid[2][0],map.grid[2][1],map.grid[2][2],map.grid[2][3],map.grid[2][4],map.grid[2][5],map.grid[2][6],map.grid[2][7],map.grid[2][8],"| Shields -",shld)
        print("6",map.grid[3][0],map.grid[3][1],map.grid[3][2],map.grid[3][3],map.grid[3][4],map.grid[3][5],map.grid[3][6],map.grid[3][7],map.grid[3][8],"| Phasers -",phsr)
        print("5",map.grid[4][0],map.grid[4][1],map.grid[4][2],map.grid[4][3],map.grid[4][4],map.grid[4][5],map.grid[4][6],map.grid[4][7],map.grid[4][8],"| Photon Torpedos -",phtn)
        print("4",map.grid[5][0],map.grid[5][1],map.grid[5][2],map.grid[5][3],map.grid[5][4],map.grid[5][5],map.grid[5][6],map.grid[5][7],map.grid[5][8],"|_______________________________")
        print("3",map.grid[6][0],map.grid[6][1],map.grid[6][2],map.grid[6][3],map.grid[6][4],map.grid[6][5],map.grid[6][6],map.grid[6][7],map.grid[6][8],"| ")
        print("2",map.grid[7][0],map.grid[7][1],map.grid[7][2],map.grid[7][3],map.grid[7][4],map.grid[7][5],map.grid[7][6],map.grid[7][7],map.grid[7][8],"| Engines -", eng)
        print("1",map.grid[8][0],map.grid[8][1],map.grid[8][2],map.grid[8][3],map.grid[8][4],map.grid[8][5],map.grid[8][6],map.grid[8][7],map.grid[8][8],"| Life Support -", life)
        print("  1 2 3 4 5 6 7 8 9")

    else:

        speech(game.lastTitle,game.lastMsg)
        print("______________________Contact: " + target.name, end = '')
        for i in range(21 - len(target.name)):
            print("_", end = '')
        print("\n")
        print("9",map.grid[0][0],map.grid[0][1],map.grid[0][2],map.grid[0][3],map.grid[0][4],map.grid[0][5],map.grid[0][6],map.grid[0][7],map.grid[0][8],"| ")
        print("8",map.grid[1][0],map.grid[1][1],map.grid[1][2],map.grid[1][3],map.grid[1][4],map.grid[1][5],map.grid[1][6],map.grid[1][7],map.grid[1][8],"| ")
        print("7",map.grid[2][0],map.grid[2][1],map.grid[2][2],map.grid[2][3],map.grid[2][4],map.grid[2][5],map.grid[2][6],map.grid[2][7],map.grid[2][8],"| ")
        print("6",map.grid[3][0],map.grid[3][1],map.grid[3][2],map.grid[3][3],map.grid[3][4],map.grid[3][5],map.grid[3][6],map.grid[3][7],map.grid[3][8],"| ")
        print("5",map.grid[4][0],map.grid[4][1],map.grid[4][2],map.grid[4][3],map.grid[4][4],map.grid[4][5],map.grid[4][6],map.grid[4][7],map.grid[4][8],"| ")
        print("4",map.grid[5][0],map.grid[5][1],map.grid[5][2],map.grid[5][3],map.grid[5][4],map.grid[5][5],map.grid[5][6],map.grid[5][7],map.grid[5][8],"| ")
        print("3",map.grid[6][0],map.grid[6][1],map.grid[6][2],map.grid[6][3],map.grid[6][4],map.grid[6][5],map.grid[6][6],map.grid[6][7],map.grid[6][8],"| ")
        print("2",map.grid[7][0],map.grid[7][1],map.grid[7][2],map.grid[7][3],map.grid[7][4],map.grid[7][5],map.grid[7][6],map.grid[7][7],map.grid[7][8],"| ")
        print("1",map.grid[8][0],map.grid[8][1],map.grid[8][2],map.grid[8][3],map.grid[8][4],map.grid[8][5],map.grid[8][6],map.grid[8][7],map.grid[8][8],"| ")
        print("  1 2 3 4 5 6 7 8 9")

def dataScreen():

    game.currentScreen = "data"
    target = game.target[0]
    if target.objType == "civilian" or target.objType == "klingon":

        speech(game.lastTitle,game.lastMsg)
        print("__Data:" + target.name + "_______________________________\n")
        print("Composition:",tgtComp(target,0),"|")
        print("            ",tgtComp(target,1),"|")
        print("            ",tgtComp(target,2),"|")
        print("            ",tgtComp(target,3),"|")
        print("                                 |")
        print("                                 |")
        print("                                 |")

    elif target.objType == "planet":

        speech(game.lastTitle,game.lastMsg)
        print("__Data:" + target.name + "_______________________________\n")
        print("Resources:",tgtDepos(target,0),"|")
        print("          ",tgtDepos(target,1),"|")
        print("          ",tgtDepos(target,2),"|")
        print("          ",tgtDepos(target,3),"|")
        print("Other Data:                     |")
        print("                                |")
        print("                                |")

    else:

        speech(game.lastTitle,game.lastMsg)
        print("__Services:" + target.name + "______________________________\n")
        print("| List of eventual Services:")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")

def listScreen():

    speech(game.lastTitle,game.lastMsg)
    game.currentScreen = "list"
    target = game.target[0]
    if target.objType == "civilian" or target.objType == "klingon":

        print("__Crew & Cargo:" + target.name + "__________________________\n")
        print("Crew:",tgtCrew(target,0),"       |")
        print("            ",tgtCrew(target,1),"|")
        print("            ",tgtCrew(target,2),"|")
        print("            ",tgtCrew(target,3),"|")
        print("            ",tgtCrew(target,4),"|")
        print("Cargo:",tgtCargo(target,0),"     |")
        print("           ",tgtCargo(target,1),"|")
        print("           ",tgtCargo(target,2),"|")
        print("           ",tgtCargo(target,3),"|")
        print("           ",tgtCargo(target,4),"|")

def objDis(id):
    msg = ""
    try:
        if game.objCount[id]:
            return game.objCount[id].sectDis
        else:
            return ''
    except:
        return msg

def disHull(id):
    msg = ""
    try:
        if game.objCount[id]:
            if game.objCount[id].objType == "civilian" or game.objCount[id].objType == "klingon":
                return "| Hull: "
            else:
                return ''
    except:
        return msg

def objHull(id):
    msg = ""
    try:
        if game.objCount[id]:
            if game.objCount[id].objType == "civilian" or game.objCount[id].objType == "klingon":
                return game.objCount[id].hull
            else:
                return ''
    except:
        return msg

def tgtCrew(target,id):
    msg = " - "
    if target.zeta == True and target.tau == True:
        return target.crew[id]
    else:
        return msg

def tgtCargo(target,id):
    msg = " - "
    if target.delta == True:
        return target.crew[id]
    else:
        return msg

def tgtDepos(target,id):
    msg = " - "
    if target.theta == True:
        return target.depos[id]
    else:
        return msg

def tgtComp(target,id):
    msg = " - "
    if target.zeta == True:
        return target.comp[id]
    else:
        return msg

def tgtMBio(target):
    msg = " - "
    if target.tau == True:
        return target.inhab
    else:
        return msg

def tgtMPop(target):
    msg = " - "
    if target.tau == True and target.delta == True:
        return target.pop
    else:
        return msg

def tgtMAtmos(target):
    msg = " - "
    if target.delta == True:
        return target.atmos
    else:
        return msg

def tgtMYear(target):
    msg = " - "
    if target.theta == True:
        return target.rotate
    else:
        return msg

def tgtMDay(target):
    msg = " - "
    if target.zeta == True:
        return target.day
    else:
        return msg

def tgtMCargo(target):
        msg = " - "
        if target.delta == True:
            return len(target.cargo)
        else:
            return msg

def tgtMCap(target):
    msg = " - "
    if target.zeta == True:
        return target.captain
    else:
        return msg

def tgtMCrew(target):
    msg = " - "
    if target.tau == True:
        return target.lSigns
    else:
        return msg

def tgtMComp(target):
    msg = " - "
    if target.zeta == True:
        return len(target.composition)
    else:
        return msg


def tgtTWeapon(target):
    nil = " - "
    off = "Offline"
    state = "Online - "
    msg = state + str(target.weaponLvl) + "%"
    if target.zeta == True:
        if target.weaponSt == True:
            return msg
        else:
            return off
    else:
        return nil

def tgtTShield(target):
    nil = " - "
    state = "Online - "
    msg = state + str(target.shieldLvl) + "%"
    if target.zeta == True:
        return msg
    else:
        return nil

def tgtTEngine(target):
    nil = " - "
    state = "Online - "
    msg = state + str(target.engineLvl) + "%"
    if target.zeta == True:
        return msg
    else:
        return nil

def tgtTLife(target):
    nil = " - "
    off = "Offline"
    state = "Online"
    if target.zeta == True:
        if target.lifeSt == True:
            return state
        else:
            return off
    else:
        return nil


""" Player Object - Discovery """

class discovery():
    def __init__(self):
        self.hOld = "5.5"
        self.pOld = "45"
        self.pX = int(self.pOld[0])
        self.pY = int(self.hOld[2])

        # data variables:
        self.energy = 2000
        self.shields = 10
        self.hull = 400
        self.photonNum = 10
        self.crewNo = 420
        self.shuttle = 3
        self.awayMode = 0
        self.team = 0
        self.inventory = []

        # system state variables:
        self.shldUp = False
        self.lifeSt = True
        self.shldSt = True
        self.phsrSt = True
        self.phtnSt = True
        self.helmSt = True
        self.warp = True
        self.impulseSt = True
        self.trnsprtSt = True
        self.shieldLvl = 100
        self.engineLvl = 100
        self.photonLvl = 100
        self.phaserLvl = 100
        self.lifeLvl = 100
        self.docked = False
        self.orbit = False
        self.away = False

    def moveAuto(self,sX,sY):

        if self.away == False:
            self.sX = sX
            self.sY = sY
            nxtCrdH = sX + "." + sY
            pX = str(int(sX) - 1)
            nxtCrdP = pX + sY

            if course(int(self.pOld[0]),int(self.pOld[1]),int(pX),int(sY)):
                if disco.energy > game.moveCount * 10:
                    map.grid[-int(sY)][int(pX)] = "D"
                    map.grid[-int(self.pOld[1])][int(self.pOld[0])] = "."
                    self.hOld = nxtCrdH
                    self.pOld = nxtCrdP
                    self.energy -= game.moveCount * 10
                    self.docked = False
                    self.orbit = False
                    speech("Lt. Detmer","Aye Sir, laying course now...")
                    discoDisplay()
                else:
                    game.lastTitle = "Lt. Detmer"
                    game.lastMsg = "Not enough energy sir..."
                    discoDisplay()
            else:
                if disco.energy > game.moveCount:
                    map.grid[-int(game.pCrash[1])][int(game.pCrash[0])] = "D"
                    if game.pCrash != self.pOld:
                        map.grid[-int(self.pOld[1])][int(self.pOld[0])] = "."
                    self.hOld = game.hCrash
                    self.pOld = game.pCrash
                    self.energy -= game.moveCount * 10
                    self.docked = False
                    self.orbit = False
                    speech("Lt. Detmer","Collision detected Captain!")
                    discoDisplay()
                else:
                    game.lastTitle = "Lt. Detmer"
                    game.lastMsg = "Not enough energy sir..."
                    discoDisplay()
        else:
            game.lastTitle = "Saru"
            game.lastMsg = "Captain! We cannot leave crew behind"
            discoDisplay()

    def moveManual(self,sX,sY):

        if self.away == False:
            self.sX = sX
            self.sY = sY
            self.xSplit = self.sX.split()
            self.ySplit = self.sY.split()

            if self.xSplit[0] == "-":
                x = int(self.xSplit[1])
                # Treat number as a Negative.
                nextX = int(self.pOld[0]) - x
            else:
                x = int(self.xSplit[0])
                # Treat number as a Positive.
                nextX = int(self.pOld[0]) + x

            if self.ySplit[0] == "-":
                y = int(self.ySplit[1])
                # Treat number as a Negative.
                nextY = int(self.pOld[1]) - y
            else:
                y = int(self.ySplit[0])
                # Treat number as a Positive.
                nextY = int(self.pOld[1]) + y

            nxtCrdH = str(nextX + 1) + "." + str(nextY)
            nxtCrdP = str(nextX) + str(nextY)
            #print(game.moveCount)
            if course(int(self.pOld[0]),int(self.pOld[1]),nextX,nextY):
                if disco.energy > game.moveCount * 10:
                    map.grid[-nextY][nextX] = "D"
                    map.grid[-int(self.pOld[1])][int(self.pOld[0])] = "."
                    self.hOld = nxtCrdH
                    self.pOld = nxtCrdP
                    self.docked = False
                    self.orbit = False
                    self.energy -= game.moveCount * 10
                    speech("Lt. Detmer","Aye Sir, laying course now...")
                    discoDisplay()
                else:
                    game.lastTitle = "Lt. Detmer"
                    game.lastMsg = "Not enough energy sir..."
                    discoDisplay()
            else:
                if disco.energy > game.moveCount:
                    map.grid[-int(game.pCrash[1])][int(game.pCrash[0])] = "D"
                    if game.pCrash != self.pOld:
                        map.grid[-int(self.pOld[1])][int(self.pOld[0])] = "."
                    self.hOld = game.hCrash
                    self.pOld = game.pCrash
                    self.energy -= game.moveCount * 10
                    self.docked = False
                    self.orbit = False
                    speech("Lt. Detmer","Collision detected Captain!")
                    discoDisplay()
                else:
                    game.lastTitle = "Lt. Detmer"
                    game.lastMsg = "Not enough energy sir..."
                    discoDisplay()
        else:
            game.lastTitle = "Saru"
            game.lastMsg = "Captain! We cannot leave crew behind"
            discoDisplay()


    def moveZone(self,zX,zY):

        if self.away == False:
            self.zX = zX
            self.zY = zY
            if courseSec(int(game.currentZone[0]),int(game.currentZone[2]),int(self.zX),int(self.zY)):
                if disco.energy > game.moveCount * 100:
                    gridPop2(sector[-int(self.zY)][int(self.zX) - 1])
                    self.energy -= game.moveCount * 100
                    self.docked = False
                    self.orbit = False
                    game.target = []
                    game.lastTitle = "Lt. Detmer"
                    game.lastMsg = "Arriving in new Zone now Captain"
                    discoDisplay()
                else:
                    game.lastTitle = "Lt. Detmer"
                    game.lastMsg = "Not enough energy sir..."
                    discoDisplay()
            else:
                print("Star/Fail/Error")
        else:
            game.lastTitle = "Saru"
            game.lastMsg = "Captain! We cannot leave crew behind"
            discoDisplay()


""" Classes and Objects """

class game():
    def __init__(self):
        self.timer = 0
        self.moveCount = 0
        self.killCount = 0
        self.atkLog = []
        self.atkQueue = []
        self.hCrash = "1.1"
        self.pCrash = "01"
        self.photonHit = []
        self.objCount = []
        self.kliCount = []
        self.currentZone = "5.5"
        self.target = []
        self.currentScreen = "disco"
        self.whiteSpace1 = 0
        self.whiteSpace2 = 0
        self.leftRight1 = 0
        self.leftRight2 = 0
        self.underScore = 0
        self.lastTitle = "Cool Dean Games presents"
        self.lastMsg = "Super Star Trek: REDUX"
        self.pType = "X"
        self.t1dam = 0
        self.t2dam = 0
        self.t3dam = 0

class object():
    instance = 0
    def __init__(self):
        self.ident = object.instance
        self.identH = object.instance + 1
        object.instance += 1
        self.delta = False
        self.zeta = False
        self.theta = False
        self.map = False
        self.tau = False
        self.sig = False

class star(object):
    instance = 0
    def __init__(self):
        object.__init__(self)
        self.starID = star.instance
        star.instance += 1
        self.symbol = "*"
        self.pX = 4
        self.pY = 5
        self.hXY = "5.5"
        self.name = "Sagitarius Something"
        self.desc = " - Star"
        map.grid[2][4] = "*"
        map.grid[3][3] = "*"
        map.grid[3][4] = "*"
        map.grid[3][5] = "*"
        map.grid[4][2] = "*"
        map.grid[4][3] = "*"
        map.grid[4][4] = "*"
        map.grid[4][5] = "*"
        map.grid[4][6] = "*"
        map.grid[5][3] = "*"
        map.grid[5][4] = "*"
        map.grid[5][5] = "*"
        map.grid[6][4] = "*"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc

class ship(object):
    instance = 0
    def __init__(self):
        object.__init__(self)
        self.shipID = ship.instance
        ship.instance += 1
        self.shieldSt = True
        self.engineSt = True
        self.lifeSt = True
        self.photonSt = True
        self.phaserSt = True
        self.shieldLvl = 100
        self.engineLvl = 100
        self.photonLvl = 100
        self.phaserLvl = 100
        self.lifeLvl = 100
        self.hull = 50
        self.hullStat = "Hull: " + str(self.hull)
        self.captured = False


class starbaseSix(object):
    instance = 0
    def __init__(self,pyX,pyY):
        object.__init__(self)
        self.baseID = starbase.instance
        starbase.instance += 1

        self.symbol = "B"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])

        self.name = "Starbase 6"
        if klingon.instance > 0:
            self.condition = "RED"
        else:
            self.condition = "Green"
        self.system = "Sohai"
        self.pop = str(random.randint(1200,3999))
        self.history = "Coming Soon..."
        self.sysInfo = []
        self.cargo = []
        baseMat = set()
        while len(baseMat) < 3:
            baseMat.add(random.choice(base_material))
        baseMat.add(random.choice(base_essential))
        self.strct = baseMat
        self.lSigns = self.pop
        self.desc = " - Space Station"
        self.affiliation = "Federation"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        self.objType = "starbase"


class klingon(ship):
    instance = 0
    def __init__(self,pyX,pyY):
        ship.__init__(self)
        self.kliID = klingon.instance
        klingon.instance += 1

        kliCrew = set()
        while len(kliCrew) < random.randint(4,7):
            kliCrew.add(random.choice(k_crew_names))
        cargo_kli = set()
        while len(cargo_kli) < random.randint(5,8):
            cargo_kli.add(random.choice(kli_cargo))

        self.symbol = "K"

        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])

        self.name = random.choice(kli_names)
        self.crew = kliCrew
        cap_list = list(kliCrew)
        self.captain = random.choice(cap_list)
        self.crew.remove(self.captain)
        self.cargo = cargo_kli
        self.house = random.choice(kli_house)
        self.strct = [random.choice(ship_material)]
        self.strct.append(random.choice(ship_essential))
        self.lSigns = len(self.crew) + 1
        self.desc = " - KLINGON"
        self.hull = 300
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        shipMat = set()
        while len(shipMat) < 3:
            shipMat.add(random.choice(ship_material))
        shipMat.add(random.choice(ship_essential))
        self.composition = shipMat
        self.objType = "klingon"

        # data variables:
        self.hullStat = "// Hull: " + str(self.hull)
        self.energy = 1000
        self.shields = 9
        self.phasers = 0
        self.photon = 0
        self.helm = 100
        self.transporter = 100

class civ(ship):
    instance = 0
    def __init__(self):
        ship.__init__(self)
        self.civID = civ.instance
        civ.instance += 1
        self.objType = "civilian"
        self.hull = 100

class derNpc(civ):
    def __init__(self,pyX,pyY):
        civ.__init__(self)
        expCrew = set()                               # Use a set and it'll NEVER contain duplicates.
        while len(expCrew) < random.randint(5,7):
            expCrew.add(random.choice(crew_names))
        cargo_exp = set()
        while len(cargo_exp) < random.randint(4,7):
            cargo_exp.add(random.choice(cargo_type))

        self.civID = civ.instance
        civ.instance += 1
        self.shieldSt = False
        self.engineSt = False
        self.lifeSt = False
        self.weaponSt = False
        self.symbol = "e"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])
        self.name = random.choice(exp_names)
        self.crew = expCrew
        cap_list = list(expCrew)
        self.captain = random.choice(cap_list)
        self.crew.remove(self.captain)
        self.cargo = cargo_exp
        self.strct = [random.choice(ship_material)]
        self.strct.append(random.choice(ship_essential))
        self.lSigns = 0
        self.desc = " - Explorer"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        shipMat = set()
        while len(shipMat) < 3:
            shipMat.add(random.choice(ship_material))
        shipMat.add(random.choice(ship_essential))
        self.composition = shipMat
        shipSalvage = set()
        while len(shipSalvage) < 4:
            shipSalvage.add(random.choice(ship_salvage))
        self.salvage = list(shipSalvage)
        self.salvage.append("Plasma Relays")

class exp(civ):
    def __init__(self,pyX,pyY):
        civ.__init__(self)
        expCrew = set()                               # Use a set and it'll NEVER contain duplicates.
        while len(expCrew) < random.randint(5,7):
            expCrew.add(random.choice(crew_names))
        cargo_exp = set()
        while len(cargo_exp) < random.randint(4,7):
            cargo_exp.add(random.choice(cargo_type))

        self.civID = civ.instance
        civ.instance += 1

        self.symbol = "e"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])
        self.name = random.choice(exp_names)
        self.crew = expCrew
        cap_list = list(expCrew)
        self.captain = random.choice(cap_list)
        self.crew.remove(self.captain)
        self.cargo = list(cargo_exp)
        xx = 0
        for i in self.cargo:
            self.cargo[xx] = [i,1]
            xx += 1
        self.strct = [random.choice(ship_material)]
        self.strct.append(random.choice(ship_essential))
        self.lSigns = len(self.crew) + 1
        self.desc = " - Explorer"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        shipMat = set()
        while len(shipMat) < 3:
            shipMat.add(random.choice(ship_material))
        shipMat.add(random.choice(ship_essential))
        self.composition = shipMat

    def hail(self):
        speech("Zenir","Stranded. Need a Plasma Injector. D'ya have one?")
        speech("You","Er, no. But, I'm sure we can find one...")

class cgo(civ):
    def __init__(self,pyX,pyY):
        civ.__init__(self)
        cgoCrew = set()
        while len(cgoCrew) < random.randint(3,6):
            cgoCrew.add(random.choice(crew_names))
        cargo_cgo = set()
        while len(cargo_cgo) < random.randint(6,7):
            cargo_cgo.add(random.choice(cargo_type))

        self.civID = civ.instance
        civ.instance += 1

        self.symbol = "f"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])
        self.name = random.choice(cgo_names)
        self.crew = cgoCrew
        cap_list = list(cgoCrew)
        self.captain = random.choice(cap_list)
        self.crew.remove(self.captain)
        self.cargo = list(cargo_cgo)
        xx = 0
        for i in self.cargo:
            self.cargo[xx] = [i,1]
            xx += 1
        self.strct = [random.choice(ship_material)]
        self.strct.append(random.choice(ship_essential))
        self.lSigns = len(self.crew) + 1
        self.desc = " - Cargo Ship"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        shipMat = set()
        while len(shipMat) < 3:
            shipMat.add(random.choice(ship_material))
        shipMat.add(random.choice(ship_essential))
        self.composition = shipMat

class sci(civ):
    def __init__(self,pyX,pyY):
        civ.__init__(self)
        sciCrew = set()
        while len(sciCrew) < random.randint(6,9):
            sciCrew.add(random.choice(crew_names))
        cargo_sci = set()
        while len(cargo_sci) < random.randint(4,7):
            cargo_sci.add(random.choice(sci_cargo))

        self.civID = civ.instance
        civ.instance += 1

        self.symbol = "r"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])
        self.name = random.choice(sci_names)
        self.crew = sciCrew
        cap_list = list(sciCrew)
        self.captain = random.choice(cap_list)
        self.crew.remove(self.captain)
        self.cargo = list(cargo_sci)
        xx = 0
        for i in self.cargo:
            self.cargo[xx] = [i,1]
            xx += 1
        self.strct = [random.choice(ship_material)]
        self.strct.append(random.choice(ship_essential))
        self.lSigns = len(self.crew) + 1
        self.desc = " - Science Vessel"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        shipMat = set()
        while len(shipMat) < 3:
            shipMat.add(random.choice(ship_material))
        shipMat.add(random.choice(ship_essential))
        self.composition = shipMat

class tpt(civ):
    def __init__(self,pyX,pyY):
        civ.__init__(self)
        tptCrew = set()
        while len(tptCrew) < random.randint(6,9):
            tptCrew.add(random.choice(crew_names))
        cargo_tpt = set()
        while len(cargo_tpt) < random.randint(4,7):
            cargo_tpt.add(random.choice(tpt_cargo))

        self.civID = civ.instance
        civ.instance += 1

        self.symbol = "t"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])
        self.name = random.choice(tpt_names)
        self.crew = tptCrew
        cap_list = list(tptCrew)
        self.captain = random.choice(cap_list)
        self.crew.remove(self.captain)
        self.cargo = list(cargo_tpt)
        xx = 0
        for i in self.cargo:
            self.cargo[xx] = [i,1]
            xx += 1
        self.strct = [random.choice(ship_material)]
        self.strct.append(random.choice(ship_essential))
        self.lSigns = len(self.crew) + 1
        self.desc = " - Transport/Liner"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        shipMat = set()
        while len(shipMat) < 3:
            shipMat.add(random.choice(ship_material))
        shipMat.add(random.choice(ship_essential))
        self.composition = shipMat

class derExp(civ):
    def __init__(self,pyX,pyY):
        civ.__init__(self)
        expCrew = set()                               # Use a set and it'll NEVER contain duplicates.
        while len(expCrew) < random.randint(5,7):
            expCrew.add(random.choice(crew_names))
        cargo_exp = set()
        while len(cargo_exp) < random.randint(4,7):
            cargo_exp.add(random.choice(cargo_type))

        self.civID = civ.instance
        civ.instance += 1
        self.shieldSt = False
        self.engineSt = False
        self.lifeSt = False
        self.weaponSt = False
        self.symbol = "e"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])
        self.name = random.choice(exp_names)
        self.crew = expCrew
        cap_list = list(expCrew)
        self.captain = random.choice(cap_list)
        self.crew.remove(self.captain)
        self.cargo = cargo_exp
        self.strct = [random.choice(ship_material)]
        self.strct.append(random.choice(ship_essential))
        self.lSigns = 0
        self.desc = " - Explorer"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        shipMat = set()
        while len(shipMat) < 3:
            shipMat.add(random.choice(ship_material))
        shipMat.add(random.choice(ship_essential))
        self.composition = shipMat
        shipSalvage = set()
        while len(shipSalvage) < 4:
            shipSalvage.add(random.choice(ship_salvage))
        self.salvage = list(shipSalvage)

class derCgo(civ):
    def __init__(self,pyX,pyY):
        civ.__init__(self)
        cgoCrew = set()                               # Use a set and it'll NEVER contain duplicates.
        while len(cgoCrew) < random.randint(5,7):
            cgoCrew.add(random.choice(crew_names))
        cargo_cgo = set()
        while len(cargo_cgo) < random.randint(4,7):
            cargo_cgo.add(random.choice(cargo_type))

        self.civID = civ.instance
        civ.instance += 1
        self.shieldSt = False
        self.engineSt = False
        self.lifeSt = False
        self.weaponSt = False
        self.symbol = "f"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])
        self.name = random.choice(cgo_names)
        self.crew = cgoCrew
        cap_list = list(cgoCrew)
        self.captain = random.choice(cap_list)
        self.crew.remove(self.captain)
        self.cargo = cargo_cgo
        self.strct = [random.choice(ship_material)]
        self.strct.append(random.choice(ship_essential))
        self.lSigns = 0
        self.desc = " - Cargo Ship"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        shipMat = set()
        while len(shipMat) < 3:
            shipMat.add(random.choice(ship_material))
        shipMat.add(random.choice(ship_essential))
        self.composition = shipMat
        shipSalvage = set()
        while len(shipSalvage) < 5:
            shipSalvage.add(random.choice(ship_salvage))
        self.salvage = list(shipSalvage)

class derSci(civ):
    def __init__(self,pyX,pyY):
        civ.__init__(self)
        sciCrew = set()
        while len(sciCrew) < random.randint(6,9):
            sciCrew.add(random.choice(crew_names))
        cargo_sci = set()
        while len(cargo_sci) < random.randint(4,7):
            cargo_sci.add(random.choice(sci_cargo))

        self.civID = civ.instance
        civ.instance += 1
        self.shieldSt = False
        self.engineSt = False
        self.lifeSt = False
        self.weaponSt = False
        self.symbol = "r"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])
        self.name = random.choice(sci_names)
        self.crew = sciCrew
        cap_list = list(sciCrew)
        self.captain = random.choice(cap_list)
        self.crew.remove(self.captain)
        self.cargo = cargo_sci
        self.strct = [random.choice(ship_material)]
        self.strct.append(random.choice(ship_essential))
        self.lSigns = 0
        self.desc = " - Science Vessel"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        shipMat = set()
        while len(shipMat) < 3:
            shipMat.add(random.choice(ship_material))
        shipMat.add(random.choice(ship_essential))
        self.composition = shipMat
        shipSalvage = set()
        while len(shipSalvage) < 6:
            shipSalvage.add(random.choice(ship_salvage))
        self.salvage = list(shipSalvage)

class derTpt(civ):
    def __init__(self,pyX,pyY):
        civ.__init__(self)
        tptCrew = set()
        while len(tptCrew) < random.randint(6,9):
            tptCrew.add(random.choice(crew_names))
        cargo_tpt = set()
        while len(cargo_tpt) < random.randint(4,7):
            cargo_tpt.add(random.choice(tpt_cargo))

        self.civID = civ.instance
        civ.instance += 1
        self.shieldSt = False
        self.engineSt = False
        self.lifeSt = False
        self.weaponSt = False
        self.symbol = "t"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])
        self.name = random.choice(tpt_names)
        self.crew = tptCrew
        cap_list = list(tptCrew)
        self.captain = random.choice(cap_list)
        self.crew.remove(self.captain)
        self.cargo = cargo_tpt
        self.strct = [random.choice(ship_material)]
        self.strct.append(random.choice(ship_essential))
        self.lSigns = 0
        self.desc = " - Transport/Liner"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        shipMat = set()
        while len(shipMat) < 3:
            shipMat.add(random.choice(ship_material))
        shipMat.add(random.choice(ship_essential))
        self.composition = shipMat
        shipSalvage = set()
        while len(shipSalvage) < 4:
            shipSalvage.add(random.choice(ship_salvage))
        self.salvage = list(shipSalvage)

class starbase(object):
    instance = 0
    def __init__(self,pyX,pyY):
        object.__init__(self)
        self.baseID = starbase.instance
        starbase.instance += 1

        self.symbol = "B"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])

        self.name = "Starbase " + str(random.randint(1,6))
        if klingon.instance > 0:
            self.condition = "RED"
        else:
            self.condition = "Green"
        self.system = "Sol"
        self.pop = str(random.randint(1200,3999))
        self.history = "Coming Soon..."
        self.sysInfo = []
        self.cargo = []
        baseMat = set()
        while len(baseMat) < 3:
            baseMat.add(random.choice(base_material))
        baseMat.add(random.choice(base_essential))
        self.strct = baseMat
        self.lSigns = self.pop
        self.desc = " - Space Station"
        self.affiliation = "Federation"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        self.objType = "starbase"

class planet(object):
    instance = 0
    def __init__(self):
        object.__init__(self)
        self.planetID = planet.instance
        planet.instance += 1
        self.objType = "planet"

class sohai(planet):
    def __init__(self,pyX,pyY):
        planet.__init__(self)

        self.symbol = "0"
        self.name = "Sohai IV"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])

        self.pClass = "M"
        game.pType = self.pClass
        self.inhab = "n/a"
        self.contact = "n/a"
        self.depos = "Fortanium"
        self.gas = ["Oxygen","Nitrogen","Hydrogen","Methane"]
        nitro = random.randint(15,31)
        oxy = random.randint(36,49)
        other = 100 - nitro - oxy
        self.atmos = str(nitro) + "% N / " + str(oxy) + "% O2 / " + str(other) + "% Other"
        self.mass = random.randint(0,4)
        self.dens = random.randint(12,65)
        self.diam = random.randint(120,5550)
        self.pop = "-"
        self.rotate = "1 Years"
        self.day = "25 hrs"
        self.lSigns = 99
        self.desc = " - M Class Planet"
        self.desc2 = "'Earth-Like'"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        self.atmoTurb = 36
        self.subsTurb = 4

class vulcan(planet):
    def __init__(self,pyX,pyY):
        planet.__init__(self)

        self.symbol = "0"
        self.name = "Vulcan"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])

        self.pClass = "M"
        game.pType = self.pClass
        self.inhab = "Diverse Biosphere"
        self.contact = "4.9 Billion"
        self.depos = random.choice(mineral_ore)
        self.gas = ["Oxygen","Nitrogen","Hydrogen","Methane"]
        nitro = random.randint(15,31)
        oxy = random.randint(49,67)
        other = 100 - nitro - oxy
        self.atmos = str(nitro) + "% N / " + str(oxy) + "% O2 / " + str(other) + "% Other"
        self.mass = "1.4x1027 kg"
        self.dens = "32.11 kg/m3"
        self.diam = "151900 km"
        self.rotate = "1 year"
        self.day = "25 hrs"
        self.pop = "4.9 Billion"
        self.grav = "1.4g"
        self.lSigns = "-"
        self.desc = " - M Class Planet"
        self.desc2 = "'Earth-Like'"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        self.atmoTurb = random.randint(8,31)
        self.subsTurb = random.randint(1,6)

class earth(planet):
    def __init__(self,pyX,pyY):
        planet.__init__(self)

        self.symbol = "0"
        self.name = "Earth"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])

        self.pClass = "M"
        game.pType = self.pClass
        self.inhab = "Diverse Biosphere"
        self.contact = "4.2 Billion"
        self.depos = random.choice(mineral_ore)
        self.gas = ["Oxygen","Nitrogen","Hydrogen","Methane"]
        nitro = random.randint(15,31)
        oxy = random.randint(49,67)
        other = 100 - nitro - oxy
        self.atmos = str(nitro) + "% N / " + str(oxy) + "% O2 / " + str(other) + "% Other"
        self.mass = "1.4x1027 kg"
        self.dens = "32.11 kg/m3"
        self.diam = "12742 km"
        self.rotate = "1 year"
        self.day = "24 hrs"
        self.pop = "4.2 Billion"
        self.grav = "1.4g"
        self.lSigns = "-"
        self.desc = " - M Class Planet"
        self.desc2 = "'Birthplace of " + random.choice(birthplace) + "'"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        self.atmoTurb = random.randint(8,68)
        self.subsTurb = random.randint(1,33)

class mPlanet(planet):
    def __init__(self,pyX,pyY):
        planet.__init__(self)

        self.symbol = "0"
        self.name = random.choice(planet_names)
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])

        self.pClass = "M"
        game.pType = self.pClass
        self.inhab = "n/a"
        self.contact = "n/a"
        self.depos = random.choice(mineral_ore)
        self.gas = ["Oxygen","Nitrogen","Hydrogen","Methane"]
        nitro = random.randint(15,31)
        oxy = random.randint(36,49)
        other = 100 - nitro - oxy
        self.atmos = str(nitro) + "% N / " + str(oxy) + "% O2 / " + str(other) + "% Other"
        self.mass = random.randint(0,4)
        self.dens = random.randint(12,65)
        self.diam = random.randint(120,5550)
        self.pop = "-"
        self.rotate = str(random.randint(1,5)) + " Years"
        self.day = "25 hrs"
        self.lSigns = 99
        self.desc = " - M Class Planet"
        self.desc2 = "'Earth-Like'"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        self.atmoTurb = random.randint(8,72)
        self.subsTurb = random.randint(1,82)

class jPlanet(planet):
    def __init__(self,pyX,pyY):
        planet.__init__(self)

        self.symbol = "0"
        self.name = "Appropriate Name"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])

        self.pClass = "J"
        game.pType = self.pClass
        if random.randint(1,100) > 99:
            self.inhab = "Molecular Life Detected"
        else:
            self.inhab = "No Biological Signatures Detected"
        self.depos = random.choice(planet_gas)
        self.gas = ["Ammonia","Nitrogen","Hydrogen","Methane","Chlorine"]
        self.mass = "1.8982×1027 kg"
        self.dens = str(random.randint(500,1700)) + " kg/m3"
        self.diam = str(random.randint(80000,160000)) + " km"
        if random.randint(1,10) > 3:
            self.rotate = str(random.randint(1,5)) + " years"
        else:
            self.rotate = str(random.randint(6,121)) + " years"
        self.day = "25 hrs"
        self.lSigns = "-"
        self.pop = "-"
        self.desc = " - J Class Planet"
        self.desc2 = "'Gas-Giant'"
        hydro = random.randint(15,31)
        meth = random.randint(15,31)
        ammo = random.randint(15,31)
        other = 100 - hydro - ammo - meth
        self.atmos = str(hydro) + "% H / " + str(meth) + "% CH4 / "  + str(ammo) + "% NH3 / "+ str(other) + "% Other"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        self.atmoTurb = 100
        self.subsTurb = 100

class lPlanet(planet):
    def __init__(self,pyX,pyY):
        planet.__init__(self)

        self.symbol = "0"
        self.name = "Appropriate Name"
        self.pX = pyX
        self.pY = pyY
        self.argY = self.pY + 1
        self.hXY = str(self.pX + 1) + "." + str(fun_num[-self.argY])
        map.grid[self.pY][self.pX] = self.symbol
        self.pY = int(fun_num[-self.argY])

        self.pClass = "L"
        game.pType = self.pClass
        if random.randint(1,100) > 60:
            self.inhab = "Molecular Life Detected"
        else:
            self.inhab = "RNA Formation Detected"
        self.depos = random.choice(mineral_ore)
        self.gas = ["Oxygen","Nitrogen","Hydrogen","Methane"]
        self.mass = "1.8982×1027 kg"
        self.dens = str(round(random.uniform(1,8), 3)) + " g/cm3"
        self.diam = str(random.randint(80000,160000)) + " km"
        if random.randint(1,10) > 3:
            self.rotate = str(random.randint(1,5)) + " years"
        else:
            self.rotate = str(random.randint(6,121)) + " years"
        self.day = "25 hrs"
        self.lSigns = "-"
        self.desc = " - L Class Planet"
        self.pop = "-"
        self.desc2 = "'Primitive Ecosystem'"
        hydro = random.randint(15,31)
        nitro = random.randint(15,31)
        oxy = random.randint(5,27)
        other = 100 - hydro - oxy - nitro
        self.atmos = str(hydro) + "% H / " + str(nitro) + "% N / "  + str(oxy) + "% O2 / "+ str(other) + "% Other"
        self.sectDis = "- " + str(self.identH) + " - " + self.name + " - " + self.hXY + self.desc
        self.atmoTurb = random.randint(8,84)
        self.subsTurb = random.randint(1,69)


""" Generators etc """

def kliGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = klingon(pgX,pgY)
            game.objCount.append(nil)
            game.kliCount.append(nil)
            break

def expGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = exp(pgX,pgY)
            game.objCount.append(nil)
            break

def cgoGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = cgo(pgX,pgY)
            game.objCount.append(nil)
            break

def sciGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = sci(pgX,pgY)
            game.objCount.append(nil)
            break

def derExpGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = derExp(pgX,pgY)
            game.objCount.append(nil)
            break

def derCgoGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = derCgo(pgX,pgY)
            game.objCount.append(nil)
            break

def derSciGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = derSci(pgX,pgY)
            game.objCount.append(nil)
            break

def derTptGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = derTpt(pgX,pgY)
            game.objCount.append(nil)
            break

def lPGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = lPlanet(pgX,pgY)
            game.objCount.append(nil)
            break

def jPGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = jPlanet(pgX,pgY)
            game.objCount.append(nil)
            break

def mPGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = mPlanet(pgX,pgY)
            game.objCount.append(nil)
            break

def baseGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = starbase(pgX,pgY)
            game.objCount.append(nil)
            break

def vulcanGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = vulcan(pgX,pgY)
            game.objCount.append(nil)
            break

def earthGen():

    pgX = random.randint(0,8)
    pgY = random.randint(0,8)
    while True:
        if map.grid[pgY][pgX] == ".":
            nil = earth(pgX,pgY)
            game.objCount.append(nil)
            break

def gridPop(c):
    if c[0] == "Y":
        quest()
        return
    if map.grid[-int(disco.pOld[1])][int(disco.pOld[0])] == ".":
        map.grid[-int(disco.pOld[1])][int(disco.pOld[0])] = "D"
    # generate each ship type (if any)
    for i in range(int(c[1])):
        # generate Klingons first:
        kliGen()
    for i in range(int(c[2])):
        expGen()
    for i in range(int(c[3])):
        cgoGen()
    for i in range(int(c[4])):
        sciGen()
    if c[6] == "Y":
        if c[7] == "V":
            vulcanGen()
        elif c[7] == "E":
            earthGen()
        elif c[7] == "M":
            mPGen()
        elif c[7] == "J":
            jPGen()
        else:
            lPGen()
    if c[8] == "B":
        baseGen()

def gridPop2(c):
    resetGrid()
    game.currentZone = c[9] + "." + c[10]
    game.objCount = []
    game.kliCount = []
    object.instance = 0
    klingon.instance = 0
    if c[0] == "N":
        if c[6] == "S":
            nil = star()
            game.objCount.append(nil)
            map.grid[0][0] = "D"
            disco.pOld = "09"
            disco.hOld = "11"
            return
        map.grid[-int(disco.pOld[1])][int(disco.pOld[0])] = "D"
        # generate each ship type (if any)
        for i in range(int(c[1])):
            # generate Klingons first:
            kliGen()
        for i in range(int(c[2])):
            expGen()
        for i in range(int(c[3])):
            cgoGen()
        for i in range(int(c[4])):
            sciGen()
        if c[6] == "Y":
            if c[7] == "V":
                vulcanGen()
            elif c[7] == "E":
                earthGen()
            elif c[7] == "M":
                mPGen()
            elif c[7] == "J":
                jPGen()
            else:
                lPGen()
        if c[8] == "B":
            baseGen()
    else:
        quest()
        return


""" Miscellaneous Functions """

def supCode(msg,nLine,delay):
    if nLine == False:
        print(msg, end = '')
        sys.stdout.flush()
        time.sleep(delay)
    else:
        print(msg)
        sys.stdout.flush()
        time.sleep(delay)

def speech(title,message):
    if len(message) > 48:
        print("Message Too Long for One Line")
    else:
        game.lastTitle = title
        game.lastMsg = message
        game.whiteSpace = 52 - len(message)
        game.leftRight = game.whiteSpace / 2

        game.underScore = 50 - len(title)
        print("\n__" + title, end = '')
        for i in range(game.underScore):
            print("_", end = '')
        print("\n")
        print(" ", end = '')
        for i in range(int(game.leftRight) - 1):
            print(" ", end = '')
        print("'" + message + "'", end = '')
        for i in range(int(game.leftRight) - 1):
            print(" ", end = '')
        print("\n____________________________________________________\n")

def speech2(title,msg1,msg2):
    if len(msg1) > 48:
        print("Message Too Long for One Line")
    else:
        game.whiteSpace1 = 52 - len(msg1)
        game.leftRight1 = game.whiteSpace1 / 2
        game.whiteSpace2 = 52 - len(msg2)
        game.leftRight2 = game.whiteSpace2 / 2

        game.underScore = 50 - len(title)
        print("\n__" + title, end = '')
        for i in range(game.underScore):
            print("_", end = '')
        print("\n")
        print(" ", end = '')
        for i in range(int(game.leftRight1) - 1):
            print(" ", end = '')
        print("'" + msg1, end = '')
        for i in range(int(game.leftRight1) - 1):
            print(" ", end = '')
        print(" ")
        for i in range(int(game.leftRight2)):
            print(" ", end = '')
        print(msg2 + "'", end = '')
        for i in range(int(game.leftRight2) - 2):
            print(" ", end = '')
        print(" ")
        print("\n____________________________________________________\n")

def klingonCount():
    for elem in game.kliCount:
        print(elem)

def enemyPha(enemy):
    if enemy.hull >= 0 and enemy.lSigns > 0:
        dam = 25 * enemy.phaserLvl
        dam /= disco.shieldLvl

        disco.hull -= dam
        print("Hit by Klingon at",enemy.hXY,"-",dam)
        sys = random.randint(0,7)
        if sys == 1:
            disco.shieldLvl -= 20
            print("  - Damage to Shields")
            if disco.shieldLvl <= 0:
                disco.shieldSt = False
                disco.shieldLvl = 0
                print("  - Shields Offline")
        elif sys == 2:
            disco.engineLvl -= 20
            print("  - Damage to Engines")
            if disco.engineLvl <= 0:
                disco.engineSt = False
                disco.engineLvl = 0
                print("  - Engines Offline")
        elif sys == 3:
            disco.lifeLvl -= 20
            print("  - Damage to Life Support")
            if disco.lifeLvl <= 0:
                disco.lifeSt = False
                disco.lifeLvl = 0
                print("  - Life Support Offline")
        elif sys == 4:
            disco.phaserLvl -= 20
            print("  - Damage to Phasers")
            if disco.phaserLvl <= 0:
                disco.phaserSt = False
                disco.phaserLvl = 0
                print("  - Phasers Offline")
        elif sys == 5:
            disco.photonLvl -= 20
            print("  - Damage to Photon Tubes")
            if disco.photonLvl <= 0:
                disco.photonSt = False
                disco.photonLvl = 0
                print("  - Photon Torpedos Offline")
        else:
            pass

        if disco.hull <= 0:
            print("Hull Destroyed ")

def phaser():
    target = game.target[0]
    dam = 25 * disco.phaserLvl
    dam /= target.shieldLvl

    if target.objType == "klingon" or target.objType == "civilian":
        print(target.objType + " ['" + target.name + "' @ " + target.hXY + "]:\n  Which System to Target-\n    1 - shields\n    2 - engines\n    3 - life support\n    4 - phasers\n    5 - photon torpedos\n")
        sys = int(input("\n> "))
        target.hull -= dam
        target.lSigns -= random.randint(0,1)
        game.atkLog.append("\nHit! " + target.objType + " @ " + target.hXY + " - " + str(int(dam)) + " units of energy")
        #print("Hit!",target.objType,"@",target.hXY,"-",int(dam),"units of energy\n")
        if random.randint(1,10) > 6:
            game.atkLog.append("    - no Systems damaged")
        elif sys == 1:
            target.shieldLvl -= 20
            game.atkLog.append("    - enemy Shields damaged")
            if target.shieldLvl <= 0:
                target.shieldSt = False
                target.shieldLvl = 0
        elif sys == 2:
            target.engineLvl -= 20
            game.atkLog.append("    - enemy Engines damaged")
            if target.engineLvl <= 0:
                target.engineSt = False
                target.engineLvl = 0
        elif sys == 3:
            target.lifeLvl -= 20
            game.atkLog.append("    - enemy Life Support damaged")
            if target.lifeLvl <= 0:
                target.lifeSt = False
                target.lifeLvl = 0
        elif sys == 4:
            target.phaserLvl -= 20
            game.atkLog.append("    - enemy Phasers damaged")
            if target.phaserLvl <= 0:
                target.phaserSt = False
                target.phaserLvl = 0
        elif sys == 5:
            target.photonLvl -= 20
            game.atkLog.append("    - enemy Photon Torpedos damaged")
            if target.photonLvl <= 0:
                target.photonSt = False
                target.photonLvl = 0
        else:
            pass


        if target.hull <= 0:
            game.killCount += 1
            map.grid[-target.pY][target.pX] = "~"
            target.hull = 0
            target.lSigns = 0
            target.shieldSt = False
            target.engineSt = False
            target.lifeSt = False
            target.phaserSt = False
            target.photonSt = False
            target.sectDis = "- " + str(target.identH) + " - # wreck - " + target.hXY + target.desc
    else:
        speech("Saru","Nope")

def phaserTarget():
    target = game.target[0]
    dam = 25 * disco.phaserLvl
    dam /= target.shieldLvl

    if target.objType == "klingon" or target.objType == "civilian":
        print(target.objType + " ['" + target.name + "' @ " + target.hXY + "]:\n  Which System to Target-\n    1 - shields\n    2 - engines\n    3 - life support\n    4 - phasers\n    5 - photon torpedos\n")
        sys = int(input("\n> "))
        target.hull -= dam
        target.lSigns -= random.randint(0,1)
        game.atkLog.append("\nHit! " + target.objType + " @ " + target.hXY + " - " + str(int(dam)) + " units of energy")
        #print("Hit!",target.objType,"@",target.hXY,"-",int(dam),"units of energy\n")
        if random.randint(1,10) > 6:
            pass
        elif sys == 1:
            target.shieldLvl -= 20
            game.atkLog.append("    - enemy Shields damaged")
            if target.shieldLvl <= 0:
                target.shieldSt = False
                target.shieldLvl = 0
        elif sys == 2:
            target.engineLvl -= 20
            game.atkLog.append("    - enemy Engines damaged")
            if target.engineLvl <= 0:
                target.engineSt = False
                target.engineLvl = 0
        elif sys == 3:
            target.lifeLvl -= 20
            game.atkLog.append("    - enemy Life Support damaged")
            if target.lifeLvl <= 0:
                target.lifeSt = False
                target.lifeLvl = 0
        elif sys == 4:
            target.phaserLvl -= 20
            game.atkLog.append("    - enemy Phasers damaged")
            if target.phaserLvl <= 0:
                target.phaserSt = False
                target.phaserLvl = 0
        elif sys == 5:
            target.photonLvl -= 20
            game.atkLog.append("    - enemy Photon Torpedos damaged")
            if target.photonLvl <= 0:
                target.photonSt = False
                target.photonLvl = 0
        else:
            pass

        if target.hull <= 0:
            game.killCount += 1
            map.grid[-target.pY][target.pX] = "~"
            target.hull = 0
            target.lSigns = 0
            target.shieldSt = False
            target.engineSt = False
            target.lifeSt = False
            target.phaserSt = False
            target.photonSt = False
            target.sectDis = "- " + str(target.identH) + " - # wreck - " + target.hXY + target.desc
        game.lastTitle = "Lt. Owosekun"
        game.lastMsg = "Direct Hit!"
    else:
        speech("Saru","Nope")
        discoDisplay()

def photon():
    target = game.target[0]
    disco.photonNum -= 1
    if course2(disco.pX,disco.pY,target.pX,target.pY):
        if disco.photonNum > 0:
            if game.photonHit[0].objType == "klingon":
                hit = game.photonHit[0]
                dam = random.randint(100,111)
                hit.hull -= dam
                hit.lSigns -= random.randint(0,2)
                print("Hit!",hit.objType,"at",hit.hXY,"-",dam,"units of energy")
                sys = random.randint(1,7)
                if sys == 1:
                    hit.shieldLvl -= 20
                elif sys == 2:
                    hit.photonLvl -= 20
                elif sys == 3:
                    hit.phaserLvl -= 20
                elif sys == 4:
                    hit.engineLvl -= 20
                elif sys == 5:
                    hit.lifeLvl -= 20
                else:
                    pass

                if hit.hull <= 0:
                    map.grid[-hit.pY][hit.pX] = "~"
                    hit.hull = 0
                    hit.lSigns = 0
                    hit.shieldSt = False
                    hit.engineSt = False
                    hit.lifeSt = False
                    hit.phaserSt = False
                    hit.photonSt = False
                    hit.sectDis = "- " + str(hit.identH) + " - # wreck - " + hit.hXY + hit.desc
            elif game.photonHit[0].objType == "civilian":
                hit = game.photonHit[0]
                hit.hull -= random.randint(100,111)
                hit.lSigns -= random.randint(0,2)
                sys = random.randint(1,7)
                if sys == 1:
                    hit.shieldLvl -= 20
                elif sys == 2:
                    hit.photonLvl -= 20
                elif sys == 3:
                    hit.phaserLvl -= 20
                elif sys == 4:
                    hit.engineLvl -= 20
                elif sys == 5:
                    hit.lifeLvl -= 20
                else:
                    pass
                if hit.hull <= 0:
                    map.grid[-hit.pY][hit.pX] = "~"
                    hit.hull = 0
                    hit.lSigns = 0
                    hit.shieldSt = False
                    hit.engineSt = False
                    hit.lifeSt = False
                    hit.phaserSt = False
                    hit.photonSt = False
                    hit.sectDis = "- " + str(hit.identH) + " - # wreck - " + hit.hXY + hit.desc
            elif game.photonHit[0].objType == "starbase":
                speech("Saru","Holy Fuck!")
                time.sleep(0.8)
                speech2("Saru","That was a Starbase","Captain!! Jesus Christ...")
                wait = str(input("- press 'ENTER' to think about your actions -"))
                discoDisplay()
            elif game.photonHit[0].objType == "planet":
                speech("Saru","Dammit Captain")
                time.sleep(0.8)
                speech2("Saru","That's a Planet'","Don't do that.")
                wait = str(input("- press 'ENTER' to think about your actions -"))
            else:
                pass
        else:
            speech("Lt. Owosekun","Out of torpedos")
    game.photonHit = []

def photonTarget():
    target = game.target[0]
    disco.photonNum -= 1
    if course2(disco.pX,disco.pY,target.pX,target.pY):
        if disco.photonNum > 0:
            if game.photonHit[0].objType == "klingon":
                hit = game.photonHit[0]
                dam = random.randint(100,111)
                hit.hull -= dam
                hit.lSigns -= random.randint(0,2)
                sys = random.randint(1,7)
                print("Hit!",hit.objType,"at",hit.hXY,"-",dam,"units of energy")
                if sys == 1:
                    hit.shieldLvl -= 20
                elif sys == 2:
                    hit.photonLvl -= 20
                elif sys == 3:
                    hit.phaserLvl -= 20
                elif sys == 4:
                    hit.engineLvl -= 20
                elif sys == 5:
                    hit.lifeLvl -= 20
                else:
                    pass

                if hit.hull <= 0:
                    map.grid[-hit.pY][hit.pX] = "~"
                    hit.hull = 0
                    hit.lSigns = 0
                    hit.shieldSt = False
                    hit.engineSt = False
                    hit.lifeSt = False
                    hit.phaserSt = False
                    hit.photonSt = False
                    hit.sectDis = "- " + str(hit.identH) + " - # wreck - " + hit.hXY + hit.desc
                game.lastTitle = "Lt. Owosekun"
                game.lastMsg = "Direct Hit!"
            elif game.photonHit[0].objType == "civilian":
                hit = game.photonHit[0]
                hit.hull -= random.randint(100,111)
                hit.lSigns -= random.randint(0,2)
                sys = random.randint(1,7)
                if sys == 1:
                    hit.shieldLvl -= 20
                elif sys == 2:
                    hit.photonLvl -= 20
                elif sys == 3:
                    hit.phaserLvl -= 20
                elif sys == 4:
                    hit.engineLvl -= 20
                elif sys == 5:
                    hit.lifeLvl -= 20
                else:
                    pass
                if hit.hull <= 0:
                    print("Destroyed")
                    map.grid[-hit.pY][hit.pX] = "~"
                    hit.hull = 0
                    hit.lSigns = 0
                    hit.shieldSt = False
                    hit.engineSt = False
                    hit.lifeSt = False
                    hit.phaserSt = False
                    hit.photonSt = False
                    hit.sectDis = "- " + str(hit.identH) + " - # wreck - " + hit.hXY + hit.desc
            elif game.photonHit[0].objType == "starbase":
                speech("Saru","Holy Fuck!")
                time.sleep(0.8)
                speech2("Saru","That was a Starbase","Captain!! Jesus Christ...")
                wait = str(input("- press 'ENTER' to think about your actions -"))
                discoDisplay()
            elif game.photonHit[0].objType == "planet":
                speech("Saru","Dammit Captain")
                time.sleep(0.8)
                speech2("Saru","That's a Planet'","Don't do that.")
                wait = str(input("- press 'ENTER' to think about your actions -"))
                discoDisplay()
            else:
                pass
        else:
            speech("Lt. Owosekun","Out of torpedos")
    game.photonHit = []
    tacticalContactScreen()

def shields(dir):
    if dir == "+":
        disco.shldUp = True
        disco.energy -= 60
        currentScreenDict[game.currentScreen]()
    elif dir == "-":
        disco.shldUp = False
        disco.energy -= 15
        currentScreenDict[game.currentScreen]()

def inventory():
    for i in disco.inventory:
        print(i)

def salvage(item):
    target = game.target[0]
    target.salvage.remove(item)
    disco.inventory.append(item)

def tradeX():
    target = game.target[0]
    if rangeFinder(2,target.symbol):
        cmd = str(input("1 - View Target Cargo\n2 - View Own Cargo\n> "))
        if cmd == "1":
            invList()
        elif cmd == "2":
            holdList()
        else:
            pass
    else:
        game.lastTitle = "Lt. Owosekun"
        game.lastMsg = "Target out of range"
        discoDisplay()

def invList():
    tgt = game.target[0]
    for elem in tgt.cargo:
        ind = tgt.cargo.index(elem) + 1
        print(ind,elem[0],"x",elem[1])
    cmd = int(input("\nItem?\n> "))
    num = int(input("\nQuantity?\n> "))
    itemMove(tgt[cmd - 1][0],num,cmd - 1,1)

def holdList():
    for elem in disco.hold:
        ind = disco.hold.index(elem) + 1
        print(ind,elem[0],"x",elem[1])
    cmd = int(input("\nItem?\n> "))
    num = int(input("\nQuantity?\n> "))
    itemMove(disco.hold[cmd - 1][0],num,cmd - 1,0)

def itemMoveX(item,qty,index,dir):
    target = game.target[0]
    if dir == 1:
        for elem in disco.hold:
            if elem[0] == item:
                mtd = 1
                update = elem
                break
            else:
                mtd = 0
        if mtd == 1:
            update[1] += qty
        else:
            disco.hold.append([item,qty])
        target.cargo[index][1] -= qty
        if target.cargo[index][1] == 0:
            target.cargo.remove(target.cargo[index])
    else:
        for elem in target.cargo:
            if elem[0] == item:
                mtd = 1
                update = elem
                break
            else:
                mtd = 0
        if mtd == 1:
            update[1] += qty
        else:
            target.cargo.append([item,qty])
        disco.hold[index][1] -= qty
        if disco.hold[index][1] == 0:
            disco.hold.remove(disco.hold[index])

def itemMove(item,dir):
    target = game.target[0]
    if dir == "+":
        target.cargo.remove(item)
        disco.inventory.append(item)
    else:
        target.cargo.append(item)
        disco.inventory.remove(item)

def trade():
    target = game.target[0]
    if rangeFinder(2,target.symbol):
        cmd = int(input("1 - Give Item?\n2 - Receive Item?\n"))
        if cmd == 2:
            listX = target.cargo
            for i in listX:
                print(str(listX.index(i) + 1),"-",i)
            cmd = int(input("Which item?\n> "))
            itemMove(target.cargo[cmd - 1],"+")
        elif cmd == 1:
            listD = disco.inventory
            for i in listD:
                print(str(listD.index(i) + 1),"-",i)
            cmd = int(input("Which item?\n> "))
            itemMove(disco.inventory[cmd - 1],"-")
    else:
        game.lastTitle = "Lt. Owosekun"
        game.lastMsg = "Target out of range"
        discoDisplay()

def guide():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Select a Topic:\n\n1) Wtf am I looking at?!\n2) Navigation\n3) Managing Yo Ship\n4) Interacting with Ships, Planets & Bases\n5) COMBAT!\n6) Everything Else...\n\n  - press 'ENTER' to exit -\n\n\n\n\n")
    cmd = str(input("\n> "))
    if cmd == '':
        discoDisplay()
    elif int(cmd) == 1:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("- Wtf am I looking at?! -\n")
        print("  Whenever you type 's' (Short Range Scanners) or 'd' (Discovery)")
        print("  you'll be met with a grid and a load of text to the right of it")
        print("  The grid represents the space around you and the characters in")
        print("  that grid are all the objects surrounding you.")
        print("  There is also a text box above this which displays some relevant")
        print("  information or message...\n")
        print("  Civilian ships are lowercase letters:")
        print("  'e'  - Explorer")
        print("  'f'  - Freighter/Cargo Ship")
        print("  'r'  - Research/Science Vessel")
        print("  't'  - Transport Ship/Liner\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to continue -"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  Everything Else:")
        print("  'K' is a Klingon ship,")
        print("  'B' is a Starbase and")
        print("  '0' is a Planet\n")
        print("  and that is largely it for the display and the types of")
        print("  object/entity you'll encounter...\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to exit -"))
        guide()
    elif int(cmd) == 2:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("- Navigation -\n")
        print("  The map is called a Sector and is comprised of ")
        print("  81 zones. Each Zone is then itself comprised of")
        print("  81 spaces. With me so far?\n")
        print("  The grid you see on the display is one of these")
        print("  zones. You can type 'lrs' (Long Range Scanners)")
        print("  to see the map and also to scan the Zones surr-")
        print("  ounding you... (more on the 'lrs' screen later)\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to continue -"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  Moving around each Zone is as easy as typing:")
        print("  'mv' followed by the coordinates you'd like to")
        print("  visit. It is important you place a space")
        print("  between 'mv' and each coordinate, for example:\n")
        print("  mv 3 7\n")
        print("  is the correct syntax to move to the coordinates")
        print("  x 3 and y 7.")
        print("  If that doesn't appeal to you for whatever")
        print("  reason, you can also type:")
        print("  'mm' followed by the Amount you'd like to move")
        print("  on the X and the Y axis, for example:\n")
        print("  mm 2 -2\n")
        print("  would move you two forward on the X axis and 2")
        print("  downwards on the Y axis (negative numbers move")
        print("  you backwards or downwards)\n\n\n")
        wait = str(input("- press 'ENTER' to continue -"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  Moving between Zones, however, requires the ")
        print("  'warp' command, naturally.")
        print("  To warp between different Zones you simply")
        print("  'warp' followed by the Zone Coordinates you'd")
        print("  like to visit. For example:\n")
        print("  warp 2 9\n")
        print("  is the correct syntax to move to the Zone at")
        print("  2 9 on the Galactic Map ('lrs' command).\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to continue -"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  The Long Range Scanner Screen:")
        print("  Each Zone on the LRS screen is represented by")
        print("  three characters. If you haven't been to or ")
        print("  scanned the Zone, it'll simply be '...'")
        print("  If you have scanned it though, it will display")
        print("  3 different things:")
        print("  The first character will be the number of Kli-")
        print("  ngons in that Zone. Blank if None.")
        print("  The second character shows a 'P' if there is a ")
        print("  planet present. Blank if Not.")
        print("  The third character shows a 'B' if there is a ")
        print("  Starbase present. Blank if Not.")
        print("  '***' represents a Star.\n")
        print("  Moving costs energy, keep an eye on it or else")
        print("  you might find yourself stranded.\n")
        print("  Oh, and you can't Warp through Stars...\n\n\n")
        wait = str(input("- press 'ENTER' to exit -"))
        guide()
    elif int(cmd) == 3:
        print("- Managing yo Ship -\n")
        print("  So you're the Captain of a Starship! That's pretty")
        print("  cool!")
        print("  It's easy enough to manage, you can put your")
        print("  shields up or down by typing:")
        print("  'shields up' or 'shields down' and if you're too")
        print("  lazy to do that, don't worry I got you fam; you")
        print("  can also just type:")
        print("  'sh u' or 'sh d', admittedly the shields don't")
        print("  actually do anything in this game yet. But that's")
        print("  how you do it.\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to continue -"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  To dock with a Starbase you type:")
        print("  'dock', as long as you're next to it, you'll then")
        print("  be docked. Same goes for orbiting planets, though")
        print("  with the command 'orbit' instead.")
        print("  Docking with a Starbase replenishes your ships")
        print("  energy and torpedos. More functionality will be")
        print("  added in time.")
        print("  You'll need to be in a planets orbit in order to")
        print("  send an away team (command 'land' once in orbit)")
        print("  or to extract its resources; again, more functio-")
        print("  nality to come in time...\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to continue -"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  Check your inventory with 'hold'\n")
        print("  Check your damage with 'damage'\n")
        print("  That's about it for managing your ship though")
        print("  it has a tonne more functionality explored in")
        print("  the Guide Topic:")
        print("  Interacting with Ships, Planets and Bases")
        print("  as well as")
        print("  COMBAT!\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to exit -"))
        guide()
    elif int(cmd) == 4:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("- Interacting with Ships, Planets & Bases -\n")
        print("  If you're curious about what's around you, type 's'")
        print("  to bring up the Short Range Scanners. This will    ")
        print("  display a numbered list of all the objects in the  ")
        print("  zone: ships, bases and planets for now.\n")
        print("  To get more info or to interact with something,")
        print("  type 't' followed by the number next to the object")
        print("  you want to Target (with a space between them).\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to continue -"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  Sensors:\n")
        print("  At first you won't know a lot about all these objects,")
        print("  to learn more you need to Scan them. There are 5")
        print("  different scans that can be performed:\n")
        print("  'delta' - Weak sensor, returns cargo")
        print("  'zeta'  - System sensor, returns ship system info")
        print("  'theta' - Powerful sensor, required to board ships")
        print("  'tau'   - Biological sensor, detects lifesigns etc")
        print("  'sigma' - Signal sensor, detects transmissions")
        print("            (not used yet)")
        print("  'sweep' - This command performs all scans at once.\n")
        print("  Performing scans uses time and energy, allowing")
        print("  enemies to attack. Scan wisely.\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to continue -"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  Some Things You Can Do With Targets:\n")
        print("  If they're Civilian or a Starbase, you could try")
        print("  'trade' to trade items, though you'll have to be")
        print("  within 2 spaces.")
        print("  If they're abandoned (0 lifesigns), and you've")
        print("  performed at least a Delta, Theta and Zeta Scan")
        print("  you can board the ship and salvage components with")
        print("  the 'sal' command.\n")
        print("  You can also board a Klingon vessel, so long as")
        print("  their shields are down and you've scanned them,")
        print("  using the 'board' command\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to continue -"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  You can find information on which Scans have and")
        print("  haven't been performed on a Target with the 'data'")
        print("  command if the Target is a Ship. Similarly, typing:")
        print("  'cc' will return info on the Crew and Cargo.")
        print("  ('data' and 'cc' are still works in progress)\n")
        print("  If the target is a planet, you can type 'planet' to")
        print("  see a print-out of information for the target")
        print("  planet.\n")
        print("  There's probs more to do, I'm sure you'll figure it")
        print("  all out...\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to exit -"))
        guide()
    elif int(cmd) == 5:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("- Combat -\n")
        print("  There are two weapons at your disposal - Phasers and")
        print("  Photon Torpedos.")
        print("  You're able to attack up to three targets at once.")
        print("  To attack multiple enemies type either 'pho' or 'pha'")
        print("  followed by the coordinates you want to attack.")
        print("  For example:\n")
        print("  pho 25 63 81\n")
        print("  would fire one Photon Torpedo at each of those coord-")
        print("  inates, if you only typed two sets of coordinates, it")
        print("  would only fire two, etc.")
        print("  If you don't enter any coordinates you'll just attack")
        print("  whatever is currently targeted.")
        print("  Also if you wanted to put spaces between each coordi-")
        print("  nate go ahead, I coded for that! (e.g: pho 3 1 5 4 9 2)\n\n\n\n")
        wait = str(input("- press 'ENTER' to continue -"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  If you destroy a ships Hull you destroy it, and thus")
        print("  cannot board or salvage it. If you manage to kill the")
        print("  crew without destroying the ship you can still board")
        print("  and salvage it. Also, don't forget to perform the Delta")
        print("  Zeta and Theta Scans if you want to board a ship...\n")
        print("  Normally, performing an attack will cost a turn, causing")
        print("  the enemy to attack or other actions to occur.")
        print("  Currently, however, the only action that will cause an")
        print("  enemy attack is the Sensor Sweep! So go ahead and do that")
        print("  on a Klingon for a glimpse of the eventual combat system!\n")
        print("  I'm sure there's more I've forgotten... good luck\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to exit -"))
        guide()
    elif int(cmd) == 6:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("- Everything Else -\n")
        print("  Coming Soon...\n\n\n\n\n\n")
        wait = str(input("- press 'ENTER' to exit -"))
        guide()
    else:
        discoDisplay()




def quest():

    if map.grid[-int(disco.pOld[1])][int(disco.pOld[0])] == ".":
        map.grid[-int(disco.pOld[1])][int(disco.pOld[0])] = "D"
    stranded = exp(7,1)
    trader = cgo(3,5)
    derelict = derNpc(8,8)
    sohaiIV = sohai(1,1)
    game.pType = "M"
    starbase = starbaseSix(6,7)
    game.objCount.append(stranded)
    game.objCount.append(trader)
    game.objCount.append(derelict)
    game.objCount.append(sohaiIV)
    game.objCount.append(starbase)
    trader.cargo.append(["Power Unit",1])

def away():
    target = game.target[0]
    if disco.away == False:
        if disco.crewNo > 2:
            if disco.orbit == True:
                if disco.shuttle > 0:
                    if disco.trnsprtSt == True:
                        while True:
                            disco.team = int(input("Away Team Size (2-10): "))
                            if disco.team > 1 and disco.team < 11:
                                break
                            else:
                                print("Team must be between 2 and 10 crew members...")
                        method = int(input("1 - Shuttle?\n2 - Transporter?\n> "))
                        while True:
                            if method > 0 and method < 3:
                                break
                            else:
                                print("Creative idea, but stick to the options")
                        if method == 1:
                            disco.awayMode = 1
                            disco.shuttle -= 1
                            print("Preparing Shuttlecraft now...")
                            print("Shuttle now launching...")
                            if random.randint(1,100) > target.atmoTurb:
                                print("Away team has landed.")
                                disco.away = True
                                disco.crewNo -= disco.team
                            else:
                                print("Damn. They straight up died.")
                                disco.crewNo -= disco.team
                                disco.team = 0
                        elif method == 2:
                            disco.awayMode = 2
                            print("Preparing Transporter now...")
                            print("Beaming Away Team...")
                            if random.randint(1,100) > target.subsTurb:
                                print("Away team arrived successfully.")
                                disco.away = True
                                disco.crewNo -= disco.team
                            else:
                                print("Damn. They straight up died.")
                                disco.crewNo -= disco.team
                                disco.team = 0
                        else:
                            pass
                    else:
                        while True:
                            disco.team = int(input("Away Team Size (2-10): "))
                            if disco.team > 1 and disco.team < 11:
                                break
                            else:
                                print("Team must be between 2 and 10 crew members...")
                        method = 1
                        disco.awayMode = 1
                        disco.shuttle -= 1
                        print("Preparing Shuttlecraft now...")
                        print("Shuttle now launching...")
                        if random.randint(1,100) > target.atmoTurb:
                            print("Away team has landed.")
                            disco.away = True
                            disco.crewNo -= disco.team
                        else:
                            print("Damn. They straight up died.")
                            disco.crewNo -= disco.team
                            disco.team = 0
                else:
                    while True:
                        disco.team = int(input("Away Team Size (2-10): "))
                        if disco.team > 1 and disco.team < 11:
                            break
                        else:
                            print("Team must be between 2 and 10 crew members...")
                    method = 2
                    disco.awayMode = 1
                    print("Preparing Transporter now...")
                    print("Beaming Away Team...")
                    if random.randint(1,100) > target.subsTurb:
                        print("Away team arrived successfully.")
                        disco.away = True
                        disco.crewNo -= disco.team
                    else:
                        print("Damn. They straight up died.")
                        disco.crewNo -= disco.team
                        disco.team = 0
            else:
                print("Find a planet first...")


def extract():
    for i in game.objCount:
        if i.objType == "planet":
            planet = i
    if game.pType == "J" and disco.orbit == True:
        cmd = int(input("1 - High Orbit Extraction?\n2 - Low Orbit Extraction?\n\n> "))
        if cmd == 1:
            ext = random.choice(planet.gas)
            print("Extracting '" + ext + "' now sir...")
            disco.inventory.append(ext)
        elif cmd == 2:
            print("Extracting '" + planet.depos + "' now sir...")
            disco.inventory.append(planet.depos)
    elif disco.away == True:
        cmd = int(input("1 - Atmospheric Extraction?\n2 - Geological Extraction?\n\n> "))
        if cmd == 1:
            ext = random.choice(planet.gas)
            print("Extracting '" + ext + "' now sir...")
            disco.inventory.append(ext)
        elif cmd == 2:
            print("Extracting '" + planet.depos + "' now sir...")
            disco.inventory.append(planet.depos)
    else:
        speech2("Saru","We first require a presence on the","planet, or must be in orbit...")

def planetType():
    for i in game.objCount:
        if i.objType == "planet":
            print(i.pClass)
            print(i.depos)
        else:
            pass

def returnTeam():
    if disco.away == True:
        if disco.orbit == True:
            if disco.awayMode == 1:
                disco.shuttle += 1
                disco.crewNo += disco.team
                disco.team = 0
                disco.away = False
                print("Shuttlecraft has safely returned...")
            elif disco.awayMode == 2:
                disco.crewNo += disco.team
                disco.team = 0
                disco.away = False
                print("Away team safely onboard...")
    else:
        game.lastTitle = "Saru"
        game.lastMsg = "All crew are already onboard captain"
        discoDisplay()

def cmdList():

    print("List of Commands:\n\nIt may look long, but it's not too bad, trust.\nAlso, if you're ever lost just hit 's' or 'd'\n")
    print("'d'        - Discovery, shows info about yourself.")
    print("'s'        - Short Range Scanners, lists and numbers all the things around you.")
    print("'t #'      - Target, replace '#' with the targets number,")
    print("             then hit 'enter' to cycle through the different Screens for\n             that object.\n             d,s & t are the Main Commands... remember them\n")
    print("'mv x y'   - Move (auto), replace x and y with the coordinates you want \n             to move to.")
    print("'mm x y'   - Move (manual), replace x and y with how Much you want to move\n             Use negative numbers to move backwards,\n             e.g. 'mm 0 -1' would move you down 1 space.")
    print("'warp x y' - Warp, this moves you a whole Zone (That 9x9 Grid you see on\n             the screen is a Zone).\n")
    print("'sh u'     - Shields Up")
    print("'sh d'     - Shields Down")
    print("'lrs'      - Long Range Scanners, shows info on Zones surrounding you.")
    print("'inv'      - Shows your inventory (It starts empty btw).")
    print("'orbit'    - Puts you in orbit of a planet, so long as you're next to it.")
    print("'dock'     - Docks with Starbase, so long as you're next to one.")
    print("'land'     - Land on Planet, send an Away Team to the surface.")
    print("'mine'     - Extracts the planets Mineral Resources")
    print("'return'   - Bring Away Team back to the ship.\n\n")
    print("Sensors:")
    print("'sweep'    - Sensor Sweep, conducts all sensor scans on target at once.")
    print("'delta'    - Delta Scan, one type of scan...")
    print("'zeta'     - Zeta Scan, one type of scan...")
    print("'theta'    - Theta Scan, one type of scan...")
    print("'tau'      - Tau Scan, one type of scan...")
    print("'sigma'    - Sigma Scan, one type of scan...\n")
    print("'board'    - Board Ship, once their shields are down and you've scanned\n             the ship, you can Board.")
    print("'trade'    - Trade, swap items between you and others.\n\n")


def thetaScan():
    target = game.target[0]
    target.theta = True
    mapShip()
    game.lastTitle = "Cmdr. Burnham"
    game.lastMsg = "Theta scan performed Captain"
    game.timer += 1
    if game.timer >= 3:
        for i in game.kliCount:
            enemyPha(i)
        game.timer = 0
    currentScreenDict[game.currentScreen]()

def zetaScan():
    target = game.target[0]
    target.zeta = True
    mapShip()
    game.lastTitle = "Cmdr. Burnham"
    game.lastMsg = "Zeta scan performed Captain"
    game.timer += 1
    if game.timer >= 3:
        for i in game.kliCount:
            enemyPha(i)
        game.timer = 0
    currentScreenDict[game.currentScreen]()

def deltaScan():
    target = game.target[0]
    target.delta = True
    mapShip()
    game.lastTitle = "Cmdr. Burnham"
    game.lastMsg = "Delta scan performed Captain"
    game.timer += 1
    if game.timer >= 3:
        for i in game.kliCount:
            enemyPha(i)
        game.timer = 0
    currentScreenDict[game.currentScreen]()

def tauScan():
    target = game.target[0]
    target.tau = True
    game.lastTitle = "Cmdr. Burnham"
    game.lastMsg = "Tau scan performed Captain"
    game.timer += 1
    if game.timer >= 3:
        for i in game.kliCount:
            enemyPha(i)
        game.timer = 0
    currentScreenDict[game.currentScreen]()

def sigScan():
    target = game.target[0]
    target.sig = True
    game.lastTitle = "Cmdr. Burnham"
    game.lastMsg = "Sigma scan performed Captain"
    game.timer += 1
    if game.timer >= 3:
        for i in game.kliCount:
            enemyPha(i)
        game.timer = 0
    currentScreenDict[game.currentScreen]()

def mapShip():

    target = game.target[0]
    if target.delta == True and target.zeta == True and target.theta == True:
        target.map = True

def target(obj):
    game.target = []
    game.target.append(obj)
    game.lastTitle = "Lt. Owosekun"
    game.lastMsg = "Target acquired Captain"
    mainScreen()

def hailTo():
    target = game.target[0]
    target.hail()

def sensorSweep():
    target = game.target[0]
    target.delta = True
    target.zeta = True
    target.theta = True
    target.tau = True
    target.sigma = True
    mapShip()
    game.lastTitle = "Cmdr. Burnham"
    game.lastMsg = "Sensor sweep performed Captain"
    game.timer += 5
    if game.timer >= 3:
        for i in game.kliCount:
            enemyPha(i)
        game.timer = 0
    currentScreenDict[game.currentScreen]()

def shipImage():
    target = game.target[0]
    print("\n-",target.name)
    borCnt = len(target.name) + 3
    for i in range(borCnt):
        print("_", end = '')
    print("\n\nTier I Data:\n")
    if target.delta == False:
        print("x - Delta Scan Required")
    else:
        print("o - Delta Scan Performed - Basic Ship Structure Acquired")
    if target.zeta == False:
        print("x - Zeta Scan Required")
    else:
        print("o - Zeta Scan Performed - Ship Composition & System Access Acquired")
    if target.theta == False:
        print("x - Theta Scan Required")
    else:
        print("o - Theta Scan Performed - Hi-Res Holograph Acquired")
    if target.delta == True and target.zeta == True and target.theta == True:
        print("o - Full Detail Ship Image Constructed...\n")
    else:
        print("x - Full Detail Ship Image Incomplete...\n")
    print("Tier II Data:\n")
    if target.tau == False:
        print("x - Tau Scan Required")
    else:
        print("o - Tau Scan Performed - Bio-Signatures Registered")
    if target.sig == False:
        print("x - Sigma Scan Required")
    else:
        print("o - Sigma Scan Performed - Subspace Traffic Monitored")

def crCgoScan():
    target = game.target[0]
    if target.map == True:
        print("-",target.name)
        borCnt = len(target.name) + 3
        for i in range(borCnt):
            print("_", end = '')
        print("\n\nCaptain: ", target.captain, "\nCrew:")
        for p in target.crew:
            print(p)
        print("\nCargo:")
        for p in target.cargo:
            print(p)
        print("\n")
    else:
        game.lastTitle = "Cmdr. Burnham"
        game.lastMsg = "Sensor scans required Captain"
        discoDisplay()

def points2(p0, p1):
    game.moveCount = 0
    x0, y0 = p0
    x1, y1 = p1

    dx = abs(x1-x0)
    dy = abs(y1-y0)
    if x0 < x1:
        sx = 1
    else:
        sx = -1


    if y0 < y1:
        sy = 1
    else:
        sy = -1
    err = dx-dy

    while True:
        if x0 == x1 and y0 == y1:
            return True


        e2 = 2*err
        if e2 > -dy:
            err = err - dy
            x0 = x0 + sx
        if e2 < dx:
            err = err + dx
            y0 = y0 + sy
        game.moveCount += 1
        if map.grid[-y0][x0] == "." or map.grid[-y0][x0] == "~":
            continue
        else:
            hitX = x0
            hitY = y0
            for obj in game.objCount:
                if obj.pX == hitX and obj.pY == hitY:
                    game.photonHit.append(obj)
                    return False
    return True

def course2(srcX,srcY,tgtX,tgtY):
    lA = [srcX,srcY]
    lB = [tgtX,tgtY]
    if points2(lA,lB):
        return False
    else:
        return True

def points(p0, p1):
    game.moveCount = 0
    x0, y0 = p0
    x1, y1 = p1

    dx = abs(x1-x0)
    dy = abs(y1-y0)
    if x0 < x1:
        sx = 1
    else:
        sx = -1


    if y0 < y1:
        sy = 1
    else:
        sy = -1
    err = dx-dy

    while True:
        game.hCrash = str(x0 + 1) + "." + str(y0)
        game.pCrash = str(x0) + str(y0)
        if x0 == x1 and y0 == y1:
            return True


        e2 = 2*err
        if e2 > -dy:
            err = err - dy
            x0 = x0 + sx
        if e2 < dx:
            err = err + dx
            y0 = y0 + sy
        game.moveCount += 1
        if map.grid[-y0][x0] == ".":
            continue
        else:
            return False
    return True

def course(srcX,srcY,tgtX,tgtY):
    lA = [srcX,srcY]
    lB = [tgtX,tgtY]
    if points(lA,lB):
        return True
    else:
        return False

def pointsSec(p0, p1):
    game.moveCount = 0
    x0, y0 = p0
    x1, y1 = p1

    dx = abs(x1-x0)
    dy = abs(y1-y0)
    if x0 < x1:
        sx = 1
    else:
        sx = -1


    if y0 < y1:
        sy = 1
    else:
        sy = -1
    err = dx-dy

    while True:
        game.hCrash = str(x0 + 1) + "." + str(y0)
        game.pCrash = str(x0) + str(y0)
        if x0 == x1 and y0 == y1:
            return True


        e2 = 2*err
        if e2 > -dy:
            err = err - dy
            x0 = x0 + sx
        if e2 < dx:
            err = err + dx
            y0 = y0 + sy
        game.moveCount += 1
        if sector[-y0][x0 - 1][6] != "S":
            continue
        else:
            return False
    return True

def courseSec(srcX,srcY,tgtX,tgtY):
    lA = [srcX,srcY]
    lB = [tgtX,tgtY]
    if pointsSec(lA,lB):
        return True
    else:
        return False

def neighbour():

    lrsX = int(game.currentZone[0]) - 1
    lrsY = int(game.currentZone[2])
    sectorScanned[-abs(lrsY)][abs(lrsX)] = sector[-abs(lrsY)][abs(lrsX)]

    try:
        lrsX += 1
        if lrsX > 8 or lrsY == 0:
            pass
        else:
            sectorScanned[-abs(lrsY)][abs(lrsX)] = sector[-abs(lrsY)][abs(lrsX)]

    except:
        pass

    try:
        lrsY += 1
        if lrsY > 9 or lrsY == 0:
            pass
        else:
            sectorScanned[-abs(lrsY)][abs(lrsX)] = sector[-abs(lrsY)][abs(lrsX)]

    except:
        pass

    try:
        lrsX -= 2
        if lrsX > 8 or lrsY == 0:
            pass
        else:
            sectorScanned[-abs(lrsY)][abs(lrsX)] = sector[-abs(lrsY)][abs(lrsX)]

    except:
        pass

    try:
        lrsY -= 2
        if lrsY > 9 or lrsY == 0:
            pass
        else:
            sectorScanned[-abs(lrsY)][abs(lrsX)] = sector[-abs(lrsY)][abs(lrsX)]

    except:
        pass

    try:
        lrsX += 1
        if lrsX > 8 or lrsY == 0:
            pass
        else:
            sectorScanned[-abs(lrsY)][abs(lrsX)] = sector[-abs(lrsY)][abs(lrsX)]

    except:
        pass

    try:
        lrsY += 2
        if lrsY > 9 or lrsY == 0:
            pass
        else:
            sectorScanned[-abs(lrsY)][abs(lrsX)] = sector[-abs(lrsY)][abs(lrsX)]

    except:
        pass

    try:
        lrsY -= 2
        lrsX += 1
        if lrsY > 9 or lrsX > 8 or lrsY == 0:
            pass
        else:
            sectorScanned[-abs(lrsY)][abs(lrsX)] = sector[-abs(lrsY)][abs(lrsX)]

    except:
        pass

    try:
        lrsY += 1
        lrsX -= 2
        if lrsY > 9 or lrsX > 8 or lrsY == 0:
            pass
        else:
            sectorScanned[-abs(lrsY)][abs(lrsX)] = sector[-abs(lrsY)][abs(lrsX)]

    except:
        pass

def rangeFinder(num,target):
    currentX = int(disco.pOld[0])
    currentY = int(disco.pOld[1])
    listX = []
    listY = []
    output = []

    if num < 2:
        listX.append(currentX - 1)
        listX.append(currentX)
        listX.append(currentX + 1)
        listY.append(currentY - 1)
        listY.append(currentY)
        listY.append(currentY + 1)

    if num > 1:
        listX.append(currentX - 1)
        listX.append(currentX)
        listX.append(currentX + 1)
        listX.append(currentX - 2)
        listX.append(currentX + 2)
        listY.append(currentY - 1)
        listY.append(currentY)
        listY.append(currentY + 1)
        listY.append(currentY - 2)
        listY.append(currentY + 2)

    if num < 2:
        for elem in listX:
            output.append([elem,listY[0]])
            output.append([elem,listY[1]])
            output.append([elem,listY[2]])

    if num > 1:
        for elem in listX:
            output.append([elem,listY[0]])
            output.append([elem,listY[1]])
            output.append([elem,listY[2]])
            output.append([elem,listY[3]])
            output.append([elem,listY[4]])


    for elem in output:
        if map.grid[-elem[1]][elem[0]] != target:
            continue
        else:
            return True
        return False

def inRange():
    target = game.target[0]

    currentX = int(disco.pOld[0])
    currentY = int(disco.pOld[1])
    num = 1
    listX = []
    listY = []
    output = []

    while num > 0:
        for i in range(num):
            listX.append(currentX - num)
            listX.append(currentX)
            listX.append(currentX + num)
            listY.append(currentY - num)
            listY.append(currentY)
            listY.append(currentY + num)
        num -= 1

    for elem in listX:
        output.append([elem,listY[0]])
        output.append([elem,listY[1]])
        output.append([elem,listY[2]])

    for elem in output:
        if elem[0] == target.pX and elem[1] == target.pY:
            return True
        else:
            continue
    return False

def rangeFinderTwo(num):
    currentX = int(disco.pOld[0])
    currentY = int(disco.pOld[1])
    listX = []
    listY = []
    output = []

    if num < 2:
        listX.append(currentX - 1)
        listX.append(currentX)
        listX.append(currentX + 1)
        listY.append(currentY - 1)
        listY.append(currentY)
        listY.append(currentY + 1)

    if num > 1:
        #first round
        listX.append(currentX - 1)
        listX.append(currentX)
        listX.append(currentX + 1)
        listX.append(currentX - 2)
        listX.append(currentX + 2)
        listY.append(currentY - 1)
        listY.append(currentY)
        listY.append(currentY + 1)
        listY.append(currentY - 2)
        listY.append(currentY + 2)

    if num < 2:
        for elem in listX:
            output.append([elem,listY[0]])
            output.append([elem,listY[1]])
            output.append([elem,listY[2]])

    if num > 1:
        for elem in listX:
            output.append([elem,listY[0]])
            output.append([elem,listY[1]])
            output.append([elem,listY[2]])
            output.append([elem,listY[3]])
            output.append([elem,listY[4]])


    for elem in output:
        if map.grid[-elem[1]][elem[0]] == ".":
            continue
        else:
            print("Object detected at:",elem[0] + 1, elem[1])
            obj = map.grid[-elem[1]][elem[0]]
            if obj == "B":
                print("Starbase, Dock")
            elif obj == "M" or obj == "L" or obj == "J" or obj == "V" or obj == "E":
                print("Planet, Orbit")
            elif obj == "e" or obj == "f" or obj == "r" or obj == "K":
                print("Ship, Trade")

def rangeFinderOne():
    currentX = int(disco.pOld[0])
    currentY = int(disco.pOld[1])
    num = 1
    listX = []
    listY = []
    output = []

    while num > 0:
        for i in range(num):
            listX.append(currentX - num)
            listX.append(currentX)
            listX.append(currentX + num)
            listY.append(currentY - num)
            listY.append(currentY)
            listY.append(currentY + num)
        num -= 1

    for elem in listX:
        output.append([elem,listY[0]])
        output.append([elem,listY[1]])
        output.append([elem,listY[2]])

    for elem in output:
        if map.grid[-elem[1]][elem[0]] == "." or map.grid[-elem[1]][elem[0]] == "D":
            continue
        else:
            print("Object detected at:",elem[0] + 1, elem[1])
            obj = map.grid[-elem[1]][elem[0]]
            if obj == "B":
                print("Starbase, Dock")
            elif obj == "0":
                print("Planet, Orbit")
            elif obj == "e" or obj == "f" or obj == "r" or obj == "K":
                print("Ship, Trade")


def dock():
    if rangeFinder(1,"B"):
        disco.docked = True
        disco.energy = 3000
        game.lastTitle = "Lt. Owosekun"
        game.lastMsg = "Docked with Starbase..."
        discoDisplay()

def orbit():
    if rangeFinder(1,"0"):
        disco.orbit = True
        disco.energy -= 15
        game.lastTitle = "Lt. Owosekun"
        game.lastMsg = "Entering standard orbit..."
        discoDisplay()

def boardCiv():
    target = game.target[0]
    if rangeFinder(2,target.symbol):
        if target.map == True:
            if target.hull > 0:
                if target.shieldSt == False:
                    print("\n")
                    speech2("Lt. Rhys","Preparing transporter lock now Captain.","How many to beam aboard...?")
                    while True:
                        cmd = int(input("Boarding Party Size (2-6): "))
                        if cmd > 1 and cmd < 7:
                            break
                        else:
                            print("Party must be between 2 and 6 crew members...")
                    party = cmd
                    speech2("Lt. Rhys","Transporter ready Captain...","What's the plan?")
                    print("-1- Salvage Components")
                    print("-2- Access Ships Database")
                    while True:
                        cmd = int(input("\n> "))
                        if cmd > 0 and cmd < 3:
                            break
                        else:
                            print("That's a creative idea but please, pick one of the options...")
                    if cmd == 1:
                        speech("Lt. Rhys","Beaming away team now...")
                        print("      Beam Across | Search Ship | Beam Back")
                        print("----------|*|           |*|          |*|\n")
                        str(input("\n-press ENTER to continue-"))
                        if random.randint(1,100) > 97:
                            print("\n__Officer Rhys______________________________________\n")
                            print("             'Captain! There's been a                ")
                            print("            transporter malfunction...'              ")
                            print("____________________________________________________\n")
                            print("      Beam Across | Search Ship | Beam Back")
                            print("----------|!|           |*|          |*|\n")
                            str(input("\n-press ENTER to continue-"))
                            print("\n__Officer Rhys______________________________________\n")
                            print("            'The team didn't make it...              ")
                            print("                " + str(party) + " souls lost sir.'  ")
                            print("____________________________________________________\n")
                            print("      Beam Across | Secure Ship | Beam Back")
                            print("----------|X|           |*|          |*|\n")
                            disco.crewNo -= party
                            str(input("\n-press ENTER to continue-"))
                            discoDisplay()
                        else:
                            print("\n__Officer Rhys______________________________________\n")
                            print("          'Away Team safely aboard sir!'              ")
                            print("____________________________________________________\n")
                            print("      Beam Across | Search Ship | Beam Back")
                            print("----------|o|-----------|*|          |*|\n")
                            str(input("\n-press ENTER to continue-"))
                            speech2("Lt. Rhys","Displaying salvageable","components now sir.")
                            for elem in target.salvage:
                                print(target.salvage.index(elem) + 1,elem)
                            cmd = int(input("> "))
                            salvage(target.salvage[cmd - 1])
                            while True:
                                for elem in target.salvage:
                                    print(target.salvage.index(elem) + 1,elem)
                                cmd = int(input("Anymore?\n> "))
                                if cmd > 0 and cmd < len(target.salvage) + 1:
                                    salvage(target.salvage[cmd - 1])
                                else:
                                    break
    else:
        game.lastTitle = "Lt. Owosekun"
        game.lastMsg = "Target out of range"
        discoDisplay()

def boardKli():
    target = game.target[0]
    if target.objType == "klingon":
        if target.map == True:
            if target.hull > 0:
                if target.shieldSt == False:
                    print("\n")
                    print("__Officer Rhys______________________________________\n")
                    print("      'Preparing transporter lock now Captain.        ")
                    print("            How many to beam aboard...?'              ")
                    print("____________________________________________________\n")
                    while True:
                        cmd = int(input("Boarding Party Size (2-6): "))
                        if cmd > 1 and cmd < 7:
                            break
                        else:
                            print("Party must be between 2 and 6 crew members...")
                    party = cmd
                    print("\n__Officer Rhys______________________________________\n")
                    print("           'Transporter ready Captain...              ")
                    print("                 What's the plan?'                    ")
                    print("____________________________________________________\n")
                    print("-1- Capture Ship")
                    print("-2- Disable System (Manually)")
                    print("-3- Disable System (Destructively)")
                    print("-4- Annihilate Ship")
                    while True:
                        cmd = int(input("\n> "))
                        if cmd > 0 and cmd < 5:
                            break
                        else:
                            print("That's a creative idea but please, pick one of the options...")
                    if cmd == 1:
                        print("\n__Officer Rhys______________________________________\n")
                        print("             'Beaming Away Team Now...'               ")
                        print("____________________________________________________\n")
                        print("      Beam Across | Secure Ship | Beam Back")
                        print("----------|*|           |*|          |*|\n")
                        str(input("\n-press ENTER to continue-"))
                        if random.randint(1,100) > 97:
                            print("\n__Officer Rhys______________________________________\n")
                            print("             'Captain! There's been a                ")
                            print("            transporter malfunction...'              ")
                            print("____________________________________________________\n")
                            print("      Beam Across | Secure Ship | Beam Back")
                            print("----------|!|           |*|          |*|\n")
                            str(input("\n-press ENTER to continue-"))
                            print("\n__Officer Rhys______________________________________\n")
                            print("            'The team didn't make it...              ")
                            print("                " + str(party) + " souls lost sir.'  ")
                            print("____________________________________________________\n")
                            print("      Beam Across | Secure Ship | Beam Back")
                            print("----------|X|           |*|          |*|\n")
                            disco.crewNo -= party
                            str(input("\n-press ENTER to continue-"))
                            discoDisplay()
                        else:
                            print("\n__Officer Rhys______________________________________\n")
                            print("          'Away Team safely aboard sir!'              ")
                            print("____________________________________________________\n")
                            print("      Beam Across | Secure Ship | Beam Back")
                            print("----------|o|-----------|*|          |*|\n")
                            str(input("\n-press ENTER to continue-"))
                            result = boardCombat(party,target.lSigns)
                            if result[0] == "0":
                                print("\n__Officer Rhys______________________________________\n")
                                print("             'Sensors showing a LOT of                ")
                                print("             phaser activity captain...'              ")
                                print("____________________________________________________\n")
                                print("      Beam Across | Secure Ship | Beam Back")
                                print("----------|o|-----------|!|          |*|\n")
                                str(input("\n-press ENTER to continue-"))
                                print("\n__Officer Rhys______________________________________\n")
                                print("          'The enemy overwhelmed our team...          ")
                                print("                 " + str(party) + " souls lost sir.'  ")
                                print("____________________________________________________\n")
                                print("      Beam Across | Secure Ship | Beam Back")
                                print("----------|o|-----------|X|          |*|\n")
                                disco.crewNo -= party
                                target.lSigns -= int(result[2])
                                print(disco.crewNo)
                                str(input("\n-press ENTER to continue-"))
                                discoDisplay()
                            else:
                                print("\n__Officer Rhys______________________________________\n")
                                print("             'Sensors showing a LOT of                ")
                                print("             phaser activity captain...'              ")
                                print("____________________________________________________\n")
                                print("      Beam Across | Secure Ship | Beam Back")
                                print("----------|o|-----------|!|          |*|\n")
                                str(input("\n-press ENTER to continue-"))
                                print("\n__Officer Rhys______________________________________\n")
                                print("             'Klingon Vessel Secured!'            ")
                                print("____________________________________________________\n")
                                print("      Beam Across | Secure Ship | Beam Back")
                                print("----------|o|-----------|o|----------|*|\n")
                                target.lSigns -= int(result[2])
                                str(input("\n-press ENTER to continue-"))
                                if result[1] == "0":
                                    print("\n__Officer Rhys______________________________________\n")
                                    print("                'Away Team suffered                  ")
                                    print("                  no fatalities!'                   ")
                                    print("____________________________________________________\n")
                                    str(input("\n-press ENTER to continue-"))
                                elif result[1] == "1":
                                    print("\n__Officer Rhys______________________________________\n")
                                    print("               'Away Team suffered                   ")
                                    print("                  1 fatality...'                   ")
                                    print("____________________________________________________\n")
                                    str(input("\n-press ENTER to continue-"))
                                else:
                                    print("\n__Officer Rhys______________________________________\n")
                                    print("                 'Away Team suffered                   ")
                                    print("                   " + str(result[1]) + " fatalities...'  ")
                                    print("____________________________________________________\n")
                                    print("      Beam Across | Secure Ship | Beam Back")
                                    print("----------|o|-----------|o|----------|*|\n")
                                    str(input("\n-press ENTER to continue-"))
                                print("\n__Officer Rhys______________________________________\n")
                                print("           'Beaming Away Team Back Now...'              ")
                                print("____________________________________________________\n")
                                print("      Beam Across | Secure Ship | Beam Back")
                                print("----------|o|-----------|o|----------|*|\n")
                                str(input("\n-press ENTER to continue-"))
                                if random.randint(1,100) > 97:
                                    print("\n__Officer Rhys______________________________________\n")
                                    print("             'Captain! There's been a                ")
                                    print("            transporter malfunction...'              ")
                                    print("____________________________________________________\n")
                                    print("      Beam Across | Secure Ship | Beam Back")
                                    print("----------|o|-----------|o|----------|!|\n")
                                    str(input("\n-press ENTER to continue-"))
                                    print("\n__Officer Rhys______________________________________\n")
                                    print("            'The team didn't make it...              ")
                                    print("                 " + str(party - int(result[1])) + " souls lost sir.'  ")
                                    print("____________________________________________________\n")
                                    print("      Beam Across | Secure Ship | Beam Back")
                                    print("----------|o|-----------|o|----------|X|\n")
                                    disco.crewNo -= party
                                    print(disco.crewNo)
                                    str(input("\n-press ENTER to continue-"))
                                    discoDisplay()
                                else:
                                    print("\n__Officer Rhys______________________________________\n")
                                    print("        'Away Team safely back aboard sir!'             ")
                                    print("____________________________________________________\n")
                                    print("      Beam Across | Secure Ship | Beam Back")
                                    print("----------|o|-----------|o|----------|o|\n")
                                    disco.crewNo -= int(result[1])
                                    print(disco.crewNo)
                                    str(input("\n-press ENTER to continue-"))
                                    discoDisplay()

def boardCombat(party,kliCrew):
    compare = party
    compareKli = kliCrew
    while party > 0:
        x = 2
        if random.randint(1,10) > x:
            kliCrew -= 1
        else:
            party -= 1
        if party == 0:
            return "0" + str(compare - party) + str(compareKli - kliCrew)
        elif kliCrew <= 0:
            return "1" + str(compare - party) + str(compareKli - kliCrew)
        else:
            x += 1

def planetInfo():
    target = game.target[0]
    if target.objType == "planet" and target.map == True:
        print("\n", target.name, target.desc)
        if target.pClass == "M":
            print("- Earth-Like\n")
        elif target.pClass == "J":
            print("- Gas Giant\n")
        elif target.pClass == "L":
            print("- Primitive Ecosystem\n")
        print("Biology:",target.inhab)
        print("Mass:",target.mass)
        print("Density:",target.dens)
        print("Diameter:",target.diam)
        print("Deposits:",target.depos)
        print("Atmosphere:",target.atmos)
        print("Turbulence:")
        print("Atmospheric -",target.atmoTurb)
        print("Subspace -",target.subsTurb)
    else:
        game.lastTitle = "Cmdr. Burnham"
        game.lastMsg = "Sensor scans required Captain"
        discoDisplay()

def coordFind():
    target = game.target[0]
    print(target.pX,target.pY)

def legend():
    print("D    - USS Discovery")
    print("e    - Explorer")
    print("f    - Freighter")
    print("r    - Research Vessel")
    print("t    - Transport")
    print("K    - Klingon")
    print("0    - Planet")
    print("B    - Starbase")
    print("S    - Station")

def damage():
    print("Shields:",disco.shieldLvl, "%")
    print("Engines:",disco.engineLvl, "%")
    print("Photon:",disco.photonLvl, "%")
    print("Phaser:",disco.phaserLvl, "%")
    print("Life Support:",disco.lifeLvl, "%")

def intro():
    supCode("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",True,0.5)
    supCode("                          Super Star Trek: REDUX\n\n\n\n\n\n\n\n\n\n\n\n",True,1)
    wait = str(input("- press 'ENTER' to continue -"))
    supCode("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",True,0.3)
    supCode("                      type 'guide' if you get Lost...\n\n\n\n\n\n\n\n\n\n\n\n",True,2)
    print(" Make your Terminal Window roughly this width...\n_____________________________________________________________________________________")
    for i in range(23):
        print("|")
    print(" and roughly this Tall...\n")
    wait = str(input("- press 'ENTER' to begin... -"))

""" Initialisation """

hints = ["Type 'cmd' for a list of Commands","Type 'guide' to read the Guide"]
map = map()
disco = discovery()
game = game()

gridPop(sector[4][4])

intro()
discoDisplay()

cmd_dict = {
    "d"     : discoDisplay,
    "s"     : objDisplay,
    "delta" : deltaScan,
    "zeta"  : zetaScan,
    "theta" : thetaScan,
    "tau"   : tauScan,
    "sigma" : sigScan,
    "sweep" : sensorSweep,
    "data"  : shipImage,
    "cc"    : crCgoScan,
    "lrs"   : lrsDisplay,
    "board" : boardKli,
    "planet": planetInfo,
    "m"     : mainScreen,
    "l"     : tacticalContactScreen,
    "n"     : dataScreen,
    "k"     : listScreen,
    "dock"  : dock,
    "target": target,
    "tar"   : target,
    "t"     : target,
    "trade" : trade,
    "where" : coordFind,
    "orbit" : orbit,
    "hold"  : inventory,
    "land"  : away,
    "return": returnTeam,
    "cmd"   : cmdList,
    "ext"   : extract,
    "type"  : planetType,
    "hail"  : hailTo,
    "range" : rangeFinderOne,
    "sal"   : boardCiv,
    "pho"   : photonTarget,
    "pha"   : phaserTarget,
    "kliC"  : klingonCount,
    "legend": legend,
    "def"   : enemyPha,
    "damage": damage,
    "guide" : guide,
    }

screenDict = {
    "main"  : tacticalContactScreen,
    "tac"   : mainScreen,
    "data"  : listScreen,
    "list"  : mainScreen
    }

currentScreenDict = {
    "main"  : mainScreen,
    "tac"   : tacticalContactScreen,
    "data"  : dataScreen,
    "list"  : listScreen,
    "obj"   : objDisplay,
    "disco" : discoDisplay,
    "lrs"   : lrsDisplay
    }


""" Main Game Loop """

while True:

    try:

        cmd = str(input("\n> "))
        cmdCheck = cmd.split()
        print("")
        if cmd == "quit":
            break
        elif cmd == "":
          if game.currentScreen == "main" or game.currentScreen == "tac" or game.currentScreen == "data" or game.currentScreen == "list":
              screenDict[game.currentScreen]()
        elif cmd == "pha" and len(cmdCheck) < 2:
            phaserTarget()
        elif cmd == "pho" and len(cmdCheck) < 2:
            photonTarget()
        elif cmdCheck[0] == "pha" and len(cmdCheck) > 1:
            if len(cmdCheck) == 7 or len(cmdCheck) == 4:
                if len(cmdCheck) == 7:
                    t1 = cmdCheck[1] + cmdCheck[2]
                    t2 = cmdCheck[3] + cmdCheck[4]
                    t3 = cmdCheck[5] + cmdCheck[6]
                    game.atkLog = []
                    for obj in game.kliCount:
                        if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                            game.atkQueue.append(obj)
                        if obj.pX == int(t2[0]) - 1 and obj.pY == int(t2[1]):
                            game.atkQueue.append(obj)
                        if obj.pX == int(t3[0]) - 1 and obj.pY == int(t3[1]):
                            game.atkQueue.append(obj)
                    for elem in game.atkQueue:
                        game.target = []
                        game.target.append(elem)
                        phaser()
                    game.atkQueue = []
                    game.lastTitle = "Lt. Owosekun"
                    game.lastMsg = "Direct Hits!"
                    for i in game.atkLog:
                        print(i)
                elif len(cmdCheck) == 4:
                    t1 = cmdCheck[1][0] + cmdCheck[1][1]
                    t2 = cmdCheck[2][0] + cmdCheck[2][1]
                    t3 = cmdCheck[3][0] + cmdCheck[3][1]
                    game.atkLog = []
                    for obj in game.kliCount:
                        if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                            game.atkQueue.append(obj)
                        if obj.pX == int(t2[0]) - 1 and obj.pY == int(t2[1]):
                            game.atkQueue.append(obj)
                        if obj.pX == int(t3[0]) - 1 and obj.pY == int(t3[1]):
                            game.atkQueue.append(obj)
                    for elem in game.atkQueue:
                        game.target = []
                        game.target.append(elem)
                        phaser()
                    game.atkQueue = []
                    game.lastTitle = "Lt. Owosekun"
                    game.lastMsg = "Direct Hits!"
                    for i in game.atkLog:
                        print(i)
            elif len(cmdCheck) == 5:
                t1 = cmdCheck[1] + cmdCheck[2]
                t2 = cmdCheck[3] + cmdCheck[4]
                for obj in game.kliCount:
                    if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                        game.atkQueue.append(obj)
                    if obj.pX == int(t2[0]) - 1 and obj.pY == int(t2[1]):
                        game.atkQueue.append(obj)
                for elem in game.atkQueue:
                    game.target = []
                    game.target.append(elem)
                    phaser()
                game.atkQueue = []
                game.lastTitle = "Lt. Owosekun"
                game.lastMsg = "Direct Hits!"
                for i in game.atkLog:
                    print(i)
            elif len(cmdCheck) == 2:
                for obj in game.kliCount:
                    t1 = cmdCheck[1]
                    game.atkLog = []
                    if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                        game.target = []
                        game.target.append(obj)
                        phaser()
                        game.lastTitle = "Lt. Owosekun"
                        game.lastMsg = "Direct Hit!"
                        for i in game.atkLog:
                            print(i)
                        tacticalContactScreen()
            elif len(cmdCheck) == 3:
                if len(cmdCheck[1]) == 1:
                    for obj in game.kliCount:
                        t1 = cmdCheck[1] + cmdCheck[2]
                        game.atkLog = []
                        if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                            game.target = []
                            game.target.append(obj)
                            phaser()
                            game.lastTitle = "Lt. Owosekun"
                            game.lastMsg = "Direct Hit!"
                            for i in game.atkLog:
                                print(i)
                            tacticalContactScreen()
                else:
                    t1 = cmdCheck[1][0] + cmdCheck[1][1]
                    t2 = cmdCheck[2][0] + cmdCheck[2][1]
                    game.atkLog = []
                    for obj in game.kliCount:
                        if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                            game.atkQueue.append(obj)
                        if obj.pX == int(t2[0]) - 1 and obj.pY == int(t2[1]):
                            game.atkQueue.append(obj)
                    for elem in game.atkQueue:
                        game.target = []
                        game.target.append(elem)
                        phaser()
                    game.atkQueue = []
                    game.lastTitle = "Lt. Owosekun"
                    game.lastMsg = "Direct Hits!"
                    for i in game.atkLog:
                        print(i)
        elif cmdCheck[0] == "pho" and len(cmdCheck) > 1:
            if len(cmdCheck) == 7 or len(cmdCheck) == 4:
                if len(cmdCheck) == 7:
                    t1 = cmdCheck[1] + cmdCheck[2]
                    t2 = cmdCheck[3] + cmdCheck[4]
                    t3 = cmdCheck[5] + cmdCheck[6]
                    for obj in game.kliCount:
                        if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                            game.atkQueue.append(obj)
                        if obj.pX == int(t2[0]) - 1 and obj.pY == int(t2[1]):
                            game.atkQueue.append(obj)
                        if obj.pX == int(t3[0]) - 1 and obj.pY == int(t3[1]):
                            game.atkQueue.append(obj)
                    for elem in game.atkQueue:
                        game.target = []
                        game.target.append(elem)
                        photon()
                    game.atkQueue = []
                    game.lastTitle = "Lt. Owosekun"
                    game.lastMsg = "Direct Hits!"
                elif len(cmdCheck) == 4:
                    t1 = cmdCheck[1][0] + cmdCheck[1][1]
                    t2 = cmdCheck[2][0] + cmdCheck[2][1]
                    t3 = cmdCheck[3][0] + cmdCheck[3][1]
                    for obj in game.kliCount:
                        if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                            game.atkQueue.append(obj)
                        if obj.pX == int(t2[0]) - 1 and obj.pY == int(t2[1]):
                            game.atkQueue.append(obj)
                        if obj.pX == int(t3[0]) - 1 and obj.pY == int(t3[1]):
                            game.atkQueue.append(obj)
                    for elem in game.atkQueue:
                        game.target = []
                        game.target.append(elem)
                        photon()
                    game.atkQueue = []
                    game.lastTitle = "Lt. Owosekun"
                    game.lastMsg = "Direct Hits!"
            elif len(cmdCheck) == 5:
                t1 = cmdCheck[1] + cmdCheck[2]
                t2 = cmdCheck[3] + cmdCheck[4]
                for obj in game.kliCount:
                    if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                        game.atkQueue.append(obj)
                    if obj.pX == int(t2[0]) - 1 and obj.pY == int(t2[1]):
                        game.atkQueue.append(obj)
                for elem in game.atkQueue:
                    game.target = []
                    game.target.append(elem)
                    photon()
                game.atkQueue = []
                game.lastTitle = "Lt. Owosekun"
                game.lastMsg = "Direct Hits!"
            elif len(cmdCheck) == 2:
                for obj in game.kliCount:
                    t1 = cmdCheck[1]
                    if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                        game.target = []
                        game.target.append(obj)
                        photon()
                        game.lastTitle = "Lt. Owosekun"
                        game.lastMsg = "Direct Hit!"
                        tacticalContactScreen()
            elif len(cmdCheck) == 3:
                if len(cmdCheck[1]) == 1:
                    for obj in game.kliCount:
                        t1 = cmdCheck[1] + cmdCheck[2]
                        if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                            game.target = []
                            game.target.append(obj)
                            photon()
                            game.lastTitle = "Lt. Owosekun"
                            game.lastMsg = "Direct Hit!"
                            tacticalContactScreen()
                else:
                    t1 = cmdCheck[1][0] + cmdCheck[1][1]
                    t2 = cmdCheck[2][0] + cmdCheck[2][1]
                    for obj in game.kliCount:
                        if obj.pX == int(t1[0]) - 1 and obj.pY == int(t1[1]):
                            game.atkQueue.append(obj)
                        if obj.pX == int(t2[0]) - 1 and obj.pY == int(t2[1]):
                            game.atkQueue.append(obj)
                    for elem in game.atkQueue:
                        game.target = []
                        game.target.append(elem)
                        photon()
                    game.atkQueue = []
                    game.lastTitle = "Lt. Owosekun"
                    game.lastMsg = "Direct Hits!"

        elif cmdCheck[0] == "sh" or cmdCheck[0] == "shields":
            if cmdCheck[1] == "up" or cmdCheck[1] == "u":
                shields("+")
            elif cmdCheck[1] == "down" or cmdCheck[1] == "d":
                shields("-")
        elif len(cmdCheck) == 3 and cmdCheck[0] == "mv":
            disco.moveAuto(cmdCheck[1],cmdCheck[2])
        elif len(cmdCheck) == 3 and cmdCheck[0] == "mm":
            disco.moveManual(cmdCheck[1],cmdCheck[2])
        elif len(cmdCheck) == 3 and cmdCheck[0] == "warp":
            disco.moveZone(cmdCheck[1],cmdCheck[2])
        elif len(cmdCheck) == 3 and cmdCheck[0] == "phad":
            phaser_debug(int(cmdCheck[1]),int(cmdCheck[2]))
        elif len(cmdCheck) == 2:
            num = int(cmdCheck[1])
            cmd_dict[cmdCheck[0]](game.objCount[num - 1])
        else:
            cmd_dict[cmd]()

    except:
        print(random.choice(hints))
