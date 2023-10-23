/*
 
 Program Design:
 Input word length
 Choose random word
 Loop
    Input guess
    Check guess
    Respond.
 */

#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

// Declare constants
const int MIN = 6;
const int MAX = 6;
const int LIM_6LETTER_DICT = 500;
const string escapeKey = "escapeKey";
const string DICT6LETTERS_FILE = "6-letter_words.txt";
const char cQUOTE = 34;

// Declare functions
int getLength(int, int);
string chooseSecretFromProgram(int);
void processGuess(string, string);

void printDictFromFile(string);
string chooseSecretFromFile(int);
string dictFileName(int);

// Main program
int main() {
    bool isGameOn = true;
    string secret, guess; // the secret word, and a variable for each guess
    int X; // the number of letters in the word
    
    // Input word length
    X = getLength(MIN, MAX);
    if (X <= 0) isGameOn = false;
    
    // Choose the secret word
    secret = chooseSecretFromProgram(X);
    cout << "Secret word of " << X << " letters has been chosen. \n"
        << "Enter " << escapeKey << " to give up. Good luck. \n";
    
    // Main gameplay
    while (isGameOn) {
        cout << "\n\n\n\n\n" << "Your guess: ";
        cin >> guess;
        
        if (guess == secret) {
            cout << "You found the secret word! \n";
            isGameOn = false; break;
        }
        else if (guess == escapeKey) {
            cout << "Exiting program. Secret was: " << secret << "\n";
            isGameOn = false; break;
        }
        else {
            // Process the guess
            processGuess(guess, secret);
        
            // Wait for user cue to reset
            cout << "\n\n\n\n\n" << "Type enter to clear console for next guess. ";
            string reset;
            cin >> reset;
        }
    };
    
    cout << "\n\n";
    return 0;
}

// Return length of x-letter word
int getLength(int min, int max) {
    int length;
    do {
        cout << "Input word length X, so that " << min-1 << " < X < " << max+1 << ": ";
        cin >> length;
        if (!cin) {
            cin.clear();
            cin.ignore();
            cout << "Numbers only \n";
        }
    } while (length < min || length > max) ;
    return length;
}

