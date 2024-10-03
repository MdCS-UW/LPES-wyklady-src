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

code_ref = r"""
#include <iostream>

void ff(int& a) { // zwróć uwagę na & oznaczający że będzie to referencja
    a = 15;
}
int main() {
    int x = 10;
    ff(x);
    std::cout << x << std::endl; // wypisze 15
}
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'comment': 'więcej C++' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_ref, "cpp")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_ref, args=["&& ./a.out"], cmd="g++")],
		],
		'text' : [
			'Mówiliśmy już trochę o wskaźnikach. <m>'
			'C++ oprócz wskaźników znanych z języka C pozwala na korzystanie z referencji. <m>'
			'W ten sposób funkcję, która modyfikuje przyjmowaną w argumencie zmienną, <m> możemy zapisać w trochę ładniejszy, bardziej standardowy sposób, <m>'
			'bo jedyną modyfikacją jest postawienie znaku ampersand <m> pomiędzy nazwą typu a nazwą tej zmiennej. <m>'
			
			'Znak ten informuje o tym że funkcja przyjmuje nie zmienną "a", <m> tylko referencje na zmienną "a". <m>'
			'Użycie takiej funkcji nie różni się niczym od funkcji która przyjmowałaby "a", <m> poza tym że zmienna "a" nie będzie kopiowana <m> i funkcja ta ma prawo zmodyfikowania jej. <m>'
			'Jeżeli chcielibyśmy jednak żeby nie mogła ona modyfikować zmiennej, <m> a przekazanie przez referencje służyło jedynie zapobieżeniu kopiowania, <m> tak samo jak w przypadku wskaźników możemy tutaj użyć słowa kluczowego const. <m>'
			
			'Referencja jest zasadniczo wskaźnikiem, przy czym jest wskaźnikiem <m> którego wartość możemy ustawić w zasadzie tylko raz. <m>'
			'Czyli mówimy że jest to wskaźnik na tą zmienną i nie możemy później <m> modyfikować adresu czy też wprost odwołać się do adresu na który wskazuje <m> nam taka referencja, ona zawsze będzie wskazywała na tą zmienną. <m>'
		]
	},
]

code_wypiszListe_A = r"""
#include <iostream>
#include <list>

void wypiszListe(std::list<int> l) {
    for (std::list<int>::iterator i = l.begin(); i != l.end(); ++i) {
        std::cout << *i << std::endl;
    }
}
"""

code_wypiszListe_B = r"""
#include <iostream>
#include <list>

void wypiszListe(const std::list<int>& l) {
    for (auto i = l.begin(); i != l.end(); ++i) {
        std::cout << *i << std::endl;
    }
}
"""

code_wypiszListe_C = r"""
#include <iostream>
#include <list>

void wypiszListe(const std::list<int>& l) {
    for (auto i : l) {
        std::cout << i << std::endl;
    }
}
"""

code_wypiszListe_D = r"""
#include <iostream>
#include <list>

void wypiszListe(const std::list<int>& l) {
    for (const auto& i : l) {
        std::cout << i << std::endl;
    }
}
"""

code_wypiszListe_E = r"""
#include <iostream>
#include <list>

template <typename T> void wypiszListe(const std::list<T>& l) {
    for (auto i : l) {
        std::cout << i << std::endl;
    }
}

