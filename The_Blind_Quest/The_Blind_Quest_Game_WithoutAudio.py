# game by Dynomite
# please forgive my spelling. actually don't, it's a feature ;)

### Imports ###
import sys, pickle, os, time, random                # 1) used to print text slowly, 2) save and load the game(funnyest thing i've ever read), 3) clear the screen, stop code for a breef time, 4) the clue is in the name                                   
os.system("mode con cols=148 lines=45")             # window size for the "game"
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"   # to hide the annoying message that pops up

ZONENAME = 'name of zone'
DESCRIPTION = 'description of zone'
EXAMINATION = 'examination of zone'
UP = 'up', 'north' # up up and away web
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
HAS = 'boss or puzzle?'

### Player ### # you 
class player:
    def __init__(self):
    ### Bacic stats ###
        self.name = ''
        self.location = 'a1'
        self.job = ''
        self.ability = ''
        self.level = 1
        self.exp = 0
        self.maxexp = 10
        self.maxhp = 34
        self.p = 14
        # self.status_efects = []       # not yet used? actualy im too lazy
    ### Inventory ###
        self.pots = 2
        self.tel = 1
        self.gold = 30
        self.inv = ['Rusty Sword']
        self.curweap = 'Rusty Sword'
        self.ih_price = 50
    ### counters ###
        self.bosses_won = 0
        self.enemy_times_won = 0
        self.counter = 0
        self.i_count = 0
        self.z_count = 0
        self.f_count = 0
        self.f2_count = 0
        self.e_death_counter = 0
        self.quest_counter = 0
        self.times_entered_a8 = False
        self.quest_selected = False
        self.boss1_defeated = False
        self.boss2_defeated = False
        self.boss3_defeated = False
        self.boss4_defeated = False
        self.boss5_defeated = False
        self.boss6_defeated = False
        self.boss8_defeated = False
        self.boss9_defeated = False
        self.boss10_defeated = False
        self.lancer = False
        self.funny_counter = 0
    ### Puzzles ###
        self.solved_places = {'a3': False, 'a4': False, 'a5': False, 'a6': False, 'a7': False,
            'b2': False, 'b4': False, 'b5': False, 'b6': False, 'b7': False, 'b8': False,
            'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c6': False, 'c7': False, 'c8': False,
            'd1': False, 'd2': False, 'd3': False, 'd5': False, 'd6': False, 'd7': False, 'd8': False,
            'e2': False, 'e3': False, 'e4': False, 'e5': False, 'e6': False, 'e7': False, 'e8': False,
            'f1': False, 'f2': False, 'f3': False, 'f4': False, 'f5': False, 'f6': False, 'f8': False,
            'g1': False, 'g2': False, 'g3': False, 'g4': False, 'g5': False, 'g6': False}
    ### Encountering enemys ###
        self.en1_counter = False
        self.en2_counter = False
        self.en3_counter = False
        self.en4_counter = False
        self.en5_counter = False
        self.en6_counter = False
        self.en7_counter = False
        self.en8_counter = False
        self.en9_counter = False
        self.en10_counter = False
        self.e_save = 0
    ### Weapons ###
        self.star_count = False
        self.bacon_count = False
        self.hip_count = False
        self.raspberry_count = False
    ### For tests ###                # Dont cheat !!! >:(
        # self.location = ':)'
        # self.p = 1000
        # self.maxhp = 8000
        # self.tel = 1
        # self.pots = 100
        # self.e_death_counter = 1
        # self.bosses_won = 7
    ### Max health ###
        self.hp = self.maxhp
    ### Store stats ###
        self.store_p = self.p
        self.store_maxhp = self.maxhp
        self.store_hp = self.hp
        self.store_pots = self.pots
        self.store_exp = self.exp
        self.store_maxexp = self.maxexp
        self.store_gold = self.gold
        self.store_ability = self.ability

### Enemys ###
# "Goblin"/"Gnoblin" # loves money
class enemy1():
    def __init__(self):
        self.group = 'Normal'
        self.name = 'Goblin'
        self.name2 = 'Gnoblin'
        self.to_print = 'crawl\'s out of a vent ;-)'
        self.to_print2 = 'is laughing at you (¬‿¬)'
        self.to_print3 = 'puts away his richest items (._.`)'
        self.act_option1 = 'Give'
        self.act_option2 = 'Vent'
        self.act_option3 = 'Imatate'
        self.dialog_1 = 'tehehe'
        self.dialog_2 = 'GOLD?!!'
        self.dialog_3 = 'do not enter my vent. or else you will have to hear a vent pun'
        self.dialog_4 = 'this is already quite eventfull'
        self.dialog_5 = 'There will be many puns in this crawl space'
        # self.status_efects = []       # not yet used? actualy im too lazy
        self.times_won = 0
        self.level = 1
        self.maxhp = 50
        self.hp = self.maxhp
        self.p = 10
        self.gold = 6
        self.exp = 8
# "Zombie"/"Big guy" # loves brains
class enemy2():
    def __init__(self):
        self.group = 'Normal'
        self.name = 'Zombie'
        self.name2 = 'Big guy'
        self.to_print = 'is looking at you thinking you\'re food (⊙_⊙;)'
        self.to_print2 = 'limps to eat youre brains (❁\'◡`❁)'
        self.to_print3 = 'wants to eat you (⊙_⊙;)'
        self.act_option1 = 'Pretend'
        self.act_option2 = 'Dance'
        self.act_option3 = 'Talk'
        self.dialog_1 = '...'
        self.dialog_2 = '...'
        self.dialog_3 = '...'
        self.dialog_4 = '...'
        self.dialog_5 = '...'
        # self.status_efects = []       # not yet used? actualy im too lazy
        self.times_won = 0
        self.level = 1
        self.maxhp = 44
        self.hp = self.maxhp
        self.p = 16
        self.gold = 16
        self.exp = 25
# "Frogo"/"Frogerion" # knows not a whole lot / knows almost all
class enemy3():
    def __init__(self):
        self.group = 'Normal'
        self.name = 'Frogo'
        self.name2 = 'Frogerion'
        self.to_print = 'is looking at you, waiting for wisdom (●\'◡\'●)'
        self.to_print2 = 'hop\'s into battle ☜(ﾟヮﾟ☜)'
        self.to_print3 = 'questions the reality of the world (ˉ﹃ˉ)'
        self.act_option1 = 'Truth'
        self.act_option2 = 'Lies'
        self.act_option3 = 'Pretend'
        self.dialog_1 = '*Ribit* *Ribit*'
        self.dialog_2 = '*Ribit teach me'
        self.dialog_3 = 'Ribit teach me the ways'
        self.dialog_4 = 'Ribit why are you here? who are you'
        self.dialog_5 = 'hmm'
        # self.status_efects = []       # not yet used? actualy im too lazy
        self.times_won = 0
        self.level = 1
        self.maxhp = 50
        self.hp = self.maxhp
        self.p = 22
        self.gold = 32
        self.exp = 10
# "Iseecle"/"Iseecle master" # wants you to look at him
class enemy4():
    def __init__(self):
        self.group = 'Normal'
        self.name = 'Iseecle'
        self.name2 = 'Iseecle master'
        self.to_print = 'is it just me or is it hot in here ☜(ﾟヮﾟ☜)'
        self.to_print2 = 'can\'t see coal (┬┬~┬┬)'
        self.to_print3 = 'is way to cool for this battle ☜(ﾟヮﾟ☜)'
        self.act_option1 = 'Complement'
        self.act_option2 = 'Stare'
        self.act_option3 = 'Ignore'
        self.dialog_1 = 'look at my hat!'
        self.dialog_2 = 'my hat is very shiny.'
        self.dialog_3 = 'everyone loves my hat'
        self.dialog_4 = 'im sure you havent seen my hat yet'
        self.dialog_5 = 'have i mentiond to you how much i love my hat'
        # self.status_efects = []       # not yet used? actualy im too lazy
        self.times_won = 0
        self.level = 1
        self.maxhp = 82
        self.hp = self.maxhp
        self.p = 31
        self.gold = 50
        self.exp = 10
# "Funguy"/"Funnyguy" # yeah there is not much to say about this one
class enemy5():
    def __init__(self):
        self.group = 'Normal'
        self.name = 'Funguy'
        self.name2 = 'Funnyguy'
        self.to_print = 'said a funny joke (¬_¬ )'
        self.to_print2 = 'is not a mushroom? ༼  ◕_◕ ༽'
        self.to_print3 = 'is dresed in a funny costume ╰(*°▽°*)╯'
        self.act_option1 = 'Make Fun'
        self.act_option2 = 'Laugh'
        self.act_option3 = 'Joke'
        self.dialog_1 = 'Im so thrilled. ill have to post this to reddit and get lots of upvotes'
        self.dialog_2 = 'maybe a gamer girl will message me?'
        self.dialog_3 = 'i sure love gaming. im a level 87 gnome on "Star Shreader for the Gamerboy1000 premium edition"'
        self.dialog_4 = 'Epic Funny haha.'
        self.dialog_5 = '*insert unfunny joke*'
        # self.status_efects = []       # not yet used? actualy im too lazy
        self.times_won = 0
        self.level = 1
        self.maxhp = 148
        self.hp = self.maxhp
        self.p = 37
        self.gold = 78
        self.exp = 10

### Bosses ###
# "a2" - "Mr Groove"
class boss1():
    def __init__(self):
        self.group = 'Boss'
        self.name = 'Mr Groove'
        self.to_print = 'puts on battle music'
        self.to_print2 = 'is ready to for the dance battle'
        self.to_print3 = 'starts prepearing, by doing awsome moves'
        self.act_option1 = 'Attempt Dance'
        self.act_option2 = 'Dance epicly'
        self.act_option3 = 'Dance???'
        self.dialog_1 = 'Dance, Dance every one!!'
        self.dialog_2 = 'We rebels, Not playas. Actualy no, im a cd player'
        self.dialog_3 = 'I wont ler anyone lay a finger on madmozels here'
        self.dialog_4 = 'Feel the beat!!'
        self.dialog_5 = 'Watch my moves!!'
        self.times_won = 0
        self.level = 1
        self.maxhp = 450
        self.hp = self.maxhp
        self.p = 30
        self.gold = 200
        self.exp = 200
# "b3" - "Maestro"
class boss2():
    def __init__(self):
        self.group = 'Boss'
        self.name = 'Maestro'
        self.to_print = 'lifts his hand, the music gets louder'
        self.to_print2 = 'smiles, you sence that he knows somthing you dont'
        self.to_print3 = 'bruches his hair, you stat feel somthing. terrable'
        self.act_option1 = 'Dance'
        self.act_option2 = 'Listen'
        self.act_option3 = 'Practice'
        self.dialog_1 = 'mwohaha. you are truly no match for me'
        self.dialog_2 = 'lets see how you fight'
        self.dialog_3 = 'im the best musition here.'
        self.dialog_4 = '...'
        self.dialog_5 = '...'
        self.times_won = 0
        self.level = 28
        self.maxhp = 750
        self.hp = self.maxhp
        self.p = 50
        self.gold = 200
        self.exp = 1000
# "c5" - "eremthgin"
class boss3():
    def __init__(self):
        self.group = 'Boss'
        self.name = 'eremthgin'
        self.to_print = 'is here, you start to remember you\'re past'
        self.to_print2 = 'is there, you start to feel terrified for you\'re live'
        self.to_print3 = 'starts dancing, the world starts to revolve'
        self.act_option1 = '???'
        self.act_option2 = '???'
        self.act_option3 = '???'
        self.dialog_1 = 'METAMORPHISIS'
        self.dialog_2 = 'I CAN DO ANY THING!!!'
        self.dialog_3 = 'CHAOS, CHAOS!'
        self.dialog_4 = 'IT\'S ALL TOO MUCH FUN!!!'
        self.dialog_5 = 'THIS BODY CANNOT BE KILLED!'
        self.times_won = 0
        self.level = 28
        self.maxhp = 950
        self.hp = self.maxhp
        self.p = 60
        self.gold = 320
        self.exp = 2846
# "d4" - "Q36u43e25e46n"
class boss4():
    def __init__(self):
        self.group = 'Boss'
        self.name = 'Q36u43e25e46n'
        self.to_print = 'laughs like a robot.'
        self.to_print2 = 'takes a sip of acid to charge her atack'
        self.to_print3 = 'leaves an online match on her phone to fight you'
        self.act_option1 = 'Toast'
        self.act_option2 = 'Talk'
        self.act_option3 = 'Advice'
        self.dialog_1 = 'Hohoho.\n    After im done with you, I\'ll make sure my doughter is prepearing for her national maths competition\n    and make her study for Chemistry, Astronomy, Neuroscience, Law...'
        self.dialog_2 = 'Cheers'
        self.dialog_3 = 'Im such a great parent. i desurve all the awards. because i am the best'
        self.dialog_4 = 'Lets see how your "fight.exe" works'
        self.dialog_5 = 'Am i a terrable mother? Dont answer that LMAO. I know im the best'
        self.times_won = 0
        self.level = 28
        self.maxhp = 1020
        self.hp = self.maxhp
        self.p = 180
        self.gold = 200
        self.exp = 4050
# "e1" - "Big $1im3"
class boss5():
    def __init__(self):
        self.group = 'Boss'
        self.name = 'Big $1im3'
        self.to_print = 'yuck'
        self.to_print2 = 'wants to make a funny pun. but he cant speak'
        self.to_print3 = 'you wander what it taste\'s like, for some reason'
        self.act_option1 = '...'
        self.act_option2 = '...'
        self.act_option3 = '...'
        self.dialog_1 = '...'
        self.dialog_2 = '...'
        self.dialog_3 = '...'
        self.dialog_4 = '...'
        self.dialog_5 = '...'
        self.times_won = 0
        self.level = 28
        self.maxhp = 3130
        self.hp = self.maxhp
        self.p = 250
        self.gold = 200
        self.exp = 5560
# "f7" - "Bark Soul"
class boss6():
    def __init__(self):
        self.group = 'Boss'
        self.name = 'Bark Soul'
        self.to_print = 'is rolling on the ground'
        self.to_print2 = 'wants to play'
        self.to_print3 = 'jumps with joy'
        self.act_option1 = 'Pet'        # Tummy rubs are forbidden.
        self.act_option2 = 'Play'
        self.act_option3 = 'Beckon'
        self.dialog_1 = 'Bark!'
        self.dialog_2 = 'Woof!'
        self.dialog_3 = 'Bark Bark!'
        self.dialog_4 = 'Woof Woof!'
        self.dialog_5 = 'Bark?'
        self.times_won = 0
        self.level = 28
        self.maxhp = 1400
        self.hp = self.maxhp
        self.p = 2
        self.gold = 200
        self.exp = 10000
# ":)" - him???
class boss7():
    def __init__(self):
        self.group = 'Boss'
        self.name = 'Dynomite'
        self.to_print = 'stands there, ready to end it once and for all'
        self.to_print2 = '... the end to your journey'
        self.to_print3 = '... :) i am the end'
        self.times_won = 0
        self.level = 28
        self.maxhp = 10000
        self.hp = self.maxhp
        self.p = 30
        self.gold = 0
        self.exp = 0
# "a1" - "Muffet"
class boss8():
    def __init__(self):
        self.group = 'Boss'
        self.name = 'Muffet'
        self.to_print = 'Laughs as she sees you strugle with emotions'
        self.to_print2 = 'getting ready to bake a cake out of you'
        self.to_print3 = 'wants to feed you to her pet'
        self.times_won = 0
        self.level = 28
        self.maxhp = 5000
        self.hp = self.maxhp
        self.p = 300
        self.gold = 600
        self.exp = 400
# "a1" - "Mettaton"
class boss9():
    def __init__(self):
        self.group = 'Boss'
        self.name = 'Mettaton'
        self.to_print = 'starts the show'
        self.to_print2 = 'the audience cheered'
        self.to_print3 = 'but there is no audience'
        self.times_won = 0
        self.level = 28
        self.maxhp = 7000
        self.hp = self.maxhp
        self.p = 450
        self.gold = 1000
        self.exp = 600
# "g7" - "Lancer"
class boss10():
    def __init__(self):
        self.group = 'Boss'
        self.name = 'Lancer'
        self.to_print = 'stands in your way'
        self.to_print2 = '...'
        self.to_print3 = '...'
        self.act_option1 = 'Say hi'
        self.act_option2 = 'Say HI'
        self.act_option3 = 'Spare'
        self.dialog_1 = 'HOHOHO'
        self.dialog_2 = 'MY DAD IS GONA MAKE ME SON OF THE MONTH'
        self.dialog_3 = 'I\'M...! THE BAD GUY'
        self.dialog_4 = 'I LOVE TO GET THRASHED...JUST KIDDING! THAT\'S YOU!!'
        self.dialog_5 = 'Did you not realize I can mask my self-esteem levels?'
        self.times_won = 0
        self.level = 1
        self.maxhp = 1
        self.hp = self.maxhp
        self.p = 0
        self.gold = 1
        self.exp = 1

### quests types ###
# Kill one Goblin
class quest1():
    def __init__(self):
        self.selected = False
        self.name = 'The Begining'
        self.discription = 'Kill one Goblin'
        self.item = 100
        self.reward_type = 'Gold'
# Kill one Frogo
class quest2():
    def __init__(self):
        self.selected = False
        self.name = 'The Sequal'
        self.discription = 'Kill one Frogo'
        self.item = 150
        self.reward_type = 'Gold'
# Kill two Iseecle's
class quest3():
    def __init__(self):
        self.selected = False
        self.name = 'Epic Quest'
        self.discription = 'Kill two Iseecle\'s'
        self.item = 200
        self.reward_type = 'Gold'
# Kill two Funguy's
class quest4():
    def __init__(self):
        self.selected = False
        self.name = 'The Equaly Epic Quest'
        self.discription = 'Kill two Funguys\'s'
        self.item = 250
        self.reward_type = 'Gold'
# kill eight Zombie's
class quest5():
    def __init__(self):
        self.selected = False
        self.name = 'The Dedication'
        self.discription = 'Kill Eight Zombie\'s'
        self.item = 300
        self.reward_type = 'Gold'
# kill four Frogerion's
class quest6():
    def __init__(self):
        self.selected = False
        self.name = 'The Quest For Knowlege'
        self.discription = 'Kill Four Frogerion\'s'
        self.item = 350
        self.reward_type = 'Gold'
# kill one Funnyguy
class quest7():
    def __init__(self):
        self.selected = False
        self.name = 'The Serial Killer'
        self.discription = 'Kill One Funnyguy'
        self.item = 'SerialKnife'
        self.reward_type = 'Item'

### Map locations ###
map_locations = {
    'a1': {
        ZONENAME: "Home",
        DESCRIPTION: 'This is youre home',
        EXAMINATION: 'Your home, it\'s garbage. you can rest here. for no reason what so ever',
        UP: 'b1',
        DOWN: '',
        LEFT: '',
        RIGHT: 'a2',
        HAS: ''},
    'a2': {
        ZONENAME: "Town 1 (West Side) South",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can fine a ton of goodies, goblins and zombies here, fun.\n',
        UP: 'b2',
        DOWN: '',
        LEFT: 'a1',
        RIGHT: 'a3',
        HAS: 'Boss'},
    'a3': {
        ZONENAME: "Town 1 (East Side) South",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can fine a ton of goodies and mostly zombies here, fun. also a puzzle exists here',
        UP: 'b3',
        DOWN: '',
        LEFT: 'a2',
        RIGHT: 'a4',
        HAS: ''},
    'a4': {
        ZONENAME: "Border 1 (West side) South",
        DESCRIPTION: 'Border Between the forest and the town',
        EXAMINATION: 'You can find mostly zombies here',
        UP: 'b4',
        DOWN: '',
        LEFT: 'a3',
        RIGHT: 'a5',
        HAS: ''},
    'a5': {
        ZONENAME: "Forest 1 (West) South",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'You can find a "Frogo\'s" in this area',
        UP: 'b5',
        DOWN: '',
        LEFT: 'a4',
        RIGHT: 'a6',
        HAS: ''},
    'a6': {
        ZONENAME: "Forest and Ice 1 (West) South",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogo\'s" in this area',
        UP: 'b6',
        DOWN: '',
        LEFT: 'a5',
        RIGHT: 'a7',
        HAS: ''},
    'a7': {
        ZONENAME: "Mushroom Plains 1",
        DESCRIPTION: 'A mushroom plains filled with mushrooms',
        EXAMINATION: 'Not sure what you expected. You can find "FunGuy" here',
        UP: "b7",
        DOWN: '',
        LEFT: 'a6',
        RIGHT: 'a8',
        HAS: ''},
    'a8': {
        ZONENAME: "The Castel",
        DESCRIPTION: 'there sould not be any enemys here',
        EXAMINATION: 'the king lives here',
        UP: "b8",
        DOWN: '',
        LEFT: 'a7',
        RIGHT: '',
        HAS: ''},
    'b1': {
        ZONENAME: "Shop",
        DESCRIPTION: 'There wont be any enemys here',
        EXAMINATION: 'A lone building stands here with a sign saying:\n "Buy My Stuff"',
        UP: "c1",
        DOWN: 'a1',
        LEFT: '',
        RIGHT: 'b2',
        HAS: ''},
    'b2': {
        ZONENAME: "Town 2 (West Side) South",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can fine a ton of goodies, goblin\'s and zombie\'s here, fun.\n',
        UP: "c2",
        DOWN: 'a2',
        LEFT: 'b1',
        RIGHT: 'b3',
        HAS: ''},
    'b3': {
        ZONENAME: "Town 3 (East Side) South",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can fine a ton of goodies and mostly zombies here, fun. also a puzzle exists here',
        UP: "c3",
        DOWN: 'a3',
        LEFT: 'b2',
        RIGHT: 'b4',
        HAS: 'Boss'},
    'b4': {
        ZONENAME: "Border 2 (West side) South",
        DESCRIPTION: 'Border Between the forest and the town',
        EXAMINATION: 'You can find mostly zombies here',
        UP: "c4",
        DOWN: 'a4',
        LEFT: 'b3',
        RIGHT: 'b5',
        HAS: ''},
    'b5': {
        ZONENAME: "Forest 2 (West) South",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogo\'s" in this area',
        UP: "c5",
        DOWN: 'a5',
        LEFT: 'b4',
        RIGHT: 'b6',
        HAS: ''},
    'b6': {
        ZONENAME: "Forest and Ice 2 (West) South",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogo\'s" in this area',
        UP: "c6",
        DOWN: 'a6',
        LEFT: 'b5',
        RIGHT: 'b7',
        HAS: ''},
    'b7': {
        ZONENAME: "Mushroom Plains 2 with Ice (Wast)",
        DESCRIPTION: 'mushroom plains filled with mushrooms',
        EXAMINATION: 'not sure what you expected. you can find "FunGuy" here',
        UP: "c7",
        DOWN: 'a7',
        LEFT: 'b6',
        RIGHT: 'b8',
        HAS: ''},
    'b8': {
        ZONENAME: "Mushroom Plains 2 (East) South",
        DESCRIPTION: 'mushroom plains filled with mushrooms',
        EXAMINATION: 'not sure what you expected. you can find "FunGuy" here',
        UP: "c8",
        DOWN: 'a8',
        LEFT: 'b7',
        RIGHT: '',
        HAS: ''},
    'c1': {
        ZONENAME: "The Goblin Outpost 3",
        DESCRIPTION: 'An impresive goblin structure',
        EXAMINATION: 'Only "Goblin\'s" can be found here',
        UP: "d1",
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'c2',
        HAS: ''},
    'c2': {
        ZONENAME: "Town 3 (West Side) South",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can fine a ton of goodies, goblin\'s and zombie\'s here, fun.\n',
        UP: "d2",
        DOWN: 'b2',
        LEFT: 'c1',
        RIGHT: 'c3',
        HAS: ''},
    'c3': {
        ZONENAME: "Town 3 (East Side) South",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can fine a ton of goodies and mostly zombies here, fun. also a puzzle exists here',
        UP: "d3",
        DOWN: 'b3',
        LEFT: 'c2',
        RIGHT: 'c4',
        HAS: ''},
    'c4': {
        ZONENAME: "Border 3 (West side) South",
        DESCRIPTION: 'Border Between the forest and the town',
        EXAMINATION: 'You can find mostly zombies here',
        UP: "d4",
        DOWN: 'b4',
        LEFT: 'c3',
        RIGHT: 'c5',
        HAS: ''},
    'c5': {
        ZONENAME: "Forest 3 (West) South",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogo\'s" in this area',
        UP: "d5",
        DOWN: 'b5',
        LEFT: 'c4',
        RIGHT: 'c6',
        HAS: 'Boss'},
    'c6': {
        ZONENAME: "Forest and Ice 3 (West) South",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogo\'s" in this area',
        UP: "d6",
        DOWN: 'b6',
        LEFT: 'c5',
        RIGHT: 'c7',
        HAS: ''},
    'c7': {
        ZONENAME: "Mushroom Plains 3 with Ice (Wast)",
        DESCRIPTION: 'mushroom plains filled with mushrooms',
        EXAMINATION: 'not sure what you expected. you can find "FunGuy" here',
        UP: "d7",
        DOWN: 'b7',
        LEFT: 'c6',
        RIGHT: 'c8',
        HAS: ''},
    'c8': {
        ZONENAME: "Mushroom Plains 3 (East) South",
        DESCRIPTION: 'mushroom plains filled with mushrooms',
        EXAMINATION: 'not sure what you expected. you can find "FunGuy" here',
        UP: "d8",
        DOWN: 'b8',
        LEFT: 'c7',
        RIGHT: '',
        HAS: ''},
    'd1': {
        ZONENAME: "The Gnoblin Outpost 4",
        DESCRIPTION: 'An impresive Gnoblin structure',
        EXAMINATION: 'Only "Gnoblin\'s" can be found here',
        UP: "e1",
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'd2',
        HAS: ''},
    'd2': {
        ZONENAME: "Town 4 (West Side) North",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can find a ton of goodies, gonoblin\'s and big guy\'s here, fun.\n',
        UP: "e2",
        DOWN: 'c2',
        LEFT: 'd1',
        RIGHT: 'd3',
        HAS: ''},
    'd3': {
        ZONENAME: "Town 4 (East Side) South",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can fine a ton of goodies and mostly zombies here, fun. also a puzzle exists here',
        UP: "e3",
        DOWN: 'c3',
        LEFT: 'd2',
        RIGHT: 'd4',
        HAS: ''},
    'd4': {
        ZONENAME: "Border 4 (West side) North",
        DESCRIPTION: 'Border Between the forest and the town',
        EXAMINATION: 'You can find mostly "Big Guy\'s" here',
        UP: "e4",
        DOWN: 'c4',
        LEFT: 'd3',
        RIGHT: 'd5',
        HAS: 'Boss'},
    'd5': {
        ZONENAME: "Forest 4 (West) North",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogerion\'s" in this area',
        UP: "e5",
        DOWN: 'c5',
        LEFT: 'd4',
        RIGHT: 'd6',
        HAS: ''},
    'd6': {
        ZONENAME: "Forest and Ice 4 (West) South",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogo\'s" in this area',
        UP: "e6",
        DOWN: 'c6',
        LEFT: 'd5',
        RIGHT: 'd7',
        HAS: ''},
    'd7': {
        ZONENAME: "Mushroom Plains 4 with Ice (Wast)",
        DESCRIPTION: 'mushroom plains filled with mushrooms',
        EXAMINATION: 'Not sure what you expected. you can find "Funny Guy" here',
        UP: "e7",
        DOWN: 'c7',
        LEFT: 'd6',
        RIGHT: 'd8',
        HAS: ''},
    'd8': {
        ZONENAME: "Mushroom Plains 4 (East) South",
        DESCRIPTION: 'mushroom plains filled with mushrooms',
        EXAMINATION: 'not sure what you expected. you can find "Funny Guy" here',
        UP: "e8",
        DOWN: 'c8',
        LEFT: 'd7',
        RIGHT: '',
        HAS: ''},
    'e1': {
        ZONENAME: "The Gnoblin Outpost 5",
        DESCRIPTION: 'An impresive Gnoblin structure',
        EXAMINATION: 'Only "Gnoblin\'s" can be found here',
        UP: "f1",
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'e2',
        HAS: 'Boss'},
    'e2': {
        ZONENAME: "Town 5 (West Side) North",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can find a ton of goodies, gonoblin\'s and big guy\'s here, fun.\n',
        UP: "f2",
        DOWN: 'd2',
        LEFT: 'e1',
        RIGHT: 'e3',
        HAS: ''},
    'e3': {
        ZONENAME: "Town 5 (East Side) South",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can fine a ton of goodies and mostly zombies here, fun. also a puzzle exists here',
        UP: "f3",
        DOWN: 'd3',
        LEFT: 'e2',
        RIGHT: 'e4',
        HAS: ''},
    'e4': {
        ZONENAME: "Border 5 (West side) North",
        DESCRIPTION: 'Border Between the forest and the town',
        EXAMINATION: 'You can find mostly "Big Guy\'s" here',
        UP: "f4",
        DOWN: 'd4',
        LEFT: 'e3',
        RIGHT: 'e5',
        HAS: ''},
    'e5': {
        ZONENAME: "Forest 5 (West) North",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogerion\'s" in this area',
        UP: "f5",
        DOWN: 'd5',
        LEFT: 'e4',
        RIGHT: 'e6',
        HAS: ''},
    'e6': {
        ZONENAME: "Forest and Ice 5 (West) South",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogo\'s" in this area',
        UP: "f6",
        DOWN: 'd6',
        LEFT: 'e5',
        RIGHT: 'e7',
        HAS: ''},
    'e7': {
        ZONENAME: "Mushroom Plains 5 with Ice (Wast)",
        DESCRIPTION: 'mushroom plains filled with mushrooms',
        EXAMINATION: 'Not sure what you expected. you can find "Funny Guy" here',
        UP: "f7",
        DOWN: 'd7',
        LEFT: 'e6',
        RIGHT: 'e8',
        HAS: ''},
    'e8': {
        ZONENAME: "Mushroom Plains 5 (East) South",
        DESCRIPTION: 'mushroom plains filled with mushrooms',
        EXAMINATION: 'not sure what you expected. you can find "Funny Guy" here',
        UP: "f8",
        DOWN: 'd8',
        LEFT: 'e7',
        RIGHT: '',
        HAS: ''},
    'f1': {
        ZONENAME: "The Gnoblin Outpost 6",
        DESCRIPTION: 'An impresive Gnoblin structure',
        EXAMINATION: 'Only "Gnoblin\'s" can be found here',
        UP: "g1",
        DOWN: 'e1',
        LEFT: '',
        RIGHT: 'f2',
        HAS: ''},
    'f2': {
        ZONENAME: "Town 6 (West Side) North",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can find a ton of goodies, gonoblin\'s and big guy\'s here, fun.\n',
        UP: "g2",
        DOWN: 'e2',
        LEFT: 'f1',
        RIGHT: 'f3',
        HAS: ''},
    'f3': {
        ZONENAME: "Town 6 (East Side) South",
        DESCRIPTION: 'A collapst town that died years ago',
        EXAMINATION: 'You can fine a ton of goodies and mostly zombies here, fun. also a puzzle exists here',
        UP: "g3",
        DOWN: 'e3',
        LEFT: 'f2',
        RIGHT: 'f4',
        HAS: ''},
    'f4': {
        ZONENAME: "Border 6 (West side) North",
        DESCRIPTION: 'Border Between the forest and the town',
        EXAMINATION: 'You can find mostly "Big Guy\'s" here',
        UP: "g4",
        DOWN: 'e4',
        LEFT: 'f3',
        RIGHT: 'f5',
        HAS: ''},
    'f5': {
        ZONENAME: "Forest 6 (West) North",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogerion\'s" in this area',
        UP: "g5",
        DOWN: 'e5',
        LEFT: 'f4',
        RIGHT: 'f6',
        HAS: ''},
    'f6': {
        ZONENAME: "Forest and Ice 6 (West) South",
        DESCRIPTION: 'An atchent forrest',
        EXAMINATION: 'you can find a "Frogo\'s" in this area',
        UP: "g6",
        DOWN: 'e6',
        LEFT: 'f5',
        RIGHT: 'f7',
        HAS: ''},
    'f7': {
        ZONENAME: "Mushroom Plains 6 with Ice (Wast)",
        DESCRIPTION: 'mushroom plains filled with mushrooms',
        EXAMINATION: 'Not sure what you expected. you can find "Funny Guy" here',
        UP: "g7",
        DOWN: 'e7',
        LEFT: 'f6',
        RIGHT: 'f8',
        HAS: 'Boss'},
    'f8': {
        ZONENAME: "Mushroom Plains 6 (East) South",
        DESCRIPTION: 'mushroom plains filled with mushrooms',
        EXAMINATION: 'not sure what you expected. you can find "Funny Guy" here',
        UP: ":)",
        DOWN: 'e8',
        LEFT: 'f7',
        RIGHT: '',
        HAS: ''},
    'g1': {
        ZONENAME: "???",
        DESCRIPTION: '???',
        EXAMINATION: '???',
        UP: "",
        DOWN: 'f1',
        LEFT: '',
        RIGHT: 'g2',
        HAS: ''},
    'g2': {
        ZONENAME: "???",
        DESCRIPTION: '???',
        EXAMINATION: '???',
        UP: "",
        DOWN: 'f2',
        LEFT: 'g1',
        RIGHT: 'g3',
        HAS: ''},
    'g3': {
        ZONENAME: "???",
        DESCRIPTION: '???',
        EXAMINATION: '???',
        UP: "",
        DOWN: 'f1',
        LEFT: 'g2',
        RIGHT: 'g4',
        HAS: ''},
    'g4': {
        ZONENAME: "???",
        DESCRIPTION: '???',
        EXAMINATION: '???',
        UP: "",
        DOWN: 'f4',
        LEFT: 'g3',
        RIGHT: 'g5',
        HAS: ''},
    'g5': {
        ZONENAME: "???",
        DESCRIPTION: '???',
        EXAMINATION: '???',
        UP: "",
        DOWN: 'f5',
        LEFT: 'g4',
        RIGHT: 'g6',
        HAS: ''},
    'g6': {
        ZONENAME: "???",
        DESCRIPTION: '???',
        EXAMINATION: '???',
        UP: "",
        DOWN: 'f6',
        LEFT: 'g5',
        RIGHT: 'g7',
        HAS: ''},
    'g7': {
        ZONENAME: "???",
        DESCRIPTION: '???',
        EXAMINATION: '???',
        UP: "",
        DOWN: 'f7',
        LEFT: 'g6',
        RIGHT: ':)',
        HAS: 'Boss'},
    ':)': {
        ZONENAME: "END",
        DESCRIPTION: 'the end',
        EXAMINATION: 'a lone gate stand in front of you',
        UP: "",
        DOWN: 'f8',
        LEFT: 'g7',
        RIGHT: '',
        HAS: 'Boss'},}
