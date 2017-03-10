
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

# the A-Z, a-z and 0-9 ranges allow us to select a pattern with a b (any character including a 0 in the middle) b
pattern6 = r"b[A-Za-z_][A-Za-z_0-9]b"

# the parenthesis allow us to look for that specific pattern in that specific order.
pattern7 = r"(aeiou)"

#the brackets allow us to search for each individual character in the word "regular expression"
pattern8 = r"[regular expression]"

#???? come back 
pattern9 = r""

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
print getMatchingWords(pattern8)
