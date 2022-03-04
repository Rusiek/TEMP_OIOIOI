# BIN
Napisz funkcję która za argumenty przyjmie kolejno posortowaną rosnąco tablicę liczb całkowitych
**TAB** oraz liczbę całkowitą **x**. Funkcja zwraca 1 jeżeli **x** znajduje się w tablicy **TAB**
oraz 0 jeżeli jej tam nie ma. Funkcja zostanie wywołana **q** razy.

## Testy
Do napisania

# MMD
Napisz funkcję która za argument przyjmuje tablicę liczb całkowitych **TAB**. Funkcja zwraca różnicę
największej i najmniejszej wartości znajdującej się w tej tablicy.

## Testy
A: 1000 małych testów sprawdzających poprawność działania programu. Tablica jest wypełniona przynajmniej
jedną a co najwyżej 10 losowymi liczbami całkowitymi z przedziału <-50, 50>. Czas wykonywania każdego testu 
powinien być rzędu 0.1s.

B: Duży test wydajnościowy. Tablica jest wypełniona 10^7 liczbami całkowitymi z przedziału <-10^8, 10^8>.
Czas wykonania zależy od sprzętu, powinien mieścić się w 10s.

# SRT
Napisz funkcję która za argument przyjmuje tablicę liczb całkowitych **TAB**. Funkcja zwraca tablicę zawierającą
posortowane elementy tablicy **TAB**. Zadanie można prosto przerobić na listy odsyłaczowe, wystarczy na początku
napisać implementację takiej listy oraz całą tablicę zamienić na listę, a po sortowaniu "zrzutować" ją spowrotem 
na tablicę.

## Testy
A: 1000 małych testów sprawdzających poprawność działania programu. Tablica jest wypełniona przynajmniej
jedną a co najwyżej 10 losowymi liczbami całkowitymi z przedziału <-50, 50>. Czas wykonywania każdego testu 
powinien być rzędu 0.1s.

B: 20 średnich testów sprawdzających wydajność programu o złożoności O(n^2). Tablica zawiera 10000 liczb całkowitych
z przedziału <-10^9, 10^9>. Czas wykonania zależy od sprzętu, powinien się mieścić w 10s.

C: Duży test sprawdzający wydajność programu o złożoności O(n*log(n)). Tablica zawiera 4*10^6 liczb całkowitych z 
przedziału <-10^9, 10^9>. Czas wykonania zależy od sprzętu, powinien się mieścić w 45s.
