# BIN
Napisz funkcję która za argumenty przyjmie kolejno posortowaną rosnąco tablicę liczb całkowitych
**TAB** oraz liczbę całkowitą **x**. Funkcja zwraca "True" jeżeli **x** znajduje się w tablicy 
**TAB** oraz "False" jeżeli jej tam nie ma. Funkcja zostanie wywołana **q** razy.

## Testy
A: 1000 małych testów sprawdzających poprawność działania programu. Tablica jest wypełniona przynajmniej
jedną a co najwyżej 10 losowymi liczbami całkowitymi z przedziału <-50, 50>. Liczba zapytań **q** wynosi 5. 
Czas wykonywania każdego testu powinien być rzędu 0.1s.

B: 20 średnich testów sprawdzających wydajność programu o złożoności O(qn). Tablica zawiera 10^4 liczb całkowitych
z przedziału <-10^9, 10^9>. Liczba zapytań **q** wynosi 50. Czas wykonania zależy od sprzętu, powinien się 
mieścić w ???.

C: Duży test sprawdzający wydajność programu o złożoności O(q*log(n)). Tablica zawiera 10^5 liczb całkowitych z 
przedziału <-10^9, 10^9>. Liczba zapytań **q** wynosi 10^5. Czas wykonania zależy od sprzętu, powinien się 
mieścić w 2s.

# CAT
Napisz funkcję która za argumenty przyjmie kolejno posortowaną rosnąco tablicę liczb całkowitych
**TAB** oraz nieujemną liczbę całkowitą **x**. Funkcja zwraca "True" jeżeli istnieją w tablicy takie dwie liczby,
że ich różnica jest równa **x**, w przeciwnym wypadku zwraca "False". Funkcja zostanie wywołana **q** razy.

## Testy
A: 1000 małych testów sprawdzających poprawność działania programu. Tablica jest wypełniona przynajmniej
jedną a co najwyżej 10 losowymi liczbami całkowitymi z przedziału <-50, 50>. Liczba zapytań **q** wynosi 5. 
Czas wykonywania każdego testu powinien być rzędu 0.1s.

B: 20 średnich testów sprawdzających wydajność programu o złożoności O(qn^2). Tablica zawiera 5000 liczb całkowitych
z przedziału <-10^9, 10^9>. Liczba zapytań **q** wynosi 50. Czas wykonania zależy od sprzętu, powinien się 
mieścić w ???.

C: Duży test sprawdzający wydajność programu o złożoności O(qn). Tablica zawiera 10^5 liczb całkowitych z 
przedziału <-10^9, 10^9>. Liczba zapytań **q** wynosi 10^3. Czas wykonania zależy od sprzętu, powinien się 
mieścić w 25s.



# MMD
Napisz funkcję która za argument przyjmuje tablicę liczb całkowitych **TAB**. Funkcja zwraca liczbę całkowitą,
która jest różnicą największej i najmniejszej wartości znajdującej się w tej tablicy.

## Testy
A: 1000 małych testów sprawdzających poprawność działania programu. Tablica jest wypełniona przynajmniej
jedną a co najwyżej 10 losowymi liczbami całkowitymi z przedziału <-50, 50>. Czas wykonywania każdego testu 
powinien być rzędu 0.1s.

B: Duży test wydajnościowy. Tablica jest wypełniona 10^7 liczbami całkowitymi z przedziału <-10^8, 10^8>.
Czas wykonania zależy od sprzętu, powinien mieścić się w 10s (6s).

# SRT
Napisz funkcję która za argument przyjmuje tablicę liczb całkowitych **TAB**. Funkcja zwraca tablicę zawierającą
posortowane elementy tablicy **TAB**. Zadanie można prosto przerobić na listy odsyłaczowe, wystarczy na początku
napisać implementację takiej listy oraz całą tablicę zamienić na listę, a po sortowaniu "zrzutować" ją spowrotem 
na tablicę.

## Testy
A: 1000 małych testów sprawdzających poprawność działania programu. Tablica jest wypełniona przynajmniej
jedną a co najwyżej 10 losowymi liczbami całkowitymi z przedziału <-50, 50>. Czas wykonywania każdego testu 
powinien być rzędu 0.1s.

B: 20 średnich testów sprawdzających wydajność programu o złożoności O(n^2). Tablica zawiera 10^4 liczb całkowitych
z przedziału <-10^9, 10^9>. Czas wykonania zależy od sprzętu, powinien się mieścić w 10s (6s).

C: Duży test sprawdzający wydajność programu o złożoności O(n*log(n)). Tablica zawiera 4*10^6 liczb całkowitych z 
przedziału <-10^9, 10^9>. Czas wykonania zależy od sprzętu, powinien się mieścić w 45s (35s).
