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

code_fwrite_A = r"""
plik = open('dane.txt', 'wt', encoding='utf8')
plik.write("teskt1\n")
plik.write("teskt2\nteskt3")
plik.close()
"""

code_fwrite_B = r"""
plik = open('dane.txt', 'wb')
plik.write("teskt1\n".encode('utf8'))
plik.write("teskt2\nteskt3".encode('utf8'))
plik.close()
"""

code_fread_A = r"""
plik = open('dane.txt', 'rt', encoding='utf8')
napis = plik.read()
plik.close()

print(napis)
"""

code_fread_B = r"""
plik = open('dane.txt', 'rt', encoding='utf8')
for linia in plik:
  print(linia, end="")

plik.seek(0)
print("pierwsza linia:", plik.readline(), end="")

plik.close()
"""

code_fread_C = r"""
plik = open('dane.txt', 'r+b')
print(plik.read())

plik.seek(0)
plik.write("ABC".encode('utf8'))

plik.seek(0)
print(plik.read())

plik.close()
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#03.4", "Python:", "pliki i czekanie", "na dane" ] },
	
	{ 'comment': 'pliki' },
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_fwrite_A, "py")],
			["fwriteB", eduMovie.clear + eduMovie.code2console(code_fwrite_B, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCommandString("rm dane.txt", cwd="/tmp")],
			[1.0, eduMovie.runCode(code_fwrite_A, [], cmd="python3")],
			[2.0, eduMovie.runCommandString("cat dane.txt", cwd="/tmp")],
			
			["fwriteB", eduMovie.runCommandString(":> dane.txt", cwd="/tmp")],
			["fwriteB + 1.0", eduMovie.runCode(code_fwrite_B, [], cmd="python3")],
			["fwriteB + 2.0", eduMovie.runCommandString("cat dane.txt", cwd="/tmp")],
		],
		'text' : [
			'Python pozwala także na korzystanie z plików <m> – możemy je czytać i zapisywać. <m>'
			'Celem wykonania takich operacji należy plik otworzyć funkcją open, <m> w której podajemy nazwę pliku, tryb otwarcia <m> (<r>[R] - odczyt, <w>[W] - zapis, <r+>[R plus] - modyfikacja, <t>[T] - tekstowy, <b>[B] - binarny). <m>'
			
			'Jeżeli wybraliśmy tryb tekstowy to możemy też określić <m> kodowanie tego pliku (domyślnie będzie to UTF8). <m>'
			'Otwarcie pliku w trybie tekstowym z określonym kodowaniem <m> pozwala na zapisywanie do niego bezpośrednio typu napisowego, <m> który automatycznie zostanie poddany określonemu kodowaniu. <mark name="fwriteB" />'
			
			'Jeżeli otworzylibyśmy ten plik jako binarny to wtedy <m> nie możemy zrobić takiej operacji, tylko musimy jawnie konwertować <m> typ napisowy na ciągi bajtowe w określonym kodowaniu. <m>'
			'Za to możemy zapisywać do niego dowolne dane binarne. <m>'
			
			'Plik zamykamy metodą close. <m>'
		]
	},
	{ #  
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_fread_A, "py")],
			["freadB", eduMovie.clear + eduMovie.code2console(code_fread_B, "py")],
			["freadC", eduMovie.clear + eduMovie.code2console(code_fread_C, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_fread_A, [], cmd="python3")],
			["freadB", eduMovie.runCode(code_fread_B, [], cmd="python3")],
			["freadC", eduMovie.runCode(code_fread_C, [], cmd="python3")],
		],
		'text' : [
			'Podobnie działa odczyt pliku, przy czym w trakcie otwierania <m> podajemy tryb read oraz używamy metod czytających otwarty plik, <m> tak jak pokazane jest to na ekranie. <mark name="freadB" />'
			
			'Przy pomocy iterowania pętlą for po otwartym do odczytu <m> pliku możemy go czytać linia po linii. <m>'
			'Odczyt linia po linii zapewnia też metoda <readline>[read line], <m> a metoda seek pozwala na przemieszczanie się po pliku. <m>'
			'Widoczny w prezentowanym przykładzie seek od zero wraca na początek pliku. <mark name="freadC" />'
			
			'Pliki otwarte jako tekstowe jeżeli podaliśmy tryb r plus możemy <m> modyfikować poprzez dopisywanie na końcu pliku nowych danych. <m>'
			'Natomiast otwarcie pliku jako binarnego w trybie r plus wraz <m> z użyciem metody seek pozwala na nadpisywanie danych w dowolnym miejscu pliku. <m>'
                ]
	},
]
