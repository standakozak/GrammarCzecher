import re

def normalize_sentence(sentence: str, lowercase=False, remove_diacritics=False, isolate_interpunction=False):
    sentence = sentence.strip()
    if lowercase:
        sentence = sentence.lower()
    
    # Remove structure information in stylistic texts
    sentence = re.sub("V?I{1,3}\.", "", sentence)
    sentence = re.sub("^[a-gA-D123456]\)", "", sentence)

    # Remove hyper-links
    sentence = re.sub("https?\S+", "", sentence)
    sentence = re.sub("www\S+", "", sentence)

    # Remove emoticons
    sentence = re.sub("[:;\.=xX<][^a-zA-Z\s]*o*[\)\(\/oDP!3]+", "", sentence)

    sentence = re.sub('["“#$%&()*+\-\/;=@[\]^_`{|}~\t\n]+', "", sentence)
    sentence = re.sub("'", "", sentence)

    if isolate_interpunction:
        inter_prefix = " "
    else:
        inter_prefix = ""
    # Use single tokens for interpunction
    sentence = re.sub("\.+", inter_prefix + ".", sentence)
    sentence = re.sub(",+", inter_prefix + ",", sentence)
    sentence = re.sub(":+", inter_prefix + ":", sentence)
    sentence = re.sub("\?+", inter_prefix + "?", sentence)
    sentence = re.sub("!+", inter_prefix + "!", sentence)
    sentence = re.sub("  ", " ", sentence)


    if remove_diacritics:
        sentence = re.sub("á", "a", sentence)
        sentence = re.sub("[éě]", "e", sentence)
        sentence = re.sub("í", "i", sentence)
        sentence = re.sub("ý", "y", sentence)
        sentence = re.sub("ó", "o", sentence)
        sentence = re.sub("[ůú]", "u", sentence)
        sentence = re.sub("č", "c", sentence)
        sentence = re.sub("ď", "d", sentence)
        sentence = re.sub("ň", "n", sentence)
        sentence = re.sub("ř", "r", sentence)
        sentence = re.sub("š", "s", sentence)
        sentence = re.sub("ť", "t", sentence)
        sentence = re.sub("ž", "z", sentence)


    return sentence

def split_sentence_to_words(sentence: str, max_length: int | None = None, END_OF_SENTENCE=""):

    sentence_tokens = sentence.strip().split(" ")
    if max_length is None:
        max_length = len(sentence_tokens) + 1
    
    #return [[START_OF_SENTENCE] + sentence_tokens[i:i+max_length-2] + [END_OF_SENTENCE] for i in range(0, len(sentence_tokens), max_length-2)]
    
    return [sentence_tokens[i:i+max_length-1] + [END_OF_SENTENCE] for i in range(0, len(sentence_tokens), max_length-1)]
    