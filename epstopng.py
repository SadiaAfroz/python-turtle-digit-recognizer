#!/usr/bin/env python3
from PIL import Image
from turtle import Screen, Turtle
import turtle

def converter():
    image_eps = 'digit.eps'
    im = Image.open(image_eps)
    fig = im.convert('RGBA')
    image_png= 'digit.png'
    fig.save(image_png, lossless= True)
