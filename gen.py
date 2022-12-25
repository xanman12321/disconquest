import random
import math

markov = {}
markov["sta"] = "AAAAAAAAAAABBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCDDDDDEEEEEEEEFFFGGGGGGGGGGGHHHHIIIIIIIIJJJKKKKKLLLLLLLLLMMMMMMMMMMMMMMMMMMNNNNNNNNNNNOPPPPPPPPPPQRRRSSSSSSSSSSSSSSSSSSSSSSSSSSTTTTTTTTTTTUUUUUUUVVVYZZ"
markov[" "] = "AAAAABCEFGGGHIIKKKKLLLMMNNPRRRRSSSSSTTVVZaaaaaadoott"
markov["'"] = "AEIOU"
markov["-"] = "BL"
markov["A"] = "fffllmnnnrrrruuz"
markov["B"] = "aaaaaeeeehiooorruuu"
markov["C"] = "aaaaehhhoooooruyzô"
markov["D"] = "eejoo"
markov["E"] = "cglmqrsst"
markov["F"] = "aiir"
markov["G"] = "aaeehrrruuuuuu"
markov["H"] = "aeoou"
markov["I"] = "cnnrrrssstv"
markov["J"] = "aao"
markov["K"] = "aeiiioouy"
markov["L"] = "aaaeeeeiiiiuu"
markov["M"] = "aaaaaaaaaaaeiooooooy"
markov["N"] = "aaeeeeeiiiooo"
markov["O"] = "m"
markov["P"] = "aaaaaaehoor"
markov["Q"] = "a"
markov["R"] = "eeeiouw"
markov["S"] = "aaaaaaaaeeeeiilloooooprttuuuwwy"
markov["T"] = "aahiooooruuuu"
markov["U"] = "gknnnrz"
markov["V"] = "aeeii"
markov["Y"] = "e"
markov["Z"] = "aei"
markov["a"] = "      -bbbbbccddddddddddegggghhiiiiiiiiiiijkkkllllllllllllllllllllmmmmmmmmmmmmnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnoopppqrrrrrrrrrrrrrssssttttttttttttuuuuuuwyyyyzz"
markov["b"] = " aaaaaaaaeeiiiiiiilllooooouwy"
markov["c"] = "  aaaaaaaaaceeeeehhhiiooorru"
markov["d"] = "          'aaaaaaaaaaeeeiiiiiioooooooosssu"
markov["e"] = "     aaaaaaaabcccdddddeegggiikllllllllmmmmnnnnnnnnnnnnnnnnnoopppprrrrrrrrrrrrrrrssssssssssssttvwwxyyz"
markov["f"] = "  grr"
markov["g"] = "aaaaaaaadeeeehiiloooooooruuuuyy"
markov["h"] = "     aaaaaaeeeeiiiiiorstuu"
markov["i"] = "   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbccccccccccccccdeeegggjjkllllmmnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnoppqrrrsssssssstttttttttttuuvvz"
markov["j"] = "aiii"
markov["k"] = "aehiiiiimr"
markov["l"] = "    aaaaaaaaaaaaaaaaaabddeeegggiiiiiiiiiillooootuvyy"
markov["m"] = "aaaaaaaaaabbbbbbbeeeeeeeiiiiooooo"
markov["n"] = "    aaaaaaaaaaaaaacccdddddddddddddddddddddddeeeeeeeeeeeeeeegggggggggiiiiiiiiiiiiiiiiiiiiiklmmoosttttttttuyyz"
markov["o"] = "  aabccdffgillllllllmmmmmmmmmnnnnnnnnnnnnnnnnoprrrrrrrrrrrrrrrrsssssttuuuuuvvvvz"
markov["p"] = "aaaeiioprtuuuu"
markov["q"] = "uu"
markov["r"] = "-aaaaaaaaaaaaaaaaaabbbbddeeeeeeeeeggggiiiiiiiiiiiiiiiiiiikkkkllmmoooooorrstttuuuuuuuwyz"
markov["s"] = "  achhiiiiillnoorssttttttttttttttww"
markov["t"] = "    aaaaaaaaaaaaaaaeeeeeeeeeeeehhhhhhhhhhhiiiiiiiiiinoorrrrsstuuvz"
markov["u"] = "aaaaaaaaaabbbbcddddeeggiiiilmnnnnrrrrrrrrrrsssssstttttvwxy"
markov["v"] = "aaaaeeiiiio"
markov["w"] = "  aaaaaeii"
markov["x"] = "ei"
markov["y"] = " aaaacpprrsz"
markov["z"] = "aaabeeeeeisu"
markov["ô"] = "t"

def markovnext(c):
    return random.choice(markov[c])

def endChance(x):
    return math.tanh(x/4-2)/2+0.5

def word():
    w = random.choice(markov['sta'])
    while True:
        w += markovnext(w[-1])
        if random.random() < endChance(len(w)):
            break
    return w.strip()