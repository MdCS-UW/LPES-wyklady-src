# Copyright (c) 2020-2021 Matematyka dla Ciekawych Świata (http://ciekawi.icm.edu.pl/)
# Copyright (c) 2020-2021 Robert Ryszard Paciorek <rrp@opcode.eu.org>
# 
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

code_vla = r"""
void xxx(int n) {
    if (n<2) n=2;
    float v[n];

    v[0] = 21;
    printf("%d %d \n", v[0], v[1]);

    /* ... */
}
"""

code_vector = r"""
#include <iostream>
#include <vector>

void xxx(int n) {
    if (n<2) n=2;
    std::vector<float> v(n);

    v[0] = 21;
    std::cout << v[0] << " " << v[1] << std::endl;

    v.push_back(123);  v.push_back(567);
    std::cout << v[n] << " " << v[n+1] << std::endl;
}

int main(int argc, char* argv[]) {  xxx(argc);  }
"""

code_listy = r"""
#include <iostream>
#include <list>

int main() {
    std::list<int> l;
    
    // dodanie elementu na końcu
    l.push_back(17); l.push_back(13);
    l.push_back(3);  l.push_back(27);
    // dodanie elementu na początku
    l.push_front(8);
    
    // wypisanie liczby elementów
    std::cout << "size=" << l.size() << std::endl;
    
    // wypisanie pierwszego i ostatniego elementu
    std::cout << "first=" << l.front() << " last=" << l.back() << std::endl;
    
    l.pop_back();   // usuniecie ostatniego elementu
    l.sort();       // posortowanie listy
    l.reverse();    // odwrócenie kolejności elementów
    l.pop_front();  // usuniecie pierwszego elementu
    
    // wypisanie wszystkich elementów
    for (std::list<int>::iterator i = l.begin(); i != l.end(); ++i) {
        std::cout << *i << std::endl; 
        // możliwe jest także:
        //  - usuwanie elementu wskazanego przez iterator
        //  - wstawianie elementu przed wskazanym przez iterator
    }
}
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'C++ typy tablicowe' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_vla, "c")],
			["vector", eduMovie.clear + eduMovie.code2console(code_vector, "cpp")],
		],
		'consoleDown': [
			[0.0, ""],
			["vector", eduMovie.runCode(code_vector, args=["&& ./a.out"], cmd="g++")],
		],
		'text' : [
			'Kolejnym elementem popularnym w C, <m> ale też i w C++ są tablice o zmiennej długości. <m>'
			'W przypadku języka C od wersji 99 możemy określić długość tablicy <m> poprzez zmienną, są to tablice zmiennej długości VLA. <m>'
			'C++ nie posiada tego typu tablic, <m> jednak na przykład kompilatory gnu czy <clang>[ce lang] pozwalają na ich używanie w C++. <m>'
			'Brak tablic VLA w C++ wynika z tego że C++ posiada własny <m> typ dla tablic zmiennej długości. <mark name="vector" />'
			
			'Jest to STD Vector, który też pełni funkcję tablic zmiennej długości, <m> w dodatku tablic których długość może być zmieniana już po ich utworzeniu. <m>'
			'Czyli możemy je łatwo rozszerzyć w trakcie działania programu <m> – przynajmniej z punktu widzenia programisty piszącego kod. <m>'
			'Bo niekoniecznie będzie to łatwe dla komputera wykonującego ten kod, <m> ponieważ jeżeli jest to duży wektor, za którym są już zaalokowane inne zmienne, <m>'
			'to w celu jego rozszerzenia musimy przekopiować <m> wszystkie dane z tego wektora w inne miejsce. <m>'
			'Vector podobnie jak klasyczna tablica C jest ciągłym obszarem pamięci. <m>'
			
			'Warto zauważyć tutaj kolejny przypadek użycia dwóch dwukropków <m> – rozdzielają one przestrzeń nazw, w tym wypadku STD <m>'
			'(w której znajdują się elementy biblioteki standardowej C++), <m> od elementu tej przestrzeni jakim jest vector. <m>'
			'Dwa dwukropki służą do odwoływania się do kolejnych przestrzeni nazw, <m> przy czym przestrzenie nazw, a nawet klasy które w pewnych aspektach <m>'
			'też są tak traktowane możemy zagnieżdzać w sobie, więc w nazwie <m> jakiegoś typu takich par dwukropków może być wiele. <m>'
		]
	},
	{
		'consoleTop': [
			[0,  eduMovie.code2console(code_listy, "cpp", first=1,  last=16)],
			*[  [10+i,  eduMovie.clear + eduMovie.code2console(code_listy, "cpp", first=1+i,  last=16+i)] for i in range(1,16)  ],
		],
		'consoleDown': [
			[0.0, ""],
			[25.0, eduMovie.runCode(code_listy, args=["&& ./a.out"], cmd="g++")],
		],
		'text' : [
			'Kolejnym standardowym typem C++, <m> o którym na pewno warto wspomnieć, są listy. <m>'
			'Listy znamy już z Pythona, przy czym w odróżnieniu od list pythonowych <m> (które w istocie były tablicą wskaźników) C++ oferuje nam prawdziwe listy. <m>'
			
			'Warto zauważyć że w nawiasie trójkątnym po STD List, <m> czy też wcześniej STD Vector, podawany jest typ <m>, który ma być przechowywany w danym kontenerze. <m>'
			'W odróżnieniu od Pythona taki kontener przechowuje zmienne <m> jednego określonego wcześniej typu. <m>'
			
			'Możemy dodawać elementy na początku, na końcu, <m> czy też wewnątrz listy (po jakimś znanym nam elemencie listy) <m> z użyciem metod push back, push front lub insert. <m>'
			'Możemy odwołać się do pierwszego i ostatniego elementu listy, <m> możemy poznać rozmiar listy, czyli ilość przechowywanych w niej elementów. <m>'
			'Natomiast odwołanie się do n-tego elementu nie jest operacją trywialną <m> – wymaga przejścia po elementach tej listy i w przypadku list <m> raczej takich rzeczy nie robimy. <m>'
			'Jeżeli chcemy często się odwoływać do n-tego elementu <m> kolekcji to stosujemy raczej wektor niż listę. <m>'
			
			'Jeżeli chcemy wypisać całą listę to możemy użyć do tego iteratorów. <m>'
			'Na temat iteratorów mówiliśmy już trochę przy programowaniu <m> w Pythonie i w C++ mamy podobne iteratory. <m>'
			'W C++ iterator pozyskuje się typowo poprzez metodę begin, <m> a w momencie kiedy iterator wychodzi za zakres kolekcji <m> po której iterujemy nie rzuca nam wyjątku <m>'
			'(pomimo że wyjątki w C++ istnieją i są obsługiwane) <m> tylko przebiera specyficzną wartość którą możemy porównywać <m> z iteratorem zwróconym przez metodę end. <m>'
		]
	},
]

code_mapa = r"""
#include <iostream>
#include <map>

