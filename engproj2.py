from tkinter import *
import random

def outputFormatter (arrayVar):
    randomArray = random.choice(arrayVar)
    return randomArray

def outputFormatterTwo (arrayVar, arrayVar2):
    randomArrayTwo = str(random.choice(arrayVar)+", "+random.choice(arrayVar2))
    return randomArrayTwo

def outputFormatterThree (arrayVar, arrayVar2, arrayVar3):
    randomArrayThree = str(random.choice(arrayVar)+", "+random.choice(arrayVar2)+", "+random.choice(arrayVar3))
    if "bald" in randomArrayThree:
        return str("bald")
    else:
        return randomArrayThree



class MainPanel:
    nameGen = " "
    npcGender = " "
    tempRaceEntry = " "
    hairGen = " "
    faceGen = " "
    eyeGen = " "
    jewelryWorn = " "
    godWorship = " "
    trait1 = " "
    trait2 = " "
    trait3 = " "

    SEX = ["Male", "Female"]

    RACE = ["Aarakocra", "Aasimar", "Bugbear", "Dragonborn", "Dwarf", "Elf",
            "Feral Tiefling", "Firbolg", "Genasi", "Gith", "Gnome", "Goblin",
            "Goliath", "Half-Elf", "Halfling", "Half-Orc", "Hobgoblin", "Human",
            "Kenku", "Kobold", "Lizardfolk", "Orc", "Tabaxi", "Tiefling", "Tortle",
            "Triton", "Yuan-ti Pureblood"]

    HAIRSTYLE = ["cropped", "long", "waist length", "short", "bald"]

    HAIRTEXTURE = ["curly", "wavy", "straight", "fine", "thick", "braided"]

    HAIRCOLOR = ["blonde", "black", "brown", "white", "gray", "silver"]

    LIZHEAD = ["Bumpy", "Scaly", "Smooth", "Rough"]

    FACEDESC = ["sharp", "round", "rectangular", "pointed", "Narrow", "gaunt", "full"]

    FACELOOKS = ["repulsive", "ugly", "average", "attractive", "very attractive"]

    EYES = ["green", "brown", "hazel", "blue", "black", "orange", "gray"]

    EYESDESC = ["dull", "sharp", "wide", "watery", "soulful", "squinty", "sunken",
                "empty", "sympathetic", "blinking", "beady", "sleepy", "fiery"]

    JEWELRY = ["necklace", "bracelet", "earring", "earrings", "ring", "nose ring",
                  "Signet ring", "None", "None", "None"] #added extra "none" to balance draw pile

    JEWELDESC = ["Shabby", "Scuffed", "Polished", "Exquisite", "Plain", "Worn",
                 "Old"]

    JEWELCOLOR = ["gold", "silver", "iron", "gemstone", "glass", "wood"]

    GODS = ["Auril, goddess of winter", "Azuth, god of wizards", "Bane, god of tyranny",
            "Beshaba, goddess of misfortune", "Bhaal, god of murder", "Chauntea, goddess of agriculture",
            "Cyric, god of lies", "Deneir, god of writing", "Eldath, goddess of peace",
            "Gond, god of craft", "Helm, god of protection", "Ilmater, god of endurance",
            "Kelemvor, god of the dead", "Lathander, god of birth and renewal",
            "Leira, goddess of illusion", "Lliira, goddess of joy", "Loviatar, goddess of pain",
            "Malar, god of the hunt", "Mask, god of thieves", "Mielikki, goddess of forests",
            "Milil, god of poetry and song", "Myrkul, god of death", "Mystra, goddess of magic",
            "Oghma, god of knowledge", "Savras, god of divination", "Selune, goddess of the moon",
            "Shar, goddess of darkness and loss", "Silvanus, god of wild nature",
            "Sune, goddess of love and beauty", "Talona, goddess of disease and poison",
            "Talos, god of storms", "Tempus, god of war", "Torm, god of courage",
            "Tymora, goddess of good fortune", "Tyr, god of justice", "Umberlee, goddess of the sea",
            "Waukeen, goddess of trade", "None"]

    GODSTYLE = ["Openly ", "Quietly ", "Loudly ", "Privately ", "Personally ", "Occasionally ",
                "Usually ", "Daily "]

    TRAITS = ["xe is a perfectionist", "xe only speaks in rhymes", "xe believes someone's watching xim",
              "xe thinks adventurers are trouble", "xe wants to travel", "xe is a slob",
              "xe prefers animals to people", "xe hates most things", "xe loves music",
              "xe doesn't believe in luck", "xe is suspicious", "xe only eats bread",
              "xe is mentally impaired", "xe is intelligent", "xis parents died when xe was young", "xe is quiet",
              "xe is trustworthy", "xe is a liar", "xe hates all other races", "xe hates Kobolds",
              "xe hates Orcs", "xe hates Mankind", "xe hates Tabaxi", "xe hates Bugbears",
              "xe is interested in magic", "xe is combative", "xe is active",
              "xe loves to eat", "xe is just here for the free food", "xe is cowardly", "xe is brave",
              "xe has big teeth", "xe likes fire", "xe is afraid of the dark", "xe is afraid of fire",
              "xe is slightly insane", "xe is a natural salesman", "xe loves to run",
              "xe is strong", "xe is good with xis hands", "xe believes xe is possessed",
              "xe is afraid of curses", "xe is charismatic", "xe is a tough soldier",
              "xe is a brilliant strategist", "xe is broke", "xe is sneaky", "xe is ambitious",
              "xe can make money", "xe is scholarly", "xe is hard headded", "xe knows many languages",
              "xe cannot read", "xe cannot write", "xe has a bad back", "xe has a joke for every situation",
              "xe rarely speaks", "xe is prone to violence", "xe is always ready to help",
              "xe spend every morning training", "xe is haunted by horrible memories",
              "xe can't keep a secret", "xe can keep a secret", "xe doesn't like the sun",
              "xe speaks in tongues", "xe gets bored easily", "xe has constant wanderlust",
              "xe is fascinated with birds", "xe is fascinated with trees", "xe is fascinated with kitchenware",
              "xe is materialistic", "xe is fascinated with leaves", "xe likes clouds",
              "xe wants to rule people", "xe compares everything to a fight",
              "xe secretly goes out at night looking for feathers", "xe keeps a list of xis fallen enemies",
              "xe intermittently thinks aloud", "xe likes to know how things work",
              "xe is non-materialistic", "xe is quick to forgive", "xe feels uncomfortable around the rich",
              "xe hates the rich", "xe hates the poor", "xe always does what xe is told to",
              "xe never does what xe is told to", "xe always does what xe is told not to do",
              "xe is a natural leader", "xe can't follow orders", "xe is a natural follower",
              "xe hates to drink", "xe wants to be a soldier", "xe wants to be a leader",
              "xe thinks xe's smarter than everyone else", "xe thinks xe's dumber than everyone else",
              "xe probably hates you", "xe doesn't like dirt", "xe distrusts shopkeepers",
              "xe uses very foul language", "xe uses very proper language", "xe never swears",
              "xe always reports crimes", "xe is a criminal", "xe never reports crimes",
              "xe thinks crime is fun", "xe hates the guards", "xe loves the guards",
              "xe is overly sensetive", "xe has a pet cat", "xe has a pet dog", "xe has a pet bird",
              "xe has a pet kobold", "xe has a pet pig", "xe has a pet horse", "xe has a pet cow",
              "xe has a pet frog", "xe has a pet worm", "xe has a pet beetle", "xe has a secret pet",
              "xe has a big secret", "xe hates secrets", "xe always plays fair", "xe has no concept of property",
              "xe likes to steal things", "xe thinks stealing is wrong", "xe collects leaves", "xe collects feathers",
              "xe collects books", "xe collects heads", "xe collects branches", "xe collects people",
              "xe collects instruments", "xe collects bowls", "xe collects stamps", "xe collects paper",
              "xe collects animals", "xe collects secrets", "xe falls in love easily", "xe falls out of love easily",
              "xe is very selfish", "xe is very giving"]

    FEMALEFIRST = ["Abigayl", "Aebria", "Aeobreia", "Breia", "Aedria", "Aodreia", "Dreia",
              "Aeliya", "Aliya", "Aella", "Aemilya", "Aemma", "Aemy", "Amy", "Ami", "Aeria",
              "Arya", "Aeva", "Aevelyn", "Evylann", "Alaexa", "Alyxa", "Alina", "Aelina",
              "Aelinea", "Allisann", "Allysann", "Alyce", "Alys", "Alysea", "Alyssia", "Aelyssa",
              "Amelya", "Maelya", "Andreya", "Aendrea", "Arianna", "Aryanna", "Arielle", "Aryell",
              "Ariella", "Ashlena", "Aurora", "Avaery", "Avyrie", "Bella", "Baella", "Brooklinea",
              "Bryanna", "Brynna", "Brinna", "Caemila", "Chloe", "Chloeia", "Claira", "Clayre",
              "Clayra", "Delyla", "Dalyla", "Elisybeth", "Aelisabeth", "Ellia", "Ellya", "Elyana",
              "Eliana", "Eva", "Falyne", "Genaesis", "Genaesys", "Gianna", "Jianna", "Janna", "Graece",
              "Grassa", "Haenna", "Hanna", "Halya", "Harperia", "Peria", "Hazyl", "Hazel", "Jasmyne",
              "Jasmine", "Jocelyne", "Joceline", "Celine", "Kaelia", "Kaelya", "Kathryne", "Kathrine",
              "Kayla", "Kaila", "Kymber", "Kimbera", "Layla", "Laylanna", "Leia", "Leya", "Leah",
              "Lilia", "Lylia", "Dick", "Luna", "Maedisa", "Maelania", "Melania", "Maya", "Mya", "Myla",
              "Milae", "Naomi", "Naome", "Natalya", "Talya", "Nathylie", "Nataliae", "Thalia",
              "Nicola", "Nikola", "Nycola", "Olivya", "Alivya", "Penelope", "Paenelope", "Pynelope",
              "Rianna", "Ryanna", "Ruby", "Ryla", "Samaentha", "Samytha", "Sara", "Sarah", "Savannia",
              "Scarletta", "Sharlotta", "Caerlotta", "Sophya", "Stella", "Stylla", "Valentyna",
              "Valerya", "Valeria", "Valia", "Valea", "Victorya", "Vilettia", "Ximena", "Imaena", "Ysabel",
              "Zoe", "Zoeia", "Zoea", "Zoesia", 'Abryia', 'Abrjia', 'Bryia', 'Brjia', 'Abyiga', 'Abjiga',
              'Adryia', 'Adrjia', 'Dryia', 'Drjia', 'Aleksa', 'Alisya', 'Alisja', 'Aliya', 'Alija', 'Alysann',
              'Alisann', 'Alyss', 'Aliss', 'Amya', 'Amja', 'Andreya', 'Andreja', 'Anika', 'Arya', 'Arja',
              'Aryana', 'Arjana', 'Aryel', 'Arjel', 'Aslyena', 'Asljena', 'Bela', 'Brooka', 'Bruka', 'Brynn',
              'Brinn', 'Dalilja', 'Dalilya', 'Elisabet', 'Ellya', 'Ellja', 'Elyana', 'Eljana', 'Ema', 'Emili',
              'Amilja', 'Eva', 'Eva', 'Falyne', 'Faline', 'Feryia', 'Ferjia', 'Graya', 'Graja', 'Halya',
              'Halja', 'Hanna', 'Hazel', 'Isabel', 'Ysabel', 'Jenesa', 'Yenesa', 'Kalya', 'Kalja', 'Kamilia',
              'Kamilja', 'Karlata', 'Sharla', 'Katrina', 'Katya', 'Katja', 'Kayla', 'Kaila', 'Klara', 'Kloya',
              'Kloja', 'Kyma', 'Kima', 'Lana', 'Leya', 'Leja', 'Lilja', 'Lilya', 'Lina', 'Lyna', 'Alyna',
              'Lippi', 'Pippi', 'Loona', 'Lona', 'Madyisa', 'Madjisa', 'Maya', 'Maja', 'Melanya', 'Melanja',
              'Lanya', 'Lanja', 'Milya', 'Milja', 'Miya', 'Mija', 'Myla', 'Mjila', 'Natalya', 'Natalja',
              'Natya', 'Natja', 'Nikola', 'Olifya', 'Olifja', 'Oyara', 'Ojara', 'Perja', 'Perya', 'Ruby',
              'Rubi', 'Ryanna', 'Rjanna', 'Ryila', 'Rjila', 'Samitya', 'Samitja', 'Sara', 'Selyne', 'Seline',
              'Skarlya', 'Skarlja', 'Sofi', 'Sosya', 'Sosja', 'Soya', 'Soja', 'Tella', 'Tylla', 'Valentina',
              'Valerya', 'Valerja', 'Valya', 'Valja', 'Vanna', 'Viktorya', 'Viktorja', 'Vila', 'Vyla', 'Yanna',
              'Janna', 'Yasmine', 'Jasmine', 'Yella', 'Jella', 'Yemina', 'Jemina', 'Yvelyn', 'Iveljin']

    MALEFIRST = ['Aaryn', 'Aaro', 'Aarus', 'Abramus', 'Abrahm', 'Abyl', 'Abelus', 'Adannius', 'Adanno',
                   'Aedam', 'Adym', 'Adamus', 'Aedrian', 'Aedrio', 'Aedyn', 'Aidyn', 'Aelijah', 'Elyjah', 'Aendro',
                   'Androe', 'Aenry', 'Hynroe', 'Hynrus', 'Aethan', 'Aethyn', 'Aevan', 'Evyn', 'Evanus', 'Alecks',
                   'Alyx', 'Alexandyr', 'Xandyr', 'Alyn', 'Alaen', 'Andrus', 'Aendrus', 'Anglo', 'Aenglo', 'Anglus',
                   'Antony', 'Antonyr', 'Astyn', 'Astinus', 'Axelus', 'Axyl', 'Benjamyn', 'Benjamyr', 'Braidyn',
                   'Brydus', 'Braddeus', 'Brandyn', 'Braendyn', 'Bryus', 'Bryne', 'Bryn', 'Branus', 'Caeleb',
                   'Caelyb', 'Caerlos', 'Carlus', 'Cameryn', 'Camerus', 'Cartus', 'Caertero', 'Charlus', 'Chaerles',
                   'Chyrles', 'Christophyr', 'Christo', 'Chrystian', 'Chrystan', 'Connorus', 'Connyr', 'Daemian',
                   'Damyan', 'Daenyel', 'Danyel', 'Davyd', 'Daevo', 'Dominac', 'Dylaen', 'Dylus', 'Elius',
                   'Aeli', 'Elyas', 'Helius', 'Helian', 'Emilyan', 'Emilanus', 'Emmanus', 'Emynwell',
                   'Ericus', 'Eryc', 'Eryck', 'Ezekius', 'Zeckus', 'Ezekio', 'Ezrus', 'Yzra', 'Gabrael',
                   'Gaebriel', 'Gael', 'Gayl', 'Gayel', 'Gaeus', 'Gavyn', 'Gaevyn', 'Goshwa', 'Joshoe',
                   'Graysus', 'Graysen', 'Gwann', 'Ewan', 'Gwyllam', 'Gwyllem', 'Haddeus', 'Hudsyn',
                   'Haesoe', 'Haesys', 'Haesus', 'Handus', 'Handyr', 'Hantus', 'Huntyr', 'Haroldus',
                   'Haryld', 'Horgus', 'Horus', 'Horys', 'Horyce', 'Hosea', 'Hosius', 'Iaen', 'Yan',
                   'Ianus', 'Ivaen', 'Yvan', 'Jaecoby', 'Jaecob', 'Jaeden', 'Jaedyn', 'Jaeremiah',
                   'Jeremus', 'Jasyn', 'Jaesen', 'Jaxon', 'Jaxyn', 'Jaxus', 'Johnus', 'Jonus', 'Jonaeth',
                   'Jonathyn', 'Jordus', 'Jordyn', 'Josaeth', 'Josephus', 'Josaeus', 'Josayah', 'Jovanus',
                   'Giovan', 'Julyan', 'Julyo', 'Jyck', 'Jaeck', 'Jacus', 'Kaevin', 'Kevyn', 'Vinkus',
                   'Laevi', 'Levy', 'Levius', 'Landyn', 'Laendus', 'Leo', 'Leonus', 'Leonaerdo', 'Leonyrdo',
                   'Lynardus', 'Lincon', 'Lyncon', 'Big Johnny Magnum', 'Linconus', 'Logaen', 'Logus', 'Louis', 'Lucius', 'Lucae',
                   'Lucaen', 'Lucaes', 'Lucoe', 'Lucus', 'Lyam', 'Maeson', 'Masyn', 'Maetho', 'Mathoe',
                   'Matteus', 'Matto', 'Maxus', 'Maximus', 'Maximo', 'Maxymer', 'Mychael', 'Mygwell', 'Miglus',
                   'Mythro', 'Mithrus', 'Naemo', 'Naethyn', 'Nathanus', 'Naethynel', 'Nicholaes', 'Nycholas',
                   'Nicholys', 'Nicolus', 'Nolyn', 'Nolanus', 'Olivyr', 'Alivyr', 'Olivus', 'Oscarus',
                   'Oscoe', 'Raen', 'Ryn', 'Robertus', 'Robett', 'Bertus', 'Romyn', 'Romanus', 'Ryderus',
                   'Ridyr', 'Samwell', 'Saemuel', 'Santegus', 'Santaegus', 'Sybasten', 'Bastyen', 'Tago', 'Aemo',
                   'Tagus', 'Theodorus', 'Theodus', 'Thaeodore', 'Thomys', 'Thomas', 'Tommus', 'Tylus',
                   'Tilyr', 'Uwyn', 'Oewyn', 'Victor', 'Victyr', 'Victorus', 'Vincynt', 'Vyncent', 'Vincentus',
                   'Wyttus', 'Wyaett', 'Xavius', 'Havius', 'Xavyer', 'Yago', 'Tyago', 'Tyego', 'Ysaac', 'Aisaac',
                   'Ysaiah', 'Aisiah', 'Siahus', 'Zacharus', 'Zachar', 'Zachaery', 'Aaro', 'Aaryn', 'Abel',
                   'Adryan', 'Adrjan', 'Adym', 'Adam', 'Aksel', 'Aleks', 'Aleksander', 'Alver', 'Andrey', 'Andrej',
                   'Andrus', 'Anton', 'Anyel', 'Anjel', 'Astyn', 'Asten', 'Aydyn', 'Ayden', 'Benyen',
                   'Benjen', 'Brahm', 'Brahn', 'Brandyn', 'Brandjen', 'Branus', 'Bronn', 'Dain', 'Davek',
                   'Dale', 'Damyin', 'Damjin', 'Dan', 'Danyel', 'Danjel', 'Domnik', 'Efan', 'Efjan', 'Efyan',
                   'Elijan', 'Eliyan', 'Elje', 'Elye', 'Emanus', 'Emilyan', 'Emiljan', 'Eryk', 'Erik', 'Esran',
                   'Ethyn', 'Gabrjel', 'Gabryel', 'Gafyn', 'Gafjen', 'Gayl', 'Gail', 'Graysen', 'Graisen',
                   'Hadsen', 'Hudsen', 'Hafyus', 'Hafjus', 'Han', 'Handus', 'Harold', 'Helyan', 'Heljan',
                   'Henrik', 'Horgus', 'Hossen', 'Ifjan', 'Yfan', 'Jak', 'Yak', 'Jakob', 'Yakob', 'Jamye',
                   'Jamje', 'Jan', 'Yak', 'Jasyn', 'Jasjen', 'Johan', 'Yohan', 'Joren', 'Yoren', 'Josef',
                   'Yosef', 'Julyan', 'Juljan', 'Yulian', 'Kaliv', 'Kamrus', 'Kanus', 'Karl', 'Yarl', 'Jarl',
                   'Karlus', 'Kartus', 'Kefyan', 'Kefjan', 'Kristofer', 'Tofer', 'Kristyan', 'Kristjan', 'Lan',
                   'Landen', 'Lefi', 'Lokan', 'Lucyus', 'Lucjius', 'Lukas', 'Lyam', 'Ljam', 'Lyenard', 'Ljenard',
                   'Lynkus', 'Linkus', 'Lyonus', 'Ljonus', 'Lyuk', 'Ljuk', 'Maks', 'Masyn', 'Matye', 'Matje',
                   'Matyus', 'Matjus', 'Miglus', 'Mitye', 'Mitje', 'Mykael', 'Natyan', 'Natjan', 'Natyanus', 'Natjanus',
                   'Nikolas', 'Nolen', 'Nom', 'Oskar', 'Owyn', 'Ojin', 'Remus', 'Robyet', 'Robjet', 'Romyn',
                   'Romen', 'Ryderus', 'Riderus', 'Ryn', 'Rjan', 'Sammen', 'Santyeg', 'Santjeg', 'Sebastyan',
                   'Sebastjan', 'Sekyus', 'Sekjus', 'Skarye', 'Skarje', 'Teodus', 'Teddus', 'Tomus', 'Tylus',
                   'Tilus', 'Viktor', 'Viktus', 'Vintus', 'Vyntus', 'Wilhelm', 'Wyat', 'Wjat', 'Yaden', 'Jaden',
                   'Yaks', 'Jaks', 'Yaksen', 'Jaksen', 'Yesten', 'Jesten', 'Ygan', 'Egan', 'Yofan', 'Jofan',
                   'Yonaf', 'Jonaf', 'Yoshen', 'Joshen', 'Yosyen', 'Josjen', 'Ysak', 'Isak', 'Isaak', 'Ysiah', 'Isjah', 'Isajas']

    SURNAME = ['Biggs', 'Bigg', 'Byggs', 'Camp', 'Campman', 'Coates', 'Frost',
                   'Furrs', 'Furrman', 'Graysky', 'Whitesky', 'Blacksky', 'Grey', 'Gray', 'Hardy',
                   'Hardison', 'Hardland', 'Harland', 'Hills', 'Hill', 'Hylls', 'Hunter', 'Huntsman',
                   'Ice', 'Iceland', 'Icewind', 'Icecutter', 'Yceland', 'Ycewind', 'Ycecutter',
                   'Longnight', 'Longdark', 'Moon', 'Wintermoon', 'North', 'Northman', 'Norman',
                   'Northland', 'Norland', 'Pix', 'Pickman', 'Pickes', 'Pyckes', 'Seales', 'Seals',
                   'Silver', 'Silvermoon', 'Sylver', 'Snow', 'Snowes', 'Star', 'Starr', 'Northstar',
                   'Stone', 'Stoneman', 'Strider', 'Stryder', 'Walker', 'White', 'Whyte', 'Winter',
                   'Winters', 'Wynters', 'Bay', 'Bayes', 'Brand', 'Carrier', 'Carryer', 'Carter',
                   'Carton', 'Cartwright', 'Chestnut', 'Colt', 'Colter', 'Driver', 'Dryver', 'Foote',
                   'Handler', 'Mares', 'Mayr', 'Mair', 'Porter', 'Quicke', 'Quick', 'Reines', 'Reynes',
                   'Reins', 'Reyns', 'Rider', 'Ryder', 'Ryde', 'Saddler', 'Stall', 'Stalls', 'Staller',
                   'Stallworth', 'Stallman', 'Swift', 'Swyft', 'Trainor', 'Trainer', 'Wain', 'Wayne',
                   'Wayn', 'Wainwright', 'Waynwright', 'Anvill', 'Anvilson', 'Bellows', 'Black', 'Blackiron',
                   'Copper', 'Coppers', 'Farrier', 'Fletcher', 'Fletchett', 'Forger', 'Forgeman',
                   'Goldsmith', 'Grey', 'Greysteel', 'Hammer', 'Hammett', 'Irons', 'Yrons', 'Ironsmith',
                   'Ironshoe', 'Ironhoof', 'Kettle', 'Kettleblack', 'Kettleman', 'Potts', 'Pott', 'Pottaker',
                   'Pound', 'Poundstone', 'Shields', 'dong', 'Shieldson', 'Slagg', 'Slagman', 'Smith', 'Smyth',
                   'Smitts', 'Smittens', 'Smitty', 'Smythett', 'Smoke', 'Smoker', 'Steel', 'Steele',
                   'Steelman', 'Swords', 'Swordson', 'Tinn', 'Tinman', 'Tynn', 'Tyne', 'Tine', 'Billy',
                   'Billie', 'Bluffe', 'Bluffclimber', 'Boulder', 'Bulder', 'Camp', 'Campman', 'Claymer',
                   'Clayms', 'Claimer', 'Cole', 'Coler', 'Coleman', 'Coalman', 'Coaler', 'Coaldigger',
                   'Coledegger', 'Condor', 'Condorman', 'Cragg', 'Cragman', 'Diggs', 'Digger', 'Diggman',
                   'Digger', 'Diggett', 'Dragonhoard', 'Dragonhord', 'Dragon', 'Drake', 'Dredge', 'Dredger',
                   'Hall', 'Haul', 'Heights', 'Hights', 'Hytes', 'Hites', 'Highland', 'Hills', 'Hill',
                   'Hillclimber', 'Hylltopper', 'Hoard', 'Hord', 'Hoar', 'Hoardigger', 'Hordegger', 'Kidd',
                   'Kipman', 'Kipper', 'Kipson', 'Kopperfield', 'Miner', 'Myner', 'Mynor', 'Minor',
                   'Sandflats', 'Stoneflats', 'Flowers', 'Gardner', 'Gardener', 'Gardiner', 'Green', 'Greene',
                   'Greenland', 'Greenyard', 'Grove', 'Groveland', 'Hays', 'Hayes', 'Hayward', 'Henkeeper',
                   'Hennerman', 'Herd', 'Hurd', 'Herdland', 'Land', 'Lander', 'Mares', 'Mayr', 'Mair', 'Meadows',
                   'Milk', 'Millet', 'Millett', 'Mills', 'Miller', 'Millard', 'Neeps', 'Neepland', 'Nutt',
                   'Nutman', 'Oates', 'Oats', 'Overland', 'Overfield', 'Peartree', 'Pearman', 'Pease', 'Peapod',
                   'Peabody', 'Picket', 'Picketts', 'Pickens', 'Pickman', 'Plant', 'Planter', 'Ploughman', 'Plowman',
                   'Plougherman', 'Pollen', 'Pollin', 'Polly', 'Pollard', 'Rains', 'Raines', 'Rayns', 'Raynes',
                   'Rainard', 'Root', 'Roote', 'Rutland', 'Shepherd', 'Shepard']


    def __init__(self, master):
        self.master = master
        master.title("DND NPC GENERATOR")
        root.geometry("850x315") #Set default window size
        root.configure(background="#35727a")
        #Generate all the main containers
        mainFrame = Frame(root, width = 400, height = 265, bg="#35727a")
        buttonFrame = Frame(root, width = 800, height = 5, bg="#35727a")
        exportFrame = Frame(root, width=400, height=265, bg="#35727a")

        #Specify locations for containers
        root.grid_columnconfigure(0, weight=1) #gives weight to the columns, allowing sticky
        root.grid_rowconfigure(0, weight=1) #gives weight to the rows, allowing sticky

        buttonFrame.grid_rowconfigure(0, weight=1)
        buttonFrame.grid_columnconfigure(0, weight=1)
        mainFrame.grid(row=0, sticky="w")
        buttonFrame.grid(row=1, sticky="sew")
        exportFrame.grid(row=0, sticky="e")

