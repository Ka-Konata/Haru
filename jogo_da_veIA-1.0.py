#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
	Jogo da Velha (IA - inteligencia artificial)              version 1.0 - Program

	Também conhecido como Jogo do Galo e Tic-Tac Toe

	Copyright (c) 2019-2020 Washington Luis de O. Santos
	
	< owashington[arroba]terra.com.br >

	This program is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation; either version 2 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License along
	with this program; if not, write to the Free Software Foundation, Inc.,
	51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

	Taubaté - SP, 4 de julho de 2020

	Vejam as minhas outras colaborações no link:
	https://www.vivaolinux.com.br/~WashingtonLuis/scripts/

	Este programa foi baseado em um outro feito em basic apresentado na:

	REVISTA GERACAO PROLOGICA Nº 3 - PG. 6 
	publicada em jan/fev de 1984
	CP-200 COMPATIVEL ZX81 - TK-85

	Disponivel em pdf no link abaixo:
	https://datassette.org/revistas/geracao-prologica-informatica-revistas/geracao-prologica-no-3
'''

import random
import os
from time import sleep

def GetLine(posicao):
	global pa, pb, pc
	posicao *= 2

	# abaixo, temos uma sequencia de "nºs mágicos" que, na realidade, de um jeito meio obscuro,
	# formam as linhas verticais, horizontais e diagonais do tabuleiro. Como por exemplo:
	# 591, 132, 258, e assim por diante...
	# Eu poderia fazer de outra forma, mas o meu ojetivo com isto é homenagear 'O CARA' que criou
	# o programinha lá pro CP-200 / TK-85 e que infelizmente não tem o nome divulgado

	# OBSERVAÇÃO: os numeros foram subtraidos em 1 para coincidir com as posições da string que
	# no PYTHON começa em 0
	#z = '59132587963756471'
	z =  '48021476852645360' 

	pa = int(z[posicao + 0])
	pb = int(z[posicao + 1])
	pc = int(z[posicao + 2])
	return board[pa] + board[pb] + board[pc]


def pc_joga():

	for x in (2, 18):
		for n in range(8):
			if GetLine(n) == x:
				if   board[pa] == vazio: pos = pa
				elif board[pb] == vazio: pos = pb
				else:                    pos = pc
				
				board[pos] = 1
				print('%s%s%i%s' % (BLUE, 'Posição Pc: ', (pos+1), RST))
				sleep(2)
				return

	while True:
		pos = random.randint(0, 8)
		if board[pos] == vazio:
			board[pos] = 1
			break

	print('%s%s%i%s' % (BLUE, 'Posição Pc: ', (pos+1), RST))
	sleep(2)
	return


def user_joga():
	while True:
		x = input('%s%s%s' % (GREEN, 'Posição user: ', RST))

		if x in ('q', 'Q', '0'):
			print('Jogo abortado...')
			exit(0)

		try:
			pos = int(x) - 1
			
			if board[pos] != vazio:
				print('Posição já ocupada')

			else :
				board[pos] = 9
				break
		except:
			pass


def display():
	global empate, micro, user
	os.system('clear')
	mk = []
	for i, v in enumerate(board):
		if   v == 0: mk.append('%s%s%s' % (YELLOW, str(i+1), RST))
		elif v == 1: mk.append('%s%s%s' % (BLUE  , 'O'     , RST))
		else:        mk.append('%s%s%s' % (GREEN , 'X'     , RST))

	print('%s%s%i%s' % (WHITE, 'Empate  = ', empate, RST))
	print('%s%s%i%s' % (BLUE , 'Micro   = ', micro , RST))
	print('%s%s%i%s' % (GREEN, 'Usuário = ', user  , RST))
	print()
	print(' %s | %s | %s' % tuple(mk[0:3]))
	print('---+---+---')
	print(' %s | %s | %s' % tuple(mk[3:6]))
	print('---+---+---')
	print(' %s | %s | %s' % tuple(mk[6:9]))
	print()


def verif():
	global empate, micro, user

	for n in range(8):
		if   GetLine(n) == 3:
			 print('%s%s%s' % (BLUE, 'O Computador Ganhou', RST))
			 micro += 1
			 sleep(2)
			 return True

		elif GetLine(n) == 27:
			 print('%s%s%s' % (GREEN, 'O Usuário Ganhou', RST))
			 user += 1
			 sleep(2)
			 return True

	if not vazio in board:
		print('Empatou...')
		empate += 1
		sleep(2)
		return True

	return False


if __name__ == '__main__':

	# Define variáveis usadas para mostrar cores no terminal
	RST     = '\033[00m'
	GRAY    = '\033[30m'
	RED     = '\033[31m'
	GREEN   = '\033[32m'
	YELLOW  = '\033[33m'
	BLUE    = '\033[34m'
	VIOLET  = '\033[35m'
	VERDAO  = '\033[36m'
	WHITE   = '\033[37m'

	empate = 0
	micro  = 0
	user   = 0
	vazio  = 0

	while True:

		board = [vazio] * 9

		Flag = random.choice([True, False])

		display()

		while True:

			Flag = not Flag

			if Flag: pc_joga()

			else:    user_joga()

			display()

			if verif(): break

		display()
		key = input('Quer jogar de Novo? (S/N)')

		if key not in ('S', 's'):
			break

	print('\nFim de Jogo')
