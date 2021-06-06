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

code_xml_A = r'''
txt = """<a>
	<b>A<h>qwe ... rty</h></b> ABCD... &amp;&apos; HIJ...
	<c x="q" w="p p">EE FĄ</c> <g y="zz" />
	<c x="pp">123 <d rr="oo">456</d> 78 90.</c>
</a>"""
'''

code_xml_B = code_xml_A + r'''
import xml.etree.ElementTree as xml

rootNode = xml.fromstring(txt)

print("nazwa głównego elementu to:", rootNode.tag)
print("jego potomkowie to:")
for subNode in rootNode:
	zawartosc = xml.tostring(subNode, encoding="unicode")
	print(" ", subNode.tag, ":", zawartosc.strip())
'''

code_json_A = r'''
txt = """{
	"info": "bbb",
	"ver": 31,
	"d": [
		{"a": 21, "b": {"x": 1, "y": 2}, "c": [9, 8, 7]},
		{"a": 17, "b": {"x": 6, "y": 7}, "c": [6, 5, 4]}
	]
}
"""
'''

code_json_B = r'''
import json
''' + code_json_A.strip() + r'''
d = json.loads(txt)

print( d["d"][1]["b"] )
d["d"][1]["b"]["x"] = "XXX"

print( json.dumps(d, ensure_ascii=False) )
'''

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#03.6", "Python:", "biblioteki (xml,", "json, sql, ...)" ] },
	
	{ 'comment': 'biblioteki' },
	{
		'consoleTop': [
			[0.0, ""],
		],
		'consoleDown': [
			[0.0, eduMovie.prompt()],
		],
		# 'image': [ [0.0, ""] ], # TODO jakiś obrazek zamiast pustej konsoli ?
		'text' : [
			'Na pierwszych zajęciach z Pythona mówiliśmy o definiowaniu funkcji <m> i o tym że jest to tak naprawdę nazwany kawałek kodu do którego <m> możemy odwołać się z innego miejsca przekazując do niego jakieś argumenty. <m>'
			'Mówiliśmy także o tym że używamy ich aby unikać powtarzania <m> tego samego kodu w różnych miejscach programu. <m>'
			
			'Rozszerzeniem tej koncepcji, pozwalającym unikać powtarzania <m> tego samego lub podobnego kodu pomiędzy różnymi programami, są biblioteki. <m>'
			'Stanowią one zbiory funkcji i związanych z nimi struktur danych. <m>'
			
			'Do tej pory korzystaliśmy z elementów biblioteki standardowej Pythona <m> na przykład pisząc import <os>[O S] włączaliśmy sobie odpowiedni kawałek tej biblioteki. <m>'
			'W tej części również pokażemy kilka przykładów rzeczy które <m> biblioteka standardowa Pythona potrafi nam ułatwić <m> oraz kilka przykładów które są poza biblioteką standardową Pythona. <m>'
			
			'Wielokrotnie już mówiliśmy o plikach tekstowych, <m> nauczyliśmy się także czytać i zapisywać takie pliki. <m>'
			'Często w pliku tekstowym chcemy przechowywać <m> jakieś dane posiadające pewną strukturę. <m>'
			'Istnieje kilka standardowych formatów umożliwiających nadanie <m> danym tekstowym jakieś struktury i co najmniej <m> o trzech najpopularniejszych warto tutaj wspomnieć. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_xml_A, "py")],
			["etree", eduMovie.clear + eduMovie.code2console(code_xml_B, "py")],
		],
		'consoleDown': [
			[0.0, ""],
			["etree", eduMovie.runCode(code_xml_B, [], cmd="python3")],
		],
		'text' : [
			'Pierwszym będzie XML, czyli język znaczników. <m>'
			'Tekst zawarty w plikach tego typu strukturyzowany jest z użyciem <m> znaczników zapisywanych przy pomocy nawiasów trójkątnych, <m> tak jak jest to widoczne na ekranie. <m>'
			
			'Znaczniki występują parami – otwierający i zamykający, <m> oba znaczniki z pary używają takiej samej nazwy, <m>'
			'którą jest tekst występujący zaraz po lewym nawiasie trójkątnym <m> (znaku mniejszości) do pierwszej spacji <m> lub prawego nawiasu trójkątnego kończącego znacznik otwierający. <m>'
			'Znacznik zamykający składa się z lewego nawiasu, <m> ukośnika, nazwy i prawego nawiasu trójkątnego. <m>'
			
			'Znaczniki mogą posiadać zawartość, <m> czyli to co jest pomiędzy znacznikiem otwierającym i zamykającym. <m>'
			'Jeżeli jej nie posiadają znacznik otwierający i zamykający <m> mogą być zapisane razem poprzez dodanie ukośnika <m> przed prawym nawiasem trójkątnym. <m>'
			'Znaczniki mogą posiadać także atrybuty postaci <m> nazwa równa się wartość w cudzysłowach, <m> rozdzielane spacjami i zapisywane wewnątrz znacznika otwierającego. <mark name="etree" />'
			'Oczywiście można napisać własnoręcznie <parser>[par ser] tego typu danych <m>, jednak Python dostarcza standardowych narzędzi do manipulowania <XMLem>[iksem elem]. <m>'
			'Jednym z nich jest moduł ElementTree. <m>'
			'W tym celu importujemy odpowiedni fragment biblioteki <m> standardowej Pythona, jako że nazwa jest długa to żeby nie wpisywać <m> jej za każdym razem nazywamy go w tym przykładzie po prostu <xml>[XML]. <m>'
			
			'Następnie poddajemy parsowaniu napis zawierający <m> kod XML poprzez wywołanie funkcji <fromstring>[from string]. <m>'
			'Po wykonaniu takiej operacji, która skutkuje odnalezieniem <m> głównego <noda>[nołda] (czyli głównego znacznika w naszym tekście) <m>'
			'możemy na przykład sprawdzić jak się on nazywa <m> i wylistować jego potomków, tak jak jest to pokazane na ekranie. <m>'
			
			'Oczywiście możliwości ElementTree na tym się nie kończą <m> – możemy wyszukiwać elementy o danej nazwie, sprawdzać ich atrybuty, itd. <m>'
			'Możemy także modyfikować strukturę danych powstałą w oparciu <m> o kod XML i wygenerować w oparciu o nią nową wersję tego kodu. <m>'
			
			'Szczegóły można znaleźć w dokumentacji tego modułu. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_json_A, "py")],
			["json", eduMovie.clear + eduMovie.code2console(code_json_B, "py")],
		],
		'consoleDown': [
			[0.0, ""],
			["json", eduMovie.runCode(code_json_B, [], cmd="python3")],
		],
		'text' : [
			'Drugim formatem o którym wspomnimy jest <JSON>[dżejson]. Przypomina on <m> bardzo zapis pythonowych obiektów takich jak słowniki czy listy. <m> Jednak nie wywodzi się z Pythona. <mark name="json" />'
			
			'Python udostępnia natomiast narzędzia do konwersji tekstu <m> w tym formacie na Pythonową strukturę danych oraz na zapis <m> (tak zwaną serializację) Pythonowych danych do tego formatu. <m>'
			'Pozwalają na to funkcje zawarte w module <json>[dżejson] <m> – funkcja loads pozwala na odwzorowanie danych z postaci tekstowej <m> do struktury Pythonowych list i słowników. <m>'
			'Natomiast funkcja dumps generuje tekstowy opis <m> pythonowych danych zgodny z formatem <JSON>[dżejson]. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("tekstowa_baza_danych.svg", negate=True)],
		],
		'text' : [
			'Trzecim formatem takich danych są pliki przypominające tabele <m> (na przykład te z arkusza kalkulacyjnego). <m>'
			'Pojedyncza linia odpowiada w nich zestawowi danych <m> (określanym jako rekord) odpowiadającemu opisowi jakiegoś pojedynczego obiektu. <m>'
			'Każda taka linia jest w taki sam sposób podzielona na pola <m> (odpowiadające komórkom tabeli), z użyciem określonego separatora. <m>'
			'Poszczególne pola opisują w ramach kolejnych kolumn <m> kolejne cechy obiektu. <m>'
			'Na ich temat będziemy sporo mówić na następnych zajęciach, <m> jako o tekstowych bazach danych.'
		]
	},
]