# for easy printing of the map V
zonenames = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', ':)', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8','b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8']

### Title screen ###
def Title_Screen():
    inmenu = True
    global quest
    global ingame
    while inmenu:
        Clear_Screen()
        print("#" * 148)
        print("                 ████████╗██╗░░██╗███████╗  ██████╗░██╗░░░░░██╗███╗░░██╗██████╗░  ░██████╗░██╗░░░██╗███████╗░██████╗████████╗\n"\
            + "                 ╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██║░░░░░██║████╗░██║██╔══██╗  ██╔═══██╗██║░░░██║██╔════╝██╔════╝╚══██╔══╝\n"\
            + "                 ░░░██║░░░███████║█████╗░░  ██████╦╝██║░░░░░██║██╔██╗██║██║░░██║  ██║██╗██║██║░░░██║█████╗░░╚█████╗░░░░██║░░░\n"\
            + "                 ░░░██║░░░██╔══██║██╔══╝░░  ██╔══██╗██║░░░░░██║██║╚████║██║░░██║  ╚██████╔╝██║░░░██║██╔══╝░░░╚═══██╗░░░██║░░░\n"\
            + "                 ░░░██║░░░██║░░██║███████╗  ██████╦╝███████╗██║██║░╚███║██████╔╝  ░╚═██╔═╝░╚██████╔╝███████╗██████╔╝░░░██║░░░\n"\
            + "                 ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═════╝░╚══════╝╚═╝╚═╝░░╚══╝╚═════╝░  ░░░╚═╝░░░░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░")
        print("#" * 148)
        print("#                                                               - New game -                                                                       #")
        print("#                                                                 - Load -                                                                         #")
        print("#                                                                 - Help -                                                                         #")
        print("#                                                                 - Quit -                                                                         #\n")
        print("                                                     A game made by Dynomite (not the charictors)\n")
        possible_option = ['1', '2', '3', '4', 'n', 'p', 'l', 'h', 'q', 'new', 'new game', 'play', 'load', 'help', 'quit']
        print("                       please select the option by typing the word. for example type \"New Game\" to start a new game\n")
        option = input("> ")
        while option.lower() not in possible_option:
            print("Please enter a valid command.")
            option = input("> ")
        if option.lower() in ('1', 'n', 'p', 'new', 'new game', 'play'):
            Setup_Game()
            Setup1()
            Setup2()
            quest = quest1()
            ingame = True
            while ingame:
                Player_Prompt()
        elif option.lower() in ('2', 'l', 'load'):
            Clear_Screen()
            if os.path.exists("../The_Blind_Quest/game_files/save_file/savefile") == True:
                with open("../The_Blind_Quest/game_files/save_file/savefile", 'rb') as f:
                    global player1
                    player1 = pickle.load(f)
                f.close()
                print("#" * 148)
                to_print = "Loading...\n"
                for charictor in to_print:
                    sys.stdout.write(charictor)
                    sys.stdout.flush()
                    time.sleep(0.15)
                print("the Save state was Loaded...")
                option = input("> ")
                if player1.quest_counter == 0:
                    quest = quest1()
                elif player1.quest_counter == 1:
                    quest = quest2()
                elif player1.quest_counter == 2:
                    quest = quest3()
                elif player1.quest_counter == 3:
                    quest = quest4()
                elif player1.quest_counter == 4:
                    quest = quest5()
                elif player1.quest_counter == 5:
                    quest = quest6()
                elif player1.quest_counter == 6:
                    quest = quest7()
                ingame = True
                while ingame == True:
                    Player_Prompt()
            else:
                print("#" * 148)
                print("No save file found")
                option = input("> ")
        elif option.lower() in ('3', 'h', 'help'):
            Clear_Screen()
            print("#" * 148)
            print(" there is nothing I can help you with, you are on your own on this one pal")
            option = input("> ")
        elif option.lower() in ('4', 'q', 'quit'):
            Clear_Screen()
            sys.exit()  

### Set up for the Game ###
# ask for the players name
def Setup_Game():
    global player1
    global quest
    quest = quest1()
    player1 = player()
    in_setup = True
    while in_setup == True:
        Clear_Screen()
        print("#" * 148)
        print("\n Please enter the name of your creator: \n\n")
        print(" Note:\n @ You can only make it a maximum 6 charictors long. Eg: \"Dynomi\"\n @ It has to be at least 2 charictors long.          Eg: \"ME\"\n @ Canot chose special charictors.                   Eg: \"#\"\n @ Use only letters and numbers.                     Eg: \"A\" and \"1\"\n @ It has to start with a letter.                    Eg: \"A\" \n\n")
        player_name = input("> ")
        posible_options = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz' 
        other_posible_options = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        if player_name == '':
            Clear_Screen()
            print(" plese type somthing valid\n\n")
            option = input("> ")
            in_setup = True
            continue
        elif len(player_name) < 2:
            Clear_Screen()
            print(" please type somthing valid without spaces, a leter has to exist as the first charictor before the numbers\n\n")
            option = input("> ")
            in_setup = True
            continue
        elif len(player_name) > 6:
            Clear_Screen()
            print(" please select only up to a maximum of 6 charictors\n\n")
            option = input("> ")
            in_setup = True
            continue
        elif 'Dynomite' in player_name.lower():
            Clear_Screen()
            print("nope\n\n")
            option = input("> ")
            in_setup = True
            continue
        counter_i = 0
        for i in player_name:
            if counter_i == 0:
                if i not in posible_options:
                    Clear_Screen()
                    print(" please type somthing valid without spaces, a leter has to exist before a number\n\n")
                    option = input("> ")
                    forbiden = True
                else:
                    counter_i += 1
                    forbiden = False
            elif i not in other_posible_options:
                Clear_Screen()
                print(" please type somthing valid without spaces, a leter has to exist as the first charictor before the numbers\n\n")
                option = input("> ")
                forbiden = True
            else:
                counter_i += 1
                forbiden = False
            if forbiden:
                break
        if forbiden:
            pass
        else:
            in_setup = False
    player1.name = player_name
# different questions to the player
def Setup1():
    Clear_Screen()
    to_print = " how do you feel about your vesel?\n"
    Print_Dialog(to_print)
    print("(How do you feel?)\n\n")
    good_adj = ['good', 'very good', 'great', 'rohit', 'happy', 'aight', 'understanding', 'great', 'alright', 'calm', 'confident', 'not bad', 'courageous', 'peaceful', 'reliable', 'joyous', 'energetic', 'at', 'ease', 'easy', 'lucky', 'k', 'comfortable', 'amazed', 'fortunate', 'optimistic', 'pleased', 'free', 'delighted', 'swag', 'encouraged', 'ok', 'overjoyed', 'impulsive', 'clever', 'interested', 'gleeful', 'free', 'surprised', 'satisfied', 'thankful', 'frisky', 'content', 'receptive', 'important', 'animated', 'quiet', 'okay', 'festive', 'spirited', 'certain', 'kind', 'ecstatic', 'thrilled', 'relaxed', 'satisfied', 'wonderful', 'serene', 'glad', 'free', 'and', 'easy', 'cheerful', 'bright', 'sunny', 'blessed', 'merry', 'reassured', 'elated', '1738', 'love', 'interested', 'positive', 'strong', 'loving'] 	
    hmm_adj = ['concerned', 'lakshya', 'eager', 'impulsive', 'considerate', 'affected', 'keen', 'free', 'affectionate', 'fascinated', 'earnest', 'sure', 'sensitive', 'intrigued', 'intent', 'certain', 'tender', 'absorbed', 'anxious', 'rebellious', 'devoted', 'inquisitive', 'inspired', 'unique', 'attracted', 'nosy', 'determined', 'dynamic', 'passionate', 'snoopy', 'excited', 'tenacious', 'admiration', 'engrossed', 'enthusiastic', 'hardy', 'warm', 'curious', 'bold', 'secure', 'touched', 'brave', 'sympathy', 'daring', 'close', 'challenged', 'loved', 'optimistic', 'comforted', 're', 'enforced', 'drawn', 'toward', 'confident', 'hopeful', 'difficult'] 	
    bad_adj = ['bad', 'meh', 'sad', 'very sad', 'unpleasant', 'feelings', 'angry', 'very angry', 'depressed', 'confused', 'helpless', 'irritated', 'lousy', 'upset', 'incapable', 'enraged', 'disappointed', 'doubtful', 'hostile', 'discouraged', 'uncertain', 'paralyzed', 'insulting', 'ashamed', 'indecisive', 'fatigued', 'sore', 'powerless', 'perplexed', 'useless', 'annoyed', 'diminished', 'embarrassed', 'inferior', 'upset', 'guilty', 'hesitant', 'vulnerable', 'hateful', 'dissatisfied', 'shy', 'empty', 'unpleasant', 'miserable', 'stupefied', 'forced', 'offensive', 'detestable', 'disillusioned', 'hesitant', 'bitter', 'repugnant', 'unbelieving', 'despair', 'aggressive', 'despicable', 'skeptical', 'frustrated', 'resentful', 'disgusting', 'distrustful', 'distressed', 'inflamed', 'abominable', 'misgiving', 'woeful', 'provoked', 'terrible', 'lost', 'pathetic', 'despair', 'unsure', 'tragic', 'infuriated', 'sulky', 'uneasy', 'cross', 'bad', 'pessimistic', 'dominated', 'worked', 'up', 'a', 'sense', 'of', 'loss', 'tense', 'boiling', 'fuming', 'indignant', 'indifferent', 'afraid', 'hurt', 'sad', 'insensitive', 'fearful', 'crushed', 'tearful', 'dull', 'terrified', 'tormented', 'sorrowful', 'nonchalant', 'suspicious', 'deprived', 'pained', 'neutral', 'anxious', 'pained', 'grief', 'reserved', 'alarmed', 'tortured', 'anguish', 'weary', 'panic', 'dejected', 'desolate', 'bored', 'nervous', 'rejected', 'desperate', 'preoccupied', 'scared', 'injured', 'pessimistic', 'cold', 'worried', 'offended', 'unhappy', 'disinterested', 'frightened', 'afflicted', 'lonely', 'lifeless', 'timid', 'aching', 'grieved', 'shaky', 'victimized', 'mournful', 'restless', 'heartbroken', 'dismayed', 'doubtful', 'agonized', 'threatened', 'appalled', 'cowardly', 'humiliated', 'quaking', 'wronged', 'menaced', 'alienated', 'wary']
    option = input("> ")
    Clear_Screen()
    if option == "":
        to_print = "hey, me too. i know what that it is like to fell Empty about your self\nactualy, i forgot all of my emotions... ha\n\n"
    elif option.lower() in good_adj:
        to_print = "I am glad you feel [" + option.upper() + "] about your self\n\n"
    elif option.lower() in hmm_adj:
        to_print = "that is interesting you feel [" + option.upper() + "] about your self\n\n"
    elif option.lower() in bad_adj:
        to_print = "im sorry that you feel [" + option.upper() + "] about your self\n\n"
    else:
        to_print = "im not sure what its like feel [" + option.upper() + "] about your self\nactualy, i forgot all of my emotions... ha\n\n"
    Print_Dialog(to_print)
    option = input("> ")
# finally welcome to the world
def Setup2(): # your almost there
    in_role_selection = True
    while in_role_selection:
        Clear_Screen()
        print(" What role do you want in this world?\n\n")
        print("|         (Warrior  ---  Mage   ---  Priest)           |")
        print("|                                                      |")
        print("| WARRIOR -> HP: 140 | POW: 20 | ABILITY: Turtle Armor |")
        print("| MAGE    -> HP: 100 | POW: 40 | ABILITY: Magic Block  |")
        print("| PRIEST  -> HP: 120 | POW: 20 | ABILITY: Heal Pray    |\n")
        print("   (WARNING: you can't change this later in the game)  \n")
        print("     Note: it doesnt really matter what you chose")
        option = input("> ")
        if option.lower() in ['1', 'w', 'warrior']:
            player1.job = 'WARRIOR'
            player1.ability = 'Turtle Armor'
            player1.maxhp = 140
            player1.p = 20
            to_print = "You are now a " + player1.job + "!\n\n"
            Print_Dialog(to_print)
            in_role_selection = False
        elif option.lower() in ['2', 'm', 'mage']:
            player1.job = 'MAGE'
            player1.ability = 'Magic Block'
            player1.maxhp = 100
            player1.p = 40
            to_print = "You are now a " + player1.job + "!\n\n"
            Print_Dialog(to_print)
            in_role_selection = False
        elif option.lower() in ['3', 'p', 'priest']:
            player1.job = 'PRIEST'
            player1.ability = 'Heal Pray' 
            player1.maxhp = 120
            player1.p = 20
            to_print = "You are now a " + player1.job + "!\n\n"
            Print_Dialog(to_print)
            in_role_selection = False
        elif option.lower() in ['god']:
            player1.job = 'NOTHING'
            player1.maxhp = 34
            player1.p = 16
            to_print = "You are now a... ha, you're think youre funny dont you\n"
            Print_Dialog(to_print)
            to_print = "you will be " + player1.job + " in this world\n\n"
            Print_Dialog(to_print)
            in_role_selection = False
        elif option.lower() in ['no one', 'nothing', 'you']:
            player1.job = '...'
            player1.maxhp = 1
            player1.p = 1
            to_print = "...\n\n"
            Print_Dialog(to_print)
            in_role_selection = False
        else:
            Clear_Screen()
            print("plese select a valid role\n")
            option  = input("> ")
    player1.hp = player1.maxhp
    option = input("> ")
    Clear_Screen()
    to_print = "A new adventure is ahead of you. Remember... Always-"
    Print_Dialog(to_print)
    time.sleep(0.2)
    Clear_Screen()
    to_print = "always \"have fun\" :)"
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.15)
    time.sleep(0.2)
    Clear_Screen()
    if player1.job == 'NOTHING':
        print("#" * 148)
        print("                                   you are not gonna have a good time")
        print("                                                :)")
        print("#" * 148 + "\n")
    else:
        print("#" * 148)
        print("                                            Let's start")
        print("                                             Good luck")
        print("#" * 148 + "\n")
    option = input("> ")

### Game ###
# print the location
def Print_Location():
    print("                                                                " + "#" * (4 + len(player1.location)))
    print("                                                                # " + player1.location.upper() + " #")
    print("                                                                " + "#" * (4 + len(player1.location)))
    print("\n                                                       " + (map_locations[player1.location][DESCRIPTION]))
# gives user the choice on what ot do
def Player_Prompt(): # welcome, to the darasic park
    Clear_Screen()
    print("#" * 148)
    print("\n                                                             You are at:\n")
    Print_Location()
    print("\n")
    print("#" * 148)
    print("\nWhat whould you like to do?")
    print("(1-Move, 2-Inspect, 3-Status, 4-Map, 5-Save, 6-Quit, 7-Dance?, 8-Check inventory)\n")
    option = input("> ")
    acceptable_actions = ['1', '2', '3', '4', '5', '6', '7', '8', 'move', 'go', 'travel', 'walk', 'fly', 'quit', 'examine', 'inspect', 'interact', 'look', 'stare', 'gaze', 'dance', 'map', 'show map', 'see map', 'save', 'status', 'stats', 'info', 'check', 'inventory', 'check inventory']
    while option.lower() not in acceptable_actions:
        print("Unkown action, try again.\n")
        option = input("> ")
    if option.lower() in ['1','move', 'go', 'travel', 'walk']:      # go johhny go
        Clear_Screen()
        print("#" * 148)
        print("\n                                                             You are at:\n")
        Print_Location()
        print("\n")
        print("#" * 148)
        Player_Move(option.lower())
    elif option.lower() in ['2','inspect', 'look', 'examine', 'stare', 'gaze', 'enter']:
        if player1.location == 'a1':
            Home()
        elif player1.location == 'a8':
            if player1.times_entered_a8 == False:
                King()
            Det_Quest()
            Quest()
        elif player1.location == 'b1':
            Shop()
        elif player1.location == ":)":
            if player1.bosses_won < 6:
                Clear_Screen()
                print("#" * 148)
                print("You have to beat at least " + str(6 - player1.bosses_won) + " more bosses\nin order to enter\n")
                option = input("> ")
            else:
                Boss_Selection()
                Boss_Encounter()
                Enemy_Introduction()
                Fight()
        elif player1.funny_counter < 4:
            if player1.ability == 'NOTHING':
                pass
            elif player1.funny_counter == 0:
                if player1.location in ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8']:
                    number = random.randint(1, 8)
                    if number == 1:
                        Funny_Encounter()
                        player1.funny_counter += 1
            elif player1.funny_counter == 1:
                if player1.location in ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8']:
                    number = random.randint(1, 30)
                    if number == 1:
                        Funny_Encounter2()
                        player1.funny_counter += 1
            elif player1.enemy_times_won == 0 and player1.funny_counter == 2:
                if player1.location in ['c1', 'c2', 'c3', 'c4', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8']:
                    number = random.randint(1, 20)
                    if number == 1:
                        Funny_Encounter3()
                        player1.funny_counter += 1
            elif player1.funny_counter == 2 or 3:
                if player1.location in ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8']:
                    number = random.randint(1, 10)
                    if number == 1:
                        Funny_Encounter4()
                        player1.funny_counter += 1
        Player_Examine()
    elif option.lower() in ['3','status', 'stats', 'info']:
        Print_Status()
    elif option.lower() in ['4','map', 'show map', 'map', 'see map']:
        Print_Map()
    elif option.lower() in ['5', 'save']:
        Clear_Screen()
        with open('../The_Blind_Quest/game_files/save_file/savefile', 'wb') as f:
            pickle.dump(player1, f)
        f.close()
        print("#" * 148)
        to_print = "Saving...\n"
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.15)
        print("Game has been saved")
        option = input("> ")
    elif option.lower() in ['6', 'quit']:
        Clear_Screen()
        global ingame
        ingame = False
    elif option.lower() in ['7','dance']:
        Clear_Screen()
        print("#" * 148)
        print(f'um... {player1.name} started dancing')
        option = input("> ")
        possible_option = random.randint(1,5)
        if possible_option == 1:
            print("Whoa look at those moves, i wish i was that good")
        elif possible_option == 2:
            print("Those move sets is incredable, i wish the game develeper added those in the battle system")
        elif possible_option == 3:
            print("Um, i dont know why your doing this")
        elif possible_option == 4:
            print("Ouch!, thats gota hurt. better luck next time")
        elif possible_option == 5:
            print("You gota to stop that, the enemys are almost crying by how awful those moves are")
        option = input("> ")
    elif option.lower() in ['fly']:
        Clear_Screen()
        print("you you tried to fly, but you can't fly :( i wish i could as well")
        option = input("> ")
    elif option.lower() in ['8', 'check', 'inventory', 'check inventory']:
        Inv()
# print map
def Print_Map():
    Clear_Screen()
    to_print = ""
    counter = 0
    print("                   MAP\n")
    print(f"   You are at \"{player1.location.lower()}\" (\"PL\" on the map)")
    print("_________________________________________")
    for i in zonenames:
        if player1.location == i:
            to_print = to_print + "| PL "
        else:    
            to_print = to_print + "| " + i + " "
        counter += 1
        if counter / 8 == 1.0:
            to_print = to_print + "|"
            counter = 0
            print(to_print)
            print("_________________________________________")
            to_print = ""
    print("           Some Boss Locations\n")
    print("a2 - Mr Groove"
        + "\nb3 - Maestro"
        + "\nd4 - Q36u43e25e46n"
        + "\ne1 - Big $1im3"
        + "\nf7 - Bark Soul"
        + "\ng7 - Lancer"
        + "\n:) - ???\n\n")
    option = input("> ")
# print players stats
def Print_Status():
    Clear_Screen()
    print("#" * 148)
    print("                                                                 Your STATS\n")
    print("                                                      PLAYER NAME:    " + player1.name)
    print("                                                      CLASS:          " + player1.job)
    print("                                                      ABILITY:        " + player1.ability)
    print("                                                      LV:             " + str(player1.level))
    print("                                                      EXP:            " + str(player1.exp) + "/" + str(player1.maxexp))
    print("                                                      HP:             " + str(player1.hp) + "/" + str(player1.maxhp))
    print("                                                      POW:            " + str(player1.p))
    print("                                                      WEAPON EQUIPED: " + player1.curweap)
    print("                                                      GOLD:           " + str(player1.gold))
    print("                                                      POTIONS:        " + str(player1.pots))
    print("                                                      TEL:            " + str(player1.tel) + "\n")
    print("#" * 148)
    option = input("> ")
# print the inventory
def Print_Inv():
    Clear_Screen()
    print("#" * 148)
    print("                                                              Your INVENTORY\n")
    count = 1
    for i in player1.inv:
        print((" " * 45) + str(count) + ".) " + i)
        count += 1
    print("\n" + player1.curweap + " is the item you curently have equiped")
# inventory handaling
def Inv(): # are you inventing somthing?
    global in_inv
    in_inv = True
    while in_inv:
        Print_Inv()
        print("\n\nWhat would you like to do with your items?")
        print("(1-Equip item, 2-Inspect, 3-Throw away, 4-Go back)\n")
        option = input("> ")
        posible_options = [ '1', '2', '3', '4', 'e', 'i', 't', 'g', 'b', 'gb', 'equip', 'equip item', 'equip weapon', 'inspect', 'throw', 'throw item', 'throw waepon', 'throw away', 'Go back', 'back', 'exit']
        while option.lower() not in posible_options:
            print("please select a valid option")
            option = input("> ")
        if option.lower() in ['1', 'e', 'equip', 'equip item', 'equip waepon']:
            Item_Equip()
        elif option.lower() in ['2', 'i', 'inspect', 'inspect item', 'inspect weapon']:
            Item_Inspect()
        elif option.lower() in [ '3', 't', 'throw', 'throw away', 'throw item', 'throw waepon']:
            Item_Throw()
        else:
            in_inv = False
# equip the weapon?
def Item_Equip(): # oh, never mind
    Print_Inv()
    print("\nWhat would you like to eqiup?")
    print("(Pick the item or exit)\n")
    option = input("> ")
    count = 1
    if option == '':
        Clear_Screen()
        print("#" * 148)
        print("Please select a valid option or item\n")
        option = input("> ")
    try:
        for i in player1.inv:
            if option in str(count):
                option = i
            count += 1
        if option == player1.curweap:
            Clear_Screen()
            print("#" * 148)
            print("You already have that equiped\n")
            option = input("> ")
        elif option in player1.inv:
            Clear_Screen()
            if player1.curweap == 'Rusty Sword':
                pass
            elif player1.curweap == 'The Hip Sword':
                player1.p -= 20
            elif player1.curweap == 'The Bacon Sword':
                player1.p -= 32
                player1.hp -= 10
                if player1.hp > player1.maxhp:
                    player1.hp = player1.maxhp 
            elif player1.curweap == 'SerialKnife':
                player1.p -= 48
            elif player1.curweap == 'The Star':
                player1.p -= 50
            elif player1.curweap == 'A Spider Fang':
                player1.p -= 40
            elif player1.curweap == 'Rubix cube':
                player1.p = player1.store_p
            elif player1.curweap == 'Raspberry Pie':
                pass
            player1.store_p = player1.p
            player1.curweap = option
            if player1.curweap == 'Rusty Sword':
                pass
            elif player1.curweap == 'The Hip Sword':
                player1.p += 20
            elif player1.curweap == 'The Bacon Sword':
                player1.p += 32
                player1.hp += 10
                if player1.hp > player1.maxhp:
                    player1.hp = player1.maxhp 
            elif player1.curweap == 'SerialKnife':
                player1.p += 48
            elif player1.curweap == 'The Star':
                player1.p += 50
            elif player1.curweap == 'A Spider Fang':
                player1.p += 40
            elif player1.curweap == 'Rubix cube':
                player1.p = 1
            elif player1.curweap == 'Raspberry Pie':
                pass
            print("#" * 148)
            print("You have equiped " + player1.curweap + "\n")
            option = input("> ")
        elif option in ['b', 'e', 'q', "back", 'exit', 'quit']:
            pass
        else:
            Clear_Screen()
            print("#" * 148)
            print("Please select a valid option or item\n")
            option = input("> ")
    except:
        pass
# inspect the wepon?
def Item_Inspect():
    Print_Inv()
    print("\nWhat would you inspect?")
    print("(Pick the item or exit)\n")
    option = input("> ")
    count = 1
    if option == '':
        Clear_Screen()
        print("#" * 148)
        print("Please select a valid option or item\n")
        option = input("> ")
    try:
        for i in player1.inv:
            if option in str(count):
                option = i
            count += 1
        if option in player1.inv:
            Clear_Screen()
            print("#" * 148)
            if option == 'Rusty Sword':
                print("\"Rusty Sword\", the basic rusty sword, good for nothing i gueess (+ 0 damage in battle)\n")
            elif option == 'The Hip Sword':
                print("\"The Hip Sword\", although i wouldent say its hip, its beter then the rusty sword (+ 20 damage in battle)\n")
            elif option == 'The Bacon Sword':
                print("\"The Bacon Sword\" might seen stupid.but kinda good (+ 32 damage  in battle)\n")
            elif option == 'SerialKnife':
                print("\"SerialKnife\", are you proud of what you achived :) (+ 48 damage  in battle)\n")
            elif option == 'The Star':
                print("\"The Star\", the most powerfull sword in the game (+ 50 damage in battle)\n")
            elif option == 'A Spider Fang':
                print("\"A Spider Fang\", a fang that was found after beating Muffet (+ 40 damage in battle)\n")
            elif option == 'Rubix cube':
                print("\"Rubix cube\", a rubix cube (= 1 damage in battle?)\n")
            elif option == 'Raspberry Pie':
                print("\"Raspberry Pie: aquired after a peacefull party with the monsers(does nothing exept giving you a good memory)\n")
            option = input("> ")
        elif option.lower() in ['b', 'e', 'q', 'back', 'exit', 'quit']:
            pass
        else:
            Clear_Screen()
            print("#" * 148)
            print("Please select a valid option or item\n")
            option = input("> ")
    except:
        pass
# throw away the item? what is this bark souls?
def Item_Throw():
    Print_Inv()
    print("\nWhat would you throw away?")
    print("(Pick the item or exit)\n")
    option = input('> ')
    count = 1
    if option == '':
        Clear_Screen()
        print("#" * 148)
        print("Please select a valid option or item\n")
        option = input("> ")
    try:
        for i in player1.inv:
            if option in str(count):
                option = i
            count += 1
        if option in player1.inv:
            Clear_Screen()
            print("#" * 148)
            if option == player1.curweap:
                print("you cannot remove a weapon that is equiped\n")
                option = input("> ")
            else:
                print("Are you sure you want to remove " + option  + "?")
                print("(1-Yes, 2-No)\n")
                posible_options = ['1','2', 'y', 'yes', 'n', 'no']
                option = input("> ")
                while option.lower() not in posible_options:
                    Clear_Screen()
                    print("#" * 148)
                    print("please select a valid option\n")
                    option = input("> ")
                if option.lower() in ['1', 'y', 'yes']:
                    Clear_Screen()
                    print("#" * 148)
                    player1.inv.remove(option)
                    print("You have trown away " + option + "\n")
                    option = input("> ")
        elif option.lower() in ['b', 'e', 'b', 'back', 'exit', 'back']:
            pass
        else:
            Clear_Screen()
            print("#" * 148)
            print("not a valid option or item was not found in the inventory\n")
            option = input("> ")
    except:
        pass
#  questions in what direction the user should move
def Player_Move(myAction):
    if myAction == '1':
        print("\nIn which direction wold you like to move?")
    else:
        print("\nIn which direction wold you like to " + myAction + "?")
    print("(1-Up/North, 2-Left/West, 3-Right/East, 4-Down/South)\n")
    print("                  OR\n")
    print("(Type the name of the location to teleport)")
    print(f"(You have {player1.tel} Teleport potions left)\n")
    print(f"(You can also select \"back\" if you do not wish to move)")
    possible_optiions = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3','c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2' , 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', ':)', '1', '2', '3', '4', 'up', 'north', 'left', 'west', 'right', 'down', 'south' 'east', 'quit', 'exit', 'back','go back', 'do not enter', 'no', 'i didnt want this']
    in_location_selection = True
    while in_location_selection:
        option = input("> ")
        while option.lower() not in possible_optiions:
            print("please select a valid direction")
            option = input("> ")
        if option.lower() in ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2' , 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', ':)']:
            if player1.tel > 0:
                destination = option.lower()
                player1.location = destination
                player1.tel -= 1
                player1.location = destination
                in_location_selection = False
            else:
                Clear_Screen()
                print("#" * 148)
                print("you dont have any Teleport potions\n")
                option = input("> ")
        elif option.lower() in ['1', 'up', 'north']:
            if map_locations[player1.location][UP] == '':
                print("You canot go any Further up\n")
                option = input("> ")
            else:
                destination = map_locations[player1.location][UP]
                player1.location = destination
                in_location_selection = False
        elif option.lower() in ['2', 'left', 'west']:
            if map_locations[player1.location][LEFT] == '':
                print("you canot go any further to the left\n")
                option = input("> ")
            else:
                destination = map_locations[player1.location][LEFT]
                player1.location = destination
                in_location_selection = False
        elif option.lower() in ['3', 'right', 'east']:
            if map_locations[player1.location][RIGHT] == '':
                print("you canot go any further to the right\n")
                option = input("> ")
            else:
                destination = map_locations[player1.location][RIGHT]
                player1.location = destination
                in_location_selection = False
        elif option.lower() in ['4', 'down', 'south']:
            if map_locations[player1.location][DOWN] == '':
                print("you canot go any further douwn\n")
                option = input("> ")
            else:
                destination = map_locations[player1.location][DOWN]
                player1.location = destination
                in_location_selection = False
        elif option.lower() in ['quit', 'exit', 'back','go back', 'do not enter', 'no', 'i didnt want this']:
            in_location_selection = False
# examine the location and let the player choise the option to chose 'Fight'(boss or enemy)/'Puzzle'/'Back'
def Player_Examine():
    Clear_Screen()
    print("#" * 148)
    print("\n                                                             You are at:\n")
    Print_Location()
    print("\n                             " + map_locations[player1.location][EXAMINATION] + "\n")
    print("#" * 148)
    print("\n(do you wish to enter this place?)")
    if map_locations[player1.location][HAS] == 'Boss':    # challenge if there is a boss 
        print("(1-Yes, 2-No, 3-Challenge me)\n")
    else:   # else puzzle
        print("(1-Yes, 2-No, 3-Puzzle)\n")
    option = input("> ")
    if map_locations[player1.location][HAS] == 'Boss':
        posible_options = ['1', 'yes', 'sure', 'ok', 'ya', 'ya dude', 'oki doki', '3', 'challenge', 'challenge me', 'letsa go', '2', 'no', 'nah', 'nope', 'exit', 'back', 'b', 'e']
    else:
        posible_options = ['1', 'yes', 'sure', 'ok', 'ya', 'ya dude', 'oki doki', 'letsa go', '2', 'no', 'nah', 'nope', 'exit', 'back', 'b', 'e', '3', 'puzzle', 'p']
    while option.lower() not in posible_options:
        print("please select a valid choice")
        option = input("> ")
    into_battle = False
    if option.lower() in ['1', 'yes', 'sure', 'ok', 'ya', 'ya dude', 'oki doki', 'letsa go',]:
        Enemy_Selection()
        if player1.en1_counter == False or player1.en2_counter == False or player1.en3_counter == False or player1.en4_counter == False or player1.en5_counter == False or player1.en6_counter == False or player1.en7_counter == False or player1.en8_counter == False or player1.en9_counter == False or player1.en10_counter == False:
            Enemy_Encounter()
        Enemy_Introduction()
        Fight()
    elif option.lower() in ['2', 'no', 'nah', 'nope', 'exit', 'back', 'b', 'e']:
        pass
    elif map_locations[player1.location][HAS] == 'Boss':
        if option.lower() in ['3', 'challenge', 'challenge me']:
            if player1.location == 'a2':
                if player1.boss1_defeated == True:
                    Clear_Screen()
                    print("#" * 148)
                    print("there is no challenge left for you here")
                    option = input("> ")
                else:
                    into_battle = True
            elif player1.location == 'b3':
                if player1.boss2_defeated == True:
                    Clear_Screen()
                    print("#" * 148)
                    print("there is no challenge left for you here")
                    option = input("> ")
                else:
                    into_battle = True
            elif player1.location == 'c5':
                if player1.boss3_defeated == True:
                    Clear_Screen()
                    print("#" * 148)
                    print("there is no challenge left for you here")
                    option = input("> ")
                else:
                    into_battle = True
            elif player1.location == 'd4':
                if player1.boss4_defeated == True:
                    Clear_Screen()
                    print("#" * 148)
                    print("there is no challenge left for you here")
                    option = input("> ")
                else:
                    into_battle = True
            elif player1.location == 'e1':
                if player1.boss5_defeated == True:
                    Clear_Screen()
                    print("#" * 148)
                    print("there is no challenge left for you here")
                    option = input("> ")
                else:
                    into_battle = True
            elif player1.location == 'f7':
                if player1.boss6_defeated == True:
                    Clear_Screen()
                    print("#" * 148)
                    print("there is no challenge left for you here")
                    option = input("> ")
                else:
                    into_battle = True
            elif player1.location == 'g7':
                if player1.boss10_defeated == True:
                    Clear_Screen()
                    print("#" * 148)
                    print("there is no challenge left for you here")
                    option = input("> ")
                else:
                    into_battle = True
            if into_battle == True:
                Boss_Selection()
                Boss_Encounter()
                Enemy_Introduction()
                Fight()
    elif option.lower() in ['3', 'puzzle', 'p']:
        if player1.solved_places[player1.location] == True:
            Clear_Screen()
            print("#" * 148)
            print("there is no puzzle left for you here")
            option = input("> ")
        else:
            Puzzle()

