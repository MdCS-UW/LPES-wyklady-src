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
	{ 'title': [ "#08.1", "Podstawy", "elektroniki", "" ] },
	
	{ 'comment': 'podstawy elektroniki' },
	{
		'image': [
			[0.0, ""], # TODO jakaś ilustracja filmik obrazujący zjawisko przepływu prądu ... https://www.youtube.com/watch?v=63FnT0W-Hxc  https://www.youtube.com/watch?v=FReDAGo5fks
		],
		'text' : [
			'Zjawisko przepływu prądu związane jest z przepływem ładunku elektrycznego, <m> czyli uporządkowanym ruchem nośników ładunku elektrycznego. <m>'
			'W teorii przyjmuje się że prąd płynie od plusa do minusa, <m> natomiast w rzeczywistości zależy to od tego w jakim ośrodku on płynie. <m>'
			'W przypadku metali ładunki elektryczne mają znak ujemny, są to elektrony <m> i fizyczne przepływ jest od potencjału ujemnego do dodatniego. <m>'
			'Istnieją jednak także środowiska w których występują nośniki ładunku <m> o obu znakach, tudzież jedynie nośniki ładunku dodatnie. <m>'
			
			'Aby występowało zjawisko przepływu ładunku konieczna jest różnica potencjałów, <m> jakieś napięcie pomiędzy końcami takiego przewodnika. <m>'
			'Natomiast sam przepływ prowadzi do neutralizacji tej różnicy, <m> dlatego dla podtrzymania stałej różnicy konieczne jest istnienie źródeł prądu, <m> prowadzących do rozdzielania ładunków dodatnich od ujemnych. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('napięcie.svg', negate=True)],
			["potencjal_def", eduMovie.convertFile("potencjał-definicja.tex", negate=True)],
			["potencjal_sym", eduMovie.convertFile("potencjał.sch", negate=True, dpi=220)],
			["gnd_sym", eduMovie.convertFile("masa.sch", negate=True)],
		],
		'text' : [
			'Na wstępie należy zdefiniować kilka pojęć. <m>'
			'Napięciem elektrycznym nazywamy różnicę potencjałów pomiędzy dwoma punktami, <m> czyli napięcie pomiędzy punktem A i punktem B jakiegoś obwodu, <m> jest to różnica potencjałów w tych punktach. <m>'
			'Jako że w przypadku odejmowania znak wyniku zależy od kolejności argumentów, <m> to również napięcie pomiędzy A i B to jest to samo co <m> minus napięcie pomiędzy B i A. <m>'
			'Znak napięcia zależy od kierunku w którym przechodzimy po obwodzie elektrycznym. <mark name="potencjal_def" />'
			
			'Do zdefiniowania napięcia skorzystaliśmy z pojęcia potencjału elektrycznego. <m>'
			'Potencjał elektryczny w jakimś punkcie jest to skalarna wielkość, <m> charakteryzująca pole elektryczne w danym punkcie. <m>'
			'Odpowiada ona pracy którą trzeba wykonać aby przenieść ładunek <m> z tego punktu do nieskończoności podzielonej przez wielkość tego ładunku. <m>'
			'Tak brzmi formalna definicja. Natomiast w większości przypadków <m> w praktyce elektronika nie jest ona mu potrzebna. <mark name="potencjal_sym" />'
			
			'W elektronice często używa się wartości potencjału <m> względem umownego potencjału zerowego. <m>'
			'Pozwala to na traktowanie samych potencjałów tak jak różnicy potencjałów, <m> czyli jak napięcia elektrycznego. <m>'
			'W efekcie czego elektronik często zamiennie używa określenia <m> stałe napięcie i stały potencjał w jakimś punkcie. <m>'
			'Jeżeli mówimy że w jakimś punkcie mamy potencjał na przykład 5 woltów, <m> to mamy na myśli że mamy tam napięcie 5 woltów w stosunku co do punktu <m> mającego ten umowny potencjał zerowy. <mark name="gnd_sym" />'
			
			'Potencjał zerowy określany jest mianem masy. <m>'
			'Do jego oznaczenia używane jest często <GND>[ge en de] od angielskiego ground. <m>'
			'Punkty na których występuje ten potencjał zerowy na schematach <m> oznaczamy najczęściej tak jak pokazano to na ekranie. <m>'
			'Jest to tak naprawdę umowa, że w danym miejscu potencjał przyjmujemy za zerowy. <m>'
			'Potencjały w innych punktach mogą być dodatnie bądź ujemne, <m> w stosunku co do potencjału zerowego. <m>'
			
			'Potencjał ten może być równy potencjałowi ziemi, <m> masie ochronnej określanej jako <PE>[Pe E]. <m>'
			'Natomiast nie musi być z nim związany – układy te mogą być izolowane, <m> czyli masa naszego układu elektronicznego niekoniecznie musi być powiązana <m> z potencjałem masy ochronnej, czyli tak zwanym uziemieniem. <m>'
			
			'Można też spotkać się z układami w których mamy więcej niż jedną masę. <m>'
			'Występuje to w sytuacji gdy w układzie <m> występują części nie połączone ze sobą elektrycznie. <m> Na przykład zasilane z osobnych źródeł napięcia lub odizolowane transformatorem. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("elektronik_vs_szkoła.sch", negate=True, dpi=160)],
			["line_crossing", eduMovie.convertFile("line_crossing.sch", negate=True, dpi=180)],
			["current", eduMovie.convertFile("current.sch", negate=True)],
		],
		'text' : [
			'Typowo w schematach stosowanych przez elektroników <m> nie znajdziemy symbolu baterii, <m> chyba że urządzenie jest fizycznie z niej zasilane, <m>'
				'natomiast będziemy tam mieli oznaczenie potencjału zerowego <m> i oznaczenie jakiś potencjałów zasilających. <m>'
			'Unika się też nadmiernej ilości linii związanych z tymi potencjałami, <m> stosując zamiast tego wielokrotnie znaczniki tych potencjałów. <m>'
			'Jeżeli w dwóch miejscach schematu widzimy ten sam potencjał, <m> na przykład symbol masy, oznacza to że są one połączone, <m> nawet jeżeli nie ma pomiędzy nimi linii. <m>'
			
			'Typowo jeżeli rysujemy jakiś schemat elektroniczny to potencjały wyższe <m> umieszcza się wyżej, a niższe niżej, czyli punkty z potencjałem na przykład <m> <5V>[pięciu woltów] będziemy mieli na górze obrazka, a masę na dole. <m>'
			
			'Również przepływ prądu jest od góry do dołu i od lewej do prawej, <m> czyli jeżeli mamy opornik narysowany poziomo <m> to typowo prąd będzie płynął od lewej do prawej. <m>'
			'Oczywiście są to tylko konwencje i dany schemat może tego nie spełniać, <m> jednak większość schematów trzyma się tych konwencji, <m> gdyż są one wygodne i ułatwiają czytanie schematów. <m>'
			'Natomiast należy zachować ostrożność bo może się zdarzyć, <m> że jednak ten prąd przez dany opornik będzie płynął odwrotnie, <m> w związku z tym że schemat narysowany jest dziwnie albo podchwytliwie. <mark name="line_crossing" />'
			
			'Powszechnie przyjętą praktyką jest oznaczanie miejsc połączeń linii, <m> nazywanych też węzłami za pomocą kropki. <m>'
			'Czyli jeżeli mamy dwie po prostu przecinające się linie <m> to oznacza brak połączenia elektrycznego między nimi, <m>'
				'a jeżeli na przecięciu zostanie umieszczona kropka <m> to znaczy że są one ze sobą połączone, <m> tworząc tak zwany węzeł sieci elektrycznej. <m>'
			
			'Zasadniczo nie ma formalnego standardu, <m> który określałby sposób rysowania schematów elektronicznych, <m> czy elektrycznych i używane na nich symbole. <m>'
			'Generalnie są to powszechnie przyjęte zwyczaje. <m>'
			'Nierzadko zdarza się że temu samemu elementowi odpowiada <m> kilka różnych reprezentacji graficznych, <m> ale o nich będziemy mówić przy omawianiu poszczególnych elementów. <mark name="current" />'
			
			'Ostatnim pojęciem które warto zdefiniować na wstępie <m> jest natężenie prądu określane skrótowo jako prąd i oznaczone jako I. <m>'
			'Jest to stosunek przemieszczanego ładunku w jakimś czasie <m> do czasu jego przepływu, <m>'
				'czyli informuje nas o tym jak szybko przepływa ładunek, <m> ile jednostek ładunku elektrycznego przepływa w jednostce czasu. <m>'
			'Im większy prąd (formalnie jego natężenie) tym więcej ładunków <m> w danym czasie jest przemieszczanych. <m>'
			'Oczywiście przepływ prądu ma również swój kierunek <m> i jak już wspomnieliśmy, niezależnie od ruchu fizycznych nośników, <m>'
				'przyjmuje się że prąd przepływa od potencjału wyższego do niższego <m> – zgodnie z kierunkiem przepływu prądu mamy spadek potencjału, napięcia. <m>'
		]
	},
]
