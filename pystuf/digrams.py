#!/bin/python
import numpy as np
class Semicond:
    
    def __init__(self, Egap, Affinity, Workfunc):
        self.Eg=Egap
        self.Chi=Affinity
        self.Psi=Workfunc
        self.Ec=-self.Chi
        self.Ef=-self.Psi
        self.Ev=self.Ec-self.Eg
        
        
class Metal:
    
    def __init__(self, Workfunc):
        self.Psi=Workfunc

