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
	{ 'section': 'wyświetlanie plików\n z podziałem na strony' },
	{
		'console': [
			[0.070374, "o", eduMovie.clear + eduMovie.prompt()],
			[1.067533, "o", "m"],
			[1.259512, "o", "a"],
			[1.41949, "o", "n"],
			[1.611479, "o", " "],
			[1.92349, "o", "m"],
			[2.115325, "o", "a"],
			[2.243465, "o", "n"],
			[2.435497, "o", " "],
			[3.475488, "o", "\r\n"],
			[3.54519, "o", "\u001b[?1049h\u001b[22;0;0t\u001b[?1h\u001b=\r"],
			[3.585094, "o", "MAN(1)                        Manual pager utils                        MAN(1)\u001b[m\r\n\u001b[m\r\n\u001b[1mNAME\u001b[0m\u001b[m\r\n       man - an interface to the on-line reference manuals\u001b[m\r\n\u001b[m\r\n\u001b[1mSYNOPSIS\u001b[0m\u001b[m\r\n       \u001b[1mman\u001b[0m  [\u001b[1m-C\u001b[0m  \u001b[4mfile\u001b[24m] [\u001b[1m-d\u001b[0m] [\u001b[1m-D\u001b[0m] [\u001b[1m--warnings\u001b[0m[=\u001b[4mwarnings\u001b[24m]] [\u001b[1m-R\u001b[0m \u001b[4mencoding\u001b[24m] [\u001b[1m-L\u001b[0m \u001b[4mlo‐\u001b[24m\u001b[m\r\n       \u001b[4mcale\u001b[24m] [\u001b[1m-m\u001b[0m \u001b[4msystem\u001b[24m[,...]] [\u001b[1m-M\u001b[0m \u001b[4mpath\u001b[24m]  [\u001b[1m-S\u001b[0m  \u001b[4mlist\u001b[24m]  [\u001b[1m-e\u001b[0m  \u001b[4mextension\u001b[24m]  [\u001b[1m-i\u001b[0m|\u001b[1m-I\u001b[0m]\u001b[m\r\n       [\u001b[1m--regex\u001b[0m|\u001b[1m--wildcard\u001b[0m]   [\u001b[1m--names-only\u001b[0m]  [\u001b[1m-a\u001b[0m]  [\u001b[1m-u\u001b[0m]  [\u001b[1m--no-subpages\u001b[0m]  [\u001b[1m-P\u001b[0m\u001b[m\r\n       \u001b[4mpager\u001b[24m] [\u001b[1m-r\u001b[0m \u001b[4mprompt\u001b[24m] [\u001b[1m-7\u001b[0m] [\u001b[1m-E\u001b[0m \u001b[4mencoding\u001b[24m] [\u001b[1m--no-hyphenation\u001b[0m] [\u001b[1m--no-justifi‐\u001b[0m\u001b[m\r\n       \u001b[1mcation\u001b[0m]  [\u001b[1m-p\u001b[0m  \u001b[4mstring\u001b[24m]  [\u001b[1m-t\u001b[0m]  [\u001b[1m-T\u001b[0m[\u001b[4mdevice\u001b[24m]]  [\u001b[1m-H\u001b[0m[\u001b[4mbrowser\u001b[24m]] [\u001b[1m-X\u001b[0m[\u001b[4mdpi\u001b[24m]] [\u001b[1m-Z\u001b[0m]\u001b[m\r\n       [[\u001b["],
			[3.585479, "o", "4msection\u001b"],
			[3.585788, "o", "[24m] \u001b[4mpage\u001b[24m[.\u001b[4msection\u001b[24m] ...] ...\u001b[m\r\n       \u001b[1mman\u001b[0m \u001b[1m-k\u001b[0m [\u001b[4mapropos\u001b[24m \u001b[4moptions\u001b[24m] \u001b[4mregexp\u001b[24m ...\u001b[m\r\n       \u001b[1mman\u001b[0m \u001b[1m-K\u001b[0m [\u001b[1m-w\u001b[0m|\u001b[1m-W\u001b[0m] [\u001b[1m-S\u001b[0m \u001b[4mlist\u001b[24m] [\u001b[1m-i\u001b[0m|\u001b[1m-I\u001b[0m] [\u001b[1m--regex\u001b[0m] [\u001b[4msection\u001b[24m] \u001b[4mterm\u001b[24m ...\u001b[m\r\n       \u001b[1mman\u001b[0m \u001b[1m-f\u001b[0m [\u001b[4mwhatis\u001b[24m \u001b[4moptions\u001b[24m] \u001b[4mpage\u001b[24m ...\u001b[m\r\n       \u001b[1mman\u001b[0m \u001b[1m-l\u001b[0m [\u001b[1m-C\u001b[0m \u001b[4mfile\u001b[24m] [\u001b[1m-d\u001b[0m] [\u001b[1m-D\u001b[0m] [\u001b[1m--warnings\u001b[0m[=\u001b[4mwarnings\u001b[24m]]  [\u001b[1m-R\u001b[0m  \u001b[4mencoding\u001b[24m]  [\u001b[1m-L\u001b[0m\u001b[m\r\n       \u001b[4mlocale\u001b[24m]  [\u001b[1m-P\u001b[0m  \u001b[4mpager\u001b[24m]  [\u001b[1m-r\u001b[0m  \u001b[4mprompt\u001b[24m]  [\u001b[1m-7\u001b[0m] [\u001b[1m-E\u001b[0m \u001b[4mencoding\u001b[24m] [\u001b[1m-p\u001b[0m \u001b[4mstring\u001b[24m] [\u001b[1m-t\u001b[0m]\u001b[m\r\n       [\u001b[1m-T\u001b[0m[\u001b[4mdevice\u001b[24m]] [\u001b[1m-H\u001b[0m[\u001b[4mbrowser\u001b[24m]] [\u001b[1m-X\u001b[0m[\u001b[4mdpi\u001b[24m]] [\u001b[1m-Z\u001b[0m] \u001b[4mfile\u001b[24m ...\u001b[m\r\n       \u001b[1mman\u001b[0m \u001b[1m-w\u001b[0m|\u001b[1m-W\u001b[0m [\u001b[1m-C\u001b[0m \u001b[4mfile\u001b[24m] [\u001b[1m-d\u001b[0m] [\u001b[1m-D\u001b[0m] \u001b[4mpage\u001b[24m ...\u001b[m\r\n       \u001b[1mman\u001b[0m \u001b[1m-c\u001b[0m [\u001b[1m"],
			[3.586087, "o", "-C\u001b[0m \u001b[4mfile\u001b[24m] [\u001b[1m-d\u001b[0m] [\u001b[1m-D\u001b[0m] \u001b[4mpage\u001b[24m ...\u001b[m\r\n       \u001b[1mman\u001b[0m [\u001b[1m-?V\u001b[0m]\u001b[m\r\n\u001b[m\r\n\u001b[1mDESCRIPTION\u001b[0m\u001b[m\r\n\u001b[7m Manual page man(1) line 1 (press h for help or q to quit)\u001b[27m\u001b[K"],
			[5.099652, "o", "\r\u001b[K"],
			[5.100412, "o", "       \u001b[1mman\u001b[0m is the system's manual pager.  Each \u001b[4mpage\u001b[24m argument given to  \u001b[1mman\u001b[0m  is\u001b[m\r\n       normally  the  name of a program, utility or function.  The \u001b[4mmanual\u001b[24m \u001b[4mpage\u001b[24m\u001b[m\r\n       associated with each of these arguments is then found and displayed.  A\u001b[m\r\n       \u001b[4msection\u001b[24m,  if  provided, will direct \u001b[1mman\u001b[0m to look only in that \u001b[4msection\u001b[24m of\u001b[m\r\n       the manual.  The default action is to search in all  of  the  available\u001b[m\r\n       \u001b[4msections\u001b[24m  following  a pre-defined order (\"1 n l 8 3 2 3posix 3pm 3perl\u001b[m\r\n       3am 5 4 9 6 7\" by default, unless overridden by the  \u001b[1mSECTION\u001b[0m  directive\u001b[m\r\n       in \u001b[4m/etc/manpath.config\u001b[24m), and to show only the first \u001b[4mpage\u001b[24m found, even if\u001b[m\r\n       \u001b[4mpage\u001b[24m exists in several \u001b[4msections\u001b[24m.\u001b[m\r\n\u001b[m\r\n       The table below shows the \u001b[4msection\u001b[24m numbers of the manual followed by the\u001b[m\r\n       types of pages they contain.\u001b[m\r\n\u001b[m\r\n       1   Executable programs or shell commands\u001b[m\r"],
			[5.10077, "o", "\n       2   System calls (functions provided by the kernel)\u001b[m\r\n       3   Library calls (functions within program libraries)\u001b[m\r\n       4   Special files (usually found in \u001b[4m/dev\u001b[24m)\u001b[m\r\n       5   File formats and conventions eg \u001b[4m/etc/passwd\u001b[24m\u001b[m\r\n       6   Games\u001b[m\r\n       7   Miscellaneous  (including  macro  packages  and  conventions), e.g.\u001b[m\r\n           \u001b[1mman\u001b[0m(7), \u001b[1mgroff\u001b[0m(7)\u001b[m\r\n       8   System administration commands (usually only for root)\u001b[m\r\n       9   Kernel routines [Non standard]\u001b[m\r\n\u001b[7m Manual page man(1) line 24 (press h for help or q to quit)\u001b[27m\u001b[K"],
			[10.259702, "o", "\r\u001b[K"],
			[10.260051, "o", "\u001b[m\r\n       A manual \u001b[4mpage\u001b[24m consists of several sections.\u001b[m\r\n\u001b[m\r\n       Conventional section names include \u001b[1mNAME\u001b[0m, \u001b[1mSYNOPSIS\u001b[0m,  \u001b[1mCONFIGURATION\u001b[0m,  \u001b[1mDE‐\u001b[0m\u001b[m\r\n       \u001b[1mSCRIPTION\u001b[0m,  \u001b[1mOPTIONS\u001b[0m,  \u001b[1mEXIT\u001b[0m \u001b[1mSTATUS\u001b[0m,  \u001b[1mRETURN\u001b[0m \u001b[1mVALUE\u001b[0m,  \u001b[1mERRORS\u001b[0m, \u001b[1mENVIRONMENT\u001b[0m,\u001b[m\r\n"],
			[10.260674, "o", "       \u001b[1mFILES\u001b[0m, \u001b[1mVERSIONS\u001b[0m, \u001b[1mCONFORMING\u001b[0m \u001b[1mTO\u001b[0m,  \u001b[1mNOTES\u001b[0m,  \u001b[1mBUGS\u001b[0m,  \u001b[1mEXAMPLE\u001b[0m,  \u001b[1mAUTHORS\u001b[0m,  and\u001b[m\r\n       \u001b[1mSEE\u001b[0m \u001b[1mALSO\u001b[0m.\u001b[m\r\n\u001b[m\r\n       The following conventions apply to the \u001b[1mSYNOPSIS\u001b[0m section and can be used\u001b[m\r\n       as a guide in other sections.\u001b[m\r\n\u001b[m\r\n       \u001b[1mbold\u001b[0m \u001b[1mtext\u001b[0m          type exactly as shown.\u001b[m\r\n       \u001b[4mitalic\u001b[24m \u001b[4mtext\u001b[24m        replace with appropriate argument.\u001b[m\r\n       [\u001b[1m-abc\u001b[0m]             any or all arguments within [ ] are optional.\u001b[m\r\n       \u001b[1m-a\u001b[0m|\u001b[1m-b\u001b[0m              options delimited by | cannot be used together.\u001b[m\r\n\u001b[m\r\n"],
			[10.261539, "o", "       \u001b[4margument\u001b[24m ...       \u001b[4margument\u001b[24m is repeatable.\u001b[m\r\n       [\u001b[4mexpression\u001b[24m] ...   entire \u001b[4mexpression\u001b[24m within [ ] is repeatable.\u001b[m\r\n\u001b[m\r\n       Exact rendering may vary depending on the output device.  For instance,\u001b[m\r\n       man will usually not be able to render italics when running in a termi‐\u001b[m\r\n       nal, and will typically use underlined or coloured text instead.\u001b[m\r\n\u001b[m\r\n\u001b[7m Manual page man(1) line 47 (press h for help or q to quit)\u001b[27m\u001b[K"],

			["search + 0.467738", "o", "\r\u001b[K/"],
			["search + 2.427696", "o", "\u001b[Km\bm"],
			["search + 2.811736", "o", "\u001b[Ka\ba"],
			["search + 3.187628", "o", "\u001b[Kn\bn"],
			["search + 4.835791", "o", "\r\u001b[K"],
			["search + 4.838372", "o", "\u001b[1;1H\u001b[m\r\n\u001b[2;1H       A manual \u001b[4mpage\u001b[24m consists of several sections.\u001b[m\r\n\u001b[3;1H\u001b[m\r\n\u001b[4;1H       Conventional section names include \u001b[1mNAME\u001b[0m, \u001b[1mSYNOPSIS\u001b[0m,  \u001b[1mCONFIGURATION\u001b[0m,  \u001b[1mDE‐\u001b[0m\u001b[m\r\n\u001b[5;1H       \u001b[1mSCRIPTION\u001b[0m,  \u001b[1mOPTIONS\u001b[0m,  \u001b[1mEXIT\u001b[0m \u001b[1mSTATUS\u001b[0m,  \u001b[1mRETURN\u001b[0m \u001b[1mVALUE\u001b[0m,  \u001b[1mERRORS\u001b[0m, \u001b[1mENVIRONMENT\u001b[0m,\u001b[m\r\n\u001b[6;1H       \u001b[1mFILES\u001b[0m, \u001b[1mVERSIONS\u001b[0m, \u001b[1mCONFORMING\u001b[0m \u001b[1mTO\u001b[0m,  \u001b[1mNOTES\u001b[0m,  \u001b[1mBUGS\u001b[0m,  \u001b[1mEXAMPLE\u001b[0m,  \u001b[1mAUTHORS\u001b[0m,  and\u001b[m\r\n\u001b[7;1H       \u001b[1mSEE\u001b[0m \u001b[1mALSO\u001b[0m.\u001b[m\r\n\u001b[8;1H\u001b[m\r\n\u001b[9;1H       The following conventions apply to the \u001b[1mSYNOPSIS\u001b[0m section and can be used\u001b[m\r\n\u001b[10;1H       as a guide in other sections.\u001b[m\r\n\u001b[11;1H\u001b[m\r\n\u001b[12;1H       \u001b[1mbold\u001b[0m \u001b[1mtext\u001b[0m          type exactly as shown.\u001b[m\r\n\u001b[13;1H       \u001b[4mitalic\u001b[24m \u001b[4mtext\u001b[24m        replace with appropriate argument.\u001b[m\r\n\u001b[14;1H       [\u001b[1m-abc\u001b[0m]             any or all arguments within [ ] are optional.\u001b[m\r\n\u001b[15;1H       \u001b[1m-a\u001b[0m|\u001b[1m-b\u001b[0m"],
			["search + 4.838671", "o", "             "],
			["search + 4.840168", "o", " options delimited by | cannot be used together.\u001b[m\r\n\u001b[16;1H\u001b[m\r\n\u001b[17;1H       \u001b[4margument\u001b[24m ...       \u001b[4margument\u001b[24m is repeatable.\u001b[m\r\n\u001b[18;1H       [\u001b[4mexpression\u001b[24m] ...   entire \u001b[4mexpression\u001b[24m within [ ] is repeatable.\u001b[m\r\n\u001b[19;1H\u001b[m\r\n\u001b[20;1H       Exact rendering may vary depending on the output device.  For instance,\u001b[m\r\n\u001b[21;1H       man will usually not be able to render italics when running in a termi‐\u001b[m\r\n\u001b[22;1H       nal, and will typically use underlined or coloured text instead.\u001b[m\r\n\u001b[23;1H\u001b[m\r\n\u001b[24;1H\u001b[1;1H\u001b[m\r\n\u001b[2;1H       A \u001b[7mman\u001b[27mual \u001b[4mpage\u001b[24m consists of several sections.\u001b[m\r\n\u001b[3;1H\u001b[m\r\n\u001b[4;1H       Conventional section names include \u001b[1mNAME\u001b[0m, \u001b[1mSYNOPSIS\u001b[0m,  \u001b[1mCONFIGURATION\u001b[0m,  \u001b[1mDE‐\u001b[0m\u001b[m\r\n\u001b[5;1H       \u001b[1mSCRIPTION\u001b[0m,  \u001b[1mOPTIONS\u001b[0m,  \u001b[1mEXIT\u001b[0m \u001b[1mSTATUS\u001b[0m,  \u001b[1mRETURN\u001b[0m \u001b[1mVALUE\u001b[0m,  \u001b[1mERRORS\u001b[0m, \u001b[1mENVIRONMENT\u001b[0m,\u001b[m\r\n\u001b[6;1H       \u001b[1mFILES\u001b[0m, \u001b[1mVERSIONS\u001b[0m, \u001b[1mCONFORMING\u001b[0m \u001b[1mTO\u001b[0m,  \u001b[1mNOTES\u001b[0m,  \u001b[1mBUGS\u001b[0m, "],
			["search + 4.840432", "o", " \u001b[1mEXAMPLE\u001b"],
			["search + 4.841096", "o", "[0m,  \u001b[1mAUTHORS\u001b[0m,  and\u001b[m\r\n\u001b[7;1H       \u001b[1mSEE\u001b[0m \u001b[1mALSO\u001b[0m.\u001b[m\r\n\u001b[8;1H\u001b[m\r\n\u001b[9;1H       The following conventions apply to the \u001b[1mSYNOPSIS\u001b[0m section and can be used\u001b[m\r\n\u001b[10;1H       as a guide in other sections.\u001b[m\r\n\u001b[11;1H\u001b[m\r\n\u001b[12;1H       \u001b[1mbold\u001b[0m \u001b[1mtext\u001b[0m          type exactly as shown.\u001b[m\r\n\u001b[13;1H       \u001b[4mitalic\u001b[24m \u001b[4mtext\u001b[24m        replace with appropriate argument.\u001b[m\r\n\u001b[14;1H       [\u001b[1m-abc\u001b[0m]             any or all arguments within [ ] are optional.\u001b[m\r\n\u001b[15;1H       \u001b[1m-a\u001b[0m|\u001b[1m-b\u001b[0m              options delimited by | cannot be used together.\u001b[m\r\n\u001b[16;1H\u001b[m\r\n\u001b[17;1H       \u001b[4margument\u001b[24m ...       \u001b[4margument\u001b[24m is repeatable.\u001b[m\r\n\u001b[18;1H       [\u001b[4mexpression\u001b[24m] ...   entire \u001b[4mexpression\u001b[24m within [ ] is repeatable.\u001b[m\r\n\u001b[19;1H\u001b[m\r\n\u001b[20;1H       Exact rendering may vary depending on the output device.  For instance,\u001b[m\r\n\u001b[21;1H       \u001b[7mman\u001b[27m will usually not be able to render italics when running in a termi‐\u001b[m\r\n\u001b[22;1H       nal, and will ty"],
			["search + 4.841183", "o", "pically use und"],
			["search + 4.842076", "o", "erlined or coloured text instead.\u001b[m\r\n\u001b[23;1H\u001b[m\r\n\u001b[24;1H       The com\u001b[7mman\u001b[27md or function illustration is a pattern that should match all\u001b[m\r\n\u001b[7m Manual page man(1) line 48 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["search + 9.491816", "o", "\r\u001b[K/\r\u001b[K"],
			["search + 9.492785", "o", "       possible invocations.  In some cases it is advisable to illustrate sev‐\u001b[m\r\n       eral exclusive invocations as is shown in the \u001b[1mSYNOPSIS\u001b[0m section of  this\u001b[m\r\n       \u001b[7mman\u001b[27mual page.\u001b[m\r\n\u001b[m\r\n\u001b[1mEXAMPLES\u001b[0m\u001b[m\r\n       \u001b[1m\u001b[7mman\u001b[27m\u001b[0m \u001b[4mls\u001b[24m\u001b[m\r\n           Display the \u001b[7mman\u001b[27mual page for the \u001b[4mitem\u001b[24m (program) \u001b[4mls\u001b[24m.\u001b[m\r\n\u001b[m\r\n       \u001b[1m\u001b[7mman\u001b[27m\u001b[0m \u001b[4m\u001b[7mman\u001b[27m\u001b[24m.\u001b[4m7\u001b[24m\u001b[m\r\n           Display the \u001b[7mman\u001b[27mual page for macro package \u001b[4m\u001b[7mman\u001b[27m\u001b[24m from section \u001b[4m7\u001b[24m.\u001b[m\r\n\u001b[m\r\n       \u001b[1m\u001b[7mman\u001b[27m\u001b[0m \u001b[1m-a\u001b[0m \u001b[4mintro\u001b[24m\u001b[m\r\n           Display,  in  succession,  all  of the available \u001b[4mintro\u001b[24m \u001b[7mman\u001b[27mual pages\u001b[m\r\n           contained within the \u001b[7mman\u001b[27mual.  It is possible to quit  between  suc‐\u001b[m\r\n           cessive displays or skip any of them.\u001b[m\r\n\u001b[m\r\n       \u001b[1m\u001b[7mman\u001b[27m\u001b[0m \u001b[1m-t\u001b[0m \u001b[4malias\u001b[24m | \u001b[4mlpr\u001b[24m \u001b[4m-Pps\u001b[24m\u001b[m\r\n           Format  the \u001b[7mman\u001b[27mual page referenced by `\u001b[4mali"],
			["search + 9.493205", "o", "as\u001b[24m', usually a shell \u001b[7mman\u001b[27m‐\u001b[m\r\n           ual page, into the default \u001b[1mtroff\u001b[0m or \u001b[1mgroff\u001b[0m format and pipe it to the\u001b[m\r\n\u001b[7m Manual page man(1) line 67 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["search + 10.755837", "o", "\r\u001b[K/\r\u001b[K"],
			["search + 10.75625", "o", "           printer  named  \u001b[4mps\u001b[24m.   The default output for \u001b[1mgroff\u001b[0m is usually Post‐\u001b[m\r\n           Script.  \u001b[1m\u001b[7mman\u001b[27m\u001b[0m \u001b[1m--help\u001b[0m should advise as to which processor is bound to\u001b[m\r\n           the \u001b[1m-t\u001b[0m option.\u001b[m\r\n\u001b[7m Manual page man(1) line 70 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["search + 11.707833", "o", "\r\u001b[K/\r\u001b[K"],
			["search + 11.708289", "o", "\u001b[m\r\n       \u001b[1m\u001b[7mman\u001b[27m\u001b[0m \u001b[1m-l\u001b[0m \u001b[1m-T\u001b[0m\u001b[4mdvi\u001b[24m \u001b[4m./foo.1x.gz\u001b[24m \u001b[1m>\u001b[0m \u001b[4m./foo.1x.dvi\u001b[24m\u001b[m\r\n           This  com\u001b[7mman\u001b[27md  will  decompress  and format the nroff source \u001b[7mman\u001b[27mual\u001b[m\r\n\u001b[7m Manual page man(1) line 73 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["search + 12.75573", "o", "\r\u001b[K/\r\u001b[K"],
			["search + 12.75613", "o", "           page \u001b[4m./foo.1x.gz\u001b[24m into a \u001b[1mdevice\u001b[0m \u001b[1mindependent\u001b[0m \u001b[1m(dvi)\u001b[0m file.   The  redi‐\u001b[m\r\n           rection is necessary as the \u001b[1m-T\u001b[0m flag causes output to be directed to\u001b[m\r\n           \u001b[1mstdout\u001b[0m with no pager.  The output could be viewed  with  a  program\u001b[m\r\n\u001b[7m Manual page man(1) line 76 (press h for help or q to quit)\u001b[27m\u001b[K"],

			["up + 0.547791", "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			["up + 0.54827", "o", "\u001b[KA\bA\r\u001b[K"],
			["up + 0.548773", "o", "\u001b[H\u001bM\u001b[1mEXAMPLES\u001b[0m\u001b[m\r\n\u001b[24;1H\r\u001b[K\u001b[7m Manual page man(1) line 75 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["up + 1.339862", "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			["up + 1.340289", "o", "\u001b[KA\bA\r\u001b[K\u001b[H\u001bM\u001b[m\r\n\u001b[24;1H\r\u001b[K\u001b[7m Manual page man(1) line 74 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["up + 2.035805", "o", "\r\u001b[K \u001b[KESC\b\b\bESC"],
			["up + 2.036168", "o", "\u001b[KO\bO\u001b[KA\bA\r\u001b[K\u001b[H\u001bM       \u001b[7mman\u001b[27mual page.\u001b[m\r\n\u001b[24;1H\r\u001b[K\u001b[7m Manual page man(1) line 73 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["up + 2.827918", "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			["up + 2.82833", "o", "\u001b[KA\bA\r\u001b[K\u001b[H\u001bM       eral exclusive invocations as is shown in the \u001b[1mSYNOPSIS\u001b[0m section of  this\u001b[m\r\n\u001b[24;1H\r\u001b[K\u001b[7m Manual page man(1) line 72 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["up + 3.459969", "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			["up + 3.46038", "o", "\u001b[KA\bA\r\u001b[K\u001b[H\u001bM       possible invocations.  In some cases it is advisable to illustrate sev‐\u001b[m\r\n\u001b[24;1H\r\u001b[K\u001b[7m Manual page man(1) line 71 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["up + 4.059878", "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			["up + 4.060296", "o", "\u001b[KA\bA\r\u001b[K\u001b[H\u001bM       The com\u001b[7mman\u001b[27md or function illustration is a pattern that should match all\u001b[m\r\n\u001b[24;1H\r\u001b[K\u001b[7m Manual page man(1) line 70 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["up + 4.731672", "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			["up + 4.73192", "o", "\u001b[KA\bA\r\u001b[K\u001b[H\u001bM\u001b[m\r\n\u001b[24;1H\r\u001b[K\u001b[7m Manual page man(1) line 69 (press h for help or q to quit)\u001b[27m\u001b[K"],
			["up + 5.331857", "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO\u001b[KA\bA\r\u001b[K"],
			["up + 5.332293", "o", "\u001b[H\u001bM       nal, and will typically use underlined or coloured text instead.\u001b[m\r\n\u001b[24;1H\r\u001b[K\u001b[7m Manual page man(1) line 68 (press h for help or q to quit)\u001b[27m\u001b[K"],
		],
		'text' : [
			# EKRAN: man - przewijnaie stron
			'Zapewne zauważyliśmy że dokumentację man przeglądaliśmy ekran po ekranie, <m> natomiast informacje wypisywane przez wywołanie komendy <m> z opcją help wypisywały się hurtem na ekran. <m>'
			'Dzieje się tak dlatego że polecenie man korzysta z programu <m> nazywanego pagerem do podziału tekstu na strony. <m>'
			'Rolę tą zazwyczaj pełni more lub less a kolejne strony <m> można wyświetlać z użyciem spacji. <mark name="search" />'
			# EKRAN: man - wyszukiwanie
			'Oba te programy pozwalają także na wyszukiwanie z użyciem ukośnika, <m> rozpoczynającego wprowadzenie szukanego tekstu <m> i klawisza n do wyszukania kolejnego wystąpienia. <m>'
			'Natomiast zakończenie działania odbywa się za pomocą klawisza q. <m>'
			'Zarówno taki sposób wyszukiwania jak też zamykania programu <m> jest wart zapamiętania, gdyż jest często spotykaną konwencją. <mark name="up" />'
			# EKRAN: man - przewijnaie w góre linia po linii
			'Less jest bardziej rozbudowany niż more i pozwala także na <m> przewijanie linia po linii, przewijanie w obu kierunkach <m> z użyciem strzałek oraz page up i page down, <m> a także wyszukiwanie wstecz z użyciem shift n <m>'
		]
	},
	{
		'console': [
			[0.058688, "o", eduMovie.clear + eduMovie.prompt()],
			[0.69478, "o", "l"],
			[0.886743, "o", "e"],
			[1.142775, "o", "s"],
			[1.294708, "o", "s"],
			[1.454712, "o", " "],
			[1.678724, "o", "/"],
			[1.838742, "o", "e"],
			[2.086702, "o", "t"],
			[2.452806, "o", "c/"],
			[2.94277, "o", "p"],
			[3.478765, "o", "a"],
			[3.702748, "o", "s"],
			[3.940034, "o", "\u0007swd"],
			[4.270745, "o", "\r\n"],
			[4.279067, "o", "\u001b[?1049h\u001b[22;0;0t\u001b[?1h\u001b=\r"],
			[4.279456, "o", "root:x:0:0:root:/root:/bin/bash\r\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\r\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\r\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\r\nsync:x:4:65534:sync:/bin:/bin/sync\r\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\r\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\r\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\r\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\r\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\r\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\r\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\r\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\r\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\r\nlist:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\r\nirc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin\r\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologi \bn\r\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\r\nrrp:x:1000:1000:Robert Paciorek,,,:/rrp:/bin/bash"],
			[4.27982, "o", "\r\nmessagebus:x:101:104::/var/run/dbus:/bin/false\r\nsshd:x:102:65534::/var/run/sshd:/usr/sbin/nologin\r\nsystemd-timesync:x:103:111:systemd Time Synchronization,,,:/run/systemd:/bin/fal \b\u001b[7m/etc/passwd\u001b[27m\u001b[K"],
			[5.254821, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[5.255221, "o", "\u001b[KB\bB\r\u001b[Kse\r\n:\u001b[K"],
			[5.638786, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[5.639159, "o", "\u001b[KB\bB\r\u001b[Ksystemd-network:x:105:113:systemd Network Management,,,:/run/systemd/netif:/bin/ \b:\u001b[K"],
			[6.83884, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[6.839274, "o", "\u001b[KA\bA\r\u001b[K\u001b[H\u001bMdaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\r\n\u001b[24;1H\r\u001b[K:\u001b[K"],
			[7.126802, "o", "\r\u001b[K \u001b[KESC\b\b\bESC\u001b[KO\bO"],
			[7.127176, "o", "\u001b[KA\bA\r\u001b[K\u001b[H\u001bMroot:x:0:0:root:/root:/bin/bash\r\n\u001b[24;1H\r\u001b[K:\u001b[K"],
		],
		'text' : [
			'Polecenia te mogą być także użyte do wyświetlania plików, <m> a także, dzięki przekierowaniom strumieni, <m> do podziału na strony outputu innych poleceń. <m>'
		]
	},
]

