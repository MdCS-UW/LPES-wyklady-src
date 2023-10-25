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

code_zmnap_A = r"""
echo $a $b
echo ${a:-"abc def"} ${b:="123 456"}
echo $a $b

a=12; b=13
echo ${a:-"abc def"} ${b:="123 456"}
echo $a $b
"""

code_zmnap_B = r"""
c=11
echo ${c:+"abc def"}
echo $c

c=""
echo ${c:+"abc def"}
echo $c
"""

code_zmnap_C = r"""
a="abcdefgh"
echo ${a:3}
echo ${a:3:2}
echo ${a:0:2}
echo ${#a}
"""

try: clipData
except NameError: clipData = []

endTitleSVG="JS.svg"

clipData += [
	{ 'title': [ "#05.3", "Bash: obsługa", "napisów, eval", "i podsumowanie" ] },
	
	{ 'comment': 'napisy w bashu' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear],
			["codeA", eduMovie.clear + eduMovie.code2console(code_zmnap_A, "sh")],
			["codeB", eduMovie.clear + eduMovie.code2console(code_zmnap_B, "sh")],
			["codeC", eduMovie.clear + eduMovie.code2console(code_zmnap_C, "sh")],
		],
		'consoleDown': [
			[0.0, ""],
			["codeA", eduMovie.runCode(code_zmnap_A, [], cmd="bash")],
			["codeB", eduMovie.runCode(code_zmnap_B, [], cmd="bash")],
			["codeC", eduMovie.runCode(code_zmnap_C, [], cmd="bash")],
		],
		'text' : [
			'Dolar nawiasy klamrowe w których podajemy nazwę zmiennej pozwalają <m> na więcej niż tylko ograniczenie ciągu znaków stanowiących nazwę zmiennej. <mark name="codeA" />'
			
			'Pozwalają nam w wielu wypadkach zastąpić <m> warunek sprawdzający czy zmienna jest pusta lub niepusta. <m>'
			'Tak jak pokazuje przykład widoczny na ekranie, jeżeli w klamerkach <m> po nazwie zmiennej damy dwukropek i myślnik możemy podać po nim wartość domyślną, <m> która będzie użyta gdy zmienna jest pusta lub niezdefiniowana. <m>'
			'Jeżeli użyjemy dwukropek znak równości to zmienna dodatkowo <m> zostanie ustawiona na tą wartość domyślną. <mark name="codeB" />'
			
			'Odwrotne znaczenie ma dwukropek plus, spowoduje on użycie <m> podanej po nim wartości jeżeli zmienna jest zdefiniowana i niepusta. <mark name="codeC" />'
			
			'Jeżeli po dwukropku podamy wartość numeryczną to uzyskamy podnapis <m> z obciętą taką ilością początkowych znaków ile wynosiła ta liczba. <m>'
			'Jeżeli po tej liczbie wystąpi kolejny dwukropek i liczba to będzie to <m> dodatkowo podnapis obcięty do długości określonej drugą liczbą. <m>'
			'Długość napisu w zmiennej możemy uzyskać poprzedzając jej nazwę krzyżykiem. <m>'
		]
	},
]

code_zmnap_repl_A = r"""
a="abbc abbd abbe"
echo ${a/bb/X}
echo ${a//bb/X}
"""

code_zmnap_repl_B = r"""
a="abbc abbd abbe"
echo ${a//b*d/X}
echo ${a//bb[cd]/X}
"""

code_zmnap_trim = r"""
a="abc.def.ghi"
echo ${a%ghi}
echo ${a%.*}
echo ${a#ab}

b="ghi"
echo ${a%$b}
"""

code_printf = r"""
printf "0o%o %d 0x%x\n" 0xf 010 3
"""

clipData += [
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_zmnap_repl_A, "sh")],
			["replB", eduMovie.clear + eduMovie.code2console(code_zmnap_repl_B, "sh")],
			["trim", eduMovie.clear + eduMovie.code2console(code_zmnap_trim, "sh")],
			["printf", eduMovie.clear + eduMovie.code2console(code_printf, "sh")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_zmnap_repl_A, [], cmd="bash")],
			["replB", eduMovie.runCode(code_zmnap_repl_B, [], cmd="bash")],
			["trim", eduMovie.runCode(code_zmnap_trim, [], cmd="bash")],
			["printf", eduMovie.runCode(code_printf, [], cmd="bash")],
		],
		'text' : [
			'Z użyciem klamerek możemy także wykonać znaną nam już operację <m> wyszukaj i zastąp na napisie znajdującym się w zmiennej. <m>'
			'Uzyskuje się ją podając po nazwie zmiennej ukośnik i wyszukiwany <m> ciąg znaków, kolejny ukośnik i ciąg znaków którym ma zostać zastąpiony. <m>'
			'W tym wariancie zastąpieniu ulegnie tylko pierwsze wystąpienie. <m>'
			'Jeżeli po nazwie zmiennej podamy dwa ukośniki <m> to zastąpieniu ulegną wszystkie wystąpienia. <mark name="replB" />'
			
			'Nie możemy tu użyć wyrażeń regularnych, <m> ale możemy użyć znaków uogólniających powłoki. <mark name="trim" />'
			
			'Mamy również operację obcięcia wskazanego podnapisu <m> od końca lub początku zmiennej uzyskiwaną z użyciem dolara i krzyżyka. <m>'
			'Tutaj także działają znaki uogólniające powłoki. <m>'
			'Operacja obcinania od końca jest szczególnie przydatna <m> do ucinania rozszerzenia z nazwy pliku celem zastąpienia go innym. <m>'
			
			'Oczywiście w ciągach wyszukiwanych, zastępujących i obcinanych możemy <m> także odwoływać się do zmiennych powłoki z użyciem standardowego znaku dolara. <m>'
			'Należy jednak pamiętać, że wiele tych operatorów jest rozszerzeniami basha, <m> nie występującymi w standardzie <sh>[es ha]. <mark name="printf" />'
			
			"Programując w bashu mamy też dostęp do instrukcji <printf>[print-f] <m> umożliwiającej <formatowane>[format'owane] wypisywanie zmiennych. <m>"
			'Instrukcja ta będąca tak naprawdę osobnym programem działa analogicznie <m> jak funkcja <printf>[print-f] z C i potrafi obsługiwać także liczby zmiennoprzecinkowe. <m>'
		]
	},
]
