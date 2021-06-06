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
	{ 'comment': 'mosfet' },
	{
		'image': [
			[0.0, eduMovie.convertFile("mosfet_symbole.sch", negate=True)],
		],
		'text' : [
			''
			'Innym typem tranzystorów są tranzystory typu mosfet, <m> stanowiące fragmenty rodziny tranzystorów polowych. <m>'
			'Wyróżniamy dwa ich typy – n i p będące analogią dla NPN i PNP. <m>'
			
			'Na ekranie widzimy symbole tych tranzystorów. <m>'
			'Posiadają one również 3 wyprowadzenia - źródło, dren i bramkę, <m> podpisane na widocznych symbolach jako S, D i G. <m>'
			
			'Przewodzenie tych tranzystorów regulowane jest napięciem <m> przykładanym pomiędzy bramką a źródłem, a nie prądem bazy. <m>'
			'Tranzystory MOSFET posiadają izolowaną bramkę to znaczy, <m> że nie pobiera ona prądu w żadnym stanie pracy. <m>'
			'Wyjątkiem jest prąd potrzebny do przeładowania pasożytniczej pojemności <m> bramka-źródło płynący w momencie przełączania takiego tranzystora. <m>'
			
			'Tranzystor N-MOSFET posiada regulowane przewodzenie w kierunku <m> od drenu do źródła, w przeciwną stronę przewodzi zawsze, <m> co symbolizuje dioda umieszczona w niektórych wariantach symboli. <m>'
			'Tranzystor ten zaczyna przewodzić gdy napięcie pomiędzy bramką a źródłem <m> jest wyższe od pewnej wielkości granicznej, oznaczanej U GS TH, <m> charakterystycznej dla danego modelu. <m>'
			'Czyli jeżeli potencjał bramki jest o U GS TH wyższy od potencjału źródła. <m>'
			'Dla tranzystorów z kanałem wzbogacanym wartość U GS TH jest dodatnia, <m> dla rzadziej spotykanych tranzystorów z kanałem zubożonym jest ujemna <m>'
				'– żeby przestały przewodzić trzeba podać na bramkę <m> potencjał niższy od potencjału źródła. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("mosfet", 0, 2)],
			["mosfet_n_off - 6", eduMovie.circuitjs("mosfet", 10, 6, [("switch", 360, 400)])],
			["mosfet_p_on - 12",  eduMovie.circuitjs("mosfet", 4, 13, preActions=[("switch", 360, 400)], actions=[("switch", 740, 260)])],
		],
		'text' : [
			'W symulacji widocznej na ekranie po lewej stronie mamy tranzystor n-mosfet <m> i w tej chwili na bramkę podane mamy 5 woltów, <m>'
				'co jest napięciem wyższym od U GS TH tego tranzystora i przewodzi on prąd. <mark name="mosfet_n_off" />'
			'Jeżeli podamy tam masę to przestanie on przewodzić. <m>'
			'Warto zauważyć że nie ma tutaj rezystora podłączonego do bramki, <m> gdyż jak było już mówione tranzystory te nie przewodzą pomiędzy bramką <m> a pozostałymi swoimi wyprowadzeniami, więc nie jest on potrzebny. <m>'
			
			'Po prawej stronie widzimy tranzystor P-MOSFET, <m> czyli symetryczny partner dla n-mosfeta. <m>'
			'Posiada on regulowane przewodzenie w kierunku od źródła do drenu, <m> w przeciwną stronę przewodzi zawsze. <m>'
			'Tranzystor ten będzie przewodził gdy napięcie pomiędzy bramką a źródłem <m> będzie mniejsze od napięcia granicznego. <mark name="mosfet_p_on" />'
			
			'W tym przypadku dla wariantu wzbogaconego U GS TH jest ujemne, <m> a dla zubożonego dodatnie, czyli odwrotnie niż w N-MOSFETach. <m>'
			'W efekcie aby wprowadzić P-MOSFET wzbogacony w przewodzenie <m> należy podać na bramkę potencjał mniejszy niż źródła, <m>'
				'aby wyłączyć zubożony należy podać na bramkę potencjał większy od źródła. <m>'
			
			'W symulacji mamy użyty p-mosfet wzbogacony, zatem jeżeli podamy mu na bramkę <m> napięcie zasilania (podłączone też do jego źródła) to nie przewodzi, <m>'
				'jeżeli podamy tam napięcie niższe o co najmniej U GS TH <m> od napięcia źródła to przewodzi. <m>'
		]
	},
	{
		'image': [
			[0.0, ""],
			["mosfet_cap1", eduMovie.circuitjs("mosfet_cap", 4, 9, [
				("switch", 440, 310), ("wait", 1.0), ("switch", 440, 310), ("wait", 1.0), ("switch", 440, 310), ("wait", 1.0), ("switch", 440, 310)
			])],
			["mosfet_cap2", eduMovie.circuitjs("mosfet_cap", 4, 12, preActions=[("switch", 440, 310)], actions=[
				("switch", 600, 300), ("wait", 3.0), ("switch", 440, 310), ("wait", 0.7), ("switch", 600, 300), ("wait", 0.7),
				("switch", 600, 300), ("wait", 2.0), ("switch", 440, 310), ("wait", 0.7), ("switch", 600, 300)
			])],
			["mosfet_cap3", eduMovie.circuitjs("mosfet_cap", 2, 9, preActions=[("setSlider", 1, 1.0)], actions=[
				("switch", 440, 310), ("wait", 2.0), ("switch", 440, 310), ("wait", 2.0), ("switch", 440, 310), ("wait", 2.0), ("switch", 440, 310)
			])],
		],
		'text' : [
			'Mówiliśmy że bramka jest izolowana, od pozostałych wyprowadzeń, <m> czyli nie ma z nimi połączenia elektrycznego. <m>'
			'Wspomnieliśmy także o tym że występuje pojemność pomiędzy bramką a źródłem. <mark name="mosfet_cap1" />'
			'Na symulacji został dodany kondensator z rezystorem obrazujący taką pojemność. <m>'
			'Działanie naszego układu nie uległo istotnej zmianie, widzimy jednak pik prądu <m> pobieranego / wypuszczanego przez bramkę w momencie przełączania. <m>'
			
			'Co się stanie jeżeli taką bramkę w pewnym momencie odłączymy, <m> czyli zostawimy ją wiszącą w powietrzu? <mark name="mosfet_cap2" />'
			'Skoro mamy do bramki podłączony pasożytniczy kondensator <m> to utrzyma on przez pewien czas potencjał tej bramki <m> na poziomie na którym była przed odpięciem jej od sygnału sterującego. <m>'
			'W związku z tym, tak jak pokazuje nasza symulacja, <m> tranzystor zachowa swój stan przewodzenia. <m>'
			
			'Oczywiście w rzeczywistości potrwa to przez jakiś nieustalony okres czasu <m> bo wyprowadzenie to stanie się rodzajem anteny, <m> zbierającej i oddającej ładunki z powietrza. <m>'
			'Z tymi zjawiskami wiążą się dwa problemy. <m>'
			
			'Pierwszym jest pobór energii przez bramkę w momencie przełączania <m> oraz spowalnianie przełączania w związku z koniecznością <m> przeładowania tego kondensatora do odpowiedniego napięcia. <mark name="mosfet_cap3" />'
			'Na symulacji widzimy jak wyglądałoby przełączanie gdyby sygnał sterujący <m> był ograniczony prądowo rezystorem 5 kiloomów, <m> '
				'(na przykład pochodził z rezystora podciągającego). <m>'
			'Taki kształt sygnału na bramce wpływa oczywiście także na kształt <m> sygnału wyjściowego – zmianę wielkości prądu przewodzonego w funkcji czasu. <m>'
			'Dlatego do przełączania mosfetów często wykorzystuje się wydajne prądowo <m> sygnały sterujące – chcemy przeładowywać ten kondensator dużym prądem <m> żeby następowało to szybko. <m>'
			'Innym efektem tego prądu przeładowującego jest zużycie energii. <m>'
			
			'Drugim problemem związanym już nie z pojemnością bramki a faktem jej izolowania <m> jest możliwość uszkodzenia tranzystorów MOSFET, <m> czy układów scalonych je zawierających przez ładunki elektrostatyczne. <m>'
			'Izolowanie bramki pozwala na elektrostatyczne gromadzenie się na niej <m> dużego ładunku, który może prowadzić do przebicia warstwy izolacyjnej <m> i zniszczenia takiego elementu. <m>'
		]
	},
]
