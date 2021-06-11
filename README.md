# Nawigacja

 **Wstęp:**       
Aplikacja do wskazywania najkrótszej i domyślnej trasy, oblicza odległość miedzy punktami.
 #   
**Instalacja:**    
Instalacja bibliotek python (lista bibliotek w pliku requirements.txt).
#
**Użyte algorytmy:**     
 Została użyta biblioteka Networkx. 
#
**Instrukcja:**
1. W aplikacji 'Nawigacja Warszawa' należy wybrać Trase oraz Styl Mapy.
2. Wpisać punkt początkowy, który na mapie pokazuje się jako zielona kropka.
3. Następnie wpisać punkt końcowy, bedzie to czerwona kropka.
4. Następnie należy kliknąć przycisk 'Szukaj trasy'.
5. Z prawej strony pokaże sie Trasa jaką wybrał użytkownik.
6. W lewym dolnym rogu obliczy się odległość między punktami w km.

**Sprawozdanie:**
1. Opis działania kodu:

   * Zaimportowanie danych bibliotek:

      ![image](https://user-images.githubusercontent.com/83244370/121735357-4dbe1300-caf6-11eb-813c-b5bb89af406b.png)


   * Utworzenie funkcji:

      **a) Funkcja kreująca wykres z trasą dla danych punktu początkowego i końcowego oraz współrzędnych skrzyżowań** - przyjmuje ona długości i szerokości w listach, współrzędne punktu początkowego i końcowego; rysuje wykres w Plotly
      
        Zdefiniowanie funkcji:
        
        ![image](https://user-images.githubusercontent.com/83244370/121736501-ef922f80-caf7-11eb-8cfc-00cb5135cf6c.png)

        Dodanie linii łączących punkty, nadanie jej nazwy, wielkości oraz koloru:
        
        ![image](https://user-images.githubusercontent.com/83244370/121736601-0d5f9480-caf8-11eb-89d0-2e637ba8aa02.png)
        
        Utworzenie stylu dla punktu początkowego na mapie:
        
        ![image](https://user-images.githubusercontent.com/83244370/121736842-629ba600-caf8-11eb-8cfe-7e309fe33a7e.png)
        
        Utworzene stylu dla punktu końcowego na mapie:
        
        ![image](https://user-images.githubusercontent.com/83244370/121736877-71825880-caf8-11eb-87ed-322c7ff8b87c.png)

        Otrzymanie współrzędnych dla środka trasy:
        
        ![image](https://user-images.githubusercontent.com/83244370/121737365-0ab16f00-caf9-11eb-9213-50919e4cfc50.png)
        
        Utworzenie stylu dla mapy oraz zakończenie funkcji:
        
        ![image](https://user-images.githubusercontent.com/83244370/121737424-2157c600-caf9-11eb-9f17-cab7ea8f6264.png)
        
        Otrzymanie najbliższych punktów do drogi dla punktu początkowego i końcowego:
        
        ![image](https://user-images.githubusercontent.com/83244469/121740912-1489a100-cafe-11eb-8eae-8ec5d24b23b3.png)
        
        Otrzymanie najkrótszej drogi:
        
        ![image](https://user-images.githubusercontent.com/83244469/121741065-46026c80-cafe-11eb-910c-0187f233da1e.png)
        
        Otrzymanie współrzędnych skrzyżowań:
        
        ![image](https://user-images.githubusercontent.com/83244469/121741157-67635880-cafe-11eb-9521-acb012083543.png)
        
        Obliczenie długości trasy:
        
        ![image](https://user-images.githubusercontent.com/83244469/121741250-8e218f00-cafe-11eb-9e79-7e1862221ab2.png)
        
        Załadowanie pliku z drogami dla Warszawy i okolicy:
        
        ![image](https://user-images.githubusercontent.com/83244469/121741358-b4472f00-cafe-11eb-950a-f214da0325ae.png)

        

        






