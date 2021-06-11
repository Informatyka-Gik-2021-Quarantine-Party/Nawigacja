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

      a) Funkcja kreująca wykres z trasą dla danych punktu początkowego i końcowego oraz współrzędnych skrzyżowań
      
        *Zdefiniowanie funkcji:
        
        ![image](https://user-images.githubusercontent.com/83244370/121736501-ef922f80-caf7-11eb-8cfc-00cb5135cf6c.png)

        *Dodanie linii łączących punkty:
        
        ![image](https://user-images.githubusercontent.com/83244370/121736601-0d5f9480-caf8-11eb-89d0-2e637ba8aa02.png)