int main() {
    std::map<std::string, int> m;
    
    m["a"] = 6;
    m["cd"] = 9;
    std::cout << m["a"] << " " << m["ab"] << std::endl;
    
    // wyszukanie elementu po kluczu
    std::map<std::string, int>::iterator iter = m.find("cd");
    // sprawdzenie czy istnieje
    if (iter != m.end()) {
        // wypisanie pary - klucz wartość
        std::cout << iter->first << " => " << iter->second << std::endl;
        // usunięcie elementu
        m.erase(iter);
    }
    
    m["a"] = 45;
    
    // wypisanie całej mapy
    for (iter = m.begin(); iter != m.end(); ++iter)
        std::cout << iter->first << " => " << iter->second << std::endl;
    // jak widać mapa jest wewnętrznie posortowana
}
"""

clipData += [
	{
		'consoleTop': [
			[0,  eduMovie.code2console(code_mapa, "cpp", first=1,  last=16)],
			*[  [5+i,  eduMovie.clear + eduMovie.code2console(code_mapa, "cpp", first=1+i,  last=16+i)] for i in range(1,12)  ],
		],
		'consoleDown': [
			[0.0, ""],
			[20.0, eduMovie.runCode(code_mapa, args=["&& ./a.out"], cmd="g++")],
		],
		'text' : [
			'Kolejnym typem kontenerowym o którym warto powiedzieć są mapy <m> i tu również mamy dość jednoznaczne odniesienie do Pythona <m> – jest to odpowiednik Pythonowych słowników. <m>'
			'W przypadku map z C++ musimy określić wprost <m> typ klucza oraz typ elementu. <m>'
			
			'W pokazanym przykładzie kluczem jest napis, <m> a elementem jest liczba całkowita. <m>'
			'Jak widzimy odwoływanie się za równo w celu pobrania, <m> jak i ustawienia wartości elementu jest zasadniczo <m> takie same jak mieliśmy do czynienia w Pythonie <m>'
			'i takie samo jak dla tablic – został tutaj <m> przeciążony operator nawiasów kwadratowych. <m>'
			'Oczywiście odwołujemy się przy pomocy klucza takiego <m> typu jaki zdefiniowaliśmy w ramach definicji mapy. <m>'
			
			'Możemy wyszukiwać po kluczu, <m> co jest też metodą na sprawdzenie czy dany element istnieje. <m>'
			'Czyli jeżeli nie wiemy czy w danej mapie mamy jakieś element to <m> aby się tego dowiedzieć należy go po prostu wyszukać. <m>'
			'W nowszym C++ jest także metoda która służy tylko i wyłącznie do <m> sprawdzenia obecności, nie zwracając iteratora do elementu jeżeli on istnieje. <m>'
			
			'Z elementu na który wskazuje iterator <m> możemy pobrać zarówno klucz jak i wartość. <m>'
			'Dokładniej iterator wskazuje na element typu STD pair, <m> w którym pierwszy element reprezentuje klucz a drugi wartość. <m>'
			'Na mapę możemy patrzeć właśnie jako na zbiór takich par<.>[ .] <m>'
			
			'Mapa nie zachowuje kolejności wstawianych elementów, <m> natomiast standardowa mapa w C++ jest kontenerem posortowanym, <m> czyli elementy w niej przechowywane będą posortowane po kluczu. <m>'
			'Jeżeli nie zależy nam na tym sortowaniu to możemy użyć <m> <unordered>[an orderd] map i wtedy mapa nie będzie posortowana, <m>'
			'za to będzie przechowywana w sposób <m> trochę bardziej optymalny dla niektórych operacji <m> – na przykład dostęp do takiej mapy będzie szybszy. <m>'
			
			'C++ pozwala również na tworzenie map w których klucz <m> nie jest unikalny są to STD multimap i STD <unordered>[an orderd] multimap. <m>'
			
			'Oczywiście w ramach kontenerów takich jak mapy, listy czy wektory <m> możemy przechowywać zarówno obiekty, jak i wskaźniki na obiekty <m>'
			' (jednak nie w tej samej mapie, <m> gdyż mapa musi mieć jednoznacznie określone przechowywane typy). <m>'
			'Jeżeli przechowujemy wskaźniki, to musimy zadbać aby obiekt na który <m> jest to wskaźnik istniał pod tym samym adresem przez cały czas życia mapy. <m>'
			'Czyli na przykład nie może to być obiekt znajdujący się w wektorze, <m> gdyż ten może zostać przeniesiony w inne miejsce celem jego powiększenia.'
		]
	},
]
