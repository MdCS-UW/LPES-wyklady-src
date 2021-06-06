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

code_opcje_krotkie = r"""
polecenie -a -y -q
polecenie -ayq
"""

code_opcje_dlugie = r"""
polecenie --opcja-dluga --kolejna
"""

code_argumenty = r"""
polecenie -a argument_opcji -y  argument_programu
polecenie --opcja-dluga=argument_opcji --opcja argument_programu
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'polecenia' },
	{ #  
		'console': [
			[0.0, eduMovie.clear],
			["argopcj",                       eduMovie.code2console("nazwa_polecenia opcje i argumenty", "sh") + "\n\r"],
			["opcjekrotkie", "\n\r\n\r\n\r" + eduMovie.code2console(code_opcje_krotkie, "sh")],
			["opcjedlugie",  "\n\r\n\r\n\r" + eduMovie.code2console(code_opcje_dlugie, "sh")],
			["argumenty",    "\n\r\n\r\n\r" + eduMovie.code2console(code_argumenty, "sh")],
		],
		'text' : [
			'Interpreter poleceń jak sama nazwa wskazuje <m> rozumie i wykonuje wpisywane polecenia, komendy. <m>'
			'Komendami unixowymi nazywamy polecenia rozumiane <m> przez interpreter zgodny ze składnią SH. <m>'
			'Czyli polecenia bashowe określamy jako komendy unixowe, <m> natomiast polecenia Pythona, który jest interpreterem nie zgodnym z SH, już nie. <mark name="argopcj" />'
			
			'Pojedyncze polecenie unixowe składa się z nazwy polecenia <m> oraz oddzielanych spacjami (od niej i od siebie na wzajem) argumentów i opcji. <m>'
			'Nazwą polecenia może być nazwa funkcji wbudowanej, alias, <m> nazwa funkcji zdefiniowanej przez użytkownika, nazwa programu znajdującego się <m> w ścieżce wyszukiwania, pełna ścieżka do programu, itd. <m>'
			
			'Nie mamy silnego rozróżnienia opcji od argumentów <m> – jest to bardziej rozróżnienie zwyczajowe. <m>'
			'Mianem opcji określamy coś co wpływa na zachowanie danego programu, <m> a jako argumenty określamy to na czym dany program operuje. <m>'
			'Opcję typowo podajemy po myślniku lub dwóch myślnikach, <m> natomiast argumenty po prostu podajemy na końcu linii poleceń, <m> po wszystkich opcjach. <mark name="opcjekrotkie" />'
			
			'Po jednym myślniku podawane są zazwyczaj <m> tak zwane opcję krótkie, czyli jednoliterowe. <m>'
			'Wiele takich opcji może wystąpić po jednym myślniku <m> lub każda z nich może mieć swój własny. <mark name="opcjedlugie" />'
			
			'Możemy też mieć do czynienia z opcjami długimi, <m> które zapisujemy po dwóch myślnikach i wtedy opcję taką określa całe słowo <m> czy też cały ciąg znaków występujący po tych dwóch myślnikach. <m>'
			'Jeżeli w ciągu stanowiącym nazwę takiej długiej opcji miałaby wystąpić spacja <m> typowo zamieniana jest na myślnik. <mark name="argumenty" />'
			
			'Oprócz wspomnianych argumentów programu, <m> podawanych na ogół po wszystkich opcjach, <m> także konkretne opcje mogą przyjmować swoje argumenty, <m> które podawane są zaraz po danej opcji i dotyczą jej działania. <m>'
			'W przypadku opcji krótkich oddzielane są one od niej <m> zazwyczaj spacją, a w przypadku opcji długich znakiem równości. <m>'
			
			'Należy pamiętać iż tak jak zostało wspomniane są to jedynie <m> dość powszechnie stosowane konwencje i istnieją wyjątki <m> – np. programy przyjmujące opcje bez myślników, <m> albo opcje długie z pojedynczym myślnikiem. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.clear + eduMovie.prompt()],
			[3.0, eduMovie.runCommandString(r"""echo a   b $q # \ !r *""")],
			[5.5, eduMovie.runCommandString(r'''echo a\ \ \ b \$q \# \\ \!r \*''')],
			["apostrofy + 1.0", eduMovie.runCommandString(r"""echo 'a   b $q # \ !r *'""")],
			["apostrofy + 5.0", eduMovie.runCommandString(r'''echo "a   b $q # \ !r *"''')],
		],
		'text' : [
			'Jeżeli np. argumenty mają zawierać spacje lub inne znaki specjalne <m> do zabezpieczenia ich możemy użyć odwrotnego ukośnika <m> poprzedzającego każdy problematyczny znak. <mark name="apostrofy" />'
			'Możemy też cały ciąg ująć w apostrofy, <m> określane też jako cudzysłów pojedynczy <m> lub w standardowe cudzysłowa, określane jako cudzysłów podwójny. <m>'
			'Należy mieć na uwadze że cudzysłów podwójny nie zabezpiecza <m> znaku dolara pozwalając na interpretację zmiennych umieszczonych <m> w zabezpieczanym napisie, ale szerzej na ten temat <m> będziemy rozmawiać na jednych z kolejnych zajęć. <m>'
			
			'Do zademonstrowania zagadnień związanych z zabezpieczaniem znaków <m> specjalnych użyte zostało polecenie echo. <m>'
			'Jest to polecenie wbudowane basha <m> (ale także program dostarczany z pakietem <coreutils>[kor jutils]) <m> które wypisuje wszystkie swoje argumenty na ekran, <m>'
			'rozdzielając je spacjami i standardowo dodając znak nowej linii na końcu. <m>'
			'Ze względu na wypisywanie wszystkich argumentów i rozdzielanie ich <m> spacjami nie widać tutaj różnicy w zabezpieczeniu <m> i braku zabezpieczenia pojedynczej spacji. <m>'
		]
	},
]