################################################################################


        #Code for generation. Assigned before button call
        def generateNPC():


            #Gender selector
            self.genderLabel = Label(mainFrame, text="Gender: ", fg='white', bg="#35727a") #Label for gender output
            self.genderLabel.grid(row=1, column=0, sticky="e")
            genderEntry = Entry(mainFrame, width=35, borderwidth=0, bg="#C9DBE4") #Entry field for outputting gender
            genderEntry.grid(row=1, column=1, sticky="ew")
            npcGender = str(outputFormatter(MainPanel.SEX))
            genderEntry.insert("0", npcGender)
            MainPanel.npcGender = "Gender: "+npcGender

            #Name generator

            self.nameLabel = Label(mainFrame, text="Name: ", fg='white', bg="#35727a")
            self.nameLabel.grid(row=0, column=0, sticky="e")
            nameEntry = Entry(mainFrame, width=35, borderwidth=0, bg="#C9DBE4")
            nameEntry.grid(row=0, column=1, sticky="ew")
            if npcGender in "Female":
                femaleName = str(outputFormatter(MainPanel.FEMALEFIRST)+ " "+
                                 outputFormatter(MainPanel.SURNAME)).title()
                MainPanel.nameGen = "Name: "+femaleName
                nameEntry.insert("0", femaleName)
            else:
                maleName = str(outputFormatter(MainPanel.MALEFIRST)+" "+
                               outputFormatter(MainPanel.SURNAME)).title()
                MainPanel.nameGen = "Name: "+maleName
                nameEntry.insert("0", maleName)



            # Race selector
            self.raceLabel = Label(mainFrame, text="Race: ", fg='white', bg="#35727a")
            self.raceLabel.grid(row=2, column=0, sticky="e")
            raceEntry = Entry(mainFrame, width=35, borderwidth=0, bg="#C9DBE4")
            raceEntry.grid(row=2, column=1, sticky="ew")
            tempRaceEntry = str(outputFormatter(MainPanel.RACE))
            raceEntry.insert("0", tempRaceEntry)
            MainPanel.tempRaceEntry = "Race: " + tempRaceEntry

            #Hairstyle selector
            self.hairstyleLabel = Label(mainFrame, text="Hair/head: ", fg='white', bg="#35727a")
            self.hairstyleLabel.grid(row=3, column=0, sticky="e")
            hairstyleEntry = Entry(mainFrame, width=35, borderwidth=0, bg="#C9DBE4")
            hairstyleEntry.grid(row=3, column=1, sticky="w")
            if tempRaceEntry in ["Dragonborn", "Kobold", "Lizardfolk", "Tortle"]:
                hairLiz = str(outputFormatter(MainPanel.LIZHEAD)).capitalize()
                hairstyleEntry.insert("0", hairLiz)
                MainPanel.hairGen = "Head: "+hairLiz
            else:
                hairNormal = str(outputFormatter(MainPanel.HAIRCOLOR)+
                                      ", "+outputFormatter(MainPanel.HAIRTEXTURE)+
                                      ", "+outputFormatter(MainPanel.HAIRSTYLE)).capitalize()
                hairstyleEntry.insert("0", hairNormal)
                MainPanel.hairGen = "Hair: "+hairNormal

            #Face selector
            self.faceLabel = Label(mainFrame, text="Face: ", fg='white', bg="#35727a")
            self.faceLabel.grid(row=4, column=0, sticky="e")
            faceEntry = Entry(mainFrame, width=35, borderwidth=0, bg="#C9DBE4")
            faceEntry.grid(row=4, column=1, sticky="w")
            faceGen = str(outputFormatter(MainPanel.FACEDESC)+", "+
                          outputFormatter(MainPanel.FACELOOKS)).capitalize()
            faceEntry.insert("0", faceGen)
            MainPanel.faceGen = "Face: "+faceGen

            #eyes GENERATOR
            self.eyeLabel = Label(mainFrame, text="Eyes: ", fg='white', bg="#35727a")
            self.eyeLabel.grid(row=5, column=0, sticky="e")
            eyeEntry = Entry(mainFrame, width=35, borderwidth=0, bg="#C9DBE4")
            eyeEntry.grid(row=5, column=1, sticky="w")
            eyeGen = str(outputFormatter(MainPanel.EYESDESC)+" " + outputFormatter(MainPanel.EYES) + " eyes").capitalize()
            eyeEntry.insert("0", eyeGen)
            MainPanel.eyeGen = "Eyes: "+eyeGen

            #Jewelry Generator
            self.jewelLabel = Label(mainFrame, text="Jewelry: ", fg='white', bg="#35727a")
            self.jewelLabel.grid(row=6, column=0, sticky="e")
            jewelEntry = Entry(mainFrame, width=35, borderwidth=0, bg="#C9DBE4")
            jewelEntry.grid(row=6, column=1, sticky="w")
            jewelryWorn = str(outputFormatter(MainPanel.JEWELRY))
            if "None" in jewelryWorn:
                jewelEntry.insert("0", "None")
                MainPanel.jewelryWorn = "Jewelry: None"
            else:
                fullJewel = str(outputFormatter(MainPanel.JEWELDESC)+" "+
                                  outputFormatter(MainPanel.JEWELCOLOR)+" "+
                                  jewelryWorn)
                jewelEntry.insert("0", fullJewel)
                MainPanel.jewelryWorn = "Jewelry: "+fullJewel

            #Worships GENERATOR
            self.godLabel = Label(mainFrame, text="Worships: ", fg='white', bg="#35727a")
            self.godLabel.grid(row=7, column=0, sticky="e")
            godEntry = Entry(mainFrame, width=45, borderwidth=0, bg="#C9DBE4")
            godEntry.grid(row=7, column=1, sticky="w")
            godWorship = str(outputFormatter(MainPanel.GODS)).capitalize()
            if "None" in godWorship:
                godEntry.insert("0", "None")
                MainPanel.godWorship = "Worship: None"
            else:
                fullGod = str(outputFormatter(MainPanel.GODSTYLE)+"worships "+
                                godWorship)
                godEntry.insert("0", fullGod)
                MainPanel.godWorship = "Worship: "+fullGod

            #Trait Generator
            self.traitLabel = Label(mainFrame, text="Traits: ", fg='white', bg="#35727a")
            self.traitLabel.grid(row=8, column=0, sticky="e")
            traitEntry = Text(mainFrame, width=35, height=3, font='Segoe 9', borderwidth=0, bg="#C9DBE4")
            traitEntry.grid(row=8, column=1, sticky="ew")
            if "Male" in npcGender:
                maleTrait = str(outputFormatter(MainPanel.TRAITS)).replace('xim', 'him').replace('xe', 'he').replace('xis', 'his').capitalize()
                maleTrait2 = str(outputFormatter(MainPanel.TRAITS)).replace('xim', 'him').replace('xe', 'he').replace('xis', 'his').capitalize()
                maleTrait3 = str(outputFormatter(MainPanel.TRAITS)).replace('xim', 'him').replace('xe', 'he').replace('xis', 'his').capitalize()
                traitEntry.insert("1.0", maleTrait +"\n"+ maleTrait2 + "\n" + maleTrait3)
                MainPanel.trait1 = maleTrait
                MainPanel.trait2 = maleTrait2
                MainPanel.trait3 = maleTrait3
            else:
                femaleTrait = str(outputFormatter(MainPanel.TRAITS)).replace('xim', 'her').replace('xis', 'her').replace('xe', 'she').capitalize()
                femaleTrait2 = str(outputFormatter(MainPanel.TRAITS)).replace('xim', 'her').replace('xis', 'her').replace('xe', 'she').capitalize()
                femaleTrait3 = str(outputFormatter(MainPanel.TRAITS)).replace('xim', 'her').replace('xis', 'her').replace('xe', 'she').capitalize()
                traitEntry.insert("1.0", femaleTrait +"\n"+ femaleTrait2 + "\n" + femaleTrait3)
                MainPanel.trait1 = femaleTrait
                MainPanel.trait2 = femaleTrait2
                MainPanel.trait3 = femaleTrait3
