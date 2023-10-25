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

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#08.4", "", "Dioda", "" ] },
	
	{ 'comment': 'dioda' },
	{
		'image': [
			[0.0, eduMovie.convertFile("../../LPES-booklets/images-src/elektronika/diody.sch", negate=True)],
		],
		'text' : [
			'Na ekranie widzimy symbole najpopularniejszych typów diód. <m>'
			'Dioda jest elementem elektronicznym, który przewodzi tylko w jednym kierunku. <m>'
			'Jest elementem nieliniowym, czyli łamie prawo Ohma. <m>'
			'Spadek napięcia na diodzie prawie nie zależy od przewodzonego przez nią prądu. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("led", 0, 3)],
			["led_r500 - 2.5", eduMovie.circuitjs("led", 4, 6, [("setSlider", 2, 0.45)])],
			["led_r100", eduMovie.circuitjs("led", 4, 6, [("setSlider", 2, 0.0)], preActions=[("setSlider", 2, 0.45)])],
		],
		'text' : [
			'Na symulacji widzimy diodę, na której mierzymy spadek napięcia <m> i wynosi on 1,6 volta, prąd płynący w obwodzie wynosi 1,9 mili ampera. <mark name="led_r500" />'
			'Jeżeli zmienimy wartość rezystora na pół kilo ohma to prąd nam wzrósł <m> prawie dwukrotnie, a spadek napięcia na diodzie się nie zmienił. <mark name="led_r100" />'
			'Jeżeli zmienimy wartość tego rezystora na 100 omów to prąd wzrósł <m> prawie dziesięciokrotnie w stosunku co do pierwotnego, <m> a napięcie pozostało prawie bez zmian (zmieniło się o kilkanaście procent). <m>'
			'Ewidentnie nie jest to zachowanie zgodne z prawem Ohma. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('diody.svg', margins=0)],
		],
		'text' : [
			'W jedną stronę przewodzi jedynie dioda idealna. <m>'
			'Rzeczywiste diody przewodzą prąd po prostu <m> zdecydowanie chętniej w jednym kierunku niż w drugim. <m>'
			'Do tego stopnia zdecydowanie chętniej, <m> że to przewodzenie w drugim kierunku na ogół się pomija. <m>'
			
			'Ponadto diody charakteryzują cechy zależne od technologii wykonania. <m>'
			'Jedną z nich jest właśnie ten spadek napięcia <m> w kierunku przewodzenia, który obserwowaliśmy. <m>'
			"Typowo dla diód krzemowych jest to około 0,7 Volta, <m> w diodach Schottky'ego jest to 0.3 volta. <m>"
			'W diodach świecących zależy od koloru i to co widzieliśmy, <m> czyli <1,7 - 1,8>[jeden i siedem, jeden i osiem dziesiątych] wolta jest charakterystyczne dla diody czerwonej <m> ewentualnie żółtej. <m>'
			'Dioda niebieska czy też biała będzie miała ten spadek około 3 woltów. <m>'
			'Jeżeli taką diodę podłączymy pod napięcie zdecydowanie mniejsze <m> niż to charakterystyczny dla tej diody, to nie będzie przewodziła, <m> czyli dioda świecąca się nie zaświeci. <m>'
			
			'Kolejnym parametrem charakteryzującym każdą rzeczywistą diodę <m> jest maksymalny prąd przewodzenia, czyli największy prąd który może przepłynąć <m> przez daną diodę nie powodując jej zniszczenia. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("led", 0, 3)],
			["led_bez_res - 3", eduMovie.circuitjs("led", 4, 6, [("switch", 600, 230)])],
			["parametry_cd", ""],
		],
		'text' : [
			'Z tymi cechami związana jest konieczność stosowania <m> zewnętrznego ograniczania prądu płynącego przez diodę. <m>'
			'Jeśli podłączylibyśmy diodę pod napięcie wyższe od <m> jej charakterystycznego napięcia przewodzenia, <m> prąd płynący przez tą diodę wzrósłby bardzo znacząco. <m>'
			'Z bardzo dużym prawdopodobieństwem przekraczając jej maksymalny <m> prąd przewodzenia, co doprowadziłoby do zniszczenia elementu. <mark name="led_bez_res" />'
			
			'Na symulacji widzimy że dla użytej tam diody przy pominięciu rezystora <m> prąd osiąga ponad 20 Amper przy napięciu zasilania <m> jedynie około trzy razy wyższym niż nominalne napięcie diody. <m>'
			'Tym samym przekracza on prąd roboczy dla typowych, sygnalizacyjnych <m> diod LED tysiąc krotnie, a ich prąd maksymalny kilkusetkrotnie. <m>'
			
			'Dlatego tak ważne jest ograniczanie prądu diody np. poprzez rezystor, <m> na którym może odłożyć się różnica pomiędzy napięciem zasilania <m> a napięciem przewodzenia diody, <m>'
				'tym samym wyznaczając prąd płynący przez rezystor i diodę. <mark name="parametry_cd" />'
			
			'Innym parametrem fizycznych, nieidealnych diod jest też czas <m> związany z przełączeniem diody, czyli przejściem pomiędzy <m> stanami przewodzenia i nieprzewodzenia. <m>'
			'Tak naprawdę wiąże się on z przeładowaniem pasożytniczego kondensatora, <m> który mamy równolegle z taką diodą <m>'
				'i jeżeli nagle zmienimy polaryzację diody to przez chwilę <m> będzie płynął prąd związany z przeładowaniem właśnie tego kondensatora. <m>'
			'Jest to dosyć krótki czas i dla diod szybkich, <m> tak zwanych diod schottkiego wynosi on około 100 piko sekund, <m>'
				'w diodach krzemowych jest dłuższy, ale też w wielu zastosowaniach <m> także całkowicie pomijalny – są to ułamki milisekund. <m>'
		]
	},
	{
		'image': [
			[0.0, ""],
			["zener", eduMovie.circuitjs("zener", 0, 4)],
			["zener_run", eduMovie.circuitjs("zener", 4, 6, [("switch", 620, 220)])],
			["zener_run2", eduMovie.circuitjs("zener", 4, 6, [("switch", 720, 220)])],
			["zener_run3", eduMovie.circuitjs("zener", 4, 12, preActions = [("switch", 620, 220), ("setSlider", 1, 0)], actions = [
				("setSlider", 1, 0.05), ("wait", 0.7), ("setSlider", 1, 0.1), ("wait", 0.7), ("setSlider", 1, 0.15), ("wait", 0.7),
				("setSlider", 1, 0.2), ("wait", 0.7), ("setSlider", 1, 0.4), ("wait", 0.7), ("setSlider", 1, 0.7), ("wait", 0.7), ("setSlider", 1, 1.0)
			])],
		],
		'text' : [
			'Jeżeli diodę podłączymy tak aby nie przewodziła (w kierunku zaporowym) <m> to po przyłożeniu odpowiednio wysokiego napięcia ona ulegnie przebiciu <m> i zacznie przewodzić w tym kierunku. <m>'
			'Napięcie to nazywamy napięciem przebicia <m> i jest kolejnym parametrem charakteryzującym daną diodę. <m>'
			'Przewodzenie w ten sposób nie jest szkodliwe dla diody, <m> dopóki prąd jest odpowiednio mały. <m>'
			
			'Zjawisko to jest wykorzystywane w jednym z typów diod – diodach Zenera. <m>'
			'Charakteryzują się one dość dobrze określoną wartością tego napięcia <m> i wykorzystywane są one właśnie w pracy w przebiciu. <mark name="zener" />'
			'Taką diodę montujemy zaporowo w szeregu z jakimś rezystorem ograniczającym prąd <m> i przykładamy napięcie wyższe od nominalnego napięcia diody. <m>'
			'Tak jak widać to na symulacji. <m>'
			'W efekcie uzyskujemy na niej spadek napięcia zgodny z jej napięciem nominalnym. <mark name="zener_run" />'
			
			'Widoczny układ nieprzypadkowo przypomina poznany już dzielnik napięcia <m> i widzimy że zachowuje się on bardziej stabilnie przy pobieraniu <m> z niego jakiegoś prądu od zwykłego dzielnika rezystancyjnego. <m>'
			'Jak widzimy załączenie obciążenia o wartości tysiąca omów <m> praktycznie nie wpływa na napięcie wyjściowe. <mark name="zener_run2" />'
			'Oczywiście obciążenie o mniejszej rezystancji będzie miało większy wpływ, <m> gdyż w układzie zacznie dominować dzielnik rezystancyjny <m> złożony z rezystora ograniczającego prąd diody i tego obciążenia. <mark name="zener_run3" />'
			'Kolejną cechą dzielnika z diodą Zenera jest przyzwoita stabilność <m> napięcia wyjściowego, przy zmianach wartości napięcia wejściowego. <m>'
			'Jeżeli zmieniamy napięcie wejściowe to napięcie na wyjściu pozostaje prawie bez zmian. <m>'
			'Nie mamy tutaj proporcjonalności pomiędzy napięciem wejściowym a wyjściowym. <m>'
			'Jest to użyteczne jeżeli chcemy ustabilizować napięcie wejściowe do jakiejś wartości, <m>'
				'ale czyni taki dzielnik bezużytecznym w zastosowaniach gdzie potrzebujemy <m> tej proporcjonalności (na przykład w obniżeniu napięcia celem jego pomiaru). <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('LED.svg', margins=0)],
			["fotodioda", eduMovie.convertFile('LED_foto.svg', margins=0)],
			["prost1", eduMovie.circuitjs("prost1", 0, 13)],
			["prost2", eduMovie.circuitjs("prost2", 0, 13)],
			["prost3", eduMovie.circuitjs("prost3", 0, 27)],
		],
		'text' : [
			'Z ważniejszych typów diod należy jeszcze wspomnieć o diodach świecących <m> oraz o fotodiodach (które są detektorami światła). <m>'
			'Diody świecące, określane też jako LED, w trakcie przewodzenia <m> (w standardowym kierunku) emitują światło o jakiejś barwie. <m>'
			'Barwa ta jest cechą danej diody <m> i zależy od materiałów z których została wykonana. <mark name="fotodioda" />',
			
			'Przewodzenie spolaryzowanej w kierunku zaporowym fotodiody <m> zależy od ilości padającego na nią światła. <m>'
			'Niespolaryzowana pod wpływem oświetlenia staje się źródłem prądu, <m> czyli jeżeli takiej fotodiody nie spolaryzujemy to pod wpływem oświetlenia <m> pojawi się na niej mierzalne napięcie. <m>'
			'Mało tego, nawet jeżeli zwykłą diodę LED oświetlimy <m> i będziemy mierzyli napięcie na jej końcówkach <m> to również woltomierz pokaże nam nie zerowe. <m>'
			'Dioda LED może również działać jako detektor światła. <mark name="prost1" />'
			
			'Dioda, <m> z tego względu że przewodzi na w jedną stronę, <m> używana jest też w prostownikach. <m>'
			'Prostownik służy zamianie prądu przemiennego <m> (czyli takiego, którego napięcie zmienia znak w czasie) na prąd wyprostowany. <m>',
			
			'Na symulacji widzimy prostownik oparty na pojedynczej diodzie, <m> który prąd przemienny 40 herców (czyli trochę mniej niż w gniazdku) <m>'
				'zamienia na prąd wyprostowany jednopołówkowo, <m> w którym nie ma już ujemnych połówek wejściowej sinusoidy. <m>'
			'Oczywiście też maksimum sinusoidy napięcia wyjściowego <m> jest obniżone o spadek napięcia na diodzie. <m>'
			'Wadą tego rozwiązania jest tracenie połowy sinusoidy <m> - w trakcie ujemnej połówki nasz układ nie może pobierać energii. <mark name="prost2" />'
			
			'Lepszym rozwiązaniem jest prostownik dwupołówkowy, <m> w postaci mostka prostowniczego. <m>'
			'Jak widzimy układ ten potrafi odbić dolną połówkę sinusoidy, <m> czyli układ może pobierać prąd o stałej polaryzacji <m> w obu połówkach wejściowej sinusoidy. <m>'
			'Widzimy też że maksimum napięcia wyprostowanego jest obniżone <m> o spadek napięcia na dwóch diodach. <m>',
			'Natomiast zalety tego układu są na tyle przeważające, <m> że na ogół stosowany jest właśnie tego typu mostek prostowniczy, <m> nazywany mostkiem Gretza. <mark name="prost3" />'
			
			'Można spotkać się też z układami prostowników trójfazowych. <m>'
			'Jeżeli posiadamy zasilanie trójfazowe, <m> czyli na zasilaniu mamy trzy sinusoidy z odpowiednim przesunięciem pomiędzy nimi, <m>'
				'to wtedy możemy użyć bardziej rozbudowanego mostka prostowniczego, <m> widocznego na symulacji. <m>'
			'W tym układzie napięcie wyjściowe nigdy nie osiąga nam zera <m> (tak jak mieliśmy to w przypadku poprzednich układów, <m> gdzie wykres napięcia wyjściowego dotykał nam punktu zerowego). <m>'
			'Tutaj jest zawsze powyżej i warto też zauważyć, <m> że w wypadku takiego prostownika jest ono powyżej maksimum <m> poszczególnych sinusoid napięć wejściowych. <m>'
			'Powodem tego jest to że prostownik ten korzysta z napięć międzyfazowych <m> a nie napięć w stosunku co do punktu neutralnego. <m>'
			
			'Widzimy że punkt neutralny, <m> który znajduje się po lewej stronie naszych źródeł, <m> nie jest w ogóle wykorzystywany. <m>'
			'Obciążenie nie zauważa tego punktu neutralnego <m> i korzysta tylko z napięć pomiędzy poszczególnymi fazami. <m>'
			'Natomiast prądami przemiennym nie będziemy zajmowali <m> się na tym kursie, więc na ich temat to było wszystko. <m>'
		]
	},
]
