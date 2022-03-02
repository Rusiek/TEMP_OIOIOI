# IEiT 2021/2026 TESTS
## TL;DR
Repozytorium z testami oraz skryptami, ułatwi wam życie oraz szukanie błędów.

## make_output.sh
Prosty dwuagrumentowy skrypt napisany w języku **bash**, który pozwoli na wygenerowanie 
wyjścia dla napisanego przez nas programu

Pierwszy argument: program o rozszerzeniu **exe**.

Drugi argument: Katalog z plikami o rozszerzeniu **in**.

Sposób działania: Skrypt dla każdego pliku **x.in** znajdującego się w drugim katalogu 
uruchomi program z wejściem takim samym jak w **x.in**, a następnie utworzy wyjście takie 
same jak program o nazwie **x.out**.

## test_program.sh
Prosty dwuargumentowy skrypt napisany w języku **bash**, który pozwoli na sprawdzenie
poprawności wyjścia dla napisanego przez nas programu oraz gotowych testów (tzn. takich,
które zawierają pliki o rozszerzeniach **in** oraz **out**).

Pierwszy argument: program o rozszerzeniu **exe**.

Drugi argument: Katalog z gotowymi testami.

Sposób działania: Skrypt dla każdego pliku **x.in** znajdującego się w drugim katalogu
uruchomi program z wejściem takim samym jak w **x.in**, a następnie porówna wyjście
programu z plikiem o nazwie **x.out**. Jeżeli będą takie same, to wykona sprawdzenie dla
kolejnego pliku z katalogu, jeżeli pliki będą różne, przerwie sprawdzanie oraz poinformuje
nas, że wyjście programu oraz plik o nazwie **x.out** są różne, co pozwoli na prostym szukaniu
błędów
