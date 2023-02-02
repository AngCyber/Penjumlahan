#!/usr/bin/python3
#coding=utf-8
#copyright © Moch Aang Ardiansyah XD.

import os
import random

P = "\x1b[0;97m"
H = "\x1b[0;92m"

__soal__ = 0
__hasil__ = 10
__nilai__ = 0

while __soal__ <= __hasil__:
	os.system("clear")
	print(f"{P}>. Soal dari {H}{__soal__}{P}/{H}{__hasil__}")
	print(f"{P}>. Nilai kamu : {H}{__nilai__}{P}")
	print(f"\n{P}?. Berapa hasil dari penjumlahan berikut")
	aku = random.randint(1,50)
	kamu = random.randint(1,50)
	anak = aku + kamu
	print(f"{P}>. {H}{aku} + {kamu}{P} = berapa?")
	__jawab__ = int(input(f"{P}?. Jawab : "))
	if __jawab__ == anak:
		print(f"\n{P}✓. {H}Jawaban benar ...")
		__nilai__ += 10
		__soal__ += 1
		input(f"{P}!. Tekan enter")
	else:
		print(f"\n{P}>. Jawaban salah, {H}{aku} + {kamu} = {anak}{P}")
		__soal__ += 1
		input(f"{P}!. Tekan enter")