int main() {
    std::list<int> x={1, 3, 7, 2, 3};
    wypiszListe(x);
    
    std::list<float> z={2.7, 5.0, 3.1, 3.9};
    wypiszListe(z);
}
"""

code_lamba = r"""
#include <iostream>
int main() {
    int x = 1, y = 1;

    // ta lamba będzie używać:
    //  wartości x z chwili wywołania (i jej zmiana bedzie widoczna na zewnątrz)
    //  wartości y z chwili utworzenia
    auto moja_lambda = [&x, y](int z) { x += z * y; return 11; };
    moja_lambda(2);
    std::cout << x << std::endl; // 3 bo x = 1 + 2 * 1

    x = 0; y = 0;
    int z = moja_lambda(2);
    std::cout << x << " " << z << std::endl; // 2 bo x = 0 + 2 * 1
}
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_wypiszListe_A, "cpp")],
			["wypiszlisteb", eduMovie.clear + eduMovie.code2console(code_wypiszListe_B, "cpp")],
			["wypiszlistec", eduMovie.clear + eduMovie.code2console(code_wypiszListe_C, "cpp")],
			["wypiszlisted", eduMovie.clear + eduMovie.code2console(code_wypiszListe_D, "cpp")],
		],
		'consoleDown': [
			[0.0, ""],
		],
		'text' : [
			'Mówiliśmy także trochę o iteratorach, natomiast jeżeli nazwy typów <m> przechowywanych na przykład w mapie są długie (bo są to np. szablony, <m>'
			'czyli mamy kolejne nawiasy trójkątne) to pisanie całego określenia <m> typu iteratora, tak jak robiliśmy to do tej pory może być uciążliwe. <mark name="wypiszlisteb" />'
			
			'C++ przychodzi tutaj z ułatwieniem, czyli typem auto. <m>'
			'Jak już kiedyś wspomnieliśmy możemy napisać <m> auto x <=>[równa się] 5 i w C++ będzie to poprawne – kompilator wydedukuje typ <m> zmiennej x w oparciu o wartość przypisaną. <m>'
			'Natomiast nie możemy napisać auto x, <m> a dopiero później przypisać do niego jakąś wartość. <m>'
			
			'Działa to w sposób identyczny jak w Pythonie – w momencie kiedy <m> definiujemy zmienną typu auto, musimy od razu określić w sposób niejawny jej typ <m> poprzez przypisanie jakieś wartości do tej zmiennej. <m>'
			'Jednak w odróżnieniu od Pythona nie możemy zmienić tego typu później, <m> on jest już przypisany na cały żywot tej zmiennej. <m>',
			
			'Jednym z miejsc bardzo naturalnych do użycia typu auto są właśnie <m> zmienne przechowujące iteratory zwracane z metod typu begin czy find. <mark name="wypiszlistec" />'
			
			'Kolejnym tego typu ułatwieniem jest pętla for each. <m>'
			'Zapisywana jest ona ze słowem kluczowym for, działa jednak jak pętla <m> for znana z Pythona, czy właśnie pętla for each <m> z innych języków programowania – iteruje po elementach kolekcji. <m>'
			
			'W nawiasach po słowie kluczowym for podajemy zmienną pod którą <m> będą postawione kolejne elementy kontenera, <m> dwukropek i kontener z którego będą pobierane. <m>'
			'Jest to też naturalne miejsce do użycia typu auto. <m>',
			
			'Jeżeli chcemy dostawać referencje, a nie kopie elementu to możemy  <mark name="wypiszlisted" /> użyć ampersanda pomiędzy auto a nazwą zmiennej. <m>'
			'Wtedy dostajemy referencję na oryginalny element np. listy <m> i jeżeli go zmodyfikujemy to element w oryginalnej liście <m> także zostanie zmodyfikowany. <m>'
			'Mamy tutaj, w odróżnieniu np. od pythonowego for, łatwy wybór <m> tego czy dostajemy kopię czy dostajemy referencje na oryginalny element. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_wypiszListe_E, "cpp")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_wypiszListe_E, args=["&& ./a.out"], cmd="g++")],
		],
		'text' : [
			'Kolejnym ważnym elementem języka C++, <m> o którym trzeba przynajmniej wspomnieć są szablony. <m>'
			
			'Przez ostatnie parę minut zajmowaliśmy się <m> udoskonalaniem funkcji wypisz listę. <m>'
			'Funkcja ta przyjmowała referencję na listę liczb całkowitych <m> typu int i tylko takie listy mogła obsłużyć. <m>'
			'Jeżeli chcielibyśmy napisać funkcję wypisującą listę liczb <m> zmienno przecinkowych to wyglądałaby ona niemalże identycznie <m> – różniłaby się tylko przyjmowanym typem listy. <m>'
			'Podobnie dla listy liczb dodatnich, listy napisów, i tak dalej. <m>'
			'Aby nie musieć ręcznie pisać dziesiątków identycznych funkcji <m> możemy skorzystać z szablonu. <m>'
			'Definiując szablony określamy używane przez nie typy szablonowe, <m> których następnie możemy w nim używać jako typów zmiennych. <m>'
			"W tym przykładzie nazwaliśmy go T <m> (na ogół nazywa się je pojedynczą wielką literą, <m> jednak można tutaj używać dowolnej nazwy) i zastąpił nam naszego int'a. <m>"
			
			'Dzięki temu możemy napisać program jaki widzimy na ekranie, <m> gdzie tej samej funkcji wypisz używamy dla różnych rodzajów list. <m>'
			'Jako że tak naprawdę każda funkcja musi mieć dobrze zdefiniowane <m> typy swoich argumentów, to kompilator po prostu wygeneruje <m> w oparciu o ten szablon potrzebne funkcje. <m>'
			'Jeżeli użyli byśmy tego szablonu dla jakiś innych typów to kompilator <m> automatycznie wygeneruje funkcje również dla tych innych typów. <m>',
			
			'Warto tu też zauważyć iż typy takie jak lista, mapa, czy wektor <m> są właśnie szablonami, a przy tworzeniu obiektów tych typów w nawiasach <m> trójkątnych podajemy typy będące parametrami tych szablonów. <m>'
			'Podobnie sami możemy deklarować też klasy będące szablonami <m> i przyjmujące jakieś typy jako jego parametry. <m>'
			
			'Należy też zwrócić uwagę na chyba główną niedogodność związaną <m> ze stosowaniem szablonów – bardzo nieczytelne komunikaty o błędach, <m>'
			'wskazujące często na wstępie jakieś pliki nagłówkowe biblioteki, <m> a dopiero na drugim, trzecim ekranie komunikatów wspominające właściwe miejsce <m> w którym szablon został użyty w błędny sposób. <m>',
			
			'Było to dość zwięzłe wprowadzenie do C i C++, <m> nie omawiające wielu aspektów tych języków i ich bibliotek standardowych, <m> a jedynie nakreślające główne koncepcje. <m>'
			'Warto także zauważyć że to czego uczyliśmy się w trakcie <m> programowania w Pythonie ma też przełożenie na programowanie w C i C++. <m>'
			'W szczególności funkcje systemowe takie jak select, fork, exec <m> są dostępne z poziomu C i są tak naprawdę oryginalnymi funkcjami, <m> które Python obudowuje i pozwala uruchomić ze swojego kodu. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_lamba, "cpp")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_lamba, args=["&& ./a.out"], cmd="g++")],
		],
		'text' : [
			'C++ pozwala także na definiowanie i używanie lamb. <m>'
			'Definicja taka składa się z listy przechwytywanych zmiennych, listy argumentów i ciała funkcji. <m>'
			'Lista przechwytywania może określać <m> przechwytywanie przez wartość lub przez referencję. <m>'
			'W pierwszym przypadku wartość zmiennej z miejsca <m> utworzenia funkcji zostanie w niej "zamrożona", <m> czyli jej dalsze zmiany nie będą widoczne w wywołaniach lambdy. <m>'
			'W drugim przypadku lambda będzie widzieć zawsze aktualną wartość, <m> a zmiany tej zmiennej wewnątrz lambdy będą widoczne także na zewnątrz. <m>'
			'Lista argumentów i ciało funkcji działa jak w zwykłych funkcjach. <m> Lambda może zwracać lub może nie zwracać wartość z użyciem return. <m>'
		]
	},
]
