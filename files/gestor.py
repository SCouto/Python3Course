#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:49:55 2019

@author: couto
"""

import pickle

class Personaje():
    
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida  = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
    
    def __str__(self):
        return "{}: vida: {}, ataque: {}, defensa: {}, alcance: {}".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)    
        
        
class Gestor():
    
    
    personajes = []


    def __init__(self):
        self.cargar()
        
    def agregar(self, nuevo):
        found = False
        for current in self.personajes:
            if current.nombre == nuevo.nombre:
                found = True
                break
        
        if not found:
            self.personajes.append(nuevo)
            self.save()
            
        else:
            print ("Personaje {} ya existe".format(nuevo.nombre))
        
        
    def borrar(self, nombre):
        for current in self.personajes:
            if current.nombre == nombre:
                self.personajes.remove(current)
                self.save()
                break
        
        
    def save(self):
         fichero = open('personajes.pckl', 'wb')
         pickle.dump(self.personajes, fichero)
         fichero.close()
        
    def mostrar(self):
        if len(self.personajes) == 0:
            print("El gestor está vacío")
        else:
            for p in self.personajes:
                print(p) 
        
    def cargar(self):
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            #Empty File
            pass
        finally:
            fichero.close()
            print("Cargados {} personajes".format(len(self.personajes)))
        


gestor = Gestor()
gestor.agregar( Personaje("Caballero",4,2,4,2) )
gestor.agregar( Personaje("Guerrero",2,4,2,4) )
gestor.agregar( Personaje("Arquero",2,4,1,8) )
gestor.mostrar()

print("Borramos arquero")
gestor.borrar("Arquero")
gestor.mostrar()
