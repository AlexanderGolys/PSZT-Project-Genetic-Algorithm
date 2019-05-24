## PSZT

Napisać program dokonujący optymalnego rozkładu czujek ruchu na danym obszarze. Należy
założyć, że czujka zapewnia pokrycie obszaru trójkątnego o kącie fi stopni (np. 120o) i długości boku d metrów. Obszar działania czujki może być ograniczony przez przeszkody
(ściany). Można przyjąć, że obserwacją ma być pokryte minimum 90% powierzchni obszaru.
Obszar 2D należy zamodelować jako mapę dyskretną NxM o wartościach: „1” przeszkoda
(ściana), „0” otwarta przestrzeń, „2” nie podlega monitorowaniu. Czujki mogą być
umieszczane tylko w punktach typu „0”. Przedmiotem minimalizacji jest liczba czujek.
Położenie czujki określone jest przez współrzedne (x,y) oraz orientację (kąt w płaszczyźnie
poziomej, można przyjąć kąty skwantowane: 0,90,180,270). Obszary objęte różnymi
czujkami mogą się oczywiście częściowo pokrywać. Aby założenia były realistyczne należy
przyjąć, że d jest znacząco mniejsze od max(N,M).

### Run program
You need to prepare data file in `src/config` directory, where you should put your map. To run program type in src directory in command line:

```bash
python3 main.py [d]
```
where `d` is coverage of motion detection
