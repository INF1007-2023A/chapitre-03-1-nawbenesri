#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    r_carré = math.sqrt(a)
    return r_carré


def square(a: float) -> float:
    carré = a**2
    return carré


def average(a: float, b: float, c: float) -> float:
    moy = (a+b+c)/3
    return moy


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    ang_a_rad = math.radians(angle_degs+ (angle_mins+ (angle_secs/60)/60))
    return ang_a_rad


def to_degrees(angle_rads: float) -> tuple:
    degrees = math.degrees(angle_rads)
    mins = (abs(degrees) - int(abs(degrees)))*60
    secs = (mins - int(mins))*60
    return degrees, mins, secs


def to_celsius(temperature: float) -> float:
    temp_c = (temperature/1.8)-32
    return temp_c


def to_farenheit(temperature: float) -> float:
    temp_f=(temperature*1.8)+32
    return temp_f


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