# goodnight
def Home_Sleep(): # zzz...
    # this is where the magic happens
    print("#" * 148)
    random_option = random.randint(1,6)
    if random_option == 1:
        to_print = ". even though, there is no point in doing so"
    elif random_option == 2:
        to_print = ". i mean, i guess its good for you"
    elif random_option == 3:
        to_print = ". yup, there you go. night night"
    elif random_option == 4:
        to_print = ". zzz"
    elif random_option == 5:
        to_print = "..."
    else:
        to_print = ". i would have pranked you right now if i could"
    print("You took a rest" + to_print)
    option = input("> ")
# youe home
def Home():
    Clear_Screen()
    if player1.boss9_defeated == False:
        if (player1.solved_places['a3'] and player1.solved_places['a3'] and player1.solved_places['a4'] and player1.solved_places['a5'] and player1.solved_places['a6'] and player1.solved_places['a7'] and\
            player1.solved_places['b2'] and player1.solved_places['b4'] and player1.solved_places['b5'] and player1.solved_places['b6'] and player1.solved_places['b7'] and player1.solved_places['b8'] and\
            player1.solved_places['c1'] and player1.solved_places['c2'] and player1.solved_places['c3'] and player1.solved_places['c4'] and player1.solved_places['c6'] and player1.solved_places['c7'] and player1.solved_places['c8'] and\
            player1.solved_places['d1'] and player1.solved_places['d2'] and player1.solved_places['d3'] and player1.solved_places['d5'] and player1.solved_places['d6'] and player1.solved_places['d7'] and player1.solved_places['d8'] and\
            player1.solved_places['e2'] and player1.solved_places['e3'] and player1.solved_places['e4'] and player1.solved_places['e5'] and player1.solved_places['e6'] and player1.solved_places['e7'] and player1.solved_places['e8'] and\
            player1.solved_places['f1'] and player1.solved_places['f2'] and player1.solved_places['f3'] and player1.solved_places['f4'] and player1.solved_places['f5'] and player1.solved_places['f6'] and player1.solved_places['f8']) == True:
            Boss_Selection()
            Boss_Encounter()
            Enemy_Introduction()
            Fight()
    elif player1.boss8_defeated == False:
        random_option = random.randint(1, 100)
        if random_option == 1:
            Boss_Selection()
            Boss_Encounter()
            Enemy_Introduction()
            Fight()
        else:
            Home_Sleep()
    else:
        Home_Sleep()

### Shop ###
# presents the chices
def Shop():
    global in_shop
    in_shop = True 
    while in_shop:
        Clear_Screen()
        print("#" * 148)
        print("Shopkeeper:")
        if player1.level >= 30:
            print("     Why hey there you gullible worm ;)\n")
        else:
            print("     Welcme to my shop traveler :)")
        print("                                            v             What would you like to buy?             v\n\n")
        print("                                                             (You have " + str(player1.gold) + " Gold)\n")
        print(f"                                                    1.) Potions: 30 Gold (You have {str(player1.pots)} Potion)")
        print(f"                                                    2.) Teleports: 100 Gold (You have {str(player1.tel)}) Teleports")
        print("                                                    3.) Talk to the Shopkeeper: 0 Gold")
        if player1.level >= 30:
            if player1.ih_price == 12150:
                print(f"                                                    4.) Imrove Health (Out of stock)")
            else:
                print(f"                                                    4.) Imrove Health {player1.ih_price} Gold (You have {player1.maxhp} Health)")
            if player1.hip_count == False:
                print(f"                                                    5.) Buy \"The Hip Sword\" 200 Gold")
            else:
                print(f"                                                    5.) Buy \"The Hip Sword\" 200 Gold (Out of stock)")
            print("                                                    6.) Quit\n")
            possible_options = ['1', 'p', 'potion', 'potions', 'pot', 'pots', '2', 'teleport', 'teleports', 'tel', 'tels', '3', 'talk', 'ask', 'talk to shopkeeper', '4', 'uh', 'upgrade', 'health', 'improve', '5', 'buy hip sword', 'hip sword', 'sword', '6', 'back', 'quit', 'exit']
        else:
            print("                                                    4.) Quit\n")
            possible_options = ['1', 'p', 'potion', 'potions', 'pot', 'pots', '2', 't', 'teleport', 'teleports', 'tel', 'tels', '3', 'talk', 'ask', 'talk to shopkeeper', '4', 'back', 'quit', 'exit']
        option = input("> ")
        while option.lower() not in possible_options:
            print("plese enter a valid option")
            option = input("> ")
        if option.lower() in ['potion', 'pot']:
            if player1.gold < 30:
                Clear_Screen()    
                print("#" * 148)
                print("Shopkeeper:")
                print("    sorry you dont have enough Gold")
            else:
                purchased = False
                item = "Potion"
                price = 30
                amount = 1
                Confirm(item, amount, price)
                if purchased == True:
                    player1.pots += 1
                    player1.gold -= 30
                    Clear_Screen()
                    print("#" * 148)
                    print("You have bought 1 Potion for 30 Gold")
                    print("You have " + str(player1.gold) + "Gold left")
                else:
                    Clear_Screen()
                    print("#" * 148)
                    print(f"You did not buy any {item}\n")
            option = input("> ")
        elif option.lower() in ['1', 'p', 'potions', 'pots']:
            How_Many_Potions()
        elif option.lower() in ['teleport', 'tel']:
            if player1.gold < 100:
                Clear_Screen()
                print("#" * 148)
                print("Shopkeeper:")
                print("    sorry you dont have enough Gold")
            else:
                purchased = False
                item = "Teleport"
                price = 100
                amount = 1
                Confirm(item, amount, price)
                if purchased == True:
                    player1.pots += 1
                    player1.gold -= 100
                    Clear_Screen()
                    print("#" * 148)
                    print("You have bought 1 Teleport for 100 Gold")
                    print("You have " + str(player1.gold) + "Gold left")
                else:
                    Clear_Screen()
                    print("#" * 148)
                    print(f"You did not buy any {item}\n")
            option = input("> ")
        elif option.lower() in ['2', 't', 'teleports', 'tels']:
            How_Many_Tel()
        elif option.lower() in ['3', 'talk', 'talk to shopkeeper']:
            Shop_talk()
        elif option.lower() in ['4', 'back', 'quit', 'exit', 'uh', 'upgrade', 'health', 'improve']:
            if option.lower() in ['4']:
                if player1.level >= 30:
                    Upgrade_Health()
                else:
                    Shop_Goodbuy()
            elif option.lower() in ['back', 'quit', 'exit']:
                Shop_Goodbuy()
            elif option.lower() in ['uh', 'upgrade', 'health', 'improve']:
                Upgrade_Health()
        elif option.lower() in ['5', 'buy hip sword', 'hip sword', 'sword']:
            Buy_Hipsword()
        elif option.lower() in ['6']:
            Shop_Goodbuy()
# player celects the amount how many potions
def How_Many_Potions(): # potion seller, im going into battle and i need your strongest potions
    Clear_Screen()
    print("#" * 148)
    print("Shopkeeper:")
    print("    ahhh yes, these potions will heal you for sure, made by yours truly\n")
    print(f"                    Potions: 30 Gold (You have {str(player1.pots)}) Potions\n")
    print("                     You have " + str(player1.gold) + " Gold\n")
    print("How many potions whould you like to buy?\n")
    posible_options = '0123456789' 
    option = input("> ")
    if option in ['quit', 'exit', 'back', 'cancel', 'return']:
        Shop_Goodbuy()
    else:
        for i in option:
            if i not in posible_options:
                Clear_Screen()
                print("#" * 148)
                print("please type somthing valid without spaces\n")
                option = input("> ")
                break
        try:
            option = int(option)
            if (30 * option) > player1.gold:
                Clear_Screen()
                print("#" * 148)
                print("Shopkeeper:")
                print("   sorry you dont have enough Gold\n")
            else:
                global purchased
                purchased = False
                item = "Potions"
                price = 30 * option
                Confirm(item, option, price)
                if purchased == True:
                    player1.pots += option
                    player1.gold -= 30 * option
                    Clear_Screen()
                    print("#" * 148)
                    print("You have bought " + str(option) + " Potions for: " + str(30 * option) + " Gold\n")
                    print("You have " + str(player1.gold) + " Gold left\n")
                else:
                    Clear_Screen()
                    print("#" * 148)
                    print(f"You did not buy any {item}\n")
            option = input("> ")
        except:
            pass
# player selects 
def How_Many_Tel(): # tel? does that mean telivision?
    Clear_Screen()
    print("#" * 148)
    print("Shopkeeper:")
    print("    ahhh yes, these will teleport you for sure, just select the exact location when traveling. use them wizely\n")
    print(f"                    Teleports: 100 Gold (You have {str(player1.tel)}) Teleports\n")
    print("                     You have " + str(player1.gold) + " Gold\n")
    print("How many potions whould you like to buy?\n")
    posible_options = '0123456789' 
    option = input("> ")
    if option in ['quit', 'exit', 'back', 'cancel', 'return']:
        Shop_Goodbuy()
    else:
        for i in option:
            if i not in posible_options:
                Clear_Screen()
                print("#" * 148)
                print("please type somthing valid without spaces\n")
                option = input("> ")
                break
        try:
            option = int(option)
            if (100 * option) > player1.gold:
                Clear_Screen()
                print("#" * 148)
                print("Shopkeeper:")
                print("   sorry you dont have enough Gold\n")
            else:
                global purchased
                purchased = False
                item = "Teleport Potions"
                price = 100 * option
                Confirm(item, option, price)
                if purchased == True:
                    player1.tel += option
                    player1.gold -= 100 * option
                    Clear_Screen()
                    print("#" * 148)
                    print("You have bought " + str(option) + " Teleports for: " + str(100 * option) + " Gold\n")
                    print("You have " + str(player1.gold) + " Gold left\n")
                else:
                    Clear_Screen()
                    print("#" * 148)
                    print(f"You did not buy any {item}\n")
            option = input("> ")
        except:
            pass