const string DICT6_LETTER_WORDS[LIM_6LETTER_DICT] = {"abroad", "accept", "access", "across", "acting", "action", "active", "actual", "advice", "advise", "affect", "afford", "afraid", "agency", "agenda", "almost", "always", "amount", "animal", "annual", "answer", "anyone", "anyway", "appeal", "appear", "around", "arrive", "artist", "aspect", "assess", "assist", "assume", "attack", "attend", "august", "author", "avenue", "backed", "barely", "battle", "beauty", "became", "become", "before", "behalf", "behind", "belief", "belong", "berlin", "better", "beyond", "bishop", "border", "bottle", "bottom", "bought", "branch", "breath", "bridge", "bright", "broken", "budget", "burden", "bureau", "button", "camera", "cancer", "cannot", "carbon", "career", "castle", "casual", "caught", "center", "centre", "chance", "change", "charge", "choice", "choose", "chosen", "church", "circle", "client", "closed", "closer", "coffee", "column", "combat", "coming", "common", "comply", "copper", "corner", "costly", "county", "couple", "course", "covers", "create", "credit", "crisis", "custom", "damage", "danger", "dealer", "debate", "decade", "decide", "defeat", "defend", "define", "degree", "demand", "depend", "deputy", "desert", "design", "desire", "detail", "detect", "device", "differ", "dinner", "direct", "doctor", "dollar", "domain", "double", "driven", "driver", "during", "easily", "eating", "editor", "effect", "effort", "eighth", "either", "eleven", "emerge", "empire", "employ", "enable", "ending", "energy", "engage", "engine", "enough", "ensure", "entire", "entity", "equity", "escape", "estate", "ethnic", "exceed", "except", "excess", "expand", "expect", "expert", "export", "extend", "extent", "fabric", "facing", "factor", "failed", "fairly", "fallen", "family", "famous", "father", "fellow", "female", "figure", "filing", "finger", "finish", "fiscal", "flight", "flying", "follow", "forced", "forest", "forget", "formal", "format", "former", "foster", "fought", "fourth", "French", "friend", "future", "garden", "gather", "gender", "german", "global", "golden", "ground", "growth", "guilty", "handed", "handle", "happen", "hardly", "headed", "health", "height", "hidden", "holder", "honest", "impact", "import", "income", "indeed", "injury", "inside", "intend", "intent", "invest", "island", "itself", "jersey", "joseph", "junior", "killed", "labour", "latest", "latter", "launch", "lawyer", "leader", "league", "leaves", "legacy", "length", "lesson", "letter", "lights", "likely", "linked", "liquid", "listen", "little", "living", "losing", "lucent", "luxury", "mainly", "making", "manage", "manner", "manual", "margin", "marine", "marked", "market", "martin", "master", "matter", "mature", "medium", "member", "memory", "mental", "merely", "merger", "method", "middle", "miller", "mining", "minute", "mirror", "mobile", "modern", "modest", "module", "moment", "morris", "mostly", "mother", "motion", "moving", "murder", "museum", "mutual", "myself", "narrow", "nation", "native", "nature", "nearby", "nearly", "nights", "nobody", "normal", "notice", "notion", "number", "object", "obtain", "office", "offset", "online", "option", "orange", "origin", "output", "oxford", "packed", "palace", "parent", "partly", "patent", "people", "period", "permit", "person", "phrase", "picked", "planet", "player", "please", "plenty", "pocket", "police", "policy", "prefer", "pretty", "prince", "prison", "profit", "proper", "proven", "public", "pursue", "raised", "random", "rarely", "rather", "rating", "reader", "really", "reason", "recall", "recent", "record", "reduce", "reform", "regard", "regime", "region", "relate", "relief", "remain", "remote", "remove", "repair", "repeat", "replay", "report", "rescue", "resort", "result", "retail", "retain", "return", "reveal", "review", "reward", "riding", "rising", "robust", "ruling", "safety", "salary", "sample", "saving", "saying", "scheme", "school", "screen", "search", "season", "second", "secret", "sector", "secure", "seeing", "select", "seller", "senior", "series", "server", "settle", "severe", "sexual", "should", "signal", "signed", "silent", "silver", "simple", "simply", "single", "sister", "slight", "smooth", "social", "solely", "sought", "source", "soviet", "speech", "spirit", "spoken", "spread", "spring", "square", "stable", "status", "steady", "stolen", "strain", "stream", "street", "stress", "strict", "strike", "string", "strong", "struck", "studio", "submit", "sudden", "suffer", "summer", "summit", "supply", "surely", "survey", "switch", "symbol", "system", "taking", "talent", "target", "taught", "tenant", "tender", "tennis", "thanks", "theory", "thirty", "though", "threat", "thrown", "ticket", "timely", "timing", "tissue", "toward", "travel", "treaty", "trying", "twelve", "twenty", "unable", "unique", "united", "unless", "unlike", "update", "useful", "valley", "varied", "vendor", "versus", "victim", "vision", "visual", "volume", "walker", "wealth", "weekly", "weight", "wholly", "window", "winner", "winter", "within", "wonder", "worker", "wright", "writer", };
string chooseSecretFromProgram(int length) {
    srand(unsigned(time(0))); // uses the current time to support the rand function
    int secretPosition = rand() % LIM_6LETTER_DICT;

    if (length == 6) {
        return DICT6_LETTER_WORDS[secretPosition];
    }
    
    return "";
}

// Process user guess
void processGuess(string guess, string secret) {
    int letterMatch = 0, positionMatch = 0, X = int(secret.length());
    bool isDup[X]; // a marker to prevent false duplicate positives.

    if (guess.length() != X) {
        cout << "Error: incorrect length. Try again. \n";
        return;
    }

    // Count letter and position matches
    for (int i=0; i<X; i++) {
        // Count letter matches
        // For each guess.letter, compare to each secret.letter; When a letter matches, flag it in the secret to prevent duplicate positives, and break to stop checking this guess.letter
        for (int j=0; j<X; j++) {
            if (!isDup[j] && guess[i] == secret[j]) {
                letterMatch++;
                isDup[j] = true;
                break;
            }
        }
        // Count position matches
        // For each guess.letter, compare to secret.letter in same position
        if (guess[i] == secret[i]) {
            positionMatch++;
        }
    }
    
    cout << guess << " has " << letterMatch << " letter(s) in secret word, "
        << positionMatch << " letter(s) in correct position. ";
}


// ------------------------------------------------------------
// Helper functions

// Get a list of dictionary words from a file, formatted with quotes
// so I can paste it into an array
void printDictFromFile(string sDictFileName) {
    string sDictWord = ""; // for each word in the dictionary
    ifstream dictFile;
    int index = 0;
    
    dictFile.open(sDictFileName);
    sDictWord += cQUOTE;
    
    for (index = 0; !dictFile.eof(); index++) {
        cout << sDictWord;
        dictFile >> sDictWord;
        sDictWord = sDictWord + cQUOTE + ", " + cQUOTE;
    }
    cout << "\n\n Array counter i = " << index << endl;
    
    dictFile.close();
}

