import os
import json
from random import *

class Entity:
    def __init__(self, _name, _class):
        self.Name = _name
        self.Class = _class
    



'''
triple : [s:Entity, p:String, o:Entity]
'''
def statement_generator(triple, action):
    template = json.load(open('temp.json', 'r', encoding='utf-8'))
    s = triple[0]
    p = triple[1]
    o = triple[2]
    index = randint(0, 9)
    sentence = template[s.Class][p][action][index]
    sentence = sentence.replace('(S)', s.Name).replace('(O)', o.Name).replace('(P)', p)
    
    return sentence

if __name__ == "__main__":
    S = Entity('카이스트', 'University')
    P = 'Country'
    O = Entity('대한민국', 'Country')
    print(statement_generator([S, P, O], 'questions'))