# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:09:12 2015

@author: Dani Bento
"""

# código do jogo da forca - Daniela Bento P. da Cunha

import turtle
window = turtle.Screen() 
window.title("Jogo da Forca!")
window.bgcolor("skyblue")

tortugaL = turtle.Turtle()
tortugaL.pen(shown =False,fillcolor="purple",pencolor="purple")
tortugaL.penup()

arquivo = open("entrada.txt", encoding="utf-8")
p = arquivo.readlines()
lpalavras = []
for i in p:
    g = i.strip()
    if g != "":
        lpalavras.append(g)

n = len(lpalavras)-1
