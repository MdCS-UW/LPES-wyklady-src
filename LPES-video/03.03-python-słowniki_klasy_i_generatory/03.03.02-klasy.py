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

code_class_A = r"""
class NazwaKlasy:
  # pola składowe
  a, d = 0, "ala ma kota"
  # metody składowe
  def wypisz(self):
    print(self.a + self.b)
  # metody statyczna
  @staticmethod
  def info():
    print("INFO")
  # konstruktor (z jednym argumentem)
  def __init__(self, x = 1):
    print("konstruktor", self.a , self.d)
    # i kolejny sposób na utworzenie pola składowego klasy
    self.b = 13 * x
"""

code_class_B = code_class_A + r"""
k = NazwaKlasy()
k.a = 67
k.wypisz()
"""

code_class_C = code_class_B + r"""
k.info()
NazwaKlasy.info()
"""

code_class_D = code_class_C + r"""
NazwaKlasy.wypisz(k)
"""


try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'klasy' },
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_class_A, "py")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_class_A, [], cmd="python3")],
		],
		'text' : [
			'Jak wiemy w Pythonie wszystko jest obiektem jakiejś klasy. <m> Oczywiście możemy również definiować własne klasy. <m>'
			'Definicja taka rozpoczyna się słowem kluczowym class, <m> po którym podajemy nazwę klasy, <m>'
			'a po niej dwukropek rozpoczynający wcięty blok wydzielający <m> wszystkie elementy (takie jak zmienne czy funkcje) do niej należące. <m>'
			
			'Jak wiemy funkcje należące do jakiejś klasy nazywamy metodami, a zmienne polami. <m>'
			'Wśród nich możemy wyróżnić takie które do działania <m> wymagają obiektu danej klasy i takie które go nie potrzebują. <m>'
			'Te drugie często określa się mianem metod statycznych. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_class_B, "py", first=4)],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_class_B, [], cmd="python3")],
		],
		'text' : [
			'Obiekt danej klasy możemy utworzyć wywołując jej nazwę <m> z nawiasami okrągłymi, wewnątrz których mogą być podane parametry <m> potrzebne do utworzenia obiektu naszej klasy. <m>'
			'Spowoduje to również wywołanie konstruktora, którym w Pythonie <m> jest metoda o nazwie <__init__>[dwa podkreślniki init dwa podkreślniki]. <m>'
			
			'Do pól składowych i metod możemy odwoływać się poprzez <m> nazwę obiektu kropkę i nazwę pola czy też metody, <m> czyli tak samo jak robiliśmy to w przypadku obiektów klas wbudowanych w Pythona. <m>'
			
			'Należy zwrócić uwagę na to że wywołaliśmy metodę wypisz bez argumentów, <m> pomimo iż jest ona zdefiniowana jako przyjmująca jeden argument.'
			'W przypadku zwykłych metod jakiegoś obiektu <m> (czyli takich które nie są oznaczone na przykład jako statyczne poprzez <@staticmethod>[małpa static method]) <m>'
			'Python jako pierwszy argument przekazuje do nich obiekt <m> (dokładniej referencję na obiekt) na którym została wywołana ta metoda. <m>'
			'Zwyczajowo nazywany on jest w Pythonie self, <m> ale możemy nazwać go dowolnie – istotne jest że jest to pierwszy argument metody, <m> a metody klasy do wszystkich jej pól muszą odwoływać się z jego użyciem. <m>'
			'Warto zauważyć, iż identycznie działa to dla konstruktora. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_class_C, "py", first=10)],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_class_C, [], cmd="python3")],
		],
		'text' : [
			'Metody statyczne możemy wywołać zarówno na obiekcie <m> danej klasy jak i na samej nazwie tej klasy, <m> gdyż nie otrzymują one argumentu wskazującego obiekt na którym są wywołane. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_class_D, "py", first=10)],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_class_D, [], cmd="python3")],
		],
		'text' : [
			'W Pythonie metody nie statyczne możemy też wywoływać <m> poprzedzając je nazwą klasy i podając jawnie <m> pierwszy argument będący obiektem tej klasy. <m>'
			'Robiliśmy tak już w przypadku metody join typu napisowego. <m>'
			
			'Dla osób znających <C++>[c plus plus] argument self może kojarzyć się <m> z wskaźnikiem this i faktycznie pełni on taką samą rolę, <m>'
			'tyle że musi być jawnie podawany przed każdym odwołaniem do elementu <m> składowego oraz jest jawnie podany na liście argumentów metody. <m>'
			'W przypadku <C++>[c plus plus] również jest on jednym z argumentów każdej <m> nie statycznej metody, ale dodawanym automatycznie przez kompilator – <m>'
			'zarówno na liście argumentów, jak też przy odwoływaniu się <m> do innych elementów składowych obiektu wewnątrz metody. <m>'
			
			'Obiekty pythonowych klas są obiektami modyfikowalnymi, <m> zatem jak wiemy zwykłe przypisanie <m> tworzy tylko inną referencję na ten sam obiekt. <m>'
			'Celem utworzenia kopii naszego obiektu możemy <m> zaimplementować własną metodę copy lub skorzystać <m> z funkcji copy dostarczanej przez moduł copy. <m>'
		]
	},
]

