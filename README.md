# Rsa
1.
Kibővített euklideszinél nem tartom számon a k-t és azt hittük, hogy nem jöhet ki negatív érték, de jöhet ki, és így nincs szükség k-ra, ezért működött a kód. Pl. kibovitett_euklideszi(2, 5)
m0=5, x=1, y=0
a=2, m=5:  q=0 → x=0,  y=1
a=5, m=2:  q=2 → x=1,  y=-2
a=2, m=1:  q=2 → x=-2, y=5
if x < 0: x = -2 + 5 = 3

2.
Miller-Rabinnál nem néztem meg, hogy az alap relatív prím-e az n-nel, ezt javítottam a kódban. Azért működött a kód, mert elvileg nagyon nagy eséllyel így is False eredményre jut más úton.

3.
A Kínai maradéktétel függvény külön csak egy része volt a tételnek, és a gyorshatványozások meg külön voltak elvégezve, így működött a kód, de értelmetlenül volt összerakva, javítottam ezt is.
