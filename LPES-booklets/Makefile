ifeq ($(MAINDIR),)
	include ../Makefile
else

SECTIONS := extra-tex-files/booklets-sections

$(OUTDIR)/LPES_00-Info.pdf:                    extra-tex-files/lpes-sections/0*
$(OUTDIR)/LPES_00-Warsztat_elektroniczny.pdf:  $(SECTIONS)/warsztat/*
$(OUTDIR)/LPES_01-Linux_1.pdf:                 $(SECTIONS)/linux/*        $(call img4tex_from_src,linux/*)
$(OUTDIR)/LPES_02-Python_1.pdf:                $(SECTIONS)/python/*
$(OUTDIR)/LPES_03-Python_2.pdf:                $(SECTIONS)/python/*
$(OUTDIR)/LPES_04-Linux_2.pdf:                 $(SECTIONS)/linux/*        $(call img4tex_from_src,linux/*)
$(OUTDIR)/LPES_05-Linux_3.pdf:                 $(SECTIONS)/linux/*
$(OUTDIR)/LPES_06-C_Cpp.pdf:                   $(SECTIONS)/c_cpp/*
$(OUTDIR)/LPES_07-warsztat.pdf:                $(SECTIONS)/warsztat/*
$(OUTDIR)/LPES_08-elektronika_1.pdf:           $(SECTIONS)/electronics/*  $(call img4tex_from_src,elektronika/*)
$(OUTDIR)/LPES_09-elektronika_2.pdf:           $(SECTIONS)/electronics/*  $(call img4tex_from_src,elektronika/*)
$(OUTDIR)/LPES_10-Sieci_1.pdf:                 $(SECTIONS)/network/*
$(OUTDIR)/LPES_11-Sieci_2.pdf:                 $(SECTIONS)/network/*                                              extra-tex-files/RJ-45_TIA-568*.png
$(OUTDIR)/LPES_12-stm32.pdf:                   $(SECTIONS)/stm32/*        $(call img4tex_from_src,stm32/*)        extra-tex-files/stm32-examples/*/*

endif