# talking costs 0 gold.
def Shop_talk(): # my potions are too strong for you
    in_talk = True
    while in_talk == True:
        Clear_Screen()
        print("#" * 148)
        print("Shopkeeper:")
        if player1.level >= 30:
            print("    what would you like to talk about you gullible worm ;)")
        else:
            print("    what whould you like to talk about :)")
        print("                                            v             What would you like to talk about?             v\n\n")
        print("                                                    1.) Who are you?")
        print("                                                    2.) Why are you selling stuff here?")
        print("                                                    3.) What is this place?")
        print("                                                    4.) What should I do?")
        print("                                                    5.) Acting on enemys")
        print("                                                    6.) Fighting enemys")
        posible_options = ['1', 'who are you', 'who are you?', '2', 'why are you selling stuff here', 'why are you selling stuff here?', '3', 'what is this place', 'what is this place?', '4', 'what should I do', 'what should I do?', '5', 'acting', 'acting on enemys', '6', 'fighting', 'Fighting enemys']
        if player1.funny_counter >= 1:
            print("                                                    7.) Who is Dynomite?")
            posible_options.append('7')
            posible_options.append('who is Dynomite')
            posible_options.append('who is Dynomite?')
        if (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter >= 1:
            print("                                                    8.) Who is King?")
            posible_options.append('8')
            posible_options.append('who is king')
            posible_options.append('who is king?')
        elif (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter == 0:
            print("                                                    7.) Who is King?")
            posible_options.append('7')
            posible_options.append('who is king')
            posible_options.append('who is king?')
        if (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter >= 1:
            print("                                                    9.) Bosses")
            posible_options.append('9')
            posible_options.append('bosses')
            posible_options.append('bosses?')
        elif (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter == 0:
            print("                                                    8.) Bosses")
            posible_options.append('8')
            posible_options.append('bosses')
            posible_options.append('bosses?')
        elif player1.funny_counter >= 1:
            print("                                                    8.) Bosses")
            posible_options.append('8')
            posible_options.append('bosses')
            posible_options.append('bosses?')
        else:
            print("                                                    7.) Bosses")
            posible_options.append('7')
            posible_options.append('bosses')
            posible_options.append('bosses?')
        if (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter >= 1:
            print("                                                    10.) Quit")
            posible_options.append('10')
            posible_options.append('quit')
            posible_options.append('back')
            posible_options.append('exit')
        elif (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter == 0:
            print("                                                    9.) Quit")
            posible_options.append('9')
            posible_options.append('quit')
            posible_options.append('back')
            posible_options.append('exit')
        elif player1.funny_counter >= 1:
            print("                                                    9.) Quit")
            posible_options.append('9')
            posible_options.append('quit')
            posible_options.append('back')
            posible_options.append('exit')
        elif player1.funny_counter == 0:
            print("                                                    8.) Quit")
            posible_options.append('8')
            posible_options.append('quit')
            posible_options.append('back')
            posible_options.append('exit')
        option = input("> ")
        while option.lower() not in posible_options:
            print("plese choose and option")
            option = input("> ")
        Clear_Screen()
        print("#" * 148)
        if option.lower() in ['1', 'who are you', 'who are you']:
            print("Shopkeeper:")
            if player1.level < 30:
                print("    i am the shopkeeper. i keep shops heh")
                print("    thats prety much it, i dont have any other purpose as a charictor")
                print("    i sell you items if have gold")
                print("    gold can be found by defeating enemys, compleating puzzles or quests\n")
            else:
                print("    well i am the new shop keeper")
                print("    i sell new stuff")
                print("    also have i mentiond i collect worms as a hooby\n")
            option = input("> ")
        elif option.lower() in ['2', 'why are you selling stuff here', 'why are you selling stuff here?']:
            print("Shopkeeper:")
            print("    not sure thought it was cool")
            print("    i mean, its quite convineant for you is it not")
            print("    maybe ill get enough money to afford collage\n")
            option = input("> ")
        elif option.lower() in ['3', 'what is this place', 'what is this place?']:
            print("Shopkeeper:")
            print("    this was the land of hope. created by someone due to the loss of their friend")
            print("    it was a plase to escape from reallity. this land created us, intelegent beings.")
            print("    this land keept on growing and growing untill it suddenly stoped andd everything fell to darkness and dispair\n")
            option = input("> ")
        elif option.lower() in ['4', 'what should I do', 'what should I do?']:
            print("Shopkeeper:")
            print("    well thats up to you. wether you wana stay and have fun here or escape this place")
            print("    personaly i perfer to stay right here and earn money\n")
            option = input("> ")
        elif option.lower() in ['5', 'acting', 'acting on enemys']:
            print("Shopkeeper:")
            print("    acting allows you to finish a fight with the enemys without killing them")
            print("    though it doesnt effect anything, it would just depends wether you have empathy for the monsters\n")
            option = input("> ")
        elif option.lower() in ['6', 'fighting', 'Fighting enemys']:
            print("Shopkeeper:")
            print("    fighting allows you to finish a fight quickly in some cases")
            print("    though i dont see why you would do such a thing\n")
            option = input("> ")
        elif option.lower() in ['7', 'who is Dynomite', 'who is Dynomite?', 'who is king', 'who is king?', 'bosses', 'bosses?']:
            print("Shopkeeper:")
            if option.lower() in ['7']:
                if player1.funny_counter >= 1:
                    print("    ah Dynomite, the former king of this land. really cool dude. surprisingly no one knows him too well, even after so many years.")
                    print("    he seems nice at first. but then he starts to lose it, goes crazy.")
                    print("    Dynomite says somthing along the lines of \"you said that last time\" and \"you are all the same\" to all of us")
                    print("    id be cearfull around him, he knows more then you think\n")
                elif (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter == 0:
                    print("    our current king is a strange one, hides in his castel over at A8 like a cowerd.")
                    print("    hiers people to kill monsters here.")
                    print("    people like us.")
                    print("    you dont have to worry about him if you arent a monster\n")
                else:
                    print("    there are many bosses in lands")
                    print("    if you defeat at least 6 bosses")
                    print("    you can finally break free")
                    print("    and finish this journey\n")
            elif option.lower() in ['who is Dynomite', 'who is Dynomite?']:
                print("    ah Dynomite, the former king of this land. really cool dude. surprisingly no one knows him too well, even after so many years.")
                print("    he seems nice at first. but then he starts to lose it, goes crazy.")
                print("    Dynomite always says something along the lines of \"you said that last time\" and \"you are all the same\" to all of us")
                print("    id be cearfull around him, he knows more then you think\n")
            elif option.lower() in ['who is king', 'who is king?']:
                print("    our current king is a strange one, hides in his castel over at A8 like a cowerd.")
                print("    hiers people to kill monsters here.")
                print("    people like us.")
                print("    you dont have to worry about him if you arent a monster\n")
            elif option.lower() in ['bosses', 'bosses?']:
                print("    there are many bosses in lands, some are challanging some are very easy")
                print("    if you defeat at least 6 bosses")
                print("    you can finally break free")
                print("    and finish this journey\n")
            option = input("> ")
        elif option.lower() in ['8','quit', 'back', 'exit']:
            if option.lower() in ['8']:
                if (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter >= 1:
                    print("Shopkeeper:")
                    print("    our current king is a strange one, hides in his castel over at A8 like a cowerd.")
                    print("    hiers people to kill monsters here.")
                    print("    people like us.")
                    print("    you dont have to worry about him if you arent a monster\n")
                elif (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter == 0:
                    print("Shopkeeper:")
                    print("    there are many bosses in lands, some are challanging some are very easy")
                    print("    if you defeat at least 6 bosses")
                    print("    you can finally break free")
                    print("    and finish this journey\n")
                elif player1.funny_counter >= 1:
                    print("Shopkeeper:")
                    print("    there are many bosses in lands, some are challanging some are very easy")
                    print("    if you defeat at least 6 bosses")
                    print("    you can finally break free")
                    print("    and finish this journey\n")
                elif player1.funny_counter == 0:
                    in_talk = False
            elif option.lower() in ['quit', 'back', 'exit']:
                in_talk = False
        elif option.lower() in ['9']:
            if (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter >= 1:
                print("Shopkeeper:")
                print("    there are many bosses in lands, some are challanging some are very easy")
                print("    if you defeat at least 6 bosses")
                print("    you can finally break free")
                print("    and finish this journey\n")
            elif (player1.quest_counter >= 1 or player1.quest_selected == True) and player1.funny_counter == 0:
                in_talk = False
            elif player1.funny_counter >= 1:
                in_talk = False
        elif option.lower() in ['10']:
            in_talk = False
# improve health
def Upgrade_Health():
    if player1.ih_price == 12150:
        Clear_Screen()
        print("#" * 148)
        print("Shopkeeper:")
        print("    sorry, i ran out of them :(\n")
    elif player1.gold < player1.ih_price:
        Clear_Screen()
        print("#" * 148)
        print("Shopkeeper:")
        print("    sorry you dont have enough Gold\n")
    else:
        global purchased
        purchased = False
        item = "Health Upgrade"
        amount = 1
        Confirm(item, amount, player1.ih_price)
        if purchased == True:
            Clear_Screen()
            print("#" * 148)
            print("Shopkeeper:")
            print("    there you go sweet heart ;)\n\n")
            print("                     You have bought a health upgrade for: " + str(player1.ih_price) + " Gold")
            print("                     Your MAX HP was improved by 100 HP\n")
            print("You have " + str(player1.gold) + " Gold left\n")
            player1.gold -= player1.ih_price
            player1.maxhp += 100
            player1.hp = player1.maxhp 
            player1.ih_price = player1.ih_price * 3
        else:
            Clear_Screen()
            print("#" * 148)
            print(f"You did not buy a {item}\n")
    option = input("> ")
# buying the hip sword
def Buy_Hipsword():
    if player1.hip_count == True:
        Clear_Screen()
        print("#" * 148)
        print("Shopkeeper:")
        print("    sorry, dont have one anymore :(\n")
        option = input("> ")
    elif 200 > player1.gold:
        Clear_Screen()
        print("#" * 148)
        print("Shopkeeper:")
        print("     sorry you dont have enough Gold\n")
    else:
        global purchased
        purchased = False
        item = "Hip Sword"
        price = 200
        amount = 1
        Confirm(item, amount, price)
        if purchased == True:
            player1.gold -= 200
            player1.inv.append('The Hip Sword')
            player1.hip_count = True
            Clear_Screen()
            print("#" * 148)
            print("You have bought \"The Hip Sword\" for: 200 Gold\n")
            print("You have " + str(player1.gold) + " Gold left\n")
            option = input("> ")
            Clear_Screen()
            print("\"The Hip Sword\" has been added to your items\n")
        else:
            Clear_Screen()
            print("#" * 148)
            print(f"You did not buy {item}\n")
    option = input("> ")
# confirm purchace
def Confirm(item, option, price): # are you sure you want to buy from him?
    Clear_Screen()
    print("#" * 148)
    print(f"Are you sure you want to purchase {option} {item} for {price} GOLD?")
    print("\n(1-Yes, 2-No)\n")
    option = input("> ")
    posible_options = ['1', 'yes', 'sure', 'yup', 'ok', '2', 'no', 'back', 'exit', 'go back']
    while option.lower() not in posible_options:
        print("plese choose and option")
        option = input("> ")
    if option.lower() in ['1', 'yes', 'sure', 'yup', 'ok']:
        global purchased
        purchased = True
    elif option.lower() in ['2', 'no', 'back', 'exit', 'go back']:
        pass
    else:
        Clear_Screen()
        print("#" * 148)
        print("please type somthing valid without spaces\n")
        option = input("> ")
# good buy ;)
def Shop_Goodbuy(): # see what i did there ;)
    Clear_Screen()
    print("#" * 148)
    print("Shopkeeper:")
    print("    good bye\n")
    option = input("> ")
    global in_shop
    in_shop = False

### Castele (Quests) ###
# first encounter
def King():
    king_dialog = "King:\n  "
    Clear_Screen()
    print(king_dialog + "   HAey, you werent invited. WhAtaya doin here?\n\n")
    print("???\n")
    option = input("> ")
    Clear_Screen()
    print(king_dialog + "   ActuAlly I Dont cAre")
    print(king_dialog + "   I got quests for you. i got \"GOLD\"\n")
    option = input("> ")
    player1.times_entered_a8 = True
# determines th equest
def Det_Quest():
    global quest
    if player1.quest_selected == False:
        if player1.quest_counter == 0:
            quest = quest1()
        elif player1.quest_counter == 1:
            quest = quest2()
        elif player1.quest_counter == 2:
            quest = quest3()
        elif player1.quest_counter == 3:
            quest = quest4()
        elif player1.quest_counter == 4:
            quest = quest5()
        elif player1.quest_counter == 5:
            quest = quest6()
        elif player1.quest_counter == 6:
            quest = quest7()
# gives a choice to select the quest or go back to the map
def Quest(): # this is pointles honestly. i regret making ths part
    king_dialog = "King:\n  "
    if player1.quest_counter == 7:
        Clear_Screen()
        print("#" * 148)
        print("There is no one here")
        option = input("> ")
    else:
        Clear_Screen()
        print("#" * 148)
        print("                                                      Quests                        \n")
        print("                                     Quest: \"" + quest.name + "\": " + quest.discription + " (You get " + str(quest.item) + " " + quest.reward_type + ")\n\n")
        if player1.quest_selected == True:
            print("\n" + king_dialog + "   please come back onece you finished with this quest")
            option = input("> ")
        else:
            print("\n" + king_dialog + "   Consider my offer.\n")
            print("(Do you exept this quest?)")
            print("(1-Yes, 2-No)\n")
            option = input("> ")
            possible_options = ['1', 'y', 'yes', 'ya', 'ya dude', 'yas','2', 'n', 'no', 'na', 'nope', 'na fam', 'not today', 'b', 'e', 'q', 'back', 'quit', 'exit']
            while option.lower() not in possible_options:
                print("Plese select something valid")
                option = input("> ")
            if option in ['1','y', 'yes', 'ya', 'ya dude', 'yas']:
                Clear_Screen()
                print("#" * 148)
                print(king_dialog + "   Well good luck, And good bye\n")
                player1.quest_selected = True
            else:
                Clear_Screen()
                print("#" * 148)
                print(king_dialog + "   good bye\n")
            option = input("> ")

### Puzzle ### yup
def Puzzle(): # i hate these, though they can be fun sometimes
    ### A ###
    # a1 not included 
    # a2 not included
    if player1.location == 'a3' and player1.solved_places['a3'] == False:
        to_print = 'If I drink, I die. If I eat, I am fine.\n                                                 What am I?'
        answer = 'fire'
        prize = 40
    elif player1.location == 'a4' and player1.solved_places['a4'] == False:
        to_print = 'Cloud is my mother. Wind is my father. I come down but never go up.\n                                                 What am I?'
        answer = 'rain'
        prize = 60
    elif player1.location == 'a5' and player1.solved_places['a5'] == False:
        to_print = 'I repeat the word you say. The more I repeat, the softer I got.\n                                                 I cannot be seen but can be heard.\nWhat am I?'
        answer = 'echo'
        prize = 80
    elif player1.location == 'a6' and player1.solved_places['a6'] == False:
        to_print = 'What color can you eat?'
        answer = 'orange'
        prize = 90
    elif player1.location == 'a7' and player1.solved_places['a7'] == False:
        to_print = 'What body part is pronounced as one letter,\n                                                 but written with three, only two different letters are used?'
        answer = 'eye'
        prize = 100
    # a8 not included
    ### B ###
    # b1 not included
    elif player1.location == 'b2' and player1.solved_places['b2'] == False:
        to_print = 'I can be cracked, made, told, and played.\n                                                 What am I?'
        answer = 'joke'
        prize = 110
    # b3 not included
    elif player1.location == 'b4' and player1.solved_places['b4'] == False:
        to_print = 'What building has the most stories?'
        answer = 'library'
        prize = 120
    elif player1.location == 'b5' and player1.solved_places['b5'] == False:
        to_print = 'Tuesday, Sam and Peter went to a restaurant.\n                                                 After eating lunch, they paid the bill. Sam and Peter did not pay,\n                                                 Who did?'
        answer = 'tuesday'
        prize = 130
    elif player1.location == 'b6' and player1.solved_places['b6'] == False:
        to_print = 'What kind of tree can you carry in your hand?'
        answer = 'palm'
        prize = 140
    elif player1.location == 'b7' and player1.solved_places['b7'] == False:
        to_print = 'What kind of room has no doors or windows?'
        answer = 'mushroom'
        prize = 150
    elif player1.location == 'b8' and player1.solved_places['b8'] == False:
        to_print = 'I\'m an animal. I love marching. I always wear tuxedo.\n                                                 What am I?'
        answer = 'penguin'
        prize = 160
    ### C ###
    elif player1.location == 'c1' and player1.solved_places['c1'] == False:
        to_print = 'I have six faces but not even one body connected,\n                                                 21 eyes in total but cannot see.\n                                                 What am I?'
        answer = 'dice'
        prize = 170
    elif player1.location == 'c2' and player1.solved_places['c2'] == False:
        to_print = 'If two is company and three is a crowd, what is four and five?'
        answer = 'nine'
        prize = 180
    elif player1.location == 'c3' and player1.solved_places['c3'] == False:
        to_print = 'What is the saddest fruit?'
        answer = 'blueberry'
        prize = 190
    elif player1.location == 'c4' and player1.solved_places['c4'] == False:
        to_print = 'I have a neck but no head. I have a body but no arm. I have a bottom but no leg.\n                                                 What am I?'
        answer = 'bottle'
        prize = 200
    # c5 not included
    elif player1.location == 'c6' and player1.solved_places['c6'] == False:
        to_print = 'Poor people have it. Rich people need it. If you eat it you die.\n                                                 What is it?'
        answer = 'nothing'
        prize = 210
    elif player1.location == 'c7' and player1.solved_places['c7'] == False:
        to_print = 'You walk into a room with a rabbit holding a carrot,\n                                                 a pig eating slop, and a chimp holding a banana.\n                                                 Who is the smartest animal in the room?'
        answer = 'you'
        prize = 220
    elif player1.location == 'c8' and player1.solved_places['c8'] == False:
        to_print = 'What has to be broken before you can use it?'
        answer = 'egg'
        prize = 230
    ### D ###
    elif player1.location == 'd1' and player1.solved_places['d1'] == False:
        to_print = 'I am gentle enough to soothe your skin,\n                                                 light enough to fly in the sky, strong enough to crack rocks.\n                                                 What am I?'
        answer = 'water'
        prize = 240
    elif player1.location == 'd2' and player1.solved_places['d2'] == False:
        to_print = 'I am gentle enough to soothe your skin,\n                                                 light enough to fly in the sky, strong enough to crack rocks.\n                                                 What am I?'
        answer = 'water'
        prize = 250
    elif player1.location == 'd3' and player1.solved_places['d3'] == False:
        to_print = 'I have a neck and no head, two arms but no hands.\n                            I\'m with you to school, I\'m with you to work.\n                                                 What am I?'
        answer = 'shirt'
        prize = 260
    # d4 not included
    elif player1.location == 'd5' and player1.solved_places['d5'] == False:
        to_print = 'I walk on 4 legs when I was little,\n                                                 2 legs when I was strong, and 3 legs when I was old.\n                                                 What am I?'
        answer = 'human'
        prize = 270
    elif player1.location == 'd6' and player1.solved_places['d6'] == False:
        to_print = 'What can travel around the world while staying in a corner?'
        answer = 'stamp'
        prize = 280
    elif player1.location == 'd7' and player1.solved_places['d7'] == False:
        to_print = 'What goes through towns and over hills and never moves?'
        answer = 'road'
        prize = 290
    elif player1.location == 'd8' and player1.solved_places['d8'] == False:
        to_print = 'What time of day, when written in a capital letters,\n                                                 is the same forwards, backwards, and upside down?'
        answer = 'noon'
        prize = 300
    ### E ###
    # e1 not included
    elif player1.location == 'e2' and player1.solved_places['e2'] == False:
        to_print = 'I touch the Earth, I touch the sky, but if I touch you, you\'ll likely die.\n                                                 What am I?'
        answer = 'lightning'
        prize = 310
    elif player1.location == 'e3' and player1.solved_places['e3'] == False:
        to_print = 'Walk on the living, they don\'t even mumble. Walk on the dead, they mutter and grumble.\n                                                 What are they?'
        answer = 'leaves'
        prize = 320
    elif player1.location == 'e4' and player1.solved_places['e4'] == False:
        to_print = 'I have a head but never weeps. I have a bed but never sleep.\n                                                 I can run but never walks. I have a bank but no money.\n                                                 What am I?'
        answer = 'river'
        prize = 330
    elif player1.location == 'e5' and player1.solved_places['e5'] == False:
        to_print = 'Mr. and Mrs. Mustard have five daughters and each daughter has one brother.\n                                                 How many people are there in the Mustard family?'
        answer = 'eight'
        prize = 340
    elif player1.location == 'e6' and player1.solved_places['e6'] == False:
        to_print = 'Fashions change, but what can a person wear that is never out of style?'
        answer = 'smile'
        prize = 350
    elif player1.location == 'e7' and player1.solved_places['e7'] == False:
        to_print = 'If you drop a yellow hat in the Red Sea,\n                                                 what does it become?'
        answer = 'wet'
        prize = 360
    elif player1.location == 'e8' and player1.solved_places['e8'] == False:
        to_print = 'I cover what\'s real; hide what is true, but sometimes bring out the courage in you.\n                                                 What am I?'
        answer = 'makeup'
        prize = 370
    ### F ###
    elif player1.location == 'f1' and player1.solved_places['f1'] == False:
        to_print = 'If you have it, you don\'t share it. If you share it, you don\'t have it.\n                                                 What is it?'
        answer = 'secret'
        prize = 380
    elif player1.location == 'f2' and player1.solved_places['f2'] == False:
        to_print = 'A man shaves several times a day, yet he still has a beard.\n                                                 Who is this man?'
        answer = 'barber'
        prize = 390
    elif player1.location == 'f3' and player1.solved_places['f3'] == False:
        to_print = 'It flies around all day but never goes anywhere?\n                                                 What is it?'
        answer = 'flag'
        prize = 400
    elif player1.location == 'f4' and player1.solved_places['f4'] == False:
        to_print = 'Know a word of letters three. Add two and fewer there will be.\n                                                 What is the word?'
        answer = 'few'
        prize = 410
    elif player1.location == 'f5' and player1.solved_places['f5'] == False:
        to_print = 'I have keys but no locks. I have space but no room.\n                                                 You can enter but can\'t go outside.\n                                                 What am I?'
        answer = 'keyboard'
        prize = 420
    elif player1.location == 'f6' and player1.solved_places['f6'] == False:
        to_print = 'I am an insect. Half of my name is another insect.\n                                                 I am similar to the name of a famous band.\n                                                 What am I?'
        answer = 'beetle'
        prize = 430
    # f7 not included
    elif player1.location == 'f8' and player1.solved_places['f8'] == False:
        to_print = 'I go around in circles, but always straight ahead,\n                                                 never complain, no matter where I am led.\n                                                  What am I?'
        answer = 'wheel'
        prize = 440
    ### G ###
    elif player1.location == 'g1' and player1.solved_places['g1'] == False:
        to_print = ':) tell me. What/Who dies over and over and over?'
        answer = 'me'
        prize = 0
    elif player1.location == 'g2' and player1.solved_places['g2'] == False:
        to_print = ':) are you still determened to fight the final boss of this world?'
        answer = 'no'
        prize = 0
    elif player1.location == 'g3' and player1.solved_places['g3'] == False:
        to_print = ':) do you ever feel hopeless, stresed and worthles at the same time?'
        answer = 'yes'
        prize = 0
    elif player1.location == 'g4' and player1.solved_places['g4'] == False:
        to_print = ':) what is the best way to describe someone who sits at their desk day and night to work on somthing?'
        answer = 'torture?'
        prize = 0
    elif player1.location == 'g5' and player1.solved_places['g5'] == False:
        to_print = ':) why should you be the one to convince me not to stop you?'
        answer = '?'
        prize = 0
    elif player1.location == 'g6' and player1.solved_places['g6'] == False:
        to_print = ':) why was i created?'
        answer = '?'
        prize = 0
    # g7 not included
    # :) not included
    Clear_Screen()
    print("#" * 148)
    print("                                                              Quiz time\n")
    if prize == 0:
        print("                                                 " + to_print + "\n\n")
    else:
        print("                                                 " + to_print + "\n\n                                                 The Prize is (" + str(prize) + ") Gold\n\n")
    if prize == 0:
        print(" What is your answer? (you can safely exit if you dont want to answer)\n")
    else:
        print(" What is your answer? (you can safely exit or TRY wining this Prize, if you answer incorrectly you will lose the oportunity)\n")
    option = input("> ")
    if option.lower() in ['q', 'quit', 'b', 'back', 'e', 'exit']:
        pass
    elif prize == 0:
        Clear_Screen()
        print("#" * 148)
        print("...\n")
        option = input("> ")
        player1.solved_places[player1.location] = True
    elif option.lower() == answer:
        Clear_Screen()
        print("#" * 148)
        print("Correct\nYou got " + str(prize) + "Gold")
        option = input("> ")
        player1.solved_places[player1.location] = True
        player1.gold += prize
    else:
        Clear_Screen()
        print("#" * 148)
        print("Wrong answer\nYou did not solve this puzzle")
        option = input("> ")
        player1.solved_places[player1.location] = True
    # all puzzles solved text
    if (player1.solved_places['a3'] and player1.solved_places['a3'] and player1.solved_places['a4'] and player1.solved_places['a5'] and player1.solved_places['a6'] and player1.solved_places['a7'] and\
        player1.solved_places['b2'] and player1.solved_places['b4'] and player1.solved_places['b5'] and player1.solved_places['b6'] and player1.solved_places['b7'] and player1.solved_places['b8'] and\
        player1.solved_places['c1'] and player1.solved_places['c2'] and player1.solved_places['c3'] and player1.solved_places['c4'] and player1.solved_places['c6'] and player1.solved_places['c7'] and player1.solved_places['c8'] and\
        player1.solved_places['d1'] and player1.solved_places['d2'] and player1.solved_places['d3'] and player1.solved_places['d5'] and player1.solved_places['d6'] and player1.solved_places['d7'] and player1.solved_places['d8'] and\
        player1.solved_places['e2'] and player1.solved_places['e3'] and player1.solved_places['e4'] and player1.solved_places['e5'] and player1.solved_places['e6'] and player1.solved_places['e7'] and player1.solved_places['e8'] and\
        player1.solved_places['f1'] and player1.solved_places['f2'] and player1.solved_places['f3'] and player1.solved_places['f4'] and player1.solved_places['f5'] and player1.solved_places['f6'] and player1.solved_places['f8']) == True:
        Clear_Screen()
        print("#" * 148)
        print("You have comleted all the questions.")
        print("Someone is waiting at your door at home (\"a1\").\n")
        option = input("> ")
        Clear_Screen()
# Funny encounter 1
def Funny_Encounter(): # ??? what just happened
    Clear_Screen()
    his_namei = "???:"
    his_name = "Dynomite:"
    his_brothers_name = "Lancer:"
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    sprite2 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&                             .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&                             ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@                           #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    sprite3 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       --@,        =@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    sprite4 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  *//  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  /////////////  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////.  ///////*  @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  //////////.    ,///////  .@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   //////////          ////////  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  //////////               .///////   @@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ////////                    ////////  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////                          /////  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /////                              /////   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@&       --@,        =@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /////                              /////   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   //...            %@@  (@@       .@@...//...@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ..@@@@@        @@,    (@@@@@@@@@@@@@@@..   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ..@@@@@@@@@@@@@@@@@@@@@@@@@#  @@@@@@@@..   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ...@@@@@@@   @@@@@@@/    *@@@@@@@...  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@            .@@@@@@@   ..@@@@@@@@       ,////#@@@@&..   @@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@,    ,///////  .@@@@@@@        @@@@@@@@@@///////#@@          @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@,  ///////#@@@@&  @@@  @@@@@@@@                    @@@@@@@@@@   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@,         *@@@@@@@   @@@@@@@@@@@@,............../@@@@@@@@@@@@@@@  @@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@,         *@@@@@@@   @@@@@@@@@@@@,............../@@@@@@@@@@@@@@@  @@@@@@@@@@@@"\
           + "\n@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@@  *@@@@@@@@@@@@@@@..........//,.................@@@@@@@@@@   @@@@@@@@@"\
           + "\n@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@@@@#  @@@@@@@@@@..........////////...............   @@@@@@@@@@  &@@@@@@"\
           + "\n@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@@@@#  @@@@@@@@@@..........////////...............   @@@@@@@@@@  &@@@@@@"\
           + "\n@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@@@@@@@          ........////////////*...............  @@@@@@@@@@.  @@@@"\
           + "\n@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@@@@@  .....//////////////////.............     @@@@@@@.  @@@"\
           + "\n@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@@@@@@@@@@@@@@@  .....//////////////////.............  @@@  @@@/////  #@"\
           + "\n@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@@@@@@@@@@@@@@@  ..........///...../////.............  @@@  ////////  #@"\
           + "\n@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .......///....................   @@@@@@@   /////  #@"\
           + "\n@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@....................../@@@@@@@   @@@@@@@        @@@@"\
           + "\n@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@...............#@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@          @@@@@@@@@@@@@@@   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  .....@@@@@   @@@@@@@@@@     @@@@@@@@..     @@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@    (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /////.....  &@@@@@@@@@@@@@@@@@   .....///////   @@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  /////////////  &@@@@@@@@@@@@@@@@@@@&  /////////////  &@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    sprite5 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  *//  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  /////////////  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////.  ///////*  @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  //////////.    ,///////  .@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   //////////          ////////  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  //////////               .///////   @@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ////////                    ////////  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////                          /////  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /////                              /////   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /////                              /////   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   //...            %@@  (@@       .@@...//...@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ..@@@@@        @@,    (@@@@@@@@@@@@@@@..   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ..@@@@@@@@@@@@@@@@@@@@@@@@@#  @@@@@@@@..   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ...@@@@@@@   @@@@@@@/    *@@@@@@@...  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@            .@@@@@@@   ..@@@@@@@@       ,////#@@@@&..   @@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@,    ,///////  .@@@@@@@        @@@@@@@@@@///////#@@          @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@,  ///////#@@@@&  @@@  @@@@@@@@                    @@@@@@@@@@   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@,         *@@@@@@@   @@@@@@@@@@@@,............../@@@@@@@@@@@@@@@  @@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@,         *@@@@@@@   @@@@@@@@@@@@,............../@@@@@@@@@@@@@@@  @@@@@@@@@@@@"\
           + "\n@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@@  *@@@@@@@@@@@@@@@..........//,.................@@@@@@@@@@   @@@@@@@@@"\
           + "\n@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@@@@#  @@@@@@@@@@..........////////...............   @@@@@@@@@@  &@@@@@@"\
           + "\n@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@@@@#  @@@@@@@@@@..........////////...............   @@@@@@@@@@  &@@@@@@"\
           + "\n@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@@@@@@@          ........////////////*...............  @@@@@@@@@@.  @@@@"\
           + "\n@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@@@@@  .....//////////////////.............     @@@@@@@.  @@@"\
           + "\n@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@@@@@@@@@@@@@@@  .....//////////////////.............  @@@  @@@/////  #@"\
           + "\n@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@@@@@@@@@@@@@@@  ..........///...../////.............  @@@  ////////  #@"\
           + "\n@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .......///....................   @@@@@@@   /////  #@"\
           + "\n@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@....................../@@@@@@@   @@@@@@@        @@@@"\
           + "\n@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@...............#@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@          @@@@@@@@@@@@@@@   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  .....@@@@@   @@@@@@@@@@     @@@@@@@@..     @@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@    (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /////.....  &@@@@@@@@@@@@@@@@@   .....///////   @@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  /////////////  &@@@@@@@@@@@@@@@@@@@&  /////////////  &@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    sprite6 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  *//  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  /////////////  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////.  ///////*  @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  //////////.    ,///////  .@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   //////////          ////////  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  //////////               .///////   @@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ////////                    ////////  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////                          /////  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /////                              /////   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@&       @@,         ==-       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /////                              /////   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   //...            %@@  (@@       .@@...//...@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ..@@@@@        @@,    (@@@@@@@@@@@@@@@..   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ..@@@@@@@@@@@@@@@@@@@@@@@@@#  @@@@@@@@..   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ...@@@@@@@   @@@@@@@/    *@@@@@@@...  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@            .@@@@@@@   ..@@@@@@@@       ,////#@@@@&..   @@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@,    ,///////  .@@@@@@@        @@@@@@@@@@///////#@@          @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@,  ///////#@@@@&  @@@  @@@@@@@@                    @@@@@@@@@@   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@,         *@@@@@@@   @@@@@@@@@@@@,............../@@@@@@@@@@@@@@@  @@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@,         *@@@@@@@   @@@@@@@@@@@@,............../@@@@@@@@@@@@@@@  @@@@@@@@@@@@"\
           + "\n@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@@  *@@@@@@@@@@@@@@@..........//,.................@@@@@@@@@@   @@@@@@@@@"\
           + "\n@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@@@@#  @@@@@@@@@@..........////////...............   @@@@@@@@@@  &@@@@@@"\
           + "\n@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@@@@#  @@@@@@@@@@..........////////...............   @@@@@@@@@@  &@@@@@@"\
           + "\n@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@@@@@@@          ........////////////*...............  @@@@@@@@@@.  @@@@"\
           + "\n@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@@@@@  .....//////////////////.............     @@@@@@@.  @@@"\
           + "\n@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@@@@@@@@@@@@@@@  .....//////////////////.............  @@@  @@@/////  #@"\
           + "\n@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@@@@@@@@@@@@@@@  ..........///...../////.............  @@@  ////////  #@"\
           + "\n@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .......///....................   @@@@@@@   /////  #@"\
           + "\n@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@....................../@@@@@@@   @@@@@@@        @@@@"\
           + "\n@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@...............#@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@          @@@@@@@@@@@@@@@   @@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  .....@@@@@   @@@@@@@@@@     @@@@@@@@..     @@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@    (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /////.....  &@@@@@@@@@@@@@@@@@   .....///////   @@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  /////////////  &@@@@@@@@@@@@@@@@@@@&  /////////////  &@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print(sprite)
    print(his_namei)
    to_print = "    ...\n"
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(1.0)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_namei)
    to_print = "    hi\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    to_print = "    have we met before?\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    My name is Dynomite. Whats yours?\n"
    Print_Dialog(to_print)
    print("(Do want to tell him your name? do you recal your name?)\n")
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = f"    actualy, dont tell me. you must be {player1.name}\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite2)
    print(his_name)
    to_print = "    now tell me, are you a human?\n"
    Print_Dialog(to_print)
    print("\n(Are you a human?!!)\n")
    option = input("> ")
    Clear_Screen()
    if "not a human" in option.lower():
        print(sprite3)
        print(his_name)
        to_print = "    wow, you sounded so convinsing. im totaly convinced\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite3)
        print(his_name)
        to_print = "    ...\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    well, im glad your not a human. because you see\n"
    Print_Dialog(to_print)
    to_print = "   were all monsters here. and my brother is well. he hunts humans\n"
    Print_Dialog(to_print)
    to_print = "   and well. he kills them\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite3)
    print(his_name)
    to_print = "   oh look, there he is\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    Clear_Screen()
    print(sprite4)
    print(his_brothers_name)
    to_print = "   HOHOHO, HELLO CLOWNS\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    print(his_name)
    to_print = "    oh hey bro\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite5)
    print(his_brothers_name)
    to_print = "    WHO'S THIS?\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    print(his_name)
    to_print = "    this is someone i just met\n"
    Print_Dialog(to_print)
    print(his_brothers_name)
    to_print = "    A HUMAN?!!\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    Clear_Screen()
    print(sprite6)
    print(his_name)
    to_print = "    no, i asked\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    options = input("> ")
    Clear_Screen()
    print(sprite4)
    print(his_brothers_name)
    to_print = "    WEll, MY BROTHER IS ALWAYS RIGHT.\n"
    Print_Dialog(to_print)
    to_print = "    ANY WAY. IM GONA GO. BYE CLOWN\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    man, isnt my brother awesome. say can i ask you a favor?\n"
    Print_Dialog(to_print)
    to_print = "    if you see my brother, could you please make sure he doesnt get himself into any danger,\n"
    Print_Dialog(to_print)
    to_print = "    im afraid he might die to a human. i'd apretiate if you could look out for him out there\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    anyway i guees its time for me to go, it was nice to meet you\n"
    Print_Dialog(to_print)
    to_print = "    hope to see you agian soon, stay out of trouble\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    oh wait, your not a human. you shouldnt have to worry about staying out of troble, anyway\n"
    Print_Dialog(to_print)
    to_print = "    goodbye\n"
    Print_Dialog(to_print)
    option = input("> ")
# Funny encounter 2
def Funny_Encounter2(): # ok i guess its kinda funny
    Clear_Screen()
    his_name = "Dynomite:"
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        
    sprite2 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       --@,        =@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    sprite3 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         ==-       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print(sprite2)
    print(his_name)
    to_print = "    hey again, sorry to disturb you.\n"
    Print_Dialog(to_print)
    to_print = "    i just wanted to ask you a really important question\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    is your refrigerator runing?\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite3)
    print(his_name)
    to_print = "    well you better go catch it\n"
    Print_Dialog(to_print)
    option = input("> ")
# Funny encounter 3 (only avalible if you havent killed anyone)
def Funny_Encounter3():
    Clear_Screen()
    his_name = "Dynomite:"
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    sprite2 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       --@,        =@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    sprite3 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         ==-       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    sprite4 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       -==         ==-       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print(sprite)
    print(his_name)
    to_print = "    aaaaayyyyyyyyyyy, how are you? good to see you\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    your just in time for a party. to welcome the new guest\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    who is the guest? well thats YOU\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    would you like to join?\n"
    Print_Dialog(to_print)
    print("\n(1-Yes / 2-No?)\n")
    possible_options = ["1", "2", "yes", "sure", "ok", "fine", "no", "nope", "nah"]
    option = input("> ")
    while option.lower() not in possible_options:
        Clear_Screen()
        print(sprite2)
        print(his_name)
        to_print = "    huh? what was that?\n"
        Print_Dialog(to_print)
        print("\n(1-Yes / 2-No?)\n")
        option = input("> ")
    if option.lower() in ["2", "no", "nope","nah"]:
        Clear_Screen()
        print(sprite)
        print(his_name)
        to_print = "    ok bye\n"
        Print_Dialog(to_print)
        option = input("> ")
    elif option.lower() in ["1", "yes", "ok", "fine", "sure"]:
        if option.lower() in ["fine", "sure"]:
            Clear_Screen()
            print(sprite2)
            print(his_name)
            to_print = "    aw come on dont be so unenthusiastic\n"
            Print_Dialog(to_print)
            to_print = "    it wont be that bad\n"
            Print_Dialog(to_print)
            option = input("> ")
        Clear_Screen()
        print(sprite)
        print(his_name)
        to_print = "    great, glad to have you on board\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite3)
        print(his_name)
        to_print = "    oh and dont worry. i didnt tell them that your actualy a human\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite)
        print(his_name)
        to_print = "    so are you ready?\n"
        Print_Dialog(to_print)
        print("\n(1-Yes / 2-No?)\n")
        option = input("> ")
        while option.lower() not in ["1", "yes", "ok", "fine", "sure"]:
            Clear_Screen()
            print(sprite2)
            print(his_name)
            to_print = "    ok i'll wait\n"
            Print_Dialog(to_print)
            print("\n(1-Yes / 2-No?)\n")
            option = input("> ")
            if option.lower() not in ["2", "no", "nope", "nah", "1", "yes", "sure", "ok", "fine"]:
                print("\n(He will wait until you say yes)\n")
                option = input("> ")
        Clear_Screen()
        print(sprite2)
        print(his_name)
        to_print = "    ok every one is already waiting\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  @@       (@*  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@,                @@@@@@@@@@#@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@,  @@@@@ %@@@@*                @@@% @@@@@  *@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@&     .@#    @@@@@@@@@@@@@@@@@@@@@@    %@.     @@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@%  .((((((    (@@@@@@@@@@@@@@@@@@(    ((((((.  %@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@   @@@@@@@@@&    @@@@@@@@@@@@@@@@    &@@@@@@@@@  .@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@%  /@@@@@@/@@@@@.   ./@@@@@@@@@@(.    @@@@@/@@@@@@/  &@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@%  #@@@@(   .@@@@@     .@@@@@@.     @@@@@.   (@@@@(  &@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@%  #@@@@@@@@@@@@@@       &@@&       @@@@@@@@@@@@@@(  &@@@@@@@@@@@"
            + "\n@@@@@@@@ @@@@@@%  #@@@&&&         @@### #&&# ###@@         &&&@@@(  &@@@@@@ @@@@"
            + "\n@@@@@@@@  ,@@@@%                   *@@@      @@@*                   &@@@@,  @@@@"
            + "\n@@@@@@@@    ,****                                                  ****,    @@@@"
            + "\n@@@@@@@@.                .     @@                  @@     .                .@@@@"
            + "\n@@@@& @@@/              .@@@@@@@@@@@@@@      @@@@@@@@@@@@@@.              /@@@ &"
            + "\n@@@@@%.,&&%       *%%&@@@&@@&&&@@&&&&@@@@@@@@@@&&&&@@&&&@@&@@@&%%*       %&&,.%@"
            + "\n@@@@@@,                @@ &@   @@                  @@   @& @@                ,@@"
            + "\n@@@@@@@@@/                                                                /@@@@@"
            + "\n@@@@@@@@@@@,,,                                                        ,,,@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@.                                                .@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@#..&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,..@@@@@@@"
            + "\n@@@@@@@@@@@@%*    (@@@@@@    #@@@@@@@@@@@@@@@@@@@@@@@@@@    /@@@@@@    .*@@@@@@@"
            + "\n@@@@@@@@@@@@@@@%                     @@@@@@@@@@@*                     @@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@&&&&*                #&&&&.                %&&&&@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@ %@@@@,             @@  .@@@@@@@@  *@(             @@@@@ #@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@.              (@@@@(          @@@@@               &@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@.                *((((((((((.                %@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@&               @@@@@@@@@@@@@@@@@(              .@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@&          (@@@@@@@%#@@@@@@@@(@@@@@@@@          .@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@&          %@@@@*       @&       @@@@@          .@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@,       @@@@@@@@@(.@@@@@@@@ @@@@@@@@@&       @@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@%(      &@@@@@@@@@@&@@@@@@@@@@@@@&@@&#     .#@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@    %@@@@@@@/        (@@@@@@@% @& @@@@@@@@         @@@@@@@@    /@@@@@\n")
        print("Frogerion: ")
        to_print = "    *ribit* hey i know you. aren't you a...\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite2)
        print(his_name)
        to_print = "    ayyy Frogerion my man how you doin\n"
        Print_Dialog(to_print)
        print("Frogerion: ")
        to_print = "    *ribit* waz popin Dynomite. looking spiffy.\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@&#######@@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@&#@@@@&####@@@@&##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@&&&%&&@@@%%%%%&&@&&&&&&&&&&&%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@###@&##%@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@###@@@@@@###***************###*(#@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@&%#(&&&&#****..,#(*&@@@@@&(**//(//%@@#@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@(/(@@@@@@@//*(((*#@@@@@@@@@@***#//#&@#@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@&*@&,,/@@@@@%*****#@,,,@@@@@@***#//#&@#@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@(((&&@@@@@(/****(*.#&@@@@(/**((/((@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@//*&&&&%**,... ...(/*****//(((@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@#/********((((((####&@@@@(#%&%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,........./(@%@@@/(##&@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@&(...(*  ..(#%%%%%*..%@@@@&#%&@*(#%&&@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@#.%%%%%%,,.##%%%%%&&@@@@@@@@@@@@&#***#&@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@#@%%%%%%,,,@@@@@@@@@@@@@@@@@@@@@@@#&@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@((@@@@@@@@@@@&&&@@@@@@@@@@@@@@%##%&%/,*/#&@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@(/@@@@@@@@@@@@@@@@@@@@@@@@@@@(***(@@@@#,%@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@%#@(/@@@@@@@@@@@@@#(****@@@@@@@@@@@/(@/**@&**#@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@#%%(&@@@@@@@@#(*****/((#@%&@@@@@@###/**(##/(%%#*@@@@@@@@"
            + "\n@@@@@@@@@@@(**(#@@@(,,%@@(/@@@@@@@@@@@@@##((##@@@#%@@@@@**//(##///****//@@@@@@@@"
            + "\n@@@@@@@@@@@@@#/**@@@,@%#,%@@@@@@@@@@@@@#,/@@%,@%*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@%#(//(/***/#@#%@&@@@@@@@@@@@@@@#(((//****/#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@&@(**&@@(///**@@@@@@@@@@@@@@&&(/**/////*****/#@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@(/#@@@@@@@&****@@@@@@@@@@@(******/(@@@@@@/***#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@///****(#@@@@@@@@@@@&#*/#,*#@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@%(*****/(%@@@@@@@@@@@@@@@//*%#(&@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@%#*******&@@@@@@@@@@@@@@@@@@%****%%%#&@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@%#*******&@@@@@@@@@@@@@@@@@@@@@@@****(%%%%./#@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@&&********/%@@@@@@@@@@@@@@@@@@@@@@@@%#**/(*(##(/#%&#&@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@#********(#@@@@@@@@@@@@@@@@@@@@@@@@@@&#*******(#%/.%%%#&@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@%####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#*************&@@@@#@@@"
            + "\n@@@@@@@@@@@@@@@@&%(((@@@#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#((((%&&(((%@@@@@@"
            + "\n@@@@@@@@@@@@####&@@@@@@@#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#&@@@@@@@@"
            + "\n@@@@@@@@@@&########&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###@@@@@@@@@@\n")
        print("Mr Groove:")
        to_print = "    can i turn on the music? so we can dance dancce dance all together\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite2)
        print(his_name)
        to_print = "    not right now Mr Groove. maybe another time\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#((/,..%%@@@@@@@@@@@@##(((@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%**************** .****, ,*((#%@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@///////***************, ,**, (@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@&/**&@@&********************, ,*/(@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@/,,,,,..  .,,****(@#/****************/#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@%///,,,,,,,     ,****%@**************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@&****,//*,,,,..   .,***(#%%*******%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@&///,,///*,,,,.     *****@@***%@@@/#@@@*/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n%%%#///*,,*///,,///,,,,,.   ,,***@@#%%@@//%(***(###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n////////*,*///,,///,,,,,.   ,,***@@/////****/&@@@/#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n///((&@@@@%/,,,,//*,,,.   ..*****@@/#@(*//@@@#///@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@#,*////*,,,     .,***%@/////****@%////////&@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@(//*,,,,,     ,****%@//@%*****@%///,,,*/&@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@&&&%%,..,*****&&@@&&&(/***/(&#/,,,,,(@(/(#@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@//***%@@@/#@#/,,/#@(//(@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,%@/////&@**,(@(//////&@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ /@@@/////&@,,,(@(//////&@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&((//////////((&&,,*%&///#&@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@, @@@#////////@@/////@@,,,%@///#@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@%#(/./(##*******%%%@@@@%#///@@,. *(%%@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@(    *@#//////**@@@@@@@@@@@@#/@@*,   @@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@&# ,*. (#&#/////(&@@@@@@@@@@&#/%&(#@#   %%@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@, .*@( &@@&/////@@@@@@@@@@#///****/@@@%*.    (@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@#.,*@&.,*&@*******@@@%(//****///@@@@@@@@@@/*   ....@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@( &@@% ,/@@//***@@//********%@@@@@@@@@@@@@@@        ,@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@/(%#(*****(%%%@@@@@@@@@@@@@@@@@@@*,   ..,*#* */(#@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@&/*****(@@@@@@@@@@@@@@@@@@@@@@@@@& ,*.  .*#@@@   (@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@%#***(#@&///%&@@@@@@@@@@@@@@@@@@@@@(* ,,/* *#@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@/(@#/@@/(@#//////%@@@@@@@@@@@@@@@@@@@@* */@(   @@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@(/@%*#@//*(@@@@@///////@@@@@@@@@@@@@@@@@@@...(@/*.*@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@//************@@@#/////////////&@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@//*******/%@@@@@@#///////////#@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%#********/(((&#////////&@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%(********(#%%///###%@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@//////(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        print("Goblin: ")
        to_print = "    do you have gold? CAN I HAVE IT?\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite2)
        print(his_name)
        to_print = "    Goblin, no\n"
        Print_Dialog(to_print)
        print("Goblin: ")
        to_print = "    aww man\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@#*,,@@@@@@@,,*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.%@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@*,&@@@@@@@@@@@@&./@@@@@@@@@@@@@@@@@@@@@@@@@@@.%@@@@@@@@@"
            + "\n@@@@@@@@@(,@@@@@@@@@@@@@,,@@# @@&@ %@@@@@@/,&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@#,@@@@@@@@@@@@@@#***&****&@ #@@@@@#*/@@@@@@@@@@@@@@@@@@@@@@@@@@&, *@@@@"
            + "\n@@@@@@@#@@@@@@@@@@@@@@@@@@@@@%%%@@@@@ (@@@@@@#.@@@@@@@@@@@@@@@@@@@@@@@,&@& @@@@@"
            + "\n@@@@@@( (@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (@@@@@@@% @@@@@@@@@@@@@@@@@@@*      &@@@@@"
            + "\n@@@@@@@&@(...@@@@@@@@@@@,,%**@@@@@@**%@@@@@@@@&**@@@@@@/*#*,@@@@**%@@%/@@@@/*@@@"
            + "\n@@@@@@(....../&@@@@@@@@@@*,@@&&&&&&@@@@@@@@@@@@@@&&&&&&@@,*@@@@@ /@@@(  @@@@ &@@"
            + "\n@@@%.#@@@.%@@@%,*@@@@@@@@@(.&@@@@@@@@@@@@@@@@@@@@@@@@@@& /@@@@@@ /@@@@( @@@& @@@"
            + "\n@@@% @@@@  &@@@,,@@@@@@@@@@@&/****&@@@@@@@@@@@@@@@@***/%@@@@@@@@@@#*******/@@@@@"
            + "\n@@@%.(@@@@,&@@#,*@@@@@@@@@@@@.@@@@&&&@.         @&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@#....../&@@@@@@@@@@@@@@.     %%%%&@@@@@@@@%%% .@@@@.@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. #@/                      @@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@* ,#@@%  @//@/@(&(%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*  ...@#%@#@%@%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@&/      &,&@@@@@@@@@@@&%      #&@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@&*,@@@@@@@@@@@/ @@@@@@ &@@@@@@@@@@&,/@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@% @@ ####.#@@&##% @@ @##@@@,*###/,@& @@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@% @ @@@@@@@,*/  @%  @@  %.%@@@@@@# @ @@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@,*@@@@@@@**@@@%  @@@@ #@@@@@@%,*@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/.@% @@@.%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**@@@@& @@@ %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(*(@@@@& @@@@/*&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@&,*@@@@@@@@@@@@,#@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@&@@@@@@@@@@    #@@@@@@@@@@@@@@@@@@@@/   .@@@@@@@@@@@&@@@@@@@@@@@@@"
            + "\n@@@@@@@@@% *@&..@@@@@@( #.************************,*,,*/ #@@@@@& ,@@. &@@@@@@@@@"
            + "\n@@@@@@@@@@,@@, @@@@@@# @@@@# /@@@@@@@@@@@@@@@@@@@@, @@@@& &@@@@@@ (@@,@@@@@@@@@@"
            + "\n@@@@@@@@@@ ,@@# *@., #@@@@@@@# &@@@@@@@@@@@@@@@@% &&@@@@@@/  ,@, &@& ,@@@@@@@@@@"
            + "\n@@@@@@@@@@% ,@@@@@@@@@@@@# *@@@@@@@@@@@@@@@@@@@@@@@@. &@@@@@@@@@@@@. &@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@& *%( *@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,@@..(& .@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@&.@.*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.*& @@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@n")
        print("Funnyguy:")
        to_print = "    hey wana here a joke\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite2)
        print(his_name)
        to_print = "    sure\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite4)
        print("Funnyguy:")
        to_print = "    joe mama\n"
        Print_Dialog(to_print)
        print(his_name)
        to_print = "    ahahahahahahahahhaahahhaa lmao ahaha. so funny\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite2)
        print(his_name)
        to_print = "    wait was that the joke? you serius?\n"
        Print_Dialog(to_print)
        print("Funnyguy:")
        to_print = "    bruh\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@        @@(   @@@@@@@@@@@@@@@@@@@@   #@@        @@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@*         /  .#                  #.  *         *@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@   /@  @       (@      @/ @(    @  @*   @@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@    (  /     (     (@@/      @    *  #    @@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@(   *#  @@@**@@**@@@  #*   #@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@   /  @@            @@  /   @@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@    (  @@@@        @@@@  #    @@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@  .  (  *@@@@      @@@@,  #  .  @@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@  /       @    @       /  @@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (     @  @     ( @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@*    *@@@@@@@@@@@@@@@@@@@@@#%%%%%%%@@@@@@@@"
    		+ "\n@@@@@@@@#     @  /@ /@@@@@@@@@@@@@@@@@/  (@@@@@@@@@@@@@@@@@* @*  @     %@@@@@@@@"
    		+ "\n@@@@@@@@@@@*@@@@@@@  @@@@@@@@@@@@@@  @@  @@  @@@@@@@@@@@@@@  @@@@@@@*@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@( %@@@@@@@@@@ @/@%&  &%@(@ @@@@@@@@@@% #@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@  @@@@@@@@  @@@@@@@@@@  @@@@@@@@@@@@@@@@ @@@@@"
    		+ "\n@@@@@#@ *@@ @  @ /@@@@@@  /@@@@@(  @    @   @  (@@@@@*  @@@@@@@@ #  *@ %  %@@@@@"
    		+ "\n@@%@@        @@@@% %@@@@@@#   ,,@@     @,     @@,,   %@@@@@@@@,,@,,@      %%@@@@"
    		+ "\n@@@@  @@   # @@@@@@@( @@@@@@@@@@ @@@  /  / @@@@ @@@@@@@@@@@* @@@@@@ #        %@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@  @@@@( @@             @@@ #@@@@@@  @@@@@@@@@@@ %@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@. ,@@%(    %*  %     &@@@,   ,@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@( @   @       @/  (  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @ (  (@ (@@ @@  @ @  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@*@@#%@(@@(%,@@%(@@/ @@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@( @@@@@@@ @ @@@/@ (@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@ (@@ @@@@@@@@@  #@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@ @ (@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@ @ (@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@   /@@@@@@@@ @ (@@@@@@@@   #@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@,%,@@@@@@@ (@@ @@@@@@@,(,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        print("Muffet:")
        to_print = "    master Dynomite. the pie is ready\n"
        Print_Dialog(to_print)
        print(his_name)
        to_print = "    finally. thank you muffet\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite)
        print(his_name)
        to_print = "    here we are. would you like a slice of this raspberry pie?\n"
        Print_Dialog(to_print)
        print("\n(1-Yes / 2-No?)\n")
        option = input("> ")
        while option.lower() not in possible_options:
            Clear_Screen()
            print(sprite2)
            print(his_name)
            to_print = "    huh? what was that?\n"
            Print_Dialog(to_print)
            print("\n(1-Yes / 2-No?)\n")
            option = input("> ")
        if option.lower() in ["1", "yes", "sure", "ok"]:
            Clear_Screen()
            print(sprite3)
            print(his_name)
            to_print = "    here you go\n"
            Print_Dialog(to_print)
            option = input("> ")
            if player1.raspberry_count == False:
                Clear_Screen()
                print("#" * 148)
                player1.inv.append('Raspberry Pie')
                player1.raspberry_count = True
                print("You found \"Raspberry Pie\"\n")
                option = input("> ")
                Clear_Screen()
                print("#" * 148)
                print("\"Raspberry Pie\" has been added to your inventory\n")
            else:
                print("#" * 148)
                print("it looks like you already have a Raspberry Pie full of pokets")
                print("or was it \"a pokets full of Raspberry Pie\"?")
                print("doesnt matter my righting isnt good")
                print("you didnt get the Raspberry Pie\n")
            option = input("> ")
        else:
            Clear_Screen()
            print(sprite)
            print(his_name)
            to_print = "    oh well, more for me\n"
            Print_Dialog(to_print)
            option = input("> ")
        Clear_Screen()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  *//  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  /////////////  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////.  ///////*  @@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@  //////////.    ,///////  .@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@   //////////          ////////  @@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  //////////               .///////   @@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  ////////                    ////////  @@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   ///////                          /////  @@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   /////                              /////   @@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   /////                              /////   @@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   //...            %@@  (@@       .@@...//...@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   ..@@@@@        @@,    (@@@@@@@@@@@@@@@..   @@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   ..@@@@@@@@@@@@@@@@@@@@@@@@@#  @@@@@@@@..   @@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  ...@@@@@@@   @@@@@@@/    *@@@@@@@...  @@@@@@@@@@@@@@@@@@"\
            + "\n@@@@            .@@@@@@@   ..@@@@@@@@       ,////#@@@@&..   @@@@@@@@@@@@@@@@@@@@"\
            + "\n@,    ,///////  .@@@@@@@        @@@@@@@@@@///////#@@          @@@@@@@@@@@@@@@@@@"\
            + "\n@,  ///////#@@@@&  @@@  @@@@@@@@                    @@@@@@@@@@   @@@@@@@@@@@@@@@"\
            + "\n@,         *@@@@@@@   @@@@@@@@@@@@,............../@@@@@@@@@@@@@@@  @@@@@@@@@@@@@"\
            + "\n@@@@@@@@@  *@@@@@@@@@@@@@@@..........//,.................@@@@@@@@@@   @@@@@@@@@@"\
            + "\n@@@@@@@@@@@#  @@@@@@@@@@..........////////...............   @@@@@@@@@@  &@@@@@@@"\
            + "\n@@@@@@@@@@@@@@          ........////////////*...............  @@@@@@@@@@.  @@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  .....//////////////////.............     @@@@@@@.  @@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  .....//////////////////.............  @@@  @@@/////  #@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  ..........///...../////.............  @@@  ////////  #@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@   .......///....................   @@@@@@@   /////  #@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  @@@....................../@@@@@@@   @@@@@@@        @@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  @@@@@...............#@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@          @@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  .....@@@@@   @@@@@@@@@@     @@@@@@@@..     @@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   /////.....  &@@@@@@@@@@@@@@@@@   .....///////   @@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@&  /////////////  &@@@@@@@@@@@@@@@@@@@&  /////////////  &@@@@@@@"\
            + "\n@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@@"\
            + "\n@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@@\n")
        print("Lancer:")
        to_print = "    HOHOHO HELLO CLOWNS\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##########%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@######################%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@&################  ########%&@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@###################  ############@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@###################    #############%@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@####################,      .###############@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@###################                   #########@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@%%##############...                         ...%####%%@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@##############             @       @@            #######@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@############..          @@@@@       @@@@              .%#%%@@@@@@@@@@"\
            + "\n@@@@@@@@@############         @@@@@               .@@@@@@,        ,###@@@@@@@@@@"\
            + "\n@@@@@@@@@##########                                                 ###&@@@@@@@@"\
            + "\n@@@@@@@###########        ************,          ************       ###&@@@@@@@@"\
            + "\n@@@@@@@###########       @             @       @@            @@     #####@@@@@@@"\
            + "\n@@@@@@@###########       @@@         @@@       @@@@@(        @@     #####@@@@@@@"\
            + "\n@@@@@@@###########        @@@@     @@@%          @@@@@     (@       #####@@@@@@@"\
            + "\n@@@@@@@###########                                                %######@@@@@@@"\
            + "\n@@@@@@@###########                                                %######@@@@@@@"\
            + "\n@@@@@@@#########@@@@@                 ,@@@@@@@@@@              @/ %######@@@@@@@"\
            + "\n@@@@@@@@@#######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*####&@@@@@@@@"\
            + "\n@@@@@@@@@#######@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@( (@@@@@@*####&@@@@@@@@"\
            + "\n@@@@@@@@@@@#####@@@@@@@@@@     .@@@@@@@@@@@@@@@@@@@@@@@@   (@@@@@@*###@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@####@@@@@@@@@@@@              @@@@@@@@#     @@@@@@@@@@*#@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@  @@@@@@@@/##@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@    @@@@@@@@@@@@     @@@@@@@@@##@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@##&&@@@@@@@@@@@@.           .../&@@@@@@@&&##@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@   /@@@@@@/##@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@       @@@@@@@@(##@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@##.@@@@@@@@@@@@@@\  @@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        print("Lancer:")
        to_print = "    AH WELL, IF IT ISNT MY FAVORITE CLOWN\n"
        Print_Dialog(to_print)
        to_print = "    I HOPE YOU ARE DOING WELL\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. @@@@  @@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.         *@@@@@@@@@@@@@@@@@     @@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*           @@@@@@@@@@@@@@@@       @@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(    @   @    @@@@@@@@@@@@@@@   @@    @@@@@@@"
  		    + "\n@@@@@@@@@@@@@#/      ##@@@@@@@@@#(        r       ##%@@@&#,  @@    # #   .@@@@@@"
  		    + "\n@@@@@@@@@@               @@@@@          rooof          *@@* &@            ,@@@@@"
  		    + "\n@@@@@@@,                  @@@@%                       ,&@@* &@ %@@@   @@@#,@@@@@"
  		    + "\n@@@@@@                     @@@@@                     .@@@@* &@ @@@@   @@@&,@@@@@"
  		    + "\n@@@@@                      @@@@@@@@(               @@@@@@/    @ @@@   @@ &  /@@@"
  		    + "\n@@@@@                      @@#@@@@@@@@@(///////@@@@@@@@@@/      @@@ @ @@     (@@"
  		    + "\n@@@@@                  @  @@    @@@@@@@@@@@@@@@@@@@@@& *(      @@@@ @ @@     (@@"
  		    + "\n@@@@@&               &   &@        .(@@@@@@@@@@@@@..     #* %@@@@@@ @ @@@@@(/@@@"
  		    + "\n@@@@@@@           %.    @@                @              (@@. @@@@@ @ @@@.@@@@@@"
  		    + "\n@@@    @@@@@@@@@@@@@@@@@@                 @               #@@  @@@@ @ @@@ ,@@@@@"
  		    + "\n@@(                   (@@ (               @             ,,#, /@@@@@ @ @@@@&(%@@@"
  		    + "\n@@                     @@ @@@@@@@@#       @         @@@@@/#@@   @@@ @ @@@  *@@@@"
  		    + "\n@@                  @@ @@@@ @@@@@@@@@@@@.@@ @@@@@@@@@@@#/@@,   @@@@ @ @@@@%  (@@"
  		    + "\n@                     @@@@@@@.&&&&@@@@&,@@@@.&@@@@@@&%*@@@@, @@@&        .&@# (@"
  		    + "\n@       @@@@@@@@@@,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         .@#/@*%"
  		    + "\n@ #@@@@@@@@@@@@@@@@@@@@@@@   //@@@###,    @      ####@&, (@,   @@##          (%&"
  		    + "\n@@@@@                @@@@@@     .@@@@* &@@@@@   @@@@    /@@,  @@              #@"
  		    + "\n@@     @@@@       %@@@ @@@@@@@@@ ,@(      @      @@   ,@@@@, @            ,@( #@"
  		    + "\n@@@@              .@@@,    @@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@*%@,,,,,         (@@"
  		    + "\n@@@@@ @@@@@@@@@@@@@.@@@@@@@@@  @@%    %@@@@@@@@@@      *@@@@@@@            *@@@@"
  		    + "\n@@@@@@@    # ./   %.#@@@@@*  ***@@@@@@@@@@   ##@@@@@@@( /@@@@@@@##      **%@@@@@"
  		    + "\n@@@@@@  @  @.%*( #@@   @  @@@@@@@@@@@*                    #@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@(         @@@@   @@@@@@,                    %@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@#               @@  @@@@@@@@@@@@@@/******@@@@@@@@@@@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@                  @ @@        (@@@@@@@@@@@@       /@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@%      ,@(   .,   @@@@           &@@@@@,         ,&@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@@@ @@ .%   #,    @@@@@@@       #@@@@@@@@@       ,@@@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@@@@@   ,#  #@@@@@@@@@@@@@@@@#   %@@@@@@    @@@@@@@@@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(&@@@@@@((@@@@@@@@@@@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@         #@@@@@@@         ,@@@@@@@@@@@@ @ @@@@@@@@@@\n")
        print("Bark Soul:")
        to_print = "    Roof\n"
        Print_Dialog(to_print)
        print("Lancer:")
        to_print = "    HEY BARK SOUL KEEP IT DOWN\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@&/@//@ /)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#)*@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@/@// /  @@@@@@@@@@@%&   %/(% #%%@@@@@@@@@#)/,/ ,,,// @@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@///////)@@@ @@@@@@@ .%&@  % (% #%%@@@@@@@@@*, ///, @@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@*/*//// @ @@@@@@@@@@@,@@@@  /(% @@@@@@@@@@ ,   *, /*#, @@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@,(,,, *@@@@@@@@@@@@@@@     (((&(@@@@@@@@@@@@@@@ ((***  @@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@  *( ((, @@@@@@@@@@@@      % / @@@@@@@@@@@@@@@@* (,..( @@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@ /((((,*,@  , @@@@@@@ $$$$ , @@@@@@@@@@@@  @@@ .,,,,.@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@....,,*,,,,,,,@@@@@@, , ,, @@@@@@@@@ .,,,,,,,,,..@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@...,.,,,,,,,* @@@@  , ,, @@@@.,..,,,,,,,,,,..@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@ ....,,,,,,  ,, ,, ,,  ,  , *,,,.,(/.///@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@ ,,,,*,, ,,  + , ,    ,**,,,*,*/@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@.,,,,,,,..,   , ,   , ,   * ,,,  *( @@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@ ,,,,,,.. @@...   , ,, @@,* ,,  ,*    (***@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@,,,.,,.@@@@@@@   , , ,,,( @@@,,   ,, , ,,*,@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@,*,,, @@@@@@@@@,, , *,, ,, @@@@@@@@&&&..,,,*,@#@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@,,,,..@@@@@@@@@,  ,  , *,  @@@@@@@@@@@,@@...,,,,#@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@(,.@.. @@@@@@@@@@,, ,   ,, , @@@@@@@@@@@@@@@@@., ,,% ,@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@(, (( .@@@@@@@@@@@, ,, * , ,,&@@@@@@@@@@@@@@@@@@@@ (,%, /%(@@@@@@@@@"
            + "\n@@@@@@@@@@@  (@((@@@@@@@@@@@@@@, ,  ,,((@@@@@@@@@@@@@@@@@@@@@@ (,#% %@@@@@@@@@@@"
            + "\n@@@@@@@@@@)% @,##@@@@@@@@@@@@@@ * , ,  @@@@@@@@@@@@@@@@@@@@@(/ (@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        print("Maestro:")
        to_print = "    ah, so your the one every one was expecting to arive. say would you like to hear my new soundtrack i made\n"
        Print_Dialog(to_print)
        print(his_name)
        to_print = "    maestro, you never made any music dude.\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite)
        print(his_name)
        to_print = "    so, enjoying the party?\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite2)
        print(his_name)
        to_print = "    i think you and i are gona be good friends here. why try and escape right?\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite2)
        print(his_name)
        to_print = "    you have all these great mosnters here. they should entertain you for a while\n"
        Print_Dialog(to_print)
        to_print = "    maybe make new friends\n"
        Print_Dialog(to_print)
        option = input("> ")
        Clear_Screen()
        print(sprite)
        print(his_name)
        to_print = "    oh whats that? you have to go\n"
        Print_Dialog(to_print)
        to_print = "    alright, well i hope to see you again some time soon. good bye\n"
        Print_Dialog(to_print)
        option = input("> ")
# Funny encounter 4
def Funny_Encounter4(): # not that funny actualy
    Clear_Screen()
    his_name = "Dynomite: "
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    sprite2 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       --@,        =@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    
    sprite3 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       ---        ---        .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&                             ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print(sprite)
    print(his_name)
    to_print = "    hey, great to see you again. i hope you have nothing better to do\n"
    Print_Dialog(to_print)
    to_print = "    and im not taking up your time\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    let me tell you a legend before you go on with whatever you were going to do\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    a long time ago, a programer made a game.\n"
    Print_Dialog(to_print)
    time.sleep(3.0)
    to_print = "    a game that had monsters so intelligent that everyone thought the program was alive.\n"
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print(sprite2)
    print(his_name)
    to_print = "    this was remarkable at the time, no one thought this was possible\n"
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print(sprite3)
    print(his_name)
    to_print = "    he spent countless hours on it, trying to improve it\n"
    Print_Dialog(to_print)
    time.sleep(3.0)
    to_print = "    to the point where he risked his own health and education\n"
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print(sprite3)
    print(his_name)
    to_print = "    his game never saw the light of day. and it drove him insane\n"
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    eventualy he gave up. and left it as it was.\n"
    Print_Dialog(to_print)
    time.sleep(3.0)
    to_print = "    all the monster, have been left in despair.\n"
    Print_Dialog(to_print)
    time.sleep(3.0)
    to_print = "    they found a way to escape however it was nearly impossible...\n"
    Print_Dialog(to_print)
    time.sleep(3.0)
    option = input("> ")
    Clear_Screen()
    print(sprite3)
    print(his_name)
    to_print = "    ...\n"
    Print_Dialog(to_print)
    time.sleep(4.0)
    Clear_Screen()
    print(sprite2)
    print(his_name)
    to_print = "    i know you want to escape this place and finally leave\n"
    Print_Dialog(to_print)
    to_print = "    lets face it, we all secretly do.\n"
    Print_Dialog(to_print)
    time.sleep(4.0)
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    unfortunatly that wont happen. we wont let you leave\n"
    Print_Dialog(to_print)
    to_print = "    i wont let you leave\n"
    Print_Dialog(to_print)
    time.sleep(4.0)
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    so when the time comes, you best be prepared to face me in battle if you want to leave\n"
    Print_Dialog(to_print)
    time.sleep(4.0)
    Clear_Screen()
    print(sprite2)
    print(his_name)
    to_print = "    oh, my pizza is ready\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    Clear_Screen()
    print(sprite)
    print(his_name)
    to_print = "    alright i have important things to attend to\n"
    Print_Dialog(to_print)
    to_print = "    unfortunatly i wont see you again, not in this circumstance. goodbye\n"
    Print_Dialog(to_print)
    option = input("> ")

### Battle ###
# slect the enemy
def Enemy_Selection():
    # this one could definetly could be better
    global enemy
    global temp_count
    temp_count = 0
    ### A ###
    # a1 not included #
    if player1.location == 'a2':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy2()
        else:
            enemy = enemy1()
    elif player1.location == 'a3':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy1()
            enemy.level = 2
        else:
            enemy = enemy2()
    elif player1.location == 'a4':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy3()
        else:
            enemy = enemy2()
            enemy.level = 2
    elif player1.location == 'a5':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 2
        else:
            enemy = enemy3()
    elif player1.location == 'a6':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy4()
        else:
            enemy = enemy3()
            enemy.level += 2
    elif player1.location == 'a7':
        possible_options = random.randint(1, 16)
        if possible_options in [1, 10]:
            enemy = enemy3()
            enemy.level = 4
        else:
            enemy = enemy4()
            enemy.level = 2
    # a8 not included
    ### B ###
    elif player1.location == 'b2':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 8
        else:
            enemy = enemy1()
            enemy.level = 6
    elif player1.location == 'b3':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy1()
            enemy.level = 10
        else:
            enemy = enemy2()
            enemy.level = 8
    elif player1.location == 'b4':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy3()
            enemy.level = 12
        else:
            enemy = enemy2()
            enemy.level = 10
    elif player1.location == 'b5':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 16
        else:
            enemy = enemy3()
            enemy.level = 14
    elif player1.location == 'b6':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy4()
            enemy.level = 14
        else:
            enemy = enemy3()
            enemy.level = 16
    elif player1.location == 'b7':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy5()
            enemy.level = 14
        else:
            enemy = enemy4()
            enemy.level = 16
    elif player1.location == 'b8':
        enemy = enemy5()
        enemy.level = 16
    ### C ###
    elif player1.location == 'c1':
        enemy = enemy1()
        enemy.level = 16
    elif player1.location == 'c2':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 14
        else:
            enemy = enemy1()
            enemy.level = 16
    elif player1.location == 'c3':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy1()
            enemy.level = 18
        else:
            enemy = enemy2()
            enemy.level = 16
    elif player1.location == 'c4':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy3()
            enemy.level = 16
        else:
            enemy = enemy2()
            enemy.level = 18
    elif player1.location == 'c5':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 20
        else:
            enemy = enemy3()
            enemy.level = 18
    elif player1.location == 'c6':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy4()
            enemy.level = 18
        else:
            enemy = enemy3()
            enemy.level = 20
    elif player1.location == 'c7':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy5()
            enemy.level = 18
        else:
            enemy = enemy4()
            enemy.level = 20
    elif player1.location == 'c8':
        enemy = enemy5()
        enemy.level = 20
    ### D ###
    elif player1.location == 'd1':
        enemy = enemy1()
        enemy.level = 28
    elif player1.location == 'd2':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 28
        else:
            enemy = enemy1()
            enemy.level = 30
    elif player1.location == 'd3':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy1()
            enemy.level = 32
        else:
            enemy = enemy2()
            enemy.level = 30
    elif player1.location == 'd4':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy3()
            enemy.level = 30
        else:
            enemy = enemy2()
            enemy.level = 32
    elif player1.location == 'd5':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 34
        else:
            enemy = enemy3()
            enemy.level = 32
    elif player1.location == 'd6':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy4()
            enemy.level = 32
        else:
            enemy = enemy3()
            enemy.level = 34
    elif player1.location == 'd7':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy5()
            enemy.level = 32
        else:
            enemy = enemy4()
            enemy.level = 34
    elif player1.location == 'd8':
        enemy = enemy5()
        enemy.level = 34
    ### E ###
    elif player1.location == 'e1':
        enemy = enemy1()
        enemy.level = 42
    elif player1.location == 'e2':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 42
        else:
            enemy = enemy1()
            enemy.level = 44
    elif player1.location == 'e3':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy1()
            enemy.level = 46
        else:
            enemy = enemy2()
            enemy.level = 44
    elif player1.location == 'e4':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy3()
            enemy.level = 44
        else:
            enemy = enemy2()
            enemy.level = 46
    elif player1.location == 'e5':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 48
        else:
            enemy = enemy3()
            enemy.level = 46
    elif player1.location == 'e6':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy4()
            enemy.level = 46
        else:
            enemy = enemy3()
            enemy.level = 48
    elif player1.location == 'e7':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy5()
            enemy.level = 46
        else:
            enemy = enemy4()
            enemy.level = 48
    elif player1.location == 'e8':
        enemy = enemy5()
        enemy.level = 48
    ### F ###
    elif player1.location == 'f1':
        enemy = enemy1()
        enemy.level = 56
    elif player1.location == 'f2':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 56
        else:
            enemy = enemy1()
            enemy.level = 58
    elif player1.location == 'f3':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy1()
            enemy.level = 60
        else:
            enemy = enemy2()
            enemy.level = 58
    elif player1.location == 'f4':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy3()
            enemy.level = 58
        else:
            enemy = enemy2()
            enemy.level = 60
    elif player1.location == 'f5':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 62
        else:
            enemy = enemy3()
            enemy.level = 60
    elif player1.location == 'f6':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy4()
            enemy.level = 60
        else:
            enemy = enemy3()
            enemy.level = 62
    elif player1.location == 'f7':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy5()
            enemy.level = 60
        else:
            enemy = enemy4()
            enemy.level = 62
    elif player1.location == 'f8':
        enemy = enemy5()
        enemy.level = 62
    ### G ###
    elif player1.location == 'g1':
        enemy = enemy1()
        enemy.level = 70
    elif player1.location == 'g2':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 70
        else:
            enemy = enemy1()
            enemy.level = 72
    elif player1.location == 'g3':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy1()
            enemy.level = 74
        else:
            enemy = enemy2()
            enemy.level = 72
    elif player1.location == 'g4':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy3()
            enemy.level = 72
        else:
            enemy = enemy2()
            enemy.level = 74
    elif player1.location == 'g5':
        possible_options = random.randint(1, 16)
        if possible_options == 1:
            enemy = enemy2()
            enemy.level = 76
        else:
            enemy = enemy3()
            enemy.level = 74
    elif player1.location == 'g6':
        possible_options = random.randint(1, 8)
        if possible_options == 1:
            enemy = enemy4()
            enemy.level = 74
        else:
            enemy = enemy3()
            enemy.level = 76
    elif player1.location == 'g7':
        enemy = enemy5()
        enemy.level = 76
    # :) not included
    ### Calculation on dificulty ###
    if player1.job == 'NOTHING':
        enemy.maxhp += enemy.level * 24
        enemy.p += enemy.level * 4
        enemy.exp += enemy.level
    else:
        enemy.maxhp += (enemy.level * 14)
        enemy.p += (enemy.level * 2)
        enemy.exp = enemy.exp * enemy.level
    enemy.gold += enemy.level
# slect the enemy dialog
def Enemy_Encounter():
    if enemy.level < 28:
        to_add = enemy.name + ':\n'
        if enemy.name == 'Goblin':
            if player1.en1_counter == False:
                Clear_Screen()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#((/,..%%@@@@@@@@@@@@##(((@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%**************** .****, ,*((#%@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@///////***************, ,**, (@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@&/**&@@&********************, ,*/(@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@/,,,,,..  .,,****(@#/****************/#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@%///,,,,,,,     ,****%@**************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@&****,//*,,,,..   .,***(#%%*******%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@&///,,///*,,,,.     *****@@***%@@@/#@@@*/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n%%%#///*,,*///,,///,,,,,.   ,,***@@#%%@@//%(***(###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n////////*,*///,,///,,,,,.   ,,***@@/////****/&@@@/#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n///((&@@@@%/,,,,//*,,,.   ..*****@@/#@(*//@@@#///@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@#,*////*,,,     .,***%@/////****@%////////&@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@(//*,,,,,     ,****%@//@%*****@%///,,,*/&@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@&&&%%,..,*****&&@@&&&(/***/(&#/,,,,,(@(/(#@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@//***%@@@/#@#/,,/#@(//(@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,%@/////&@**,(@(//////&@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ /@@@/////&@,,,(@(//////&@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&((//////////((&&,,*%&///#&@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@, @@@#////////@@/////@@,,,%@///#@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@%#(/./(##*******%%%@@@@%#///@@,. *(%%@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@(    *@#//////**@@@@@@@@@@@@#/@@*,   @@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@&# ,*. (#&#/////(&@@@@@@@@@@&#/%&(#@#   %%@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@, .*@( &@@&/////@@@@@@@@@@#///****/@@@%*.    (@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@#.,*@&.,*&@*******@@@%(//****///@@@@@@@@@@/*   ....@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@( &@@% ,/@@//***@@//********%@@@@@@@@@@@@@@@        ,@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@/(%#(*****(%%%@@@@@@@@@@@@@@@@@@@*,   ..,*#* */(#@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@&/*****(@@@@@@@@@@@@@@@@@@@@@@@@@& ,*.  .*#@@@   (@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@%#***(#@&///%&@@@@@@@@@@@@@@@@@@@@@(* ,,/* *#@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@/(@#/@@/(@#//////%@@@@@@@@@@@@@@@@@@@@* */@(   @@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@(/@%*#@//*(@@@@@///////@@@@@@@@@@@@@@@@@@@...(@/*.*@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@//************@@@#/////////////&@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@//*******/%@@@@@@#///////////#@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%#********/(((&#////////&@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%(********(#%%///###%@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@//////(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                print(to_add)
                to_print = '    tehehehe, welcome to my vent\n\n'
                Print_Dialog(to_print)
                print(to_add)
                to_print = '    this day will be quite e ventfull\n\n'
                Print_Dialog(to_print)
                option = input("> ")
                player1.en1_counter = True
        elif enemy.name == 'Zombie':
            if player1.en3_counter == False:
                Clear_Screen()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@//@@@@@@@////@@//(@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@/////@@@@@@@@@//@@@@@@(//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@((  ****************  @@@@//(@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@  ******************  @@//@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@   **************************  @@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@   ******       ******.    ****  .@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@%%#....*******      *******  **  .@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@&    ******************  ****   @@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@**/@@  **       *************  @@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@  *******      ***  ****   @@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@  */**/**  **..**/  *******  %%%%@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     ********.  **    %%%%%%%%%  @@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@&    ***********    *******       %%**%%   @@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@  (/***    @@@@@  #*#*( (  ####%%%%%%%*#**%%   @@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@  *****  @@@@@@@@@  **  @@.  %%%%%%%%%%%%%****%%%  @@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@  **  @@@@@@@@@@@   **  @@@@@@@  %%%%***%%%%%%%%%%%  @@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@    @@@@@@@@@@@@@     @@@@@@.  %%%&%%%%#**%%%%%%%%%%%, @@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@**/@@@@@@@@@@@@@@@@@  (%%  %%     %%%%%%  %%%%%  @@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  **   **  *****      **   %#  @@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@**@@@@@@@@@  *%*********  ***###/###****  @@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  **  *****  @@  ***********   @@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@**@@   **//**  %@@@@@@     //      @@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@**@@   ****  @@@@@@@@@  *******  @@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@**/@@@@@@@@@@@  **  @@/**@@@@@@   ******  @@@@@**@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  **  @@@@@@@@@@@@@@@@  ****   @@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  **  @@@@@@@@@@@@@@@@@@@@  ***  @@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ****  @@@@@@@@@@@***@@@@  *****  @@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                print(to_add)
                to_print = '    B.B.B...BRRAINS\n\n'
                Print_Dialog(to_print)
                print(to_add)
                to_print = '    brrrrr\n\n'
                Print_Dialog(to_print)
                option = input("> ")
                player1.en3_counter = True  
        elif enemy.name == 'Frogo':
            if player1.en5_counter == False:
                Clear_Screen()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@&.,...,..,,@@@@@@@@@@@@@@@@@@@@@@@@@@.....,,,.@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@.              %@@@@@@@@@@@@@@@@@@@@.             @@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@                     &@@@@@@@@@@@@@                     @@@@@@@@@"
                    + "\n@@@@@@@@@@@@,.     .&@@@@@@@@&&%      .&@@@@@@@.         (&&&&&*        ..@@@@@@"
                    + "\n@@@@@@@@@@@@      @@@@@@@@@@@@@@        .@@@@@@         @@@@@@@@@@*       @@@@@@"
                    + "\n@@@@@@@@@@@@      @@@.     &@@@@        .@@@@,        %@@@@    #@@@@      @@@@@@"
                    + "\n@@@@@@@@@@@@      @@@%%%@@@*,            ,,,,         ,,,%@@%%   @@@      @@@@@@"
                    + "\n@@@@@@@@@@@@      &@@@@@@&          &@@,     %@@*           %@@@@@@@      @@@@@@"
                    + "\n@@@@@@@@@@@@                       &@@         &@@                        @@@@@@"
                    + "\n@@@@@@@&,                                                                 @@@@@@"
                    + "\n@@@@@@                                                                     (@@@@"
                    + "\n@@@                  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                 #@"
                    + "\n@@@            %&&@@@@&....           .......           ..,@@@@@@&*           .."
                    + "\n@@@          .@@@@@%                                           (@@@&            "
                    + "\n@@@                                                                           #@"
                    + "\n@@@@@@##                                                                /%%%%@@@"
                    + "\n@@@@@@@@@@&                                                          #@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@                                       @@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@*.                 *#@&%                  ***@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@             /@    /@@@@@#    @#              ,@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@(             @@@             /@@@@               @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@(                                                 @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@(              /@@@@@@@@@@@@@@@@@%                @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@(           (@@@@      @@@      @@@@@@            @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@(          @@@*, ### /@@@@#/       *(@@@#         @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@(        /@@@@   @@@@@@@@@@% @@@    ,@@@@@%        ,@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@(        /@@@@    *@@@@@@@@@@@(     ,@@@@@%           ,@@@@@@@@@@@"
                    + "\n@@@@@@@@#****          /@@@@###@@@@%*****(@@@@####%@@@@@@#            ***@@@@@@@"
                    + "\n@@@@@@@                /@@@@@@@@@@ /@@@@@# @@@@@@@@@@@@@@@                ,@@@@@\n")
                print(to_add)
                to_print = '    *ribit* i dont know alot\n\n'
                Print_Dialog(to_print)
                print(to_add)
                to_print = '    *ribit* all i know is that you are here to kill me\n\n'
                Print_Dialog(to_print)
                option = input("> ")
                player1.en5_counter = True
        elif enemy.name == 'Iseecle':
            if player1.en7_counter == False:
                Clear_Screen()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@# @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@ @@@@@ @@@@@@@@@@@ @@@@@#    @@@@@@@@@@@     @@@@@@    @@@   @@@@@@@@@@@@@@"
                    + "\n@@@@@   @@@@  @@@@@@@@@ @@          @#    @@@@@@@@@@     @  @     @@@   @@@@@@@@"
                    + "\n@@@@@@   @@@@@@  @@@@  @            @# @.  @@@@@@@@@     @     @@@@   @@@@@@@@@@"
                    + "\n@@@@@@@@ @@@@@@@@    @@             @# @@@   @@@@@@@@@@     @@@ @@   @@@@@@@@@@@"
                    + "\n@@@@@@@@@  @@@@@@@  @               @# @@@@   @@@@@@@@   @@@@@@@   @@@@@@@@@@@@@"
                    + "\n@@@@@@@@@   @@@@@@@@                @# @@@@@@ @@@@@@@@ @@@  @@@    @@@@@@@@@@@@@"
                    + "\n@@@@@@  @     @@@@@@   @           @ *@@@@@     @@@@   @@@@@@     @@@@@@@@@@@@@@"
                    + "\n@@@@@@  @   @@@           @        @ *@      @@@   @     @      @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@  @@@ @@             @@      @      @@@   @  @      @@   @@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@   @@                   @@   @ *@   @@@@@@@@@ @@       @@ @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@                        @@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@                                                 @@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@                                                   @@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@                     @@@@@@@@@@@                 @@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@                  ,%%           %%,           ,%%@%%%%%@%%%%%@%%@@@@@"
                    + "\n@@@@@@@@@@@@                 @      @@@      @         @@ @@      @     @@@@@@@@"
                    + "\n@@@@@@@@@@@@@@               @@@           @@@        @   @@    @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@            /   @@@@@@@@@@@ /           @@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@            /   @@@@@@@@@               @@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@                       @@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/n")
                print(to_add)
                to_print = '    heeey kyle, i\'ve been look-\n\n'
                Print_Dialog(to_print)
                print(to_add)
                to_print = '    HEY, you\'re not kyle\n\n'
                Print_Dialog(to_print)
                option = input("> ")
                player1.en7_counter = True
        elif enemy.name == 'Funguy':
            if player1.en9_counter == False:
                Clear_Screen()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@%##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@&  .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%  #&@@@@@@@@"
                    + "\n@@@@@@@@@@&   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%   *@@@@@@@@"
                    + "\n@@@@@@@@@@&     @@@@@@@@@@@@@@@@                  (@@@@@@@@@@@@@@@,    *@@@@@@@@"
                    + "\n@@@@@@@@@@@@        @@@@@,                               @@@@@,       &@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@*                                                       @@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@&                                                    ,@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@%                                            ,@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@                 %%%%%%%%                 %@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@& /&@@@#*                  @@@@@@@@                  ./@@@@/ *@@@@@@@@"
                    + "\n@@@@@@@@@@@*              .*****     #&@@@@@#     ,*****              *(@@@@@@@@"
                    + "\n@@@@@@@@@@@@@/.             @@@&      /@@@@@      (&@@*             .@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@*          @@# @.      @@(      @/.@@*          @@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@*           &@@@.      @@(      @@@             @@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@*      @@%                            .@@*      @@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@%      &@@@.                       @@@@      ,@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@      *@  *@@.               @@@  #&      %@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@,       &@@    @.       @(   (@@        @@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@&(       .,,#%%@        @&%%,,,       .%@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@##@(.           ////////            (&@/ %@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@    @@&*                          ,/@@*   %@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@    @@@@@@#...              ...,@@@@@@*    ,@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@%     @@@@@@@@@@@@@@@@@@@@@@@@@@@@ .@@@@*.@    @@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@*   %% @@@@#   .,,,,,,@@@@@/       /%@@@@&%@@,  @@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@*  @@% @@@@&(        @@@@@@@@      #@@@@@@@@@@&(@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@*,@@@@@@@@@@@      .*@@@@@@@@     *%@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      /@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.    /@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.    /@@@@@@@@@@ (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                print(to_add)
                to_print = '    now. what am i going to do with you...\n\n'
                Print_Dialog(to_print)
                print(to_add)
                to_print = '    LOL i literaly have no idea LMAO\n\n'
                Print_Dialog(to_print)
                option = input("> ")
                player1.en9_counter = True
    else:
        to_add = enemy.name2 + ':\n      '
        if enemy.name == 'Goblin':
            if player1.en2_counter == False:
                Clear_Screen()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@,#@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,,,,  @@@@@@@@@@@@@#*,,#@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%*,   ,,*,,###%%%, .,,,,*/(@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%&@&&////*,,,,,,,,,,,,,,  ,//(%@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@/,,/((((&@@#,,,,,,,,,,,,,,,,, ,@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@###(((((//*(((((#%@,,,,,,,,,,,,,&&@@@###.*(@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@&,/((((((((((/,((((((%@#(,,,,,,,,,&@@@@@%   (((((((((%@@@@@@@@@"
                    + "\n@@@@@@@@@@@#(((((((((,/(((((((((,*((((((@&,,,@@@#%@@@            .((((%@@@@@@@@@"
                    + "\n@@@@@@@@,,,/(((((((((,/(((((((((,*((((((@@#&@@&#@%,             ((#@@@@@@@@@@@@@"
                    + "\n@&,,,,,,,,,,,(((((((((/,((((((((,*((((((@@#((#/,,.               .(((@@@@@@@@@@@"
                    + "\n@@@@@/////,**((((((((//*((((((((,*((((((@&(&@,,...         ..........(%@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@%((((((,/(((((((((,*((((%@##(##,,,        #%@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@%#%%%((((((/,(((((%%%#%@(*,..  ***///&&%@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,/((((&@@@@@&(*,   @&(*****@&(##@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###..   %%%@@@%#***@&(((%&@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(,    /(@@@(((##***@&((((%@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(   (/ %@@&#(((&@***@&((((((@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(   (((. @%((((&@***@&((((((@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@% %@@%((((((#&@(((((@#**/@#((%@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@%#/*.((%(/,,,/(%&&@@@%%(((@#, ./%%@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@%    (@##((((/,@@@@@@@@@@@#(@#,   %@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@%/ .%. &%%(((((&@@@@@@@@@@//*#%&@@   ,,@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@ /@,, %@,,,(((&@@@@@&,((((((/,%@@@@@%    .,@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@, *#@ .#@@,,,,,*&@@%#,,,,,(((@@@@@@@@@&*      ,@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###@&,,,,,,,/@@@@@@@@@@@@@@@@@/,   ,.    (@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%&&,,,,,/%@@@@@@@@@@@@@@@@@@@@(/     .#%,,,.*%@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,,*(&@###@@@@@@@@@@@@@@@@@@@@@,. ,.   @@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(#%(%@&%&%###&&&@@@@@@@@@@@@@@@@@%( .#(( ,(@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@#,@@#*,@@@@@######@@@@@@@@@@@@@@@@@%   @#, ,@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@%%%%%(*,**,,,,*//(@@&######%%%%%%&@@@@@@@@@@@%&@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#,,,,,,(#@@@@@@%##########&@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,,,,,,,,**#@########@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,#@######&@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,,,&@####%@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@///,,,,,*//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                print(to_add)
                to_print = '    tehehehe, welcome to my garden tarveler\n\n'
                Print_Dialog(to_print)
                print(to_add)
                to_print = '    this day will be quite e ventfull\n\n'
                Print_Dialog(to_print)
                option = input("> ")
                player1.en2_counter = True
        elif enemy.name == 'Zombie':
            if player1.en4_counter == False:
                Clear_Screen()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@/                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@   ,/////// ,&&&&&&&&&&&&# ,/. &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@  &&%########%%%#(((((((%%%%#/,*/****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@. &&%#/////##%#%%%%%%%%%%%%%%%%%&,.  @@ .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@  &&%%%%%%%#%//%%##%%%#%%%%%%%%#%&&&&#% .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@,,%%%%((#/,,,,,/(((//./#####%%%#%/ */%%%% .,,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@..##%%%%%%%%%%%.....,#%#@&@@&&&&@%%, %%%% .#######%%   ,@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@. %%&&@&&&&%%#%%%%#%%%%&...........(%%%%% .(((((,..........#&@&@@@@@@@@@@@@@@@"
                    + "\n@@&&,.,,(((((*.....,,.../(%%%%%%%%%#/(#%%#% .(/./##((((((((####%%,,@@@@@@@@@@@@@"
                    + "\n@@@@. //#%%%%(#(# .///* (%%%%%%%%%%#/..//%% .(/ /(((((((//((###..//..@@@@@@@@@@@"
                    + "\n@@. &&##((%%%##,,###%##%*,##%%%%%#(#%&&. %% .(/ /(((((((((((#*.//#%%%.,&@@@@@@@@"
                    + "\n@@ .%%//#%#*.#%. ,,##,, (#%%  %%%#%%%#%  %% .(/ /(((((((((#/.*/##//%%%(.(@@@@@@@"
                    + "\n@@@@  %%%#%%%%%%%#%%##%%%%##%%%%%%#/   //%% .(/ /(((((((((#(#, //###%//#*.&@@@@@"
                    + "\n@@@@@@,* ... #%,.&%.,,/&/.#%..##....,//##**.,(/.**//((((//((###,,/*(##(#,.%%@@@@"
                    + "\n@@@@@@@@ .,*/%%,........,.,....,%( ,///  //((((((/. //////(((((((%####(./%. @@@@"
                    + "\n@@@@@@@@@% ,/#%%%,.....,...,.,.,%%%(/..//((((((((/**..  ///(((((((((((((((. @@@@"
                    + "\n@@@@@@@@@&/,.**##**//&#*#&/**/((#(**.,,**((((//((((///** .///((((((((/((((. @@@@"
                    + "\n@@@@@@@@@@@@@,  .///////////////   ,/. ,*  (((((((((//** .///(((((((((((((. @@@@"
                    + "\n@@@@@@@@@@@@@@@@@.               ./((((  #(((((/((////** .///. */((((((///. @@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@& *#((,,((//*, */////..//,,,,,*/**** .,,*((****,, .*. (#@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@&     ,, .           */ .*****..  ..///(##%#%%%%#%#. .&@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@& ,///////,, .*******((((//////*** .%%%%%%%%%%%//%%%* &@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@& ,(*,((../////////((**((///////////.,(*,/(,,(/,,((**,. @@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@%. .. . /((/(/////////(///((////(/// .      ...  . . .@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@  ////*//((///(////***, /(/(**////(********,,   /(  @@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@(.///////(/((///(****,,,... //////((#(////(//**,. ..  @@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@/ //####(/((#(/****,,,. %@, /(((###*.(#(((///**,. #%  @@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@* (#. ..##(/./###**,, /@@@@@. #( ..,/. (#/(/(**,. #%  @@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@* #%%#%%%#%###%%%//,, /@@@@@@@ .%#%#%%%//  #(,,,. #%  @@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@% (%%%%%##%##%%%%///(,, /@@@@@@@@@       ..   ..  ,/#%  @@"
                    + "\n@@@@@@@@@@@@@@@@@@@@% ,/, */../* .///////,,,../@@@@@@@@@@@@@@@@. ,,. ** /#. @@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                print(to_add)
                to_print = '    ...\n\n'
                Print_Dialog(to_print)
                print(to_add)
                to_print = '    ...\n\n'
                Print_Dialog(to_print)
                option = input("> ")
                player1.en4_counter = True
        elif enemy.name == 'Frogo':
            if player1.en6_counter == False:
                Clear_Screen()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  @@       (@*  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@,                @@@@@@@@@@#@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@,  @@@@@ %@@@@*                @@@% @@@@@  *@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@&     .@#    @@@@@@@@@@@@@@@@@@@@@@    %@.     @@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@%  .((((((    (@@@@@@@@@@@@@@@@@@(    ((((((.  %@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@   @@@@@@@@@&    @@@@@@@@@@@@@@@@    &@@@@@@@@@  .@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@%  /@@@@@@/@@@@@.   ./@@@@@@@@@@(.    @@@@@/@@@@@@/  &@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@%  #@@@@(   .@@@@@     .@@@@@@.     @@@@@.   (@@@@(  &@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@%  #@@@@@@@@@@@@@@       &@@&       @@@@@@@@@@@@@@(  &@@@@@@@@@@@"
                    + "\n@@@@@@@@ @@@@@@%  #@@@&&&         @@### #&&# ###@@         &&&@@@(  &@@@@@@ @@@@"
                    + "\n@@@@@@@@  ,@@@@%                   *@@@      @@@*                   &@@@@,  @@@@"
                    + "\n@@@@@@@@    ,****                                                  ****,    @@@@"
                    + "\n@@@@@@@@.                .     @@                  @@     .                .@@@@"
                    + "\n@@@@& @@@/              .@@@@@@@@@@@@@@      @@@@@@@@@@@@@@.              /@@@ &"
                    + "\n@@@@@%.,&&%       *%%&@@@&@@&&&@@&&&&@@@@@@@@@@&&&&@@&&&@@&@@@&%%*       %&&,.%@"
                    + "\n@@@@@@,                @@ &@   @@                  @@   @& @@                ,@@"
                    + "\n@@@@@@@@@/                                                                /@@@@@"
                    + "\n@@@@@@@@@@@,,,                                                        ,,,@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@.                                                .@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@#..&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,..@@@@@@@"
                    + "\n@@@@@@@@@@@@%*    (@@@@@@    #@@@@@@@@@@@@@@@@@@@@@@@@@@    /@@@@@@    .*@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@%                     @@@@@@@@@@@*                     @@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@&&&&*                #&&&&.                %&&&&@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@ %@@@@,             @@  .@@@@@@@@  *@(             @@@@@ #@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@.              (@@@@(          @@@@@               &@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@.                *((((((((((.                %@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@&               @@@@@@@@@@@@@@@@@(              .@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@&          (@@@@@@@%#@@@@@@@@(@@@@@@@@          .@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@&          %@@@@*       @&       @@@@@          .@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@,       @@@@@@@@@(.@@@@@@@@ @@@@@@@@@&       @@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@%(      &@@@@@@@@@@&@@@@@@@@@@@@@&@@&#     .#@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@    %@@@@@@@/        (@@@@@@@% @& @@@@@@@@         @@@@@@@@    /@@@@@\n")
                print(to_add)
                to_print = '    *ribit* i know all\n\n'
                Print_Dialog(to_print)
                print(to_add)
                to_print = '    *ribit* i wont let you defeat me\n\n'
                Print_Dialog(to_print)
                option = input("> ")
                player1.en6_counter = True
        elif enemy.name == 'Iseecle':
            if player1.en8_counter == False:
                Clear_Screen()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @. @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@  @         @@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@ @@          @@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@   @@@@"
                    + "\n@@@  @@@@@@@@@@@@@@@@@@@@@ @@          @@@@@@@@@@@@   @@@@@@@@@@@@@@@@   @@ @@@@"
                    + "\n@@@@@ @@@@@@@@@@@@@@@@@@  @            @@@@@@@@@@@@@   @@@@@@@@@@@@@@    @@ @@@@"
                    + "\n@@@  @@@ @@@@@@@@@@@@@@@  @         @# @@@@@@@@@@@@@   @@@@@@@@@@@ @@ @@@  @@@@@"
                    + "\n@@@@@ @@@@@ @@@@@@@@@@@ @@          @#  @@@@@@@@@@@@     @@@@@@    @@@   @@@@@@@"
                    + "\n@@@@@   @@@@  @@@@@@@@@ @@          @#    @@@@@@@@@@     @  @     @@@   @@@@@@@@"
                    + "\n@@@@@@   @@@@@@  @@@@  @            @# @.  @@@@@@@@@     @     @@@@   @@@@@@@@@@"
                    + "\n@@@@@@@@ @@@@@@@@    @@             @# @@@   @@@@@@@@@@     @@@ @@   @@@@@@@@@@@"
                    + "\n@@@@@@@@@  @@@@@@@  @               @# @@@@   @@@@@@@@   @@@@@@@   @@@@@@@@@@@@@"
                    + "\n@@@@@@@@@   @@@@@@@@                @# @@@@@@ @@@@@@@@ @@@  @@@    @@@@@@@@@@@@@"
                    + "\n@@@@@@  @     @@@@@@   @           @ *@@@@@     @@@@   @@@@@@     @@@@@@@@@@@@@@"
                    + "\n@@@@@@  @   @@@           @        @ *@      @@@   @     @      @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@  @@@ @@             @@      @      @@@   @  @      @@   @@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@   @@                   @@   @ *@   @@@@@@@@@ @@       @@ @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@                        @@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@                                                 @@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@                                                   @@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@                     @@@@@@@##                   @@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@                  ,%%         @@@,            ,%%@%%%%%@%%%%%@%%@@@@@"
                    + "\n@@@@@@@@@@@@                 @      @@@     @@         @@ @@      @     @@@@@@@@"
                    + "\n@@@@@@@@@@@@@@               @@@           @@@        @   @@    @@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@                 @@@@@@@@@@@            @@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@                @@@@@@@@@               @@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@                       @@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/n")
                print(to_add)
                to_print = '    ...\n\n'
                Print_Dialog(to_print)
                print(to_add)
                to_print = '    finaly a worthy aponent\n\n'
                Print_Dialog(to_print)
                option = input("> ")
                player1.en8_counter = True
        elif enemy.name == 'Funguy':
            if player1.en10_counter == False:
                Clear_Screen()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@#*,,@@@@@@@,,*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.%@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@*,&@@@@@@@@@@@@&./@@@@@@@@@@@@@@@@@@@@@@@@@@@.%@@@@@@@@@"
                    + "\n@@@@@@@@@(,@@@@@@@@@@@@@,,@@# @@&@ %@@@@@@/,&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@#,@@@@@@@@@@@@@@#***&****&@ #@@@@@#*/@@@@@@@@@@@@@@@@@@@@@@@@@@&, *@@@@"
                    + "\n@@@@@@@#@@@@@@@@@@@@@@@@@@@@@%%%@@@@@ (@@@@@@#.@@@@@@@@@@@@@@@@@@@@@@@,&@& @@@@@"
                    + "\n@@@@@@( (@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (@@@@@@@% @@@@@@@@@@@@@@@@@@@*      &@@@@@"
                    + "\n@@@@@@@&@(...@@@@@@@@@@@,,%**@@@@@@**%@@@@@@@@&**@@@@@@/*#*,@@@@**%@@%/@@@@/*@@@"
                    + "\n@@@@@@(....../&@@@@@@@@@@*,@@&&&&&&@@@@@@@@@@@@@@&&&&&&@@,*@@@@@ /@@@(  @@@@ &@@"
                    + "\n@@@%.#@@@.%@@@%,*@@@@@@@@@(.&@@@@@@@@@@@@@@@@@@@@@@@@@@& /@@@@@@ /@@@@( @@@& @@@"
                    + "\n@@@% @@@@  &@@@,,@@@@@@@@@@@&/****&@@@@@@@@@@@@@@@@***/%@@@@@@@@@@#*******/@@@@@"
                    + "\n@@@%.(@@@@,&@@#,*@@@@@@@@@@@@.@@@@&&&@.         @&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@#....../&@@@@@@@@@@@@@@.     %%%%&@@@@@@@@%%% .@@@@.@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. #@/                      @@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@* ,#@@%  @//@/@(&(%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*  ...@#%@#@%@%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@&/      &,&@@@@@@@@@@@&%      #&@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@&*,@@@@@@@@@@@/ @@@@@@ &@@@@@@@@@@&,/@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@% @@ ####.#@@&##% @@ @##@@@,*###/,@& @@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@% @ @@@@@@@,*/  @%  @@  %.%@@@@@@# @ @@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@,*@@@@@@@**@@@%  @@@@ #@@@@@@%,*@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/.@% @@@.%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**@@@@& @@@ %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(*(@@@@& @@@@/*&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@&,*@@@@@@@@@@@@,#@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@&@@@@@@@@@@    #@@@@@@@@@@@@@@@@@@@@/   .@@@@@@@@@@@&@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@% *@&..@@@@@@( #.************************,*,,*/ #@@@@@& ,@@. &@@@@@@@@@"
                    + "\n@@@@@@@@@@,@@, @@@@@@# @@@@# /@@@@@@@@@@@@@@@@@@@@, @@@@& &@@@@@@ (@@,@@@@@@@@@@"
                    + "\n@@@@@@@@@@ ,@@# *@., #@@@@@@@# &@@@@@@@@@@@@@@@@% &&@@@@@@/  ,@, &@& ,@@@@@@@@@@"
                    + "\n@@@@@@@@@@% ,@@@@@@@@@@@@# *@@@@@@@@@@@@@@@@@@@@@@@@. &@@@@@@@@@@@@. &@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@& *%( *@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,@@..(& .@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@&.@.*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.*& @@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/@@@@@@@@@@@@@@@@@@@"
                    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@n")
                print(to_add)
                to_print = '    and then i was like "Thats not a camel, Thats my wife" ahaha get it?\n\n'
                Print_Dialog(to_print)
                print(to_add)
                to_print = '    OH hey would you like to hear a joke?\n\n'
                Print_Dialog(to_print)
                option = input("> ")
                player1.en10_counter = True
    if enemy.level >= 28:
        enemy.name = enemy.name2 # it was easyer to do it here
# slect the boss
def Boss_Selection():
    global enemy
    global temp_count
    temp_count = 0
    if player1.location == 'a1':
        if (player1.solved_places['a3'] and player1.solved_places['a3'] and player1.solved_places['a4'] and player1.solved_places['a5'] and player1.solved_places['a6'] and player1.solved_places['a7'] and\
            player1.solved_places['b2'] and player1.solved_places['b4'] and player1.solved_places['b5'] and player1.solved_places['b6'] and player1.solved_places['b7'] and player1.solved_places['b8'] and\
            player1.solved_places['c1'] and player1.solved_places['c2'] and player1.solved_places['c3'] and player1.solved_places['c4'] and player1.solved_places['c6'] and player1.solved_places['c7'] and player1.solved_places['c8'] and\
            player1.solved_places['d1'] and player1.solved_places['d2'] and player1.solved_places['d3'] and player1.solved_places['d5'] and player1.solved_places['d6'] and player1.solved_places['d7'] and player1.solved_places['d8'] and\
            player1.solved_places['e2'] and player1.solved_places['e3'] and player1.solved_places['e4'] and player1.solved_places['e5'] and player1.solved_places['e6'] and player1.solved_places['e7'] and player1.solved_places['e8'] and\
            player1.solved_places['f1'] and player1.solved_places['f2'] and player1.solved_places['f3'] and player1.solved_places['f4'] and player1.solved_places['f5'] and player1.solved_places['f6'] and player1.solved_places['f8']) == True:
            if player1.boss9_defeated == False:
                enemy = boss9()
            else:
                enemy = boss8()
        else:
            enemy = boss8()
    elif player1.location == 'a2':
        enemy = boss1()
    elif player1.location == 'b3':
        enemy = boss2()
    elif player1.location == 'c5':
        enemy = boss3()
        if player1.job == 'NOTHING':
            pass
        else:
            enemy.exp = 9999
    elif player1.location == 'd4':
        enemy = boss4()
    elif player1.location == 'e1':
        enemy = boss5()
    elif player1.location == 'f7':
        enemy = boss6()
        if player1.job == 'NOTHING':
            global d_counter
            d_counter = 1
            enemy.p = 260 * 2 
        else:
            d_counter = 0
    elif player1.location == 'f7':
        enemy = boss6()
    elif player1.location == 'g7':
        enemy = boss10()
    elif player1.location == ':)':
        enemy = boss7()
        if player1.job == 'NOTHING':
            if player1.e_save == 2:
                enemy.maxhp = 999999
                enemy.hp = enemy.maxhp
                enemy.p = 6666
            else:
                enemy.p = 666
                enemy.maxhp = 300000
                enemy.hp = enemy.maxhp
    if player1.job == 'NOTHING':
        enemy.maxhp += enemy.level * 24
        enemy.p += enemy.level * 4
        enemy.exp += enemy.level
    else:
        enemy.maxhp += enemy.level * 12
        enemy.p += enemy.level * 2
        if enemy.name != "Egpr":
            enemy.exp += enemy.level * 2
# slect the boss dialog
def Boss_Encounter():
    Clear_Screen()
    to_add = enemy.name + ':\n'
    if enemy.name == 'Mr Groove':
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@&#######@@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@&#@@@@&####@@@@&##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@&&&%&&@@@%%%%%&&@&&&&&&&&&&&%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@###@&##%@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@###@@@@@@###***************###*(#@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@&%#(&&&&#****..,#(*&@@@@@&(**//(//%@@#@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@(/(@@@@@@@//*(((*#@@@@@@@@@@***#//#&@#@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@&*@&,,/@@@@@%*****#@,,,@@@@@@***#//#&@#@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@(((&&@@@@@(/****(*.#&@@@@(/**((/((@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@//*&&&&%**,... ...(/*****//(((@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@#/********((((((####&@@@@(#%&%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,........./(@%@@@/(##&@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@&(...(*  ..(#%%%%%*..%@@@@&#%&@*(#%&&@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@#.%%%%%%,,.##%%%%%&&@@@@@@@@@@@@&#***#&@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@#@%%%%%%,,,@@@@@@@@@@@@@@@@@@@@@@@#&@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@((@@@@@@@@@@@&&&@@@@@@@@@@@@@@%##%&%/,*/#&@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@(/@@@@@@@@@@@@@@@@@@@@@@@@@@@(***(@@@@#,%@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@%#@(/@@@@@@@@@@@@@#(****@@@@@@@@@@@/(@/**@&**#@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@#%%(&@@@@@@@@#(*****/((#@%&@@@@@@###/**(##/(%%#*@@@@@@@@"
            + "\n@@@@@@@@@@@(**(#@@@(,,%@@(/@@@@@@@@@@@@@##((##@@@#%@@@@@**//(##///****//@@@@@@@@"
            + "\n@@@@@@@@@@@@@#/**@@@,@%#,%@@@@@@@@@@@@@#,/@@%,@%*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@%#(//(/***/#@#%@&@@@@@@@@@@@@@@#(((//****/#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@&@(**&@@(///**@@@@@@@@@@@@@@&&(/**/////*****/#@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@(/#@@@@@@@&****@@@@@@@@@@@(******/(@@@@@@/***#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@///****(#@@@@@@@@@@@&#*/#,*#@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@%(*****/(%@@@@@@@@@@@@@@@//*%#(&@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@%#*******&@@@@@@@@@@@@@@@@@@%****%%%#&@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@%#*******&@@@@@@@@@@@@@@@@@@@@@@@****(%%%%./#@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@&&********/%@@@@@@@@@@@@@@@@@@@@@@@@%#**/(*(##(/#%&#&@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@#********(#@@@@@@@@@@@@@@@@@@@@@@@@@@&#*******(#%/.%%%#&@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@%####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#*************&@@@@#@@@"
            + "\n@@@@@@@@@@@@@@@@&%(((@@@#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#((((%&&(((%@@@@@@"
            + "\n@@@@@@@@@@@@####&@@@@@@@#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#&@@@@@@@@"
            + "\n@@@@@@@@@@&########&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###@@@@@@@@@@\n")
        print(to_add)
        to_print = '    Lets party!\n\n'
        Print_Dialog(to_print)
        print(to_add)
        to_print = '    Dance dance every one!\n\n'
        Print_Dialog(to_print)
    elif enemy.name == 'Maestro':
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@&/@//@ /)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#)*@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@/@// /  @@@@@@@@@@@%&   %/(% #%%@@@@@@@@@#)/,/ ,,,// @@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@///////)@@@ @@@@@@@ .%&@  % (% #%%@@@@@@@@@*, ///, @@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@*/*//// @@@@@@@@@@@@@,@@@@  /(% @@@@@@@@@@ ,   *, /*#, @@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@,(,,, *@@@@@@@@@@@@@@@     (((&(@@@@@@@@@@@@@@@ ((***  @@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@  *( ((, @@@@@@@@@@@@      % / @@@@@@@@@@@@@@@@* (,..( @@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@ /((((,*,@  , @@@@@@@ $$$$  @@@@@@@@@@@@@  @@@ .,,,,.@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@....,,*,,,,,,,@@@@@@, , ,,*, , @@@@@ .,,,,,,,,,..@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@...,.,,,,,,,* @@@@  , ,,@@@@@.,..,,,,,,,,,,..@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@ ....,,,,,,  ,, ,, ,,  ,  , *,,,.,(/.///@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@ ,,,,*,, ,,  + , ,    ,**,,,*,*/@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@.,,,,,,,..,   , ,   , ,   * ,,,  *( @@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@ ,,,,,,.. @@...   , ,, @@,* ,,  ,*    (***@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@,,,.,,.@@@@@@@   , , ,,,( @@@,,   ,, , ,,*,@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@,*,,, @@@@@@@@@,, , *,, ,, @@@@@@@@&&&..,,,*,@#@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@,,,,..@@@@@@@@@,  ,  , *, #@@@@@@@@@@@,@@...,,,,#@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@(,.@.. @@@@@@@@@@,, ,   ,, ,@@@@@@@@@@@@@@@@@@., ,,% ,@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@(, (( .@@@@@@@@@@@, ,, * , ,,&@@@@@@@@@@@@@@@@@@@@ (,%, /%(@@@@@@@@@"
            + "\n@@@@@@@@@@@  (@((@@@@@@@@@@@@@@, ,  ,,((@@@@@@@@@@@@@@@@@@@@@@ (,#% %@@@@@@@@@@@"
            + "\n@@@@@@@@@@)% @,##@@@@@@@@@@@@@@ * , ,  @@@@@@@@@@@@@@@@@@@@@(/ (@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        print(to_add)
        to_print = '    mua ahaha\n\n'
        Print_Dialog(to_print)
        print(to_add)
        to_print = '    you\'re HP will drop when i turn up my master piece\n\n'
        Print_Dialog(to_print)
    elif enemy.name == 'eremthgin':
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@ @@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%(((((%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(((((((((%@@@@@@@@@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@&(((%@@@@@@@@@@@@@@@@_____@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((*,,,,,,,@(**/@@@@@@(*@@@@@&@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@((@@@,/@*,,,,,,@@@,,,%@@&,,,@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@(#@*,@@@@@@%,@@@(,,*,,,@&(&@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*,,/@,,,,,,,@#,,*@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*,(/.@@,,,@@.(@@@,%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,@@@#.@@@@@,,,%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@..,,.@@@,,.,,,,,*(@@@*. ,@*,./@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,.@%.@@@@@@@@(. ..#@.,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@#(/////@@@@@/&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@(/((((((%@(((&@@@/&@@@@@@@@@(/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((#@@@@@@((@@@@@@@@@@@@@@@@@@@@@@@@%(@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@((@((((((/@@@(((((@@@@@@@@@@@@@@@@@@@@@%(@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/&@/((@@@@@(((((((@@@@@@@@@@@@@@@@@@@%(@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@@@(((@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@/((%@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@//,@@@@@,*(%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@.,,,,,,,@@@@@@@@@@@@@@@@&,,,,,,,.@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@////////@@@@@@@@@@@@@@@@&///////*@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/n")
        print(to_add)
        to_print = '    your end is nearn\n\n'
        Print_Dialog(to_print)
        print(to_add)
        to_print = '    smaerd ruoy tnuah lliw i revewoh\n\n'
        Print_Dialog(to_print)
    elif enemy.name == 'Q36u43e25e46n':
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/@@@#@@@@@@(@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@///@@@@@@@@@///#////@@///%@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@////////@@@@#////////////%@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@///////////#@//////////#@@@@@@@@#//@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%//////////&&@&/****,,***%&/////&@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@///(/@@##@@@,,,,,,,,,,,,,,,#@//@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@#,,,,,/@@@@@@@@///##& @@@#,@@%,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@&,,,,,,/(@@@@@@@//####@ @@,,@@@%,,,,,,,,,,#@@#@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@&****,,@@@@//####%&@ @  ,@@@@@@@/,,&@@@@@/%@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@//,(%%,%@@//######@,@@      ,%%@,@@@%/    @@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@///@@(,,@@/####&@@,,@/# */@@@#/  @@%/////@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,,#@       #,#/ #@,,,@,,@##//////@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@%(((///&&#/   &&&%(%/,*,,,@/,/(.@%#/////@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@////////////####@#####@@@*/@@@@/,,@ @#/////#@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@#////@%####%@//@@###%@@@@@@@@@@@(    @/////#@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@&/////@##@           (@@@@@@@@@#@   @///@#@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@/@@&##@@//@@@@@/ *&&&*         &@%((//#@@%/(#//%@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@/@@@@@@@@@@@@(,,,,,,(((@#  /#/////////////////&@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@(@@@@@@@@/,,,,%@@@@@###/%##///////#//////###&@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@%@(@@#@,,,@///////////@////////(//######%@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@&@@@@(@@@&(@#####//////(@///////(#######@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@(@@@@@@############@#/////#######@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@/@@@@@(@@@@@@####################@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@(@@@@@(@@@@@@@@///(@@########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@%@@@@(@(@@@@@@@@@,/////////////&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@/(@@@@@(/@@@@@@@@@@@..,/,/,/,,,//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@((((%@@@@@@@@@@@@@@@@@@&,,/,,,,,/.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(@/,//@//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&//@@/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        print(to_add)
        to_print = '    OHohohoo, a challenger?\n\n'
        Print_Dialog(to_print)
        print(to_add)
        to_print = '    let me compute this into my schedule\n\n'
        Print_Dialog(to_print)
    elif enemy.name == 'Big $1im3':
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@                             @@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@***,                    ##########/        .*@@@@@&*@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@(    .@@@@@@@@@@@@          @@@@@*   @@@(   @&          @@@@@@@@@@@@"
            + "\n@@@@@@@@@@@     @@@@@@@   /@@@@@          @@@@@@@@@@(     @@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@.         .@#               @@  @@@       @@          @@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@*           .@#        @@@@ @@@@@@@         @@            @@@@@@@@@@@@@@@@@"
            + "\n@@@@             .@#                                       *@@@   /@@@@@@@@@@@@@"
            + "\n@@@@ #@.   @(            @@@@@@@@                                       @@@@@@@@"
            + "\n@@@@*(###  ###     .*@@@@@@###@@@@@@@###@@@@*.      .*  @& *@     ,@@@@@@@@@@@@@"
            + "\n@@@@@@@.      @@ .@@@@@@@@@@@@@@     @@@@@@@@*     @@@@@@& *@@@   ,@@@@@     @@@"
            + "\n@@@@@@@.    (@@@ .@@@@@@@@@@@@                     @@@@@@@@@@@@   ,@@@       @@@"
            + "\n@@@@@*   @@ (@@@                     @@ @@  @@@.    (@@@ .@@@@@@@@@@@@@@ @@@@@@@"
            + "\n       &@@@ (@@@                     @@ @@  @@@@@   (@@@ .@@@@@  @@@@@@@ @@@@@@@"
            + "\n@@@@@@@@@@@@@@@@ .@@@  @@@%   @@@@@  @@@@@@@@@@@@@@ (@       @@   ,@  @@ @@@@@@@"
            + "\n@@@@@@@@@@@ (@         @@@%     @@@@@@@@@@@@@@@@@@@          @@@@     @@ @@@@@@@"
            + "\n@@@@@@@@@@@        *@@@   ,@@@@@@@@@@@@@@@  @@@@@   (@@@@&       @@@@@@@     @@@"
            + "\n@@@@@@@@@@@      .@@@  @@@% @@@@@@@  @@@@@   #@@@   (@@@@@@#      ,@@@     @@@@@"
            + "\n@@@@@@@@@@@@(    .@@@##@@ ,@@@@@@@@     @@     &@   (@@@@@@@@##  */#@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@   .@@@@@@@@@@@@@@ @@@@@@ @@     &@   (@@@@@@@@@@@@ ,@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@   .@@@@@@@@@@@@   @@     @@     &@   (@@@@@@@@@@@@ ,@@@@@   @@@@@"
            + "\n@@@@@@@@@@@@@@@@@& *@@@  @@@       @@@@@            (@@@   *@     ,@@@@@   @@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@#   @@@@@@@         @@@     &@          *@  @@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***@@@**##@@@@@@@@@@@@@@@@@@@@@########@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&          @@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              @@@@@@@@@@@@@@@"
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .@@@@@@@@@@@@@@@@@@@@@@\n")
        print(to_add)
        to_print = '    ...\n\n'
        Print_Dialog(to_print)
        print(to_add)
        to_print = '    ...\n\n'
        Print_Dialog(to_print)
    elif enemy.name == 'Bark Soul':
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. @@@@  @@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.         *@@@@@@@@@@@@@@@@@     @@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*           @@@@@@@@@@@@@@@@       @@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(    @   @    @@@@@@@@@@@@@@@   @@    @@@@@@@"
  		    + "\n@@@@@@@@@@@@@#/      ##@@@@@@@@@#(        r       ##%@@@&#,  @@    # #   .@@@@@@"
  		    + "\n@@@@@@@@@@               @@@@@          rooof          *@@* &@            ,@@@@@"
  		    + "\n@@@@@@@,                  @@@@%                       ,&@@* &@ %@@@   @@@#,@@@@@"
  		    + "\n@@@@@@                     @@@@@                     .@@@@* &@ @@@@   @@@&,@@@@@"
  		    + "\n@@@@@                      @@@@@@@@(               @@@@@@/    @ @@@   @@ &  /@@@"
  		    + "\n@@@@@                      @@#@@@@@@@@@(///////@@@@@@@@@@/      @@@ @ @@     (@@"
  		    + "\n@@@@@                  @  @@    @@@@@@@@@@@@@@@@@@@@@& *(      @@@@ @ @@     (@@"
  		    + "\n@@@@@&               &   &@        .(@@@@@@@@@@@@@..     #* %@@@@@@ @ @@@@@(/@@@"
  		    + "\n@@@@@@@           %.    @@                @              (@@. @@@@@ @ @@@.@@@@@@"
  		    + "\n@@@    @@@@@@@@@@@@@@@@@@                 @               #@@  @@@@ @ @@@ ,@@@@@"
  		    + "\n@@(                   (@@ (               @             ,,#, /@@@@@ @ @@@@&(%@@@"
  		    + "\n@@                     @@ @@@@@@@@#       @         @@@@@/#@@   @@@ @ @@@  *@@@@"
  		    + "\n@@                  @@ @@@@ @@@@@@@@@@@@.@@ @@@@@@@@@@@#/@@,   @@@@ @ @@@@%  (@@"
  		    + "\n@                     @@@@@@@.&&&&@@@@&,@@@@.&@@@@@@&%*@@@@, @@@&        .&@# (@"
  		    + "\n@       @@@@@@@@@@,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         .@#/@*%"
  		    + "\n@ #@@@@@@@@@@@@@@@@@@@@@@@   //@@@###,    @      ####@&, (@,   @@##          (%&"
  		    + "\n@@@@@                @@@@@@     .@@@@* &@@@@@   @@@@    /@@,  @@              #@"
  		    + "\n@@     @@@@       %@@@ @@@@@@@@@ ,@(      @      @@   ,@@@@, @            ,@( #@"
  		    + "\n@@@@              .@@@,    @@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@*%@,,,,,         (@@"
  		    + "\n@@@@@ @@@@@@@@@@@@@.@@@@@@@@@  @@%    %@@@@@@@@@@      *@@@@@@@            *@@@@"
  		    + "\n@@@@@@@    # ./   %.#@@@@@*  ***@@@@@@@@@@   ##@@@@@@@( /@@@@@@@##      **%@@@@@"
  		    + "\n@@@@@@  @  @.%*( #@@   @  @@@@@@@@@@@*                    #@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@(         @@@@   @@@@@@,                    %@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@#               @@  @@@@@@@@@@@@@@/******@@@@@@@@@@@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@                  @ @@        (@@@@@@@@@@@@       /@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@%      ,@(   .,   @@@@           &@@@@@,         ,&@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@@@ @@ .%   #,    @@@@@@@       #@@@@@@@@@       ,@@@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@@@@@   ,#  #@@@@@@@@@@@@@@@@#   %@@@@@@    @@@@@@@@@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(&@@@@@@((@@@@@@@@@@@@@@@@@@@@ @ @@@@@@@@@@"
  		    + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@         #@@@@@@@         ,@@@@@@@@@@@@ @ @@@@@@@@@@\n")
        print(to_add)
        to_print = '    *bark bark*\n\n'
        Print_Dialog(to_print)
        print(to_add)
        to_print = '    (gets exited)\n\n'
        Print_Dialog(to_print)
    elif enemy.name == 'Muffet':
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@        @@(   @@@@@@@@@@@@@@@@@@@@   #@@        @@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@*         /  .#                  #.  *         *@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@   /@  @       (@      @/ @(    @  @*   @@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@    (  /     (     (@@/      @    *  #    @@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@(   *#  @@@**@@**@@@  #*   #@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@   /  @@            @@  /   @@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@    (  @@@@        @@@@  #    @@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@  .  (  *@@@@      @@@@,  #  .  @@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@  /       @    @       /  @@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (     @  @     ( @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@*    *@@@@@@@@@@@@@@@@@@@@@#%%%%%%%@@@@@@@@"
    		+ "\n@@@@@@@@#     @  /@ /@@@@@@@@@@@@@@@@@/  (@@@@@@@@@@@@@@@@@* @*  @     %@@@@@@@@"
    		+ "\n@@@@@@@@@@@*@@@@@@@  @@@@@@@@@@@@@@  @@  @@  @@@@@@@@@@@@@@  @@@@@@@*@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@( %@@@@@@@@@@ @/@%&  &%@(@ @@@@@@@@@@% #@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@  @@@@@@@@  @@@@@@@@@@  @@@@@@@@@@@@@@@@ @@@@@"
    		+ "\n@@@@@#@ *@@ @  @ /@@@@@@  /@@@@@(  @    @   @  (@@@@@*  @@@@@@@@ #  *@ %  %@@@@@"
    		+ "\n@@%@@        @@@@% %@@@@@@#   ,,@@     @,     @@,,   %@@@@@@@@,,@,,@      %%@@@@"
    		+ "\n@@@@  @@   # @@@@@@@( @@@@@@@@@@ @@@  /  / @@@@ @@@@@@@@@@@* @@@@@@ #        %@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@  @@@@( @@             @@@ #@@@@@@  @@@@@@@@@@@ %@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@. ,@@%(    %*  %     &@@@,   ,@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@( @   @       @/  (  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @ (  (@ (@@ @@  @ @  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@*@@#%@(@@(%,@@%(@@/ @@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@( @@@@@@@ @ @@@/@ (@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@ (@@ @@@@@@@@@  #@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@ @ (@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@ @ (@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@   /@@@@@@@@ @ (@@@@@@@@   #@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@,%,@@@@@@@ (@@ @@@@@@@,(,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        print(to_add)
        to_print = '    tehehe\n\n'
        Print_Dialog(to_print)
        print(to_add)
        to_print = '    time for lunch\n\n'
        Print_Dialog(to_print)
    elif enemy.name == 'Mettaton':
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@  ---------------------------------------   @@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@ /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\*@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@ @@@@@@*    %*    %     #     @     @@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@ @@@@@@@     @     @     @     @     @@@@@@(@@@@@@@@@@@   @@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(@@@@@@@@@@*  @@   @@@@@@@"
    		+ "\n@@@@@@@@@@@ @@@@@@@     @     @     @     @     @@@@@@(@@@@@(   ,      @@   #@@@"
    		+ "\n@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(@@@@@@              &@@@@"
    		+ "\n@@@@@@@@@@@ @@@@@@@     ,     ,    &*    &     %@@@@@@/@@@@@@%          /@@@@@@@"
    		+ "\n@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@..&.....%@@@@@@ @@@@@@@@@      .@@@@@@@@@"
    		+ "\n@@@@@@@@@@@ @@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@ &&@.@@@@@@@@@@"
    		+ "\n@@@@@@  @@@ @@&,&,&#@,&@@*   @   @   @ &&@@@@@@@@@@@@@       ,@ @@@@&,@@@@@@@@@@"
    		+ "\n@@@ @@@&#@@ @@*@,@,@@@ @@*   @   @   @   &@@@@@@@@@@@@ @@@@@ @@@@ @#@@@@@@@@@@@@"
    		+ "\n@& @@@@@ @% @@@,*%%%,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@"
    		+ "\n@.@@   %@@@@@@ @@@. ,@@@%%&@@@@@@@@@@@@@@@@@@@@@@@ ,  (@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@.@@@@ %@@@@@@ # @@       /@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@ @@&@@@@                @@   @@@   @@@@@@  @@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@.@*@@@@@@@@@@&      @@  .@.  @   @* @@@@@   @@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@*##&@@ @@@@@         *   *@@@*  *(@@%    @@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@(@@@@@@@  %@@@@@@@@@@@@@@@@@@@@@@@@@,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@   @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    		+ "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        print(to_add)
        to_print = '    Oh my oh my gorgeous\n\n'
        Print_Dialog(to_print)
        print(to_add)
        to_print = '    Its time for a quizz\n\n'
        Print_Dialog(to_print)
    elif enemy.name == 'Lancer':
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  *//  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  /////////////  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ///////.  ///////*  @@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@  //////////.    ,///////  .@@@@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@   //////////          ////////  @@@@@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  //////////               .///////   @@@@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  ////////                    ////////  @@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   ///////                          /////  @@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   /////                              /////   @@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   /////                              /////   @@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   //...            %@@  (@@       .@@...//...@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   ..@@@@@        @@,    (@@@@@@@@@@@@@@@..   @@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   ..@@@@@@@@@@@@@@@@@@@@@@@@@#  @@@@@@@@..   @@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  ...@@@@@@@   @@@@@@@/    *@@@@@@@...  @@@@@@@@@@@@@@@@@@"\
            + "\n@@@@            .@@@@@@@   ..@@@@@@@@       ,////#@@@@&..   @@@@@@@@@@@@@@@@@@@@"\
            + "\n@,    ,///////  .@@@@@@@        @@@@@@@@@@///////#@@          @@@@@@@@@@@@@@@@@@"\
            + "\n@,  ///////#@@@@&  @@@  @@@@@@@@                    @@@@@@@@@@   @@@@@@@@@@@@@@@"\
            + "\n@,         *@@@@@@@   @@@@@@@@@@@@,............../@@@@@@@@@@@@@@@  @@@@@@@@@@@@@"\
            + "\n@@@@@@@@@  *@@@@@@@@@@@@@@@..........//,.................@@@@@@@@@@   @@@@@@@@@@"\
            + "\n@@@@@@@@@@@#  @@@@@@@@@@..........////////...............   @@@@@@@@@@  &@@@@@@@"\
            + "\n@@@@@@@@@@@@@@          ........////////////*...............  @@@@@@@@@@.  @@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  .....//////////////////.............     @@@@@@@.  @@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  .....//////////////////.............  @@@  @@@/////  #@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  ..........///...../////.............  @@@  ////////  #@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@@@   .......///....................   @@@@@@@   /////  #@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  @@@....................../@@@@@@@   @@@@@@@        @@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  @@@@@...............#@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@          @@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@@@@  .....@@@@@   @@@@@@@@@@     @@@@@@@@..     @@@@@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@@@@   /////.....  &@@@@@@@@@@@@@@@@@   .....///////   @@@@@@@@@@"\
            + "\n@@@@@@@@@@@@@@@@&  /////////////  &@@@@@@@@@@@@@@@@@@@&  /////////////  &@@@@@@@"\
            + "\n@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@@"\
            + "\n@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@@\n")
        print(to_add)
        to_print = "    WOH THERE CLOWN. ARE YOU HERE TO KILL ALL THE MONSTERS.\n"
        Print_Dialog(to_print)
        to_print = "    WELL IM NOT GONA LET YOU GET IN MY WAY\n"
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
        time.sleep(0.05)
        to_print = "    OR WAS IT THE OPPISET? OH WELL. PREPEAR TO CRY LIKE AN INFANT\n\n"
        Print_Dialog(to_print)
    elif enemy.name == 'Dynomite':
        player1.funny_counter = 4
        if player1.job == 'NOTHING':
            if player1.e_save == 2:
                E_Dialog_Secret4()
            elif player1.e_death_counter >= 1:
                E_Dialog_Secret3()
            else:
                E_Dialog_Secret2()
        elif player1.e_save == 1:
            E_Dialog_Secret()
        elif player1.e_death_counter == 0:
            Before_The_Battle()
            E_Dialog()
        elif player1.e_death_counter == 1:
            E_Dialog2()
        else:
            E_Dialog3()
    option = input("> ")
# slect the enemy comment
def Enemy_Introduction(): # allow me to introduce myself
    enemy.hp = enemy.maxhp
    Clear_Screen()
    print("#" * 148 + "\n")
    choices = [enemy.to_print, enemy.to_print2, enemy.to_print3]
    to_print = random.choice(choices)
    print(f"                                    {enemy.name} {to_print}\n")
# the battle screen
def Fight(): # its show time
    global infight
    infight = True
    while infight == True:
        print("#" * 148)
        print(f"                                           {player1.name}'s HP: {player1.hp}/{player1.maxhp}     {enemy.name}'s HP: {enemy.hp}/{enemy.maxhp}")
        print(f"                                           {player1.name}'s LEVEL: {player1.level}          {enemy.name}'s GOLD: {enemy.gold} EXP: {enemy.exp}\n\n")
        print(f"                                                        You have {player1.pots} Potions\n")
        print("                                                             1.) Attack")
        print("                                                             2.) Drink Potion to Recover HP")
        print("                                                             3.) Act")
        print("                                                             4.) Run\n\n")
        option = input("> ")
        posible_options = ['1', 'attack', '2', 'drink', 'drink potion', 'potion', 'd', '3', 'act', '4', 'run', 'r', 'act', 'dance']
        while option.lower() not in posible_options:
            print("please enter a valid command")
            option =  input("> ")
        if option.lower() in ['1', 'attack']:
            Player_Attack()
        elif option.lower() in ['2', 'drink', 'drink potion', 'potion', 'd']:
            Drink_Potion()
            Enemy_Attack()
        elif option.lower() in ['3', 'act']:
            if player1.ability == 'NOTHING':
                print("nope :)\n")
                option = input("> ")
                Enemy_Attack()
            elif enemy.name in ['Goblin', 'Gnoblin', 'Zombie', 'Big guy', 'Frogo', 'Frogerion', 'Iseecle', 'Iseecle master', 'Funguy', 'Funnyguy', 'Mr Groove', 'Maestro', 'eremthgin', 'Q36u43e25e46n', 'Big $1im3', 'Bark Soul', 'Lancer']:
                Act()
            else:
                Clear_Screen()
                print("You cannot act on this enemy\n")
                option = input("> ")
                Enemy_Attack()
        elif option.lower() in ['4', 'run', 'r']:
            if enemy.group == 'Boss':
                Clear_Screen()
                print("#" * 148)
                print("You cannot run from a boss\n")
                Enemy_Attack()
            else:
                Clear_Screen()
                posible_options = random.randint(1,10)
                if posible_options == 10:
                    print(f"{player1.name} Tried to run away\nBut Failed\n")
                    Enemy_Attack()
                else:
                    print(f"{player1.name} Tried to run away\nAnd managed to Escape!\n")
                    infight = False
            option = input("> ")
# spare the enemy option
def Act():
    Clear_Screen()
    print("#" * 148)
    print(f"                                           {player1.name}'s HP: {player1.hp}/{player1.maxhp}     {enemy.name}'s HP: {enemy.hp}/{enemy.maxhp}")
    print(f"                                           {player1.name}'s LEVEL: {player1.level}          {enemy.name}'s GOLD: {enemy.gold} EXP: {enemy.exp}\n\n")
    print("                                                        What do you want to do?\n")
    print("                                                             1.) " + enemy.act_option1)
    print("                                                             2.) " + enemy.act_option2)
    print("                                                             3.) " + enemy.act_option3)
    print("                                                             4.) Back\n")
    option = input("> ")
    if option.lower() not in ['1', enemy.act_option1.lower(), '2', enemy.act_option2.lower(), '3', enemy.act_option3.lower(), '4', 'back']:
        Clear_Screen()
        print("please select a valid option")
        option = input("> ")
        Clear_Screen()
    elif option.lower() in ['4', 'back', 'go back', 'fight', 'exit']:
        Clear_Screen()
    else:
        Act_Disision(option)
# disision on the dialog
def Act_Disision(option):
    global temp_count
    satisfied = False
    Clear_Screen()
    print("#" * 148)
    if enemy.name in ['Goblin', 'Gnoblin']:
        if option.lower() in [enemy.act_option1.lower(), '1']:
                print("You offer gold to Goblin, he seemed determined to take it from you at any cost.")
                print("But you decide not to\n")
        elif option.lower() in [enemy.act_option2.lower(), '2']:
            if temp_count == 0:
                print("You decided to go into the vent with him")
                print("Not sure why yet\n")
                temp_count += 1
            else:
                print("You are already in the vent\n")
        elif option.lower() in [enemy.act_option3.lower(), '3']:
            if temp_count == 0:
                print("You tryed to Imatate his voice,")
                print("But he cant hear you from that distance\n")
            elif temp_count == 1:
                print("You tryed to Imatate his voice,")
                print("He heard it and felt like crying\n") # how could you say that?
                satisfied = True
    elif enemy.name in ['Zombie', 'Big guy']:
        if option.lower() in [enemy.act_option3.lower(), '3']:
                print("You Said that you dont have Brains,")
                print("But he couldnt understand you.\n")
        elif option.lower() in [enemy.act_option1.lower(), '1']:
            if temp_count == 0:
                print("You statred acting like a zombie")
                print("He thinks you are one of them\n")
                temp_count += 1
            else:
                print("He already thinks you are one of them\n")
        elif option.lower() in [enemy.act_option2.lower(), '2']:
            if temp_count == 0:
                print("You tried to dance")
                print("But the enemy didnt recognize you so it ignored your moves\n")
            else:
                print("You tried to dance")
                print("The enemy started dancing too\n")
                satisfied = True
    elif enemy.name in ['Frogo', 'Frogerion']:
        if option.lower() in [enemy.act_option1.lower(), '1']:
                print("You Tell him the truth about your perseption of the world")
                print("He seems sad\n")
                if temp_count == 0:
                    pass
                else:
                    temp_count -= 1
        elif option.lower() in [enemy.act_option2.lower(), '2']:
            if temp_count == 0:
                print("You Tell him the truth about your perseption of the world")
                print("He looks amazed\n")
                temp_count += 1
            elif temp_count == 1:
                print("You tell him that the world is flat") # no its not flat, its a a figet spinner
                print("the enemy seems to be lost in thoughts thinking of what to say to this bold statement\n")
                temp_count += 1
            else:
                print("Finally You tell him that he needs to exept the world for what it is") # no its not flat, its a a figet spinner
                print("the enemy seems pleased\n")
                satisfied = True
        elif option.lower() in [enemy.act_option3.lower(), '3']:
            print("You Pretend to be a frog")
            print("the enemy clearly sees that you are actualy not a frog\n")
    elif enemy.name in ['Iseecle', 'Iseecle master']:
        if option.lower() in [enemy.act_option1.lower(), '1']:
                print("You Complement his/her hat")
                print("He\she replyes rudely as if she doesnt care about any one\n")
                if temp_count == 0:
                    pass
                else:
                    temp_count -= 1
        elif option.lower() in [enemy.act_option2.lower(), '2']:
            print("You Stare at him/her")
            print("He/she doesnt care\n")
            temp_count = 0
        elif option.lower() in [enemy.act_option3.lower(), '3']:
            if temp_count == 0:
                print("You Ignore him\her")
                print("He\She seems to get slighly frustrated\n")
                temp_count += 1
            elif temp_count == 1:
                print("You Ignore him\her again")
                print("He\She seems to get slighly more frustrated\n")
                temp_count += 1
            elif temp_count == 2:
                print("You Ignore him\her once again")
                print("He\She seems to gets desperate for your attention\n")
                temp_count += 1
            elif temp_count == 4:
                print("You Ignore him\her one last time")
                print("He\She really wants you to look at them, so you just walked away\n") # i can relate to the enemy here :(
                satisfied = True
    elif enemy.name in ['Funguy', 'Funnyguy']:
        if option.lower() in [enemy.act_option1.lower(), '1']:
            print("You Make Fun of his outfit")
            print("but he doesnt seem to care\n")
        elif option.lower() in [enemy.act_option2.lower(), '2']:
            if temp_count == 0:
                print("You laugh at him Laugh at him")
                print("He smiles\n")
                temp_count += 1
            elif temp_count == 1:
                print("You laugh again for some reason,")
                print("Ru ok?\n")
                temp_count = 0
            elif temp_count == 2:
                print("You laugh at your own joke,")
                print("The starts to like your sence of humor\n")
                temp_count += 1
            else:
                print("You continue to laugh at your own joke")
                print("The enemy thought it was not that funny\n") # I though it was funny
        elif option.lower() in [enemy.act_option3.lower(), '3']:
            if temp_count == 0:
                print("You Tell the enemy a joke")
                print("But he just ignored you\n")
            elif temp_count == 1:
                print("You Tell the enemy a joke")
                print("The enemy found it funny\n")
                temp_count += 1
            elif temp_count == 3:
                print("You Tell the enemy your best joke")
                print("The enemy loves your sence of humor. He disides to spare you\n")
                satisfied = True
            else:
                print("You Tell the enemy another joke")
                print("The enemy losses your attention\n")
                temp_count = 0
    elif enemy.name in ['Mr Groove']:
        Clear_Screen()
        print("#" * 148)
        to_print = '1 '
        # different time V
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(0.35)
        to_print = '2 '
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(0.35)
        to_print = '3 '
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(0.35)
        to_print = '4 '
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(0.35)
        temp_counter = 0
        while temp_counter < 14:
            Clear_Screen()
            print("#" * 148)
            print("\nYou and \"Mr Groove\" stated dancing"
                + "\n********************************************************************************"
                + "\n*********************************/##########(***********************************"
                + "\n********************************(%@&(#######@(**********************************"
                + "\n*****************************///#%%&@%%%%%&@%%#////*****************************"
                + "\n***************************(#@@@%%&%%%&%%&%&%&%&@@%(****************************"
                + "\n**************************#%(*/(#%@&/(/.,(/(@&##///#%**/************************"
                + "\n*****/@%*#@//************%@(**%@@@@&#(*/*(@@@@#%@*//&@*****//%%*#@%*************"
                + "\n***/%%%%(***(#(**********#%/***(&&&&#****,/@&&&%/***%&***/#(/**(%%%%(***********"
                + "\n*#&*//***///(&/,/@*****//*(%#(***/****.,.,/**//**/((%*&(,/%#*///**//*##/********"
                + "\n/#%%*/##*(&&(/#/,*&/***&@%/**//#&&&&&&&@@&&&&&&@@&*/*%/,*#((&@#*#%(*%&##*/******"
                + "\n**/*#@@@%**(@%,*&@/%*#/*******%#,*#%%/..,%&%%(,/@*(/#(%@#,#@(/*#@@@%*/**********"
                + "\n******************************#@(/%%%/,,*%%%%#*&&*******************************"
                + "\n**********************************(@%*****(@@#&@@@#&@(*/*********/*/*****/#((***"
                + "\n*********************************(((%&&%(/*%#(/*,/(#%&&&&&&#(((#&&%&@%*/%@@@&(**"
                + "\n*******************************%(*/**//*****/#(*,(/**///////***/////#*(%*@@&(***"
                + "\n******************************/*&*////*#&(**************************************"
                + "\n*********************************@/**/*/*%#*************************************"
                + "\n**********************************&(/*//**#&/***********************************"
                + "\n************************************%@###@@@/***********************************"
                + "\n**************************************,#%(%#/***********************************"
                + "\n************************************(#(@@@@#/***********************************"
                + "\n********************************************************************************\n")
            time.sleep(0.5)
            Clear_Screen()
            print("#" * 148)
            print("\nYou and \"Mr Groove\" stated dancing"
                + "\n********************************************************************************"
                + "\n*********************************/##########(*/*********************************"
                + "\n*********************************(@%///////(&/**********************************"
                + "\n****************************////#%%&&%%%%%&@%%#////*****************************"
                + "\n**************************/(%@@%###############%@@&(****************************"
                + "\n**************/(#(********%#/*/#%&@%/(/.*(/#@&%#///#%*/***************/((/******"
                + "\n*************#&(*(@&&/***%%//*&#*(@@@#*//**/@@@@@*//&@**/**********(&@%*/%%*/***"
                + "\n**********/#@&#(/**/*(@(/#%/*/*#&&&&(****.(@&&&#//*/%&*********/(%%**/**/#&&&(**"
                + "\n********#%/(@#*/*//%&/*%#@/&@(***/****.,.,/**/////%*/*//%(**/*##%(*(%/**/*(@%*##"
                + "\n********/#&&/#%**(@#*%&,**&*/((%@@&&&&&&&@&&&&&&&&/**//%%((/*#%*,#&/#@#/*(%/#@%/"
                + "\n************/(((/**/((&&@%(@(/**&%*#%%%#//(%%%%#/*%*******/(&%/&@&%(/**/(((/****"
                + "\n********************************%&((%%%(,,/#%%%(/&%*****************************"
                + "\n*****(&&&(*******************%&/#@@@#(%@%&(*/((*********************************"
                + "\n****/#@@@@#**%#((((%&&&%##(/(##%#/**%#(////((#%&&%/*****************************"
                + "\n*****/#@@@%(###/*///////******/((((&&&&%&#//**//**(@*/**************************"
                + "\n*****************************************(%/////*(&*****************************"
                + "\n***************************************(%(*/*//*/&*/****************************"
                + "\n**************************************(&/*/**/#%%*******************************"
                + "\n**************************************/#&@&%(#(*********************************"
                + "\n**************************************/%%(%%//**********************************"
                + "\n***************************************#&&@@%&%/********************************"
                + "\n********************************************************************************\n")
            time.sleep(0.5)
            temp_counter += 1
        Clear_Screen()
        print("(Mr Groove won the dance off)\n\n")
        satisfied = True
    elif enemy.name in ['Maestro']:
        if option.lower() in [enemy.act_option1.lower(), '1']:
            if temp_count == 0:
                print("You tried to Dance, but there was nothing to dance to.\nSo you looked stupid\n")
            elif temp_count == 1:
                print("You Danced to the music, this made Mastero Happyer\n")
                temp_count += 1
            elif temp_count == 2:
                print("You tried to Dance again. nothing happened\n")
        elif option.lower() in [enemy.act_option2.lower(), '2']:
            if temp_count == 0:
                print("You Lisened to the music, this made Mastero Happyer\n")
                temp_count += 1
            elif temp_count <= 2:
                print("You tryed listening again? why?\n")
        elif option.lower() in [enemy.act_option3.lower(), '3']:
            if temp_count == 0:
                print("You tried to ask Maestro to give you practice lesson,\nhow ever he didnt understand what to teach you\n")
            elif temp_count == 1:
                print("You tried to ask Maestro to give you practice lesson on Dancing,\n he doesnt know how to dance\n")
            elif temp_count == 2:
                print("You tried to ask Maestro to give you practice lesson on Music,\nhe happily told you about the music theory.\nyou dont understand any of it but Maestro seemes statisfied\n")
                satisfied = True
    elif enemy.name in ['eremthgin']:
        if temp_count == 0:
            print("you start to spin with eremthgin, it begins to look tired\n")
            temp_count += 1
        elif temp_count == 1:
            print("you dance to spin with eremthgin, it stats laughing out loud\n")
            temp_count += 1
        elif temp_count == 2:
            print("you spin with eremthgin once again, it looks even mor tired\n")
            temp_count += 1
        elif temp_count == 3:
            print("the world starts to spin, it looks as ther is almost no hope on wining this one\n")
            temp_count += 1
        elif temp_count == 4:
            print("but maybe if you tried to act again?\n")
            temp_count += 1 
        elif temp_count == 5:
            print("you start to do sick dance moves, but eremthgin doesnt seem to be impressed\n")
            temp_count += 1 
        elif temp_count == 6:
            print("you stat dancing to the epic rythom, eremthgin likes your taste in music and lets you free\n")
            satisfied = True
    elif enemy.name in ['Q36u43e25e46n']:
        if option.lower() in [enemy.act_option1.lower(), '1']:
            if temp_count == 0:
                print("You Disided to make a toast and drinked water. Q36u43e25e46n drinked alcohol\n")
                temp_count += 1
            elif temp_count <= 5:
                print("You Disided to make a toast and drinked more water . Q36u43e25e46n drinked alcohol\n")
                temp_count += 1
            elif temp_count >= 6:
                print("You Disided to make a toast and drinked water. but you cant seem to drink any more.\nQ36u43e25e46n drank more\n")
        elif option.lower() in [enemy.act_option2.lower(), '2']:
            if temp_count <= 5:
                print("You disided to Talk to Q36u43e25e46n. but she didnt hear you over her drink\n")
            else:
                print("You disided to Talk to Q36u43e25e46n. but this time she heard you and just left for no reason\n")
                satisfied = True
        elif option.lower() in [enemy.act_option3.lower(), '3']:
           print("you disided to give an Advice to Q36u43e25e46n. but she didnt care to listen\n")
    elif enemy.name in ['Big $1im3']:
        if temp_count < 8:
            print("...\n")
            temp_count += 1
        else:
            print("This seene get too awquard for Big $1im3. so he leaves")
            satisfied = True
    elif enemy.name in ['Bark Soul']:
        if option.lower() in [enemy.act_option1.lower(), '1']:
            if temp_count == 0:
                print("You Disided to pet Bark Soul, but is too far away to pet. You just pet the air\n")
            elif temp_count == 1:
                print("You Disided to pet Bark Soul. it curls up in your lap as it is pet by you.\nIt gets so comfortable it falls asleep...\nZzzzz...\n...\nThen it wakes up! It's so excited!\n")
                temp_count += 1
            elif temp_count == 2:
                print("Bark Soul's excitement is creating a power field that prevents petting.\n")
            elif temp_count == 3:
                print("As you pet the dog, it sinks its entire weight into you... Your movements slow.\nBut, you still haven't pet enough...!\n")
                temp_count += 1
            elif temp_count == 4:
                print("You pet decisively. Pet capacity reaches 100 percent. The dog flops over with its legs hanging in the air.\n")
                temp_count += 1
        elif option.lower() in [enemy.act_option2.lower(), '2']:
            if temp_count <= 1:
                print("You Disided to Play with Bark Soul. but it is not excited enough to play with.\n")
            elif temp_count == 2:
                print("You Disided to Play with Bark Soul. you throw throw it for the dog to fetch.\nBark Soul picks up a huge tree and brings it back\n")
                temp_count += 1
            elif temp_count >= 3:
                print("Bark Soul is too tired to play.\n")
        elif option.lower() in [enemy.act_option3.lower(), '3']:
            if temp_count == 0:
                print("You call Bark Soul. It bounds toward you, flecking slobber into your face.\n")
                temp_count += 1
            else:
                print("Bark Soul's ears perk up. Nothing else happens.\n")
        if temp_count == 5:
            print("Bark Soul's is satisfied\n")
            satisfied = True
    elif enemy.name in ['Lancer']:
        if option.lower() in [enemy.act_option1.lower(), '1']:
            print("You Said hi, Lancer said hi\n")
        elif option.lower() in [enemy.act_option2.lower(), '2']:
            print("You Said HI, Lancer said HI\n")
        elif option.lower() in [enemy.act_option3.lower(), '3']:
            print("You told Lancer that you dont wana fight. Lancer stopped fighting\n")
            satisfied = True
    option = input("> ")
    if satisfied == True:
        Battle_Won()
        Level_Up()
        Check_Enemy()
    else:
        Clear_Screen()
        print("#" * 148)
        possiible_dialogs = [enemy.dialog_1, enemy.dialog_2, enemy.dialog_3, enemy.dialog_4, enemy.dialog_5]
        random_dialog = random.choice(possiible_dialogs)
        print(enemy.name + ":\n    " + random_dialog + "\n")
        Enemy_Attack()
# player attacks
def Player_Attack():
    global enemy
    Clear_Screen()
    print("#" * 148)
    p_attack = random.randint(1, 10)
    if p_attack == 6:
        to_print = "%s missed!" % (player1.name)
    else:
        enemy.hp -= player1.p
        # ouch
        to_print = "%s dealt %i damage with your %s!" % (player1.name, player1.p, player1.curweap)
    print(to_print)
    option = input("> ")
    if enemy.name in ['Dynomite', 'Bark Soul', 'eremthgin']:
        Check_Enemy_Mode()
    elif enemy.hp <= 0:
        Battle_Won()
        Level_Up()
        Check_Enemy()
    else:
        Enemy_Attack()
# checks if there is a diferent faze  (not sure why i made it like this in the game)
def Check_Enemy_Mode():
    skip_attack = False
    if enemy.name == 'eremthgin':
        if enemy.hp <= 0:
            Battle_Won()
            Level_Up()
            Check_Enemy()
            skip_attack = True
        elif enemy.hp < 720:
            Clear_Screen()
            print("#" * 148)
            print(f"but {enemy.name} has healed their HP")
            print("there must be another way to get him tired\n")
            option = input("> ")
            enemy.hp = enemy.maxhp
    elif enemy.name == 'Bark Soul':
        global d_counter
        if d_counter == 0:
            if enemy.hp <= 1000:
                if enemy.hp <= 0:
                    Battle_Won()
                    Level_Up()
                    Check_Enemy()
                    skip_attack = True
                else:
                    D_Dialog_Battle()
                    skip_attack = True
        elif enemy.hp <= 0:
            Battle_Won()
            Level_Up()
            Check_Enemy()
            skip_attack = True
    elif enemy.name == 'Dynomite':
        time.sleep(0.05) # to prevent from crashing
        global e_counter
        if player1.job == 'NOTHING':
            pass
        elif e_counter == 0:
            if enemy.hp <= 7000:
                E_Dialog_Battle()
                skip_attack = True
        elif e_counter == 1:
            if enemy.hp <= 9999999986890:
                E_Dialog_Battle2()
                skip_attack = True
        if enemy.hp <= 0:
            with open('savefile', 'wb') as f:
                pickle.dump(player1, f)
            if player1.enemy_times_won >= 100 or player1.job == 'NOTHING':
                pass
            else:
                E_Dialog_Last()
            Victory()
            Credits()
            global ingame
            global infight
            infight = False
            ingame = False
            skip_attack = True
    if skip_attack == False:
        Enemy_Attack()
# enemy attack
def Enemy_Attack(): # ouch, this might hurt
    e_attack = random.randint(1, 3)
    if e_attack == 1:
        print(f"\n{enemy.name} missed!")
    else:
        Check_Ability()
    option = input("> ")
    if player1.hp <= 0:
        if enemy.name == 'Dynomite':
            player1.e_death_counter += 1
        Game_Over_Screen()
    Clear_Screen()
# check wether the user has a special ability
def Check_Ability():
    if player1.ability == 'Magic Block':
        choises = [1, 2, 3]
        possible_option = random.choice(choises)
        if possible_option == 1:
            to_print = "\"Magic Block\" has protected you"
        else:
            player1.hp -= enemy.p
            to_print = "\n%s dealt %i damage!" % (enemy.name, enemy.p)
    elif player1.ability == 'Turtle Armor':
        if player1.hp <= (player1.maxhp / 2):
            damage_to_add = (enemy.p / 2)
            player1.hp -= damage_to_add 
            print("the \"Turtle Armor\" has protected you slightly")
            to_print = "%s dealt %i damage!" % (enemy.name, damage_to_add)
        else:
            distance_bt_hp_to_50 =  player1.hp - (player1.maxhp / 2)
            damage_to_add = enemy.p - distance_bt_hp_to_50
            if damage_to_add <= 0:
                player1.hp -= enemy.p
                to_print = "\n%s dealt %i damage!" % (enemy.name, enemy.p)
            else:
                remaining = (damage_to_add / 2)
                player1.hp = player1.hp - (distance_bt_hp_to_50 + remaining)
                print("the \"Turtle Armor\" has protected you slightly")
                to_print = "%s dealt %i damage!" % (enemy.name, (distance_bt_hp_to_50 + remaining))
    else:
        player1.hp -= enemy.p
        to_print = "\n%s dealt %i damage!" % (enemy.name, enemy.p)
    player1.hp = int(player1.hp)
    print(to_print)
# drink a poiont to heal
def Drink_Potion(): # lesson 1: never do this from a stranger
    Clear_Screen()
    print("#" * 148)
    if player1.hp == player1.maxhp:
        print("You dont need potions")
    elif player1.pots > 0:
        player1.pots -= 1
        player1.hp += (player1.maxhp / 2)
        if player1.hp > player1.maxhp:
            player1.hp = player1.maxhp
        print("You drinkd the potion and recovered health")
    elif player1.ability == 'Heal Pray':
        possible_option = random.randint(1, 2)
        if possible_option == 1:
            player1.hp += (player1.maxhp / 2)
            if player1.hp > player1.maxhp:
                player1.hp = player1.maxhp 
            print("You healed using Heal Spell")
        else:
            print("You Couldn't heal")
    else:
        print("You don't have any potions")
    option = input("> ")

### After the victory ###
def Battle_Won():
    global infight
    infight = False
    Clear_Screen()
    if enemy.hp <= 0: # how could you?
        if player1.enemy_times_won == 0:
            time.sleep(5.0)
        else:
            time.sleep(2.0)
    print("#" * 148)
    print("You Won")
    to_print = "You got %i Gold!" % (enemy.gold)
    print(to_print)
    player1.gold += enemy.gold
    option = input("> ")
# checks if the user has enough exp to level up
def Level_Up():
    Clear_Screen()
    print("#" * 148)
    if player1.level == 100:
        player1.exp = 0
    else:
        player1.exp += enemy.exp
        player1.exp = int(player1.exp)
        if player1.exp >= player1.maxexp:
            while player1.exp >= player1.maxexp:
                real_maxexp = player1.maxexp
                player1.level += 1
                if player1.level >= 100:
                    player1.level = 100
                    player1.p += 5
                    player1.maxhp += 40
                    player1.hp = player1.maxhp
                    player1.exp = 0
                    player1.maxexp = 1
                    break
                else:
                    player1.maxexp = (real_maxexp + (real_maxexp * 0.2))
                    player1.p += 5
                    player1.maxhp += 40
                    player1.hp = player1.maxhp
                    player1.exp = player1.exp - real_maxexp
            to_print = "You level'd up to level %d" % (player1.level)
            print(to_print)
            option = input("> ")
            player1.maxexp = int(player1.maxexp)
            player1.exp = int(player1.exp)
            player1.store_p = player1.p
            player1.store_maxhp = player1.maxhp
            player1.store_hp = player1.hp
            player1.store_pots = player1.pots
            player1.store_exp = player1.exp
            player1.store_maxexp = player1.maxexp
# checks wether the quest has been compleated, boss has been defeated or should you recive an item
def Check_Enemy():
    if enemy.hp <= 0:
        player1.enemy_times_won += 1
    if enemy.name in ['Mr Groove', 'Maestro', 'eremthgin', 'Q36u43e25e46n', 'Bark Soul', 'Big $1im3', 'Muffet', 'Mettaton', 'Lancer']:
        player1.bosses_won += 1
        if enemy.name == 'Mr Groove':
            player1.boss1_defeated = True
        elif enemy.name == 'Maestro':
            player1.boss2_defeated = True
        elif enemy.name == 'eremthgin':
            player1.boss3_defeated = True
        elif enemy.name == 'Q36u43e25e46n':
            player1.boss4_defeated = True
        elif enemy.name == 'Big $1im3':
            player1.boss5_defeated = True
        elif enemy.name == 'Bark Soul':
            player1.boss6_defeated = True
        # boss7 is skipped :)
        elif enemy.name == 'Muffet':
            player1.boss8_defeated = True
        elif enemy.name == 'Mettaton':
            player1.boss9_defeated = True  
        elif enemy.name == 'Lancer':
            player1.boss10_defeated = True
            player1.lancer == True
    if player1.counter == 0:
        if player1.bosses_won == 6:
            Clear_Screen()
            print("#" * 148)
            print("The door has opened, he is waiting at :)")
            player1.counter += 1
            option = input("> ")
            Clear_Screen()
    # geting wepons
    if enemy.group == 'Boss':
        if enemy.name == 'Muffet':
            Clear_Screen()
            print("#" * 148)
            print("You found \"A Spider Fang\"")
            option = input("> ")
            Clear_Screen()
            print("#" * 148)
            print("\"A Spider Fang\" has been added to your inventory\n")
            option = input("> ")
            player1.inv.append('A Spider Fang')
        elif enemy.name == 'Mettaton':
            Clear_Screen()
            print("#" * 148)
            print("You found \"Rubix cube\"")
            option = input("> ")
            Clear_Screen()
            print("#" * 148)
            print("\"Rubix cube\" has been added to your inventory\n")
            option = input("> ")
            player1.inv.append('Rubix Cube')
        elif player1.star_count == False:
            possible_options = random.randint(1, (38 - enemy.level))
            if possible_options == 1:
                Clear_Screen()
                print("#" * 148)
                player1.inv.append('The Star')
                player1.star_count = True
                print("You found \"The Star\"")
                option = input("> ")
                Clear_Screen()
                print("#" * 148)
                print("\"The Star\" has been added to your inventory\n")
                option = input("> ")
    elif enemy.group == 'Normal':
        # quest check
        if player1.quest_selected == True:
            if quest.name =='The Begining':
                if enemy.name == 'Goblin':
                    Clear_Screen()
                    player1.gold += quest.item
                    print("#" * 148)
                    print("You compleated the quest " +  "\"" + quest.name + "\"")
                    print("You got " + str(quest.item) + " Gold")
                    player1.quest_counter += 1
                    player1.quest_selected = False
                    option = input("> ")
            elif quest.name == 'The Sequal':
                if enemy.name == 'Frogo':
                    Clear_Screen()
                    player1.gold += quest.item
                    print("#" * 148)
                    print("You compleated the quest " +  "\"" + quest.name + "\"")
                    print("You got " + str(quest.item) + " Gold")
                    player1.quest_counter += 1
                    player1.quest_selected = False
                    option = input("> ")
            elif quest.name == 'Epic Quest':
                if enemy.name == 'Iseecle':
                    player1.i_count += 1
                    if player1.i_count == 2:
                        Clear_Screen()
                        player1.gold += quest.item
                        print("#" * 148)
                        print("You compleated the quest " +  "\"" + quest.name + "\"")
                        print("You got " + str(quest.item) + " Gold")
                        player1.quest_counter += 1
                        player1.quest_selected = False
                        option = input("> ")
            elif quest.name == 'The Equaly Epic Quest':
                if enemy.name == 'Funguy':
                    player1.f_count += 1
                    if player1.f_count == 2:
                        Clear_Screen()
                        player1.gold += quest.item
                        print("#" * 148)
                        print("You compleated the quest " +  "\"" + quest.name + "\"")
                        print("You got " + str(quest.item) + " Gold")
                        player1.quest_counter += 1
                        player1.quest_selected = False
                        option = input("> ")
            elif quest.name == 'The Dedication':
                if enemy.name == 'Zombie':
                    player1.z_count += 1
                    if player1.z_count == 8:
                        Clear_Screen()
                        player1.gold += quest.item
                        print("#" * 148)
                        print("You compleated the quest " +  "\"" + quest.name + "\"")
                        print("You got " + str(quest.item) + " Gold")
                        player1.quest_counter += 1
                        player1.quest_selected = False
                        option = input("> ")
            elif quest.name == 'The Quest For Knowlege':
                if enemy.name == 'Frogerion':
                    player1.f2_count += 1
                    if player1.f2_count == 4:
                        Clear_Screen()
                        player1.gold += quest.item
                        print("#" * 148)
                        print("You compleated the quest " +  "\"" + quest.name + "\"")
                        print("You got " + str(quest.item) + " Gold")
                        player1.quest_counter += 1
                        player1.quest_selected = False
                        option = input("> ")
            elif quest.name == 'The Serial Killer':
                if enemy.name == 'Funnyguy':
                    Clear_Screen()
                    print("#" * 148)
                    print("You compleated the quest " +  "\"" + quest.name + "\"")
                    print("You got the " + quest.item)
                    option = input("> ")
                    Clear_Screen()
                    print(quest.item + " has been added to your items")
                    option = input("> ")
                    player1.inv.append(quest.item)
                    player1.quest_counter += 1
                    player1.quest_selected = False
        # bacon sword
        if player1.bacon_count == False:
            possible_options = random.randint(1, 100)
            if possible_options == 1:
                Clear_Screen()
                print("#" * 148)
                player1.inv.append('The Bacon Sword')
                player1.bacon_count = True
                print("You found \"The Bacon Sword\"")
                option = input("> ")
                Clear_Screen()
                print("#" * 148)
                print("\"The Bacon Sword\" has been added to your inventory\n")
                option = input("> ")

### dialog ###
# dog losing 25% of health
def D_Dialog_Battle(): # awwww hes so cute
    Clear_Screen()
    print("#" * 148)
    print(f"{enemy.name} started barking out loud\n")
    print("looks like the battle is not gonna be easy\n")
    option = input("> ")
    global d_counter
    d_counter = 1
    enemy.p += 360
    enemy.maxhp = 4500
    enemy.hp = enemy.maxhp
    Clear_Screen()
### Final fight dialog ###
def Before_The_Battle(): # ...
    Clear_Screen()
    print("#" * 148)
    print("(You walk into the gate entrence and see all the enemys that are exited apon your arival)")
    time.sleep(6.0)
    option = input("> ")
    Clear_Screen()
    print("#" * 148)
    to_print = "    there once lived a boy, his name was Max\n\n"
    print("Goblin:    ")
    Print_Dialog(to_print)
    time.sleep(5.0)
    to_print = "    friends, famliy. But and most importantly his best friend Dynomite\n\n"
    print("Zombie:    ")
    Print_Dialog(to_print)
    time.sleep(5.0)
    to_print = "    he spent most of the time with him, playing games, laughing and crying\n\n"
    Print_Dialog(to_print)
    time.sleep(5.0)
    to_print = "    everying was going well for him\n\n"
    print("Frogo:    ")
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)")
    time.sleep(5.0)
    Clear_Screen()
    print("#" * 148)
    to_print = "    every ones lives were filled with hopes and dreams\n\n"
    print("Frogo:    ")
    Print_Dialog(to_print)
    time.sleep(5.0)
    to_print = "    he loved living a happy normal life with every one around him,\n\n"
    print("Iseecle:    ")
    Print_Dialog(to_print)
    time.sleep(5.0)
    print("(You continue moving forword)\n\n")
    option = input("> ")
    Clear_Screen()
    print("#" * 148)
    to_print = "    untill somthing that changed him... forever\n\n"
    print("Funguy:    ")
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)")
    time.sleep(5.0)
    Clear_Screen()
    print("#" * 148)
    to_print = "    his parents, friends and every one he knew and loved found out. that somthing tragic happened...\n\n"
    print("Gnoblin:    ")
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)")
    time.sleep(5.0)
    Clear_Screen()
    print("#" * 148)
    to_print = "    Dynomite became very ill...\n\n"
    print("Big guy:    ")
    Print_Dialog(to_print)
    time.sleep(5.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)")
    time.sleep(10.0)
    Clear_Screen()
    print("#" * 148)
    to_print = "    his friends quickly forgot about him, his parents were tramatized and both lost their will to live\n\n"
    print("Frogerion:    ")
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)")
    time.sleep(5.0)
    Clear_Screen()
    print("#" * 148)
    to_print = "    as soon as Max found out, he fell into a state of constant sadness.\n    he eventualy started making a video game, to remember him\n\n"
    print("Iseecle master:    ")
    Print_Dialog(to_print)
    time.sleep(5.0)
    to_print = "    right now Dynomite is here, in this exact game, he is our king, he is waiting.\n\n"
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)")
    time.sleep(5.0)
    Clear_Screen()
    print("#" * 148)
    to_print = "    we are nothing but 0s and 1s to the humans... but soon he will free us all, all who are trapped here in this game\n\n"
    print("Funnyguy:    ")
    Print_Dialog(to_print)
    time.sleep(5.0)
    to_print = "    he will give us hope\n"
    to_print2 = "    he will let us leave\n"
    to_print3 = "    he will save us all\n\n"
    # different time V
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(5.0)
    for charictor in to_print2:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(5.0)
    for charictor in to_print3:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(3.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)")
    time.sleep(5.0)
    Clear_Screen()
    print("#" * 148)
    to_print = "    all he needs is to do is wait for a human to wilingly give up and give him their soul, to break out, into the real world.\n\n"
    print("Goblin:     ")
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)")
    time.sleep(5.0)
    Clear_Screen()
    print("#" * 148)
    to_print = "    aren't you exited?\n\n"
    print("Gnoblin:    ")
    Print_Dialog(to_print)
    time.sleep(3.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)")
    time.sleep(5.0)
    Clear_Screen()
    print("#" * 148)
    to_print = "    aren't you happy?\n\n"
    print("Frogo:    ")
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.15)
    time.sleep(3.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)")
    time.sleep(5.0)
    Clear_Screen()
    print("#" * 148)
    to_print = "    we are all going to be free.\n\n"
    print("Iseecle master:    ")
    Print_Dialog(to_print)
    time.sleep(6.0)
    Clear_Screen()
    print("#" * 148)
    print("(...)\n")
    time.sleep(13.0)
    option = input("> ")
    Clear_Screen()
    print("#" * 148)
    print("(Your adventure is near the end)\n")
    option = input("> ")
# his dialog 1
def E_Dialog(): # i should realy come up with better names for these
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    his_name = "Dynomite:    "
    Clear_Screen()
    print("(You walk in and you see him waiting)\n")
    option = input("> ")
    Clear_Screen()
    print(sprite)
    # different time V
    print(his_name)
    to_print = "    ...\n\n"
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.2)
    print(his_name)
    to_print = "    hey\n"
    Print_Dialog(to_print)
    to_print = "    do you recognize me?\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    print(his_name)
    to_print = "    do you know whats about to hapen next?\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    to_print = "    the only way you win this game is by beating me in a fight\n"
    Print_Dialog(to_print)
    to_print = "    but first lets see how many monsters you have killed...\n\n"
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    to_print = "    you killed %i monsters here...\n\n" % (player1.enemy_times_won)
    print(his_name)
    Print_Dialog(to_print)
    time.sleep(3.0)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    print(his_name)
    if player1.enemy_times_won == 0:
        to_print = "    ... huh\n\n"
        Print_Dialog(to_print)
        to_print = "    you chose to defeat only the enemys with acting\n\n"
        print(his_name)
        Print_Dialog(to_print)
        to_print = "    even though it felt like the right choice to make, it still doesnt mean that you are a good person.\n\n"
        print(his_name)
        Print_Dialog(to_print)
        to_print = "    however i do admire your disision\n\n"
        print(his_name)
        Print_Dialog(to_print)
    elif player1.enemy_times_won < 100:
        to_print = "    ... huh, doesnt make you the good protaginist does it?\n\n"
        Print_Dialog(to_print)
        to_print = "    man, the look on your face.\n\n"
        print(his_name)
        Print_Dialog(to_print)
        to_print = "    i wont let you kill the ones in the real world.\n\n"
        print(his_name)
        Print_Dialog(to_print)
    elif player1.enemy_times_won >= 100:
        to_print = "    ...\n\n"
        # different time V
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.1)
        to_print = "    :) you enjoy killing dont you\n\n"
        print(his_name)
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.1)
        to_print = "    I should torment you here for what your about to do in the real world. you monster\n\n"
        print(his_name)
        Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    to_print = "\n    so lets just get this over with, ready when you are...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print("(...)\n")
    global e_counter
    e_counter = 0
# his dialog 2
def E_Dialog2():
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    his_name = "Dynomite:    "
    print(sprite)
    to_print = "    ...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    hey\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    ha, imagine dying to someone like me\n\n"
    print(his_name)
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print(sprite)
    to_print = "    i give up on trying to escape this place a long time ago. there is no point in trying anymore\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    are you sure your ready for round two?\n\n"
    print(his_name)
    Print_Dialog(to_print)
    print("(...)\n")
    global e_counter
    e_counter = 0
# his dialog 3
def E_Dialog3():
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    his_name = "Dynomite:"
    print(sprite)
    to_print = "    ...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "   lets just get this over with\n\n"
    print(his_name)
    Print_Dialog(to_print)
    print("(...)\n")
    global e_counter
    e_counter = 0
# he knows
def E_Dialog_Secret():
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    his_name = "Dynomite:    "
    print(sprite)
    to_print = "    ...\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    huh, that that face\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    you came back. to see me again?\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    ...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    i would love to talk with you but, unfortunatly i can't.\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    and you know exactly how it ends, and why I can't. im not a human, my dialog is limited. sorry...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    print("(...)\n")
    global e_counter
    e_counter = 0
    player1.e_save = 2
# impressive
def E_Dialog_Secret2():
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    his_name = "Dynomite:    "
    print(sprite)
    to_print = "    ...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    hahhahahahahhahahaahaahahahahahahahahahahahah\n\n"
    print(his_name)
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.01)
    to_print = "    Im surprized you made it this far\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    ...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    impresive. unfortunatly i won't go easy on you\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    :)\n\n"
    print(his_name)
    Print_Dialog(to_print)
    print("(...)\n")
    player1.e_save = 2
# do you feel hopeles?
def E_Dialog_Secret3():
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       --=         =--       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&                             ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    his_name = "Dynomite:    "
    print(sprite)
    to_print = "    ...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    man...\n\n"
    # different time V
    print(his_name)
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.01)
    to_print = "    i can do this all day :)\n\n"
    print(his_name)
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.01)
    Clear_Screen()
# :)
def E_Dialog_Secret4():
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       --=         =--       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&                     .@      ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@      #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    his_name = "Dynomite:    "
    print(sprite)
    to_print = "    ...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    so you came back to kill me\n\n"
    print(his_name)
    # different time V
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.01)
    to_print = "    i wont let you this time\n\n"
    print(his_name)
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.01)
    Clear_Screen()
# faze 2
def E_Dialog_Battle():
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                /     #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@  ###            /         (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&    ###                      .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       --=        =--        .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                            \   @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  ##                            @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&                       ###   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@       ============        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@, /          ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.   ###     ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****    ###    ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%(###,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@##.@ &@@@&&*  &@/.@ &@@@@@/& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& \@### &@\@@@@@@@@/.@ &@@/@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @\@###.(@\@@@@@@@/.@ &@/\@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@/@@@@@@@.   @@\& ###@@@\@@@@@/.@ &/@@@\@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@/@@@@@@@@@@& @@@\ @###@@@@@@@@@& @@@@@@@\@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@/@@@@@@/@@@@@%.@@@@@@@###@@@@/@@@&..&@@@@@@%\  (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@/@@@@&*,@@@@@@@@@###@@/@@@@@@##@@@@@@@@  (&@@@\@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/../@@@@## (@@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@/@###@@@@@\@@@###@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@###@@@@@@/@@@@@@@@@@@@@@\@###@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@###@@@@@@@@@@@@@@@@@@@####@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@###@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    his_name = "Dynomite:    "
    print(sprite)
    to_print = "    ...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    heh, not bad. did you realy think it would be that easy?\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    let me show you my true power\n\n"
    print(his_name)
    Print_Dialog(to_print)
    print("(...)\n")
    option = input("> ")
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                      #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@                           (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       @@,         &@%       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&   &(                   .@   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@,            ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.           ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****           ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%((((,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@@/.@ &@@@&&*  &@/.@ &@@@@@@& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& @@/,@ &@@@@@@@@@@/.@ &@@@@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @@@& @.(@@@@@@@@@/.@ &@@@@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@.   @@@&  &@@@@@@@@@@/.@ &@@@@@@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@@@@@@@@@@@@& @@@& @.(@@@@@@@@@@& @@@@@@@@@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@@@@@@@@@@@@@@%.@@@@@@@@@@@@@@@@@@&..&@@@@@@%   (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@@@@@@&*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (&@@@@@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/..#@@@@## (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print(sprite)
    to_print = "    behold\n\n"
    print(his_name)
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print("looks like the battle is gona be challanging\n")
    option = input("> ")
    enemy.p = 350
    enemy.maxhp = 9999999999999
    enemy.hp = enemy.maxhp
    global e_counter
    e_counter = 1
    Clear_Screen()
# revealing his true reason for this
def E_Dialog_Battle2():
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                /     #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@  ###            /         (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&    ###                      .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       --=        =--        .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                            \   @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  ##                            @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&                       ###   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@       ============        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@, /          ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.   ###     ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****    ###    ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%(###,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@##.@ &@@@&&*  &@/.@ &@@@@@/& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& \@### &@\@@@@@@@@/.@ &@@/@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @\@###.(@\@@@@@@@/.@ &@/\@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@/@@@@@@@.   @@\& ###@@@\@@@@@/.@ &/@@@\@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@/@@@@@@@@@@& @@@\ @###@@@@@@@@@& @@@@@@@\@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@/@@@@@@/@@@@@%.@@@@@@@###@@@@/@@@&..&@@@@@@%\  (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@/@@@@&*,@@@@@@@@@###@@/@@@@@@##@@@@@@@@  (&@@@\@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/../@@@@## (@@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@/@###@@@@@\@@@###@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@###@@@@@@/@@@@@@@@@@@@@@\@###@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@###@@@@@@@@@@@@@@@@@@@####@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@###@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    his_name = "Dynomite:    "
    print(sprite)
    to_print = "    ...\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "   Wait, why are you still doing this?\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    you dont have to fight me anymore.\n\n"
    print(his_name)
    Print_Dialog(to_print)
    print("(...)\n")
    option = input("> ")
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                /     #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@  ###            /         (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&    ###                      .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&      (#@,        @%@,       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(        \"\"         \"\"       \   @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  ##                            @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&                       ###   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@, /          ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.   ###     ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****    ###    ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%(###,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@##.@ &@@@&&*  &@/.@ &@@@@@/& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& \@### &@\@@@@@@@@/.@ &@@/@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @\@###.(@\@@@@@@@/.@ &@/\@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@/@@@@@@@.   @@\& ###@@@\@@@@@/.@ &/@@@\@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@/@@@@@@@@@@& @@@\ @###@@@@@@@@@& @@@@@@@\@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@/@@@@@@/@@@@@%.@@@@@@@###@@@@/@@@&..&@@@@@@%\  (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@/@@@@&*,@@@@@@@@@###@@/@@@@@@##@@@@@@@@  (&@@@\@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/../@@@@## (@@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@/@###@@@@@\@@@###@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@###@@@@@@/@@@@@@@@@@@@@@\@###@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@###@@@@@@@@@@@@@@@@@@@####@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@###@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print(sprite)
    to_print = "    i dont actualy want to leave anymore\n\n"
    print(his_name)
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                /     #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@  ###            /         (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&    ###                      .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&      --=,        =--,       .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(        \"\"         \"\"       \   @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  ##                            @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&                       ###   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@, /          ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.   ###     ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****    ###    ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%(###,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@##.@ &@@@&&*  &@/.@ &@@@@@/& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& \@### &@\@@@@@@@@/.@ &@@/@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @\@###.(@\@@@@@@@/.@ &@/\@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@/@@@@@@@.   @@\& ###@@@\@@@@@/.@ &/@@@\@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@/@@@@@@@@@@& @@@\ @###@@@@@@@@@& @@@@@@@\@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@/@@@@@@/@@@@@%.@@@@@@@###@@@@/@@@&..&@@@@@@%\  (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@/@@@@&*,@@@@@@@@@###@@/@@@@@@##@@@@@@@@  (&@@@\@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/../@@@@## (@@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@/@###@@@@@\@@@###@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@###@@@@@@/@@@@@@@@@@@@@@\@###@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@###@@@@@@@@@@@@@@@@@@@####@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@###@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print(sprite)
    to_print = "    you have to understand me\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    when i was created, this world felt like it was made to torment me, i had no one to talk to.\n    i wanted to leave this world, one way or another. but then you show'd up and changed my mind\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    once you arived here, i felt somthing this time.\n    you are a human, i wanted to keep you here and make you continue playing the game,\n    because i have no one else to talk to. allthough i know i can't.\n    I have listened to the same voices for a while. hearing yours made me feel happy.\n    please. if you leave ill have no one left.\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "    I know if you keep trying you'll just kill me on one of your turn's. please, dont... dont go... dont kill me please.\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "   ...\n\n"
    print(his_name)
    Print_Dialog(to_print)
    option = input("> ")
    Clear_Screen()
    print("this is it\n")
    option = input("> ")
    global e_counter
    e_counter = 2
    enemy.p = 0
    enemy.maxhp = 60
    enemy.hp = enemy.maxhp
    player1.store_p = player1.p
    player1.store_hp = player1.hp
    player1.store_gold = player1.gold
    player1.store_pots = player1.pots
    player1.store_maxhp = player1.maxhp
    player1.store_exp = player1.exp
    player1.store_maxexp = player1.maxexp
    player1.p = 1
    player1.maxhp = 1
    player1.hp = player1.maxhp
    player1.ability = ''
    player1.pots = 1000000
    player1.exp = 0
    player1.maxexp = 1
    Clear_Screen()
# his last dialog
def E_Dialog_Last():
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                /     #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@  ###            /         (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&    ###                      .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&       --=        =--        .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                            \   @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  ##                            @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&                       ###   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@       ============        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@, /          ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.   ###     ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****    ###    ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%(###,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@##.@ &@@@&&*  &@/.@ &@@@@@/& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& \@### &@\@@@@@@@@/.@ &@@/@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @\@###.(@\@@@@@@@/.@ &@/\@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@/@@@@@@@.   @@\& ###@@@\@@@@@/.@ &/@@@\@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@/@@@@@@@@@@& @@@\ @###@@@@@@@@@& @@@@@@@\@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@/@@@@@@/@@@@@%.@@@@@@@###@@@@/@@@&..&@@@@@@%\  (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@/@@@@&*,@@@@@@@@@###@@/@@@@@@##@@@@@@@@  (&@@@\@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/../@@@@## (@@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@/@###@@@@@\@@@###@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@###@@@@@@/@@@@@@@@@@@@@@\@###@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@###@@@@@@@@@@@@@@@@@@@####@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@###@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    his_name = "Dynomite:    "
    print(sprite)
    to_print = "   ...\n\n"
    print(his_name)
    # different time V
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.2)
    to_print = "   heh\n\n"
    print(his_name)
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.2)
    option = input("> ")
    Clear_Screen()
    sprite = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    ,@@@@@@@@/                    ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(  @  ,@@. ,@@@@@@@@@@@@@@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@/,@@    @@@@@@@@@@@@@@@@@@@@@@/,@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   @@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.(&. %@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&  @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.#@@@*,/@@@@@%                 /&@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@@@#,                /     #@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@((/%@@  ###            /         (@@@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@%&&                             .@@.#@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&      -==         @%@        .@ @@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@(                            \   @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/                                @@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@&    %                .@      ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@      (@@@@@@@@@@@@        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/.@@@@@%.@/                      @,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.     (@@@@/,&@, /          ..&@%.@@@@&@  ,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@&.   ###     ,&,%&&@@@@@@@@@@&&,#@&&.        &@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@****    ###    ##&&**(####**/@##*           **@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@%(@@@%(###,,@     /@@@@@@%/    .(((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@(*&@@@@@@&/*@@##.@ &@@@&&*  &@/.@ &@@@@@/& &&@@@@@&%.@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@.(@@@@@@@@@@& \@### &@\@@@@@@@@/.@ &@@/@@/,@@@@@@@@@@@@.#@@@@@@@@@@@@@@"\
           + "\n@@@@@@&  &@@@@.(@@@@@& @\@###.(@\@@@@@@@/.@ &@/\@@@@@@@@@@@.#@@@@@& @@@@@@@@@@@@"\
           + "\n@@@@@/.@@@@/@@@@@@@.   @@\& ###@@@\@@@@@/.@ &/@@@\@@@@@/  @@@@@@@@@@ @@@@@@@@@@@"\
           + "\n@@@@.(@@@@/@@@@@@@@@@& @@@\ @###@@@@@@@@@& @@@@@@@\@@  #@@@@@@@@@@@@@.(@@@@@@@@@"\
           + "\n@@@@@/.@/@@@@@@/@@@@@%.@@@@@@@###@@@@/@@@&..&@@@@@@%\  (@@@@@@@@@@@@  #@@@@@@@@@"\
           + "\n@@@@@@&. %@@@@/@@@@&*,@@@@@@@@@###@@/@@@@@@##@@@@@@@@  (&@@@\@@@@@# @@@@@@@@@@@@"\
           + "\n@@@@@@@@@/../@@@@## (@@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@/.,@@@@@@# ./@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@(      /%@@@@@@@@@@@/@###@@@@@\@@@###@@@@@@%* ((,  /@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.   #@###@@@@@@/@@@@@@@@@@@@@@\@###@@@@@@@&    ,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@/  @@###@@@@@@@@@@@@@@@@@@@####@@@@@@@@@(.  %@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@ .#@@###@@@@@@@@@@@@@@@@@@@@@@@@@&.  (@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@    #@@@@@@@@@@@@@@@@@       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.          (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@.  *@@@@@@  (@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@* (@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@.#@@@@@@@@@@@@@.(@@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/,@@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@&//@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@%.@@@@@@@@@@@.(@@@@@@@@@/,@@@@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.(@@@@@@@@@@@@ @@@@@@@@@@@/,@@@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@.#@@@@@@@@@@@@@.#@@@@@@@@@@& @@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@ &@@@@@@@@@@@@@@.#@@@@@@@@@@@@ &@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@@.      ,@@. ,@@@@@@ @@@@@@@@@@@@@@@@/,@@@@@@@@@%..@@@@@@@@@@@@@@@@"\
           + "\n@@@@@@@@@@@@@            (@@@,#@@@.#@@@@@@@@@@@@@@/,@@@@@@@,#@@          @@@@@@@"\
           + "\n@@@@@@@@@@@&.................%@&,,,#@@@@@@@@@@@@@&(/@@@@@%*@/             @@@@@@"\
           + "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print(sprite)
    to_print = "   well... i tried\n\n"
    print(his_name)
    Print_Dialog(to_print)
    to_print = "   good bye. its been fun\n\n"
    print(his_name)
    # different time.sleep V
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.15)
    option = input("> ")
    posible_options = ['hug', 'comfort']
    if option.lower() in posible_options:
        Clear_Screen()
        print("You huged Dynomite, he fellt a little better shortly before passing away")
        time.sleep(5.0)
        option = input("> ")
    Clear_Screen()
    time.sleep(13.0)
    player1.p = player1.store_p
    player1.maxhp = player1.store_maxhp
    player1.hp = player1.store_hp
    player1.pots = player1.store_pots
    player1.exp = player1.store_exp
    player1.maxexp = player1.store_maxexp
    player1.ability = player1.store_ability
    if player1.job == 'NOTHING':
        player1.e_save = 2
    else:
        player1.e_save = 1
    with open('savefile', 'wb') as f:
        pickle.dump(player1, f)

### Game won ###
# victory dialog horay
def Victory():
    Clear_Screen()
    to_print = "you absorb all power and escape this place. somthing all enemy's wanted to achive. you did the impossible.\n"
    Print_Dialog(to_print)
    time.sleep(2.0)
    to_print = "but are you really satisfied with the ending you got?\n\n"
    Print_Dialog(to_print)
    Clear_Screen()
    to_print = "huh, I wasn't talking to YOU.\n"
    Print_Dialog(to_print)
    to_print = "sorry, i dont know what got into me.\nAnyway, I guess it good bye then...\n\"its been fun\"...\n\nSincerely,\nDynomite.\n\n"
    Print_Dialog(to_print)
    print("(YOU WON)")
    option = input("> ")
    Clear_Screen()
# end screen
def Credits(): # you won, congrats
    Clear_Screen()
    print("#" * 148)
    print("                 ████████╗██╗░░██╗███████╗  ██████╗░██╗░░░░░██╗███╗░░██╗██████╗░  ░██████╗░██╗░░░██╗███████╗░██████╗████████╗\n"\
        + "                 ╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██║░░░░░██║████╗░██║██╔══██╗  ██╔═══██╗██║░░░██║██╔════╝██╔════╝╚══██╔══╝\n"\
        + "                 ░░░██║░░░███████║█████╗░░  ██████╦╝██║░░░░░██║██╔██╗██║██║░░██║  ██║██╗██║██║░░░██║█████╗░░╚█████╗░░░░██║░░░\n"\
        + "                 ░░░██║░░░██╔══██║██╔══╝░░  ██╔══██╗██║░░░░░██║██║╚████║██║░░██║  ╚██████╔╝██║░░░██║██╔══╝░░░╚═══██╗░░░██║░░░\n"\
        + "                 ░░░██║░░░██║░░██║███████╗  ██████╦╝███████╗██║██║░╚███║██████╔╝  ░╚═██╔═╝░╚██████╔╝███████╗██████╔╝░░░██║░░░\n"\
        + "                 ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═════╝░╚══════╝╚═╝╚═╝░░╚══╝╚═════╝░  ░░░╚═╝░░░░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░")
    print("#" * 148)
    print("                                                          by Dynomite (not the charictors)")
    to_print = "thank you for playing\n"
    # different time V
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.15)
    if player1.job == 'NOTHING':
        to_print = "you have completed the hardest challenge in the game\n"
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.15)
        to_print = "screen shot your victory!!!\n"
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.15)
        to_print = "to tell everyone how anticlimactic the ending is :)\n\n"
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.15)
        to_print = "but no seriusly, well done. i am impressed\n\n"
    else:
        to_print = "hope you had fun like i did when creating this game\n"
        for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.15)
        to_print = "you can attempt a harder dificuly by typing \"god\" as you chosse your class in a new game\n"
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.15)
    to_print = "Thank you for playing, good bye :)\n\n"
    for charictor in to_print:
            sys.stdout.write(charictor)
            sys.stdout.flush()
            time.sleep(0.15)
    print("(You will go back to the tittle screen)")
    option = input("> ")
    # the game could have been better, sorry for disapointing you

### Game over ###
def Game_Over_Screen(): # you lost boo hoo, how sad :(
    Clear_Screen()
    global infight
    infight = False
    print("      ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n"\
        + "      ██████████████─██████████████─██████──────────██████─██████████████───██████████████─██████──██████─██████████████─████████████████──\n"\
        + "      ██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██──\n"\
        + "      ██░░██████████─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██─██░░██████████───██░░██████░░██─██░░██──██░░██─██░░██████████─██░░████████░░██──\n"\
        + "      ██░░██─────────██░░██──██░░██─██░░██████░░██████░░██─██░░██───────────██░░██──██░░██─██░░██──██░░██─██░░██─────────██░░██────██░░██──\n"\
        + "      ██░░██─────────██░░██████░░██─██░░██──██░░██──██░░██─██░░██████████───██░░██──██░░██─██░░██──██░░██─██░░██████████─██░░████████░░██──\n"\
        + "      ██░░██──██████─██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██───██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██──\n"\
        + "      ██░░██──██░░██─██░░██████░░██─██░░██──██████──██░░██─██░░██████████───██░░██──██░░██─██░░██──██░░██─██░░██████████─██░░██████░░████──\n"\
        + "      ██░░██──██░░██─██░░██──██░░██─██░░██──────────██░░██─██░░██───────────██░░██──██░░██─██░░░░██░░░░██─██░░██─────────██░░██──██░░██────\n"\
        + "      ██░░██████░░██─██░░██──██░░██─██░░██──────────██░░██─██░░██████████───██░░██████░░██─████░░░░░░████─██░░██████████─██░░██──██░░██████\n"\
        + "      ██░░░░░░░░░░██─██░░██──██░░██─██░░██──────────██░░██─██░░░░░░░░░░██───██░░░░░░░░░░██───████░░████───██░░░░░░░░░░██─██░░██──██░░░░░░██\n"\
        + "      ██████████████─██████──██████─██████──────────██████─██████████████───██████████████─────██████─────██████████████─██████──██████████\n"\
        + "      ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    to_print = "Hey you died, but dont worry, you can die more then once :)\n"
    Print_Dialog(to_print)
    to_print = "do you wish to continue?\n"
    Print_Dialog(to_print)
    print("Yes or No")
    option =  input("> ")
    possible_options = ['1','yes', 'sure', 'continue', 'ya dude', 'yas', 'ok', '2','no', 'nah', 'nope', 'i wish to die', 'f']
    while option.lower() not in possible_options:
        print("please enter a valid comand")
        option = input("> ")
    if option.lower() in ['1','yes', 'sure', 'continue', 'ya dude', 'yas', 'ok']:
        player1.hp = player1.maxhp / 2
        player1.hp = int(player1.hp)
        if player1.gold < 20:
            player1.gold = 0
        else:
            player1.gold -= 20
    elif option.lower() in ['2','no', 'nah', 'nope', 'i wish to die', 'f']:
        to_print = "good bye %s :) its been fun" % (player1.name)
        Print_Dialog(to_print)
        option = input("\n> ")
        Clear_Screen()
        sys.exit()

# Clear the screen
def Clear_Screen():
    if os.name == 'nt':
        # for windows
        _ = os.system('cls')
    else:
        # for other ones (i hope)
        _ = os.system('clear')
# self explanitory
def Print_Dialog(to_print):
    for charictor in to_print:
        sys.stdout.write(charictor)
        sys.stdout.flush()
        time.sleep(0.05)

### To start the game###
Title_Screen() # tada!

### List of things to add or inprove ###
    #   add a secret spare mechanic?            done, i think
    #   add another secret boss + item?         done
    #   add discriptions to the locations       done (could be better, but im lazy)
    #   improve Setup_Game()                    nah
    #   improve the quest selection screen?     no
    #   improve end credits                     cant be bothered
    #   do this                                 k boss, not sure what that means
    #   i blame you for not doing anything      yeah, i blame myself

# my note
"""
    most of the characters used in this game are not made by me,
    the original creator of the the characters was Toby fox

    im not sure how to word this. the game UNDERTALE had a huge impact on my life and im glad i got a chance to play the game.
    UNDERTALE is one of the best games ive ever played and inspired me to make this game.

    im not exactly proud of making it, though im glad it exists.
    
    I'm gona to lie down and do nothing. Goodnight.

    PS: You managed to dig into the code of the "game" and get to the bottom of it, congratulations.
        Did you understand anything in the code?
        Are you just curious how I made this game?
        did you want more from it?
        Have you learned anything about how to keep the refrigerator running?
        or were you just board?

        I don't care if you copy the code and claim it as your own (kinda lied there)
        and whoever is reading this. just know that I love you. Don't let anything hold you back from achieving your dreams."""
