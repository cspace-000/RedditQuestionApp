import json, re
import pdb
import random


def translate(sentence):
    translators = [TranslateFullMatch(), TranslatePartialMatch(), TranslateStartingMatch(), TranslateEndingMatch()]

    for t in translators:
        sentence = t.translate(sentence)     
    
    return sentence




class TranslateBase():
    def __init__(self, filename):
        self.filename = '.\\dicts\\' + filename
        self.json_dict = self.get_json_dict()
        
    def get_json_dict(self):
        json_file = open(self.filename, 'r')
        return json.load(json_file)        
    
        
    def get_pattern(self, pattern):
        pattern_obj = re.compile(pattern, flags=re.IGNORECASE) 
        return pattern_obj
    
    def repl_func(self, matchobj):
        m = matchobj.group()
        
        repl = random.choice(self.gungan_word)        
        if m.istitle(): return repl.title()
        if m.isupper(): return repl.capitalize()
        if m.islower(): return repl.lower()
        return repl           
    
    def translate(self, sentence):
        #replacing on inumerating through dict, looking for matches throughout entire string    
        for english_word in self.json_dict.keys():

            self.gungan_word = self.json_dict[english_word]
            pattern_obj = self.get_pattern(english_word)    
            
            
            sentence = re.sub(pattern=pattern_obj, 
                                repl=self.repl_func, 
                                string=sentence)
            
        
        return sentence


class TranslateFullMatch(TranslateBase):
    def __init__(self):
        super().__init__(filename= 'full_match.json')

    def get_pattern(self, pattern):
        pattern = r'(?<!\w)?' + pattern + r'(?!\w)'
        pattern_obj = re.compile(pattern, flags=re.IGNORECASE)    
        return pattern_obj

    
class TranslatePartialMatch(TranslateBase):
    def __init__(self):
        super().__init__(filename= 'partial_match.json')
        

class TranslateStartingMatch(TranslateBase):
    def __init__(self):
        super().__init__(filename= 'starting_match.json')

    def get_pattern(self, pattern):
        pattern = r'(?<!\w)?' + pattern + r'(?=\w)'
        return re.compile(pattern, flags=re.IGNORECASE)
                    
class TranslateEndingMatch(TranslateBase):
    def __init__(self):
        super().__init__(filename= 'ending_match.json')

    def get_pattern(self, pattern):
        pattern = r'(?<=\w)' + pattern + r'(?!\w)'
        return re.compile(pattern, flags=re.IGNORECASE)            
            
            


if __name__=='__main__':


    sentence = "....the captured ISIS fighters and families. The U.S. has done far more than anyone could have ever expected, including the capture of 100% of the ISIS Caliphate. It is time now for others in the region, some of great wealth, to protect their own territory. THE USA IS GREAT!"
    sentence = "I've tried to str(array[cnt]) before inserting it, but the same issue is happening, the database only has one column, which is a TEXT value. again 2 . heaven this is a sentance"
    sentence= "He needed a new helmet because his got smashed when he was riding his bike bikes."
    sentence = 'At least they still use her a lot in the video games. more'
    #sentence = 'Can’t believe how badly @FoxNews is doing in da ratings. They played right into da hands of da Radical Left Demo…'
    #sentence = 'parent comment 2'
    sentence = "Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline"
    #TFM = TranslateEndingMatch()
    translated_sentence = translate(sentence)
    print(sentence)
    print('\n')
    print(translated_sentence)





