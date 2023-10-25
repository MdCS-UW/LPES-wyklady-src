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
	{ 'comment': 'kondensator' },
	{
		'image': [
			[0.0, eduMovie.convertFile("kondensator.sch", negate=True)],
			["wzory1", eduMovie.convertFile('kondensator_wzory_1.tex', margins=12, viaCairo=True, negate=True)],
			["wzory2", eduMovie.convertFile('kondensator_wzory_2.tex', margins=12, viaCairo=True, negate=True)],
		],
		'text' : [
			'Kolejnym elementem biernym o którym trzeba powiedzieć jest kondensator. <m>'
			'Kondensator wprowadza do układu pojemność związaną ze swoją wartością nominalną, <m> czyli jest elementem na którym może gromadzić się ładunek elektryczny. <m>'
			'Kondensator oprócz ładunku musi gromadzić też energię w polu elektrycznym <m> – inaczej mielibyśmy problem z zasadą zachowania energii. <m>'
			
			'Kondensator oznaczany jest, tak jak widzimy na ekranie, <m> w formie dwóch pionowych kresek, jedna z nich może być albo prostokątem <m> albo być zaokrąglona, co oznacza polaryzację kondensatora. <m>'
			'Wiąże się to z tym że niektóre kondensatory ze względu na swoją konstrukcję, <m> mogą być podłączone do układu tylko w ten sposób, że na jednej z jego okładek <m> musi być napięcie wyższe niż na drugiej, <m>'
				'bo inaczej element może ulec zniszczeniu. <m>'
			'Wtedy takie kondensatory również na schematach są stosownie oznaczone. <mark name="wzory1" />'
			
			'Pojemność wyraża zdolność do gromadzenia ładunku wyrażamy ją w Faradach, <m> a najczęściej nano lub mikro faradach <m> i możemy ją opisać wzorem widocznym na ekranie. <m>'
			'Jeżeli mamy większą pojemność to przy tym samym napięciu <m> kondensator jest w stanie zgromadzić więcej ładunku. <m>'
			'A jeżeli mamy stałą pojemność to im większe napięcie <m> tym więcej ładunku zgromadzi nam kondensator. <m>'
			
			'Kondensator typowo służy do ograniczenia zmian napięcia <m> (dzięki temu że potrafi gromadzić ten ładunek i energię) <m> lub wprowadzania opóźnień związanych z czasem jego ładowania. <mark name="wzory2" />'
			'Opóźnienia te wynikają z faktu że jeżeli mamy skończony prąd, <m> który może popłynąć, to dostarczenie ładunku potrzebnego do naładowania <m> kondensatora o danej pojemności do danego napięcia wymaga pewnego czasu. <m>'
			'Napięcie na kondensatorze będzie rosło w funkcji czasu, <m> a nie będzie zmieniało się natychmiastowo. <m>'
			'Czas ładowania rośnie ze wzrostem pojemności i napięcia do którego chcemy <m> ją naładować, a maleje ze wzrostem prądu ładowania. <m>'
			'Im wydajniejsze źródło z którego ładujemy, im większy prąd może dostarczyć, <m> im mniejszą mamy tam rezystancje, tym szybciej kondensator się naładuje. <m>'
			'Jednak w tego typu zastosowaniach chodzi o to aby ładował, rozładowywał się <m> określony czas więc często dodawany jest rezystor, <m>'
				'aby nie polegać na ograniczeniu prądowym źródła <m> a zapewnić to ograniczenie w bardziej kontrolowany, lokalny sposób. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("cap", 0, 0.1)],
			["cap_ladowanie - 3", eduMovie.circuitjs("cap", 3, 8, [("switch", 560, 140)])],
			["cap_rozladowanie - 5", eduMovie.circuitjs("cap", 2, 18, [("switch", 560, 140), ("switch", 560, 140)], preActions=[("switch", 560, 140), ("wait", 6)])],
			["cap_rozladowanie2 + 1",    eduMovie.circuitjs("cap", 1, 12, [("setSlider", 2, 0), ("wait", 2), ("switch", 560, 140), ("switch", 560, 140)], preActions=[("switch", 560, 140), ("wait", 6)])],
			["cap_ac - 6", eduMovie.circuitjs("cap_ac", 0, 12)],
		],
		'text' : [
			'Na symulacji mamy kondensator 200 mikrofaradów, <m> do ładowania którego używamy napięcia 5 woltów i rezystora 100 omów, <m> a do rozładowywania będziemy używali sumy rezystancji tych 100 omów i 1 kilo oma. <m>'
			'Ładowanie bądź rozładowywanie jest zależne od położenia przełącznika. <m>'
			'Kondensator początkowo był nie naładowany, więc aktualnie prąd nie płynie. <mark name="cap_ladowanie" />'
			'Zatem gdy podłączymy ładowanie kondensatora <m> to widzimy na wykresie oscyloskopowym wzrost napięcia na tym kondensatorze <m> do momentu aż osiąga ono prawie 5 woltów, gdyż tyle wynosi napięcie zasilania. <m>'
			
			'Przełączmy teraz na rozładowywanie, <mark name="cap_rozladowanie" /> jak widzimy dzięki zastosowaniu większej rezystancji zachodzi ono znacznie wolniej. <m>'
			'Mamy tutaj rezystancję ponad dziesięciokrotnie większą, <m> w związku z czym rozładowywanie zachodzi również ponad dziesięciokrotnie dłużej. <m>'
			
			'Możemy naładować ponownie ten kondensator <mark name="cap_rozladowanie2" /> i zmienić tutaj na przykład też na 100 omów. <m>'
			'Zobaczymy że rozładowywanie zachodzi teraz już tylko dwa razy wolniej <m> niż ładowanie, bo użyta rezystancja jest dwukrotnie większa. <m>'
			
			'Warto tutaj zauważyć że kondensator pomimo bycia przerwą w obwodzie <m> zdaje się przewodzić prąd zmienny. <m>'
			'Po zmianie przyłożonego do niego napięcia prąd płynie do momentu, <m> aż kondensator nie naładuje się do poziomu nowej wartości napięcia. <m>'
			'I wtedy praktycznie przestaje przewodzić. <m>'
			
			'Z przewodzeniem prądów zmiennych związane jest kolejne <m> zastosowanie kondensatorów, którym jest odcinanie składowej stałej. <mark name="cap_ac" />'
			'Możemy to zobaczyć trochę lepiej na widocznej teraz symulacji gdzie mamy prąd <m> zmienny 20 herców, który w takim układzie non-stop płynie przez kondensator. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('kondensatory.svg', margins=0)],
		],
		'text' : [
			'Oczywiście w rzeczywistości kondensatory nie są idealne <m> (tak jak było to na pokazywanych symulacjach) i występują w nich <m> zjawiska pasożytnicze oraz posiadają one pewne parametry graniczne. <m>'
			'Głównymi zjawiskami pasożytniczymi jest upływność kondensatora <m> (czyli to że kondensator przewodzi jakiś niewielki prąd stały, <m> w związku z uciekaniem z niego ładunku) <m>'
				'oraz rezystancja wewnętrzna (czyli szeregowy opór <m> dołączony do idealnego kondensatora, który ogranicza maksymalną <m> częstotliwość jego pracy, spowalnia jego reakcje na zmiany napięcia). <m>'
			
			'Najistotniejszym parametrem kondensatorów rzeczywistych oprócz <m> pojemności nominalnej jest maksymalne napięcie <m> które możemy przyłożyć do takiego kondensatora. <m>'
			'Jeżeli zostanie ono przekroczone, <m> to nastąpi przebicie kondensatora, jego uszkodzenie i zacznie on przewodzić. <m>'
			'Drugim takim ważnym parametrem jest to <m> czy wymaga on zachowania polaryzacji, czy nie. <m>'
			'Oprócz tego mamy też parametry takie jak <m> maksymalna temperatura pracy, żywotność elementu, itd. <m>'
		]
	},
]
