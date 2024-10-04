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
	{ 'comment': 'podstawy elektroniki - Prawo Ohma, Praw Kirchhoffa' },
	{
		'image': [
			[0.0, eduMovie.convertFile('prawoOhma.tex', margins=12, viaCairo=True, negate=True)],
		],
		'text' : [
			'Na ekranie mamy wyświetloną zależność nazywaną prawem Ohma, <m> którą powinniście kojarzyć z zajęć fizyki w szkole. <m>'
			'Zachodzi ona dla elementów liniowych, czyli na przykład <m> (w dobrym przybliżeniu) dla zwykłego kawałka drutu. <m>'
			'Polega ona na proporcjonalności natężenia płynącego prądu <m> do napięcia pomiędzy końcami takiego przewodnika. <m>'
			'Im większe napięcie tym większy prąd będzie płynął, <m> im bardziej oporny przewodnik przy danym napięciu <m> tym mniejszy prąd popłynie i tak dalej. <m>'
			'Ten stosunek napięcia i prądu nazywany jest właśnie <m> oporem elektrycznym i oznaczany symbolem R. <m>'
			
			'Prawo Ohma jest jednak bardziej regułą empiryczną, <m> niż takim prawdziwym prawem przyrody <m>'
				'(jak na przykład prawo zachowania energii czy też inne prawa <m> związane z elektrycznością o których będziemy jeszcze mówili). <m>'
			'Prawo Ohma stosuje się wyłącznie do pewnej grupy <m> materiałów i w pewnym zakresie warunków. <m>'
			'Nawet zwykła, klasyczna żarówka również po części łamie prawo Ohma, <m>'
				'ponieważ opór w momencie kiedy żarnik jest nie rozgrzany ma <m> zupełnie inną wartość niż po jego rozgrzaniu (zmienia się on <m> bardzo szybko w momencie podłączenia do żarówki odpowiedniego napięcia). <m>'
			
			'Opór wielu materiałów zależy od ich temperatury i moglibyśmy <m> dodać uzupełnienie na ten temat do prawa Ohma, <m> natomiast to niczego nie rozwiązuje. <m>'
			'Mamy także elementy których opór zależy od przyłożonego napięcia, <m> albo elementy które niezależnie od prądu jaki przez nie płynie <m> charakteryzują się praktycznie stałym spadkiem napięcia. <m>'
			
			'Mimo tych ograniczeń prawo Ohma pozostaje bardzo przydatne. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile("Kirchhoff_1.sch", negate=True)], 
			["kirchhoff2", eduMovie.convertFile("Kirchhoff_2.sch", negate=True, dpi=160)],
			["kirchhoff_szeregowe", eduMovie.convertFile("Kirchhoff_szeregowe.sch", negate=True, dpi=140)]
		],
		'text' : [
			"Kolejnymi prawami które się przydają i na dodatek są dość <fundamentalnymi>[fundament'alnymi] <m> prawami przyrody są prawa Kirchhoffa. <m>"
			"Są także dosyć intuicyjne. <m>"
			
			'Pierwsze prawo Kirchhoffa mówi że jeżeli mamy węzeł, czyli np. punkt połączenia <m> kilku przewodów, to suma prądów do niego wpływających jest równa <m> sumie prądów wypływających <–>[.] prąd nie bierze się znikąd i nie znika. <m>'
			'Jeżeli wiemy, że prąd to przepływ ładunku, to prawo to powinno wydawać się <m> dość oczywiste - węzeł nie jest w stanie wytwarzać ani pochłaniać ładunków, <m> zatem to co do niego wpływa musi być tym co z niego wypływa. <m>'
			'W rzeczywistości możemy spotkać się z jakimiś zjawiskami pasożytniczymi w węźle, <m> pozwalającymi na gromadzenie się tam jakiegoś niewielkiego zapasu ładunku, <m>'
				'ale na ogół jest on tak niewielki że nie zmienia nam działania tego prawa. <m> Tym bardziej w stanie ustalonym gdzie już np. zgromadził się w maksymalnej ilości. <m>'
			'Jednak jeżeli zjawiska te byłyby istotne, dla naszej analizy, to należałoby <m> zaznaczyć je jako odpowiednie elementy dołączone do idealnego węzła. <mark name="kirchhoff2" />'
			
			'Drugie prawo Kirchhoffa mówi że jeżeli przejdziemy po dowolnej pętli w układzie <m> to suma spadków i wzrostów napięć <m> (z uwzględnieniem znaków) musi być równa zero. <m>'
			'Jako że napięcia to są różnice potencjałów, <m> to przechodząc po takiej pętli suma napięć musi być równa zero, <m>'
				'aby potencjał w punkcie A z którego wychodzimy, <m> był równy potencjałowi w tym samym punkcie A do którego dochodzimy <m> – również wydaje się dość oczywiste. <m>'
			
			'Najtrudniejsze w stosowaniu praw Kirchhoffa jest pamiętanie o <m> znakach napięcia na poszczególnych elementach, <m> czy też kierunku prądu wpływającego, wypływającego z węzła. <m>'
			'Zwłaszcza w bardziej skomplikowanych obwodach. <mark name="kirchhoff_szeregowe" />'
			
			'Warto zauważyć że z praw Kirchhoffa <m> (oraz charakterystyki danego elementu, wynikającej np. z prawa Ohma) <m>'
				'wynikają reguły dotyczące obliczeń dla <m> połączeń równoległych i szeregowych różnych elementów (np. oporników). <m>'
		]
	},
]
