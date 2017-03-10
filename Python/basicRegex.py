
pattern1 = r"v"

#the + looks for instances where the linked characters are found together
pattern2 = r"s+s"

#\w* allows word characters in front of e
#\b ensures that it is the last letter in the word. \b is a boundary assertion
pattern3 = r"\w*e\b"

# . allows us to select a pattern with a b (random character in the middle) b
pattern4 = r"b.b"
# .+ allows us to select a pattern with a b (one or more random characters in the middle) b

pattern5 = r"b.+b"

pattern6 = r"b.?b"

pattern7 = r"(aeiou)"

pattern8 = r"b.b"

pattern9 = r"[a-z]*([a-z])\1([a-z])\2[a-z]*"

import re
def getMatchingWords(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable",
    "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress",
     "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid",
     "unbearable", "union", "videotape", "aeiou",]
    matches = []

    for word in words:
        if re.search(regex, word):
            matches.append(word)
    return matches
print getMatchingWords(pattern9)
