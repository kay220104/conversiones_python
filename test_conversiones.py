import pytest
import Conversion as con

def test_centimetros_pulgadas():
    assert con.centimetrosApulgadas(5.08) == pytest.approx(2)

def test_pulgadas_centimetros():
    assert con.pulgadasAcentimetros(2) == pytest.approx(5.08)

def test_pies_metros():
    assert con.piesAmetros(10) == pytest.approx(3.048)

def test_metros_pies():
    assert con.metrosApies(3.048) == pytest.approx(10)

def test_millas_kilometros():
    assert con.millasAkilometros(1) == pytest.approx(1.60934)

def test_kilometros_millas():
    assert con.kilometrosAmillas(1.60934) == pytest.approx(1)

def test_galones_litros():
    assert con.galonesAlitros(1) == pytest.approx(3.78541)

def test_litros_galones():
    assert con.litrosAgalones(3.78541) == pytest.approx(1)

def test_libras_kilogramos():
    assert con.librasAkilogramos(1) == pytest.approx(0.45359237)

def test_kilogramos_libras():
    assert con.kilogramosAlibras(0.45359237) == pytest.approx(1)