code_sql_A = r'''
import sqlite3
'''

code_sql_B = code_sql_A + r'''
conn = sqlite3.connect('example.db')
c = conn.cursor()
'''

code_sql_C = code_sql_B + '''
c.execute("CREATE TABLE users (uid INT PRIMARY KEY, name TEXT);")
c.execute("CREATE TABLE posts (pid INT PRIMARY KEY, uid INT, text TEXT);")

c.execute("INSERT INTO users VALUES (21, 'user A');")
c.execute("INSERT INTO users VALUES (2671, 'user B');")

c.execute("INSERT INTO posts VALUES (1, 21, 'abc ..');")
c.execute("INSERT INTO posts VALUES (2, 21, 'qwe xyz');")
c.execute("INSERT INTO posts VALUES (3, 2671, 'test');")

conn.commit()
'''

code_sql_D = code_sql_B + r"""
maxUid = 100
for r in c.execute("SELECT * FROM users WHERE uid < ?;", (maxUid,)):
	print(r)
"""

code_sql_E = code_sql_B + r"""
for r in c.execute("SELECT u.name, p.text FROM users AS u JOIN posts AS p ON (u.uid = p.uid);"):
	print(r)
"""

clipData += [
	{ #  
		'consoleTop': [
			[0.0, ""],
			["sqlA", eduMovie.clear + eduMovie.code2console(code_sql_A, "py")],
			["sqlB", eduMovie.clear + eduMovie.code2console(code_sql_B, "py")],
			["sqlC", eduMovie.clear + eduMovie.code2console(code_sql_C, "py")],
		],
		'consoleDown': [
			[0.0, ""],
			["sqlC", eduMovie.runCode(code_sql_C, [], cmd="python3")],
		],
		'text' : [
			'Skoro wspomnieliśmy o bazach danych, warto pokazać że z użyciem <m> odpowiedniej biblioteki możemy z nich z łatwością korzystać w Pythonie. <m>'
			
			'Do komunikacji z bazami danych bardzo często wykorzystywany jest SQL, <m> jest to ustandaryzowany język służący do wykonywania zapytań na bazach danych. <m>'
			
			'Większość baz danych (takich jak na przykład Maria DB, Postgres) <m> działa na zasadzie klient-serwer. <m>'
			'Klient podłącza się do serwera, działającego jako osobna usługa. <m>'
			'Jest to wygodne w przypadku dużych systemów i aplikacji, <m> ale w przypadku mniejszych systemów wygodniejsze może być posiadanie <m> po prostu pliku binarnego z którego możemy korzystać poprzez zapytania SQL. <m>'
			'W tym celu stosowany jest często <Sqlite>[SQ lajt], wykorzystywany na przykład <m> wewnętrznie przez Firefoxa do trzymania informacji <m> o zakładkach, historii odwiedzanych stron, <itp.>[i tym podobnych.] <mark name="sqlA" />'
			
			'<Sqlite>[SQ lajt] jest biblioteką pozwalającą na odwoływanie się <m> do przechowywanej w pliku bazy danych z pomocą zapytań SQL. <m>'
			'Aby skorzystać z niego w Pythonie, należy zainstalować moduł <sqlite3>[SQ lajt 3] <m> (nie jest on częścią biblioteki standardowej Pythona), <m> a następnie zaimportować go w tworzonym programie. <mark name="sqlB" />'
			
			'Następnie tworzymy połączenie do bazy danych przy pomocy funkcji connect, <m> do której jako argument podajemy nazwę pliku w którym jest baza danych. <m>'
			'Jeżeli pliku nie było zostanie on utworzony, w związku z tym <m> pomocne może być wcześniejsze sprawdzenie istnienia tego pliku, <m> tak aby po jego utworzeniu móc zainicjalizować bazę danych. <m>'
			'Przykład jak to można zrobić jest podany w skrypcie do dzisiejszych zajęć. <m> W tej chwili założymy że wiemy że tego pliku nie było i <m> przejdziemy do wydawania poleceń SQL inicjujących strukturę bazy danych. <m>'
			
			'Po utworzeniu połączenia do bazy danych należy utworzyć również <m> obiekt tak zwanego kursora, którego będziemy używać do wykonywania poleceń SQL. <mark name="sqlC" />'
			
			'W tym momencie widzimy na ekranie kod tworzący dwie tabele <m> – users i posts oraz wstawiający do nich jakieś dane. <m>'
			'Do tworzenia tabel używamy <SQLowego>[eskuelowego] polecenia create table <m> po którym następuje nazwa tabeli a następnie, w nawiasach okrągłych, <m> rozdzielana przecinkami lista jej kolumn. <m>'
			'Określenie każdej kolumny składa się z jej nazwy <m> oraz typu i ewentualnych dodatkowych flag. <m>'
			'Na przykład w tabeli users tworzymy kolumnę uid będącą <m> liczbami całkowitymi i stanowiącą klucz w tej tabeli <m> (co oznacza między innymi iż wartości w tej kolumnie muszą być unikalne) <m> oraz kolumnę name przechowującą tekst. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, ""],
			["sqlD", eduMovie.clear + eduMovie.code2console(code_sql_D, "py")],
			["sqlE", eduMovie.clear + eduMovie.code2console(code_sql_E, "py")],
		],
		'consoleDown': [
			[0.0, ""],
			["sqlD", eduMovie.runCode(code_sql_D, [], cmd="python3")],
			["sqlE", eduMovie.runCode(code_sql_E, [], cmd="python3")],
		],
		'text' : [
			'Do wstawiania danych korzystamy z <SQLowego>[eskuelowego] polecenia insert into <m> po którym podajemy nazwę tabeli następnie słowo kluczowe values <m> i w nawiasach okrągłych listę wartości w kolejności <m> odpowiadającej kolumnom danej tabeli. <mark name="sqlD" />'
			
			'Na bazie możemy przy pomocy poleceń SQL wykonać także jakieś zapytania. <m>'
			'Do pobierania danych używane jest <SQLowe>[eskuelowe] polecenie select, <m> po którym określamy co chcemy pobrać, czyli na przykład jakie kolumny <m> (gwiazdka oznacza wszystkie), a następnie po słowie kluczowym <m> from, skąd chcemy te dane pobrać. <m>'
			'Możemy tu podać nazwę tabeli lub bardziej złożone wyrażenie. <m>'
			'Po słowie kluczowym where możemy określić <m> warunki na pobierane dane, ten fragment możemy też pominąć. <m>'
			
			'W widocznym na ekranie przykładzie pod pytajnik zostanie podstawiona <m> wartość zmiennej maxUid, oczywiście moglibyśmy ją wpisać <m> też bezpośrednio w polecenie SQL. <mark name="sqlE" />'
			
			'Siła SQL polega na możliwości formuowania złożonych warunków <m> i pobierania danych z połączonych tabel, <m> tak jak to widzimy w drugim przykładzie. <m>'
			'Pobieramy tutaj jedną kolumnę z tabeli users i jedną z tabeli posts, <m> ale w taki sposób że wiersze tych tabel połączone są <m> ze sobą w oparciu o zgodność pola uid. <m>'
			'Dla naszej symulowanej bazy jakiegoś systemu komentarzy oznacza to <m> że pobieramy nazwy użytkowników i treści ich postów, <m> gdzie dane te przechowywane są w osobnych tabelach, <m> z których każda zawiera uid – numeryczny identyfikator użytkownika. <m>'
			
			'Polecenia <SQLowe>[eskuelowe] nie są wrażliwe na wielkość liter, <m> a to że wszystkie słowa kluczowe w pokazanych przykładach zapisane były <m> wielkimi literami jest jedynie dość często spotykaną konwencją. <m>'
			'SQL jest rozbudowanym narzędziem i pokazaliśmy <m> tutaj tylko jego niewielki kawałek. <m>',
			
			
			'Z użyciem bibliotek możemy na przykład także łatwo <m> tworzyć graficzny interfejs użytkownika. <m>'
			'Nie będziemy tego jednak omawiać bardziej szczegółowo <m> w ramach tego kursu, a osoby zainteresowane tym zagadnieniem odsyłam do skryptu <m>, gdzie podany jest link do odpowiednich przykładów kodu. <m>'
			
			'Było to dość pobieżne pokazanie kilku <m> wybranych bibliotek dostępnych dla Pythona. <m>'
			'W prezentowanych przykładach nie chodzi o to żeby nauczyć się <m> korzystania z tych konkretnych bibliotek, <m> ponieważ uczenie się korzystania z bibliotek na zapas nie za bardzo ma sens. <m>'
			'Chodzi o to żeby poznać pewne mechanizmy, schematy <m> i przekonać się że używanie bibliotek jest przydatne. <m>'
			'Bibliotek istnieją tysiące (albo i więcej) i programowanie <m> w dużej mierze polega na korzystaniu z nich. <m>'
			'Programista musi znaleźć bibliotekę która w danym zastosowaniu <m> będzie dla niego najwygodniejsza i najbardziej odpowiednia do tego zastosowania, <m> następnie zapoznać się z jej dokumentacją i ją zastosować w programie. <m>'
		]
	},
]

