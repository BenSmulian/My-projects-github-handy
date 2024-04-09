import math
import random


WordList = [

    "apple", "banana", "orange", "grape", "kiwi", "melon", "pear", "strawberry", "blueberry", "raspberry",
    "carrot", "potato", "broccoli", "cucumber", "spinach", "lettuce", "pepper", "tomato", "onion", "garlic",
    "dog", "cat", "rabbit", "hamster", "goldfish", "turtle", "parrot", "snake", "lizard", "gerbil",
    "house", "apartment", "cabin", "bungalow", "mansion", "condo", "hut", "cottage", "villa", "duplex",
    "sun", "moon", "star", "planet", "galaxy", "universe", "asteroid", "comet", "nebula", "cosmos",
    "tree", "flower", "grass", "bush", "shrubs", "oak", "maple", "pine", "birch", "willow",
    "shirt", "pants", "dress", "skirt", "jacket", "sweater", "coat", "blouse", "tie", "scarf",
    "car", "bicycle", "motorcycle", "truck", "bus", "train", "airplane", "boat", "helicopter", "submarine",
    "book", "magazine", "newspaper", "novel", "dictionary", "encyclopedia", "journal", "diary", "comic", "storybook",
    "computer", "phone", "tablet", "laptop", "keyboard", "mouse", "monitor", "printer", "router", "speaker",
    "pen", "pencil", "marker", "crayon", "eraser", "sharpener", "highlighter", "ruler", "scissors", "glue",
    "school", "college", "university", "preschool", "kindergarten", "classroom", "library", "gym", "cafeteria", "playground",
    "music", "art", "math", "science", "history", "english", "geography", "physical", "chemistry", "biology",
    "happy", "sad", "angry", "excited", "nervous", "bored", "tired", "hungry", "thirsty",
    "red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black",
    "big", "small", "tall", "short", "long", "wide", "narrow", "thick", "thin",
    "hot", "cold", "warm", "cool", "freezing", "boiling", "mild", "spicy", "sweet",
    "fast", "slow", "quick", "easy", "hard", "simple", "complex", "smooth", "rough",
    "loud", "quiet", "noisy", "silent", "bright", "dark", "light", "heavy", "lightweight",
    "clean", "dirty", "tidy", "messy", "neat", "filthy", "shiny", "dull", "polished",
    "day", "night", "morning", "afternoon", "evening", "dawn", "dusk", "noon", "midnight",
    "summer", "winter", "spring", "autumn", "fall", "January", "February", "March", "April",
    "May", "June", "July", "August", "September", "October", "November", "December", "Monday",
    "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "week", "month", "year",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
    "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred",
    "thousand", "million", "billion", "trillion", "zero", "first", "second", "third", "fourth",
    "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth",
    "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "thirtieth", "fortieth",
    "fiftieth", "sixtieth", "seventieth", "eightieth", "ninetieth", "hundredth", "thousandth", "millionth", "billionth",
    "trillionth", "north", "south", "east", "west", "up", "down", "left", "right", "front",
    "back", "inside", "outside", "top", "bottom", "middle", "center", "edge", "corner", "near",
    "far", "here", "there", "everywhere", "nowhere", "somewhere", "anywhere", "always", "never", "sometimes",
    "often", "rarely", "occasionally", "frequently", "seldom", "daily", "weekly", "monthly", "yearly",
    "today", "tomorrow", "yesterday", "soon", "late", "early", "now", "before", "after", "while",
    "since", "until", "ago", "then", "firstly", "secondly", "thirdly", "finally", "next", "last",
    "also", "and", "but", "or", "because", "so", "therefore", "however", "although", "even",
    "though", "while", "when", "where", "why", "what", "who", "which", "whom", "whose",
    "how", "how much", "how many", "how often", "how long", "if", "unless", "whether", "either",
    "neither", "both", "not only", "but also", "as well as", "either or", "neither nor", "whether or",
    "every", "each", "all", "some", "any", "none", "many", "few", "several", "most",
    "none", "more", "less", "much", "little", "enough", "too", "so", "very", "almost",
    "nearly", "just", "exactly", "well", "better", "best", "bad", "worse", "worst", "good",
    "well", "fine", "great", "awesome", "amazing", "fantastic", "excellent", "outstanding", "superb",
    "delicious", "tasty", "yummy", "sour", "bitter", "sweet", "spicy", "hot", "cold",
    "warm", "cool", "refreshing", "beautiful", "pretty", "handsome", "ugly", "plain", "ordinary",
    "extraordinary", "remarkable", "unbelievable", "wonderful", "marvelous", "splendid", "gorgeous", "charming",
    "lovely", "adorable", "attractive", "fascinating", "interesting", "captivating", "engaging", "appealing", "enticing",
    "delightful", "enchanting", "enjoyable", "pleasant", "satisfying", "fulfilling", "exciting", "thrilling", "exhilarating",
    "fun", "entertaining", "enlightening", "inspiring", "motivating", "encouraging", "uplifting", "positive", "optimistic",
    "cheerful", "happy", "joyful", "jolly", "merry", "lively", "vibrant", "energetic", "spirited",
    "dynamic", "active", "productive", "efficient", "effective", "successful", "prosperous", "wealthy", "rich",
    "affluent", "fortunate", "lucky", "privileged", "blessed", "grateful", "thankful", "appreciative", "content",
    "satisfied", "fulfilled", "accomplished", "proud", "confident", "secure", "comfortable", "relaxed", "peaceful",
    "calm", "serene", "tranquil", "soothing", "restful", "rejuvenating", "refreshing", "reassuring", "reliable",
    "trustworthy", "loyal", "devoted", "dedicated", "committed", "faithful", "consistent", "persistent", "perseverant",
    "patient", "tolerant", "forgiving", "understanding", "compassionate", "empathetic", "sympathetic", "caring", "loving",
    "kind", "generous", "charitable", "altruistic", "selfless", "thoughtful", "considerate", "courteous", "polite",
    "respectful", "honorable", "dignified", "ethical", "moral", "principled", "upright", "virtuous", "noble",
    "honest", "sincere", "genuine", "authentic", "real", "true", "legitimate", "valid", "credible",
    "reliable", "dependable", "substantial", "reasonable", "logical", "rational", "sensible", "practical", "feasible",
    "attainable", "achievable", "possible", "plausible", "credible", "convincing", "persuasive", "compelling", "forceful",
    "effective", "powerful", "impactful", "influential", "inspiring", "motivating", "stimulating", "provocative", "engaging",
    "interesting", "fascinating", "captivating", "intriguing", "appealing", "attractive", "enticing", "enticing", "tempting",
    "alluring", "irresistible", "seductive", "charming", "enchanting", "mesmerizing", "hypnotic", "spellbinding", "entrancing",
    "delightful", "enjoyable", "pleasurable", "satisfying", "gratifying", "fulfilling", "rewarding", "beneficial", "valuable",
    "important", "meaningful", "significant", "substantial", "relevant", "pertinent", "vital", "essential", "crucial",
    "indispensable", "necessary", "required", "obligatory", "mandatory", "compulsory", "fundamental", "basic", "elementary",
    "primary", "essential", "vital", "crucial", "imperative", "paramount", "utmost", "foremost", "predominant",
    "dominant", "chief", "principal", "main", "major", "significant", "essential", "integral", "key",
    "critical", "vital", "important", "relevant", "pertinent", "applicable", "suitable", "appropriate", "acceptable",
    "admissible", "feasible", "possible", "achievable", "attainable", "accessible", "available", "reachable", "obtainable",
    "affordable", "cost-effective", "practical", "usable", "functional", "operational", "efficient", "effective", "productive",
    "successful", "prosperous", "fruitful", "beneficial", "advantageous", "helpful", "useful", "valuable", "significant",
    "substantial", "considerable", "noteworthy", "remarkable", "memorable", "unforgettable", "impressive", "extraordinary", "exceptional",
    "outstanding", "remarkable", "uncommon", "rare", "unique", "distinctive", "special", "exclusive", "particular",
    "specific", "individual", "personal", "private", "intimate", "secret", "confidential", "exclusive", "privileged",
    "unique", "rare", "exceptional", "extraordinary", "uncommon", "unusual", "peculiar", "distinctive", "different",
    "diverse", "varied", "assorted", "mixed", "heterogeneous", "various", "multiple", "many", "numerous",
    "several", "different", "diverse", "varied", "assorted", "mixed", "heterogeneous", "various", "multiple",
    "many", "numerous", "several", "various", "different", "diverse", "many", "several", "varied"]

def Loop():
    UserInput = input("Enter a word: ")
    newWordList = []

    print("\n")
    
    for i,v in enumerate(WordList):
        try:
            if v[0] == UserInput[len(UserInput) - 1] or v[0] == UserInput[len(UserInput) - 1].lower():
                newWordList.append(v)
        except:
            print("HOW DID YOU EVEN BREAK THIS XD")
            return
            
    
    if len(newWordList) > 0:
        try:
            print("here is a word to be it's friend:", newWordList[random.randint(1 ,len(newWordList) - 1)])
        except:
            print("we are sorry for the unfortunate andundelighfull unforgivable case, we are here with you for your mental health, but no friend has been found for this word.")
            return
    else:
        print("HOW DID YOU EVEN BREAK THIS XD")
    
    

while True:
    Loop()