################################################################################
        def exportGen():
            exportLabel = Label(exportFrame, text="Copy/Paste", fg='white', bg="#35727a")
            exportLabel.grid(row=0, column=3, sticky="n")
            exportText = Text(exportFrame, width=53, height=13, borderwidth=0, bg="#C9DBE4")
            exportText.grid(row=1, column=3)
            exportText.insert("1.0", MainPanel.nameGen +"\n"+ MainPanel.npcGender +"\n"+ MainPanel.tempRaceEntry +"\n"+ MainPanel.hairGen +"\n"+
                                    MainPanel.faceGen +"\n"+ MainPanel.eyeGen +"\n"+ MainPanel.jewelryWorn +"\n"+
                                    MainPanel.godWorship +"\n"+ MainPanel.trait1 +"\n"+ MainPanel.trait2 +"\n"+
                                    MainPanel.trait3)


        #Button creation.
        self.gen_button = Button(buttonFrame, text="Generate New", font='Tahoma 10',
        relief=SOLID, borderwidth=1, command=generateNPC, fg='white', bg="#35727a", pady=2, padx=2)
        self.gen_button.grid(row=1, column=0, sticky="ew")
        self.exp_button = Button(buttonFrame, text="Export", command=exportGen,
        font='Tahoma 10', relief=SOLID, borderwidth=1, fg='white', bg="#35727a", pady=2, padx=2)
        self.exp_button.grid(row=1, column=1, sticky="ew")

root = Tk()
my_gui = MainPanel(root)
root.mainloop()
