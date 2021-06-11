# Nawigacja

 **Wstęp:**       
Aplikacja do wskazywania najkrótszej i domyślnej trasy, oblicza odległość miedzy punktami.
 #   
**Instalacja:**    
Instalacja bibliotek python (lista bibliotek w pliku requirements.txt).
 #
**Instrukcja:**

1. W aplikacji 'Nawigacja Warszawa' należy wybrać Trase oraz Styl Mapy.
2. Wpisać punkt początkowy, który na mapie pokazuje się jako zielona kropka.
3. Następnie wpisać punkt końcowy, bedzie to czerwona kropka.
4. Następnie należy kliknąć przycisk 'Szukaj trasy'.
5. Z prawej strony pokaże sie Trasa jaką wybrał użytkownik.
6. W lewym dolnym rogu obliczy się odległość między punktami w km.

#
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
        
        
      **b) Funkcja wywołująca listę z liniami pokrywających się z drogą
    dla danych współrzędnych skrzyżowań** - otwiera plik z drogami, przyjmuje wartości ze współrzędnymi skrzyżowań przy drodze w listach oraz przyjmuje wartości ze współrzędnymi     punktów pokrywających się z drogą w różnych formatach w listach
    
    Zdefiniowanie funkcji:
               
    ![image](https://user-images.githubusercontent.com/83244469/121744291-f7a39c80-cb02-11eb-80a0-d3dfe6f5f8d7.png)
    
    Otrzymanie współrzędnych skrzyżowań przy drodze:
    
    ![image](https://user-images.githubusercontent.com/83244469/121744656-831d2d80-cb03-11eb-8431-ac2b2d9862f8.png)


        
     **c) Funkcja wprowadzająca dane do stworzenia mapy i obliczająca długość trasy** - otwiera ona pilk z drogami, przyjmuje adres lub nazwę miejsca pkt. początkowego lub końcowego, określa typ stylu drogi oraz mapy, rysuje wykres w Plotly i oblicza długość drogi
        
      Zdefiniowanie funkcji:
        
      ![image](https://user-images.githubusercontent.com/83244469/121743894-5a486880-cb02-11eb-8f1f-0ac72c07cf66.png)

        
      Otrzymanie najbliższych punktów do drogi dla punktu początkowego i końcowego:
        
      ![image](https://user-images.githubusercontent.com/83244469/121742250-ddb48a80-caff-11eb-82c6-81eb27d0aa32.png)

        
      Otrzymanie najkrótszej drogi:
        
      ![image](https://user-images.githubusercontent.com/83244469/121742301-ef962d80-caff-11eb-8f07-dc9fd2a5b112.png)

        
      Otrzymanie współrzędnych skrzyżowań:
        
      ![image](https://user-images.githubusercontent.com/83244469/121742361-02106700-cb00-11eb-8461-6c554301097e.png)

      Otrzymanie współrzędnych dla każdego punktu załamania drogi:
        
      ![image](https://user-images.githubusercontent.com/83244469/121742497-2f5d1500-cb00-11eb-928d-e11e35d08c4c.png)

      Tworzenie wykresu w Plotly:
        
      ![image](https://user-images.githubusercontent.com/83244469/121742564-48fe5c80-cb00-11eb-81a5-5dd9e132caf4.png)

        
      Obliczenie długości trasy:
        
      ![image](https://user-images.githubusercontent.com/83244469/121742611-574c7880-cb00-11eb-9c3d-8bf8e2abcb6e.png)

        
      Załadowanie pliku z drogami dla Warszawy i okolicy:
        
      ![image](https://user-images.githubusercontent.com/83244469/121742669-6e8b6600-cb00-11eb-9020-e5b4b946e597.png)

      **Interfejs użytkownika**
      
      W oknie aplikacji zostały zawarte niezbędne komponenty do działania programu.
      Okno, gdzie użytkownik wspisuję swoją lokalizację i lokalizację do, której chciałby znależć najbliższą trasę lub domyślną.
      Użytkownik ma możliwość wybory stylu mapy na, której zostanie zaprezentowana droga.
      Dodatkową funkcją powodujacą, że aplikacja jest bardziej atrakcyjna jest obliczanie długości trasy.
      Aplikacja ukazuje na mapie punkt początkowy i końcowy oraz współrzędne geograficzne.
      
      ![obraz](https://user-images.githubusercontent.com/83244425/121745951-6255d780-cb05-11eb-9f96-c84886ba0abc.png)

        

        







