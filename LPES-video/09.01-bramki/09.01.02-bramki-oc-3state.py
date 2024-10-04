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
	{ 'comment': 'bramki - 3 stanowe, open drain' },
	{
		'image': [
			[0.0, eduMovie.convertFile('trojstanowosc.tex', negate=True)],
			["trzystanowe - 1", eduMovie.circuitjs("ster", 2, 20, [
				("switch", 160, 185), ("wait", 1.7), ("switch", 160, 185), ("wait", 1.7),
				("switch", 160, 320), ("wait", 1.7), ("switch", 160, 320), ("wait", 1.7),
				("switch", 300, 185), ("switch", 300, 320),
				("switch", 160, 320), ("wait", 1.7), ("switch", 160, 320), ("wait", 1.7),
				("switch", 160, 185), ("wait", 1.7), ("switch", 160, 185), ("wait", 1.7),
			])],
			["trzystanowe2 - 2.5", eduMovie.circuitjs("ster", 2, 2, [("switch", 300, 320)])],
		],
		'text' : [
			'Typowa bramka logiczna wymusza w sposób silny stan na swoim wyjściu, <m> czyli podłącza je do napięcia zasilania lub do poziomu masy. <m>'
			'Z tego względu nie możemy połączyć dwóch bramek bezpośrednio ze sobą, <m> bo w przypadku wymuszania przeciwnych stanów, <m> prowadziłoby to do zwarcia i mogłoby uszkodzić bramki. <m>'
			'Mamy tutaj dwa istotne wyjątki <m> – są to bramki trójstanowe oraz bramki typu open kolektor / open drain. <m>'
			
			'Bramki trójstanowe oprócz stanu wysokiego i niskiego <m> mają też stan wysokiej impedancji, czyli nie podłączonego wyjścia. <m>'
			'Posiadają one dodatkowe wejście decydujące o tym czy ich wyjście <m> jest podłączone do stanu wynikającego z funkcji logicznej, jaką realizują, <m> czy jest odłączone. <mark name="trzystanowe" />'
			'Symulację takiego przypadku widzimy po lewej stronie ekranu <m> – mamy tam wyjścia trzech bramek trójstanowych <m> – każda z nich może być odłączona, podawać stan niski lub wysoki. <m>'
			'Wyjścia tych bramek są ze sobą połączone <m> i o stanie linii wyjściowej decyduje podłączona do niej aktualnie bramka. <m>'
			
			'Jeżeli podpięli byśmy 2 takie bramki równocześnie <m> i wymusili na nich przeciwny stan to dochodzi do zwarcia. <mark name="trzystanowe2" />'
			'Warto zwrócić uwagę że symulacja pokazuje bardzo duży prąd, <m> oczywiście w rzeczywistości prąd byłby znacznie mniejszy, <m> ale i tak mógłby doprowadzić do uszkodzenia bramek. <m>'
			
			'Dlatego nie możemy łączyć wyjść zwykłych bramek, <m> a przy bramkach trójstanowych musimy dbać o to żeby tylko jedna z nich <m>'
				'w danej chwili była podpięta do takiej magistrali, <m> a pozostałe były w stanie wysokiej impedancji. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("ster", 0, 1)],
			["opencolector", eduMovie.circuitjs("ster", 2, 10, [
				("switch", 620, 210), ("wait", 1.7), ("switch", 620, 440), ("wait", 1.7), ("switch", 620, 325), ("wait", 1.7), ("wait", 1.7), ("switch", 620, 440)
			])],
		],
		'text' : [
			'Innym typem bramek, których wyjścia możemy łączyć bezpośrednio ze sobą <m> są bramki typu otwarty kolektor, <m> które na wyjściu mają tak naprawdę tranzystor NPN lub n-mos. <m>'
			'W zależności od tego czy to jest tranzystor <bipolarny>[bi polarny] czy mosfet to <m> mówimy o open kolektorze albo open drenie. <m>'
			'Jednak często układy w rzeczywistości będące open drenem <m> określane są i tak jako open kolektor. <m>'
			'Wynika to z faktu iż ta terminologia jest starsza i na tyle przyjęła się <m> w nazewnictwie że większość takich układów nazywana jest open kolektor, <m>'
				'nawet jeżeli faktycznie mamy tranzystor mosfet który kolektora nie ma. <m>'
			
			'Nazewnictwo to wynika z faktu wyprowadzenia na zewnątrz <m> nie podłączonego do niczego kolektora lub drenu tranzystora, <m>'
				'który gdy bramka ma mieć na wyjściu stan niski zwiera do masy, <m> a gdy bramka ma mieć stan wysoki nie robi nic. <m>'
			
			'Jako że dla stanu wysokiego bramka nie robi nic to musimy zewnętrznie <m> zapewnić stan wysoki takiej linii gdy żadna z bramek jej nie zwiera. <m>'
			'Robimy to z użyciem rezystora podciągającego, aby zapewnić ograniczenie prądu <m> gdy któraś zacznie zwierać i uniknąć zwarcia w takiej sytuacji. <mark name="opencolector" />'
			
			'Układ tego typu, w odróżnieniu od wcześniej omówionego układu <m> z bramkami trójstanowymi, pozwala na realizowanie funkcji logicznej na drucie. <m>'
			'Jak widzimy wystarczy żeby wyjście jednej bramki było w stanie niskim, <m> aby całość była w stanie niskim - jest to zatem funkcja logiczna and . <m>'
			'Dużą zaletą tego rozwiązania jest brak konieczności <m> troszczenia się o sterowanie wyjściem trójstanowym. <m>'
			
			'Warto zwrócić uwagę, że symulacja jest tak wykonana, <m> aby literka oddawała stan wyjścia całej bramki, <m> a nie stan podawany na bazę tranzystora do której jest podłączona. <m>'
		]
	},
]
