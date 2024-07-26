#AFD = {Q,Sigma,Transicoes,q0,F }
from typing import Any

Q = {'q1','q2'}

alfabeto = {"a","b"}
transicao = [['q1','q2'],
            ['q1','q2']]


transition = {
            'q1': {'a':'q1','b':'q2'},
            'q2': {'a':'q1','b':'q2'}
}
class Automato:
    def __init__(self,
                Q:set,
                alfa:set,
                transition:dict,
                q0:Any,
                F:set):
        
        self.Q = Q
        self.alfa = alfa
        self.transition = transition
        self.F = F
        self.q0 = q0
        self.state = None
    
    def transite(self,character):
        if self.state is None:
            self.state = self.q0
        
        self.state = self.transition[self.state][character]
    
    def accepts(self,word):
        for char in word:
            if char not in self.alfa:
                return False
            self.transite(char)
        
        if not self.state in self.F:
            return False
        
        return True



transition = {
            'q1': {'a':'q1','b':'q2'},
            'q2': {'a':'q1','b':'q3'},
            'q3': {'a':'q2','b':'q2'}
}

afd = Automato(
    Q = {'q1','q2','q3'},
    alfa = {'a','b'},
    transition = transition,
    q0 = 'q1',
    F = {'q2'}

)

print(afd.accepts('bbba'))
