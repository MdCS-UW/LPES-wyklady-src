# Copyright (c) 2019-2021 Robert Ryszard Paciorek <rrp@opcode.eu.org>
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

MAINDIR     := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
OUTDIR      := $(MAINDIR)/output-www
TEXBUILDDIR := $(MAINDIR)/tmp-build
LIBFILESDIR := $(MAINDIR)/OpCode.eu.org/OpCode-core/lib
SVGICONURL  := https://bytebucket.org/OpCode-eu-org/svgiconset/raw/HEAD/other/
export PATH := $(MAINDIR)/OpCode.eu.org/TextUtils/convert:$(PATH)


.PHONY: help init installDependencies all
help:
	@echo see README.md

init: | checkout-submodules $(MAINDIR)/LPES-video/GoogleCloudTextToSpeach.py
	mkdir -p "$(TEXBUILDDIR)" "$(OUTDIR)"
	@(cd OpCode.eu.org && ln -fs $(MAINDIR)/output-www $(MAINDIR)/tmp-build . && make init )
	@echo ""
	@echo ""
	@echo -e '\033[1;96m Congratulation, all repos init OK \033[0;m\n'
	@echo "If you have installed external dependencies you can build this project."
	@echo "If not READ OpCode.eu.org/README.md and install dependencies of that submodule:"
	@(cd OpCode.eu.org && make --no-print-directory help | grep -v 'make init' | sed '/you must install/,+1d')

all:
	$(MAKE) buildAll
	@ [ "$(MAINDIR)" = "$(PWD)" ] && (cd LPES-booklets && $(MAKE) -f ../Makefile buildAll) || true
	@ [ "$(MAINDIR)" = "$(PWD)" ] && (cd LPES-video    && $(MAKE) -f ../Makefile buildAll) || true

$(MAINDIR)/LPES-video/GoogleCloudTextToSpeach.py:
	echo "token = ''" > $(MAINDIR)/LPES-video/GoogleCloudTextToSpeach.py

#
# submodules
#

.PHONY: checkout-submodules update-submodules protect-submodules

update-subsubmodules:
	# run `submodule update` action in selected submodules
	(cd OpCode.eu.org && make checkout-submodules)

checkout-submodules:
	git submodule update --init
	$(MAKE) update-subsubmodules

update-submodules: | checkout-submodules
	git submodule foreach 'git pull origin master; git checkout -f .'
	$(MAKE) update-subsubmodules

#
# include core makefile from TextUtils
#

-include $(MAINDIR)/OpCode.eu.org/TextUtils/makefiles/buildWebSite.mk

#
# addionals files
#

include $(wildcard $(MAINDIR)/LPES*/Makefile)
