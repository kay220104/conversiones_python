import pytest
import Conversion as con 

def test_pulgadas_cm():
    assert con.centimetrosApulgadas(5.08) == pytest.approx(2)
    assert con.pulgadasAcentimetros(2) == pytest.approx(5.08)

def centimetrosApulgadas(cm):
    pulgadas = cm / 2.54
    return pulgadas

def pulgadasAcentimetros(pulgadas):
    cm = pulgadas * 2.54
    return cm

def piesAmetros(pies):
    metros = pies * 0.3048
    return metros

def metrosApies(metros):
    pies = metros / 0.3048
    return pies

def millasAkilometros(millas):
    kilometros = millas * 1.60934
    return kilometros

def kilometrosAmillas(kilometros):
    millas = kilometros / 1.60934
    return millas

def galonesAlitros(galones):
    litros = galones * 3.78541
    return litros

def litrosAgalones(litros):
    galones = litros / 3.78541
    return galones

def librasAkilogramos(libras):
    kilogramos = libras * 0.45359237
    return kilogramos

def kilogramosAlibras(kilogramos):
    libras = kilogramos / 0.45359237
    return libras
