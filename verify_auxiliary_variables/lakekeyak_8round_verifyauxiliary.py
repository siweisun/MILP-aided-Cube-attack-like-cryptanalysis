from brial import *
import copy
import pdb
import xdrlib ,sys
import random
import time

Keccak=declare_ring([Block('k',256),Block('v',1600)],globals())


def theta(state):
	tempstate=[[] for i in range(25)]
	for i in range(25):
		for j in range(64):
			tempstate[i].append(state[i][j])
			for k in range(5):
				tempstate[i][j]+=state[(i%5+5-1)%5+5*k][j]+state[(i%5+1+5)%5+5*k][(j-1+64)%64]

	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]



def rio(state):
	rot=[0,1,62,28,27,36,44,6,55,20,3,10,43,25,39,41,45,15,21,8,18,2,61,56,14]
	tempstate=[[] for i in range(25)]
	for i in range(25):
		for j in range(64):
			tempstate[i].append(state[i][(j-rot[i]+64)%64])

	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]

def pi(state):
	tempstate=[[] for i in range(25)]
	for i in range(25):
		y=floor(i/5)
		x=i%5
		x1=y
		y1=(2*x+3*y)%5
		temp=5*y1+x1
		for j in range(64):
			tempstate[temp].append(state[i][j])
	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]

def chi(state):
	tempstate=[[] for i in range(25)]
	for i in range(5):
		for j in range(5):
			for k in range(64):
				tempstate[5*i+j].append(state[5*i+j][k]+(state[5*i+(j+1)%5][k]+1)*state[5*i+(j+2)%5][k])

	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]

state=[[] for i in range(25)]
for i in range(25):
	for j in range(64):
		state[i].append(Keccak(0))




state[0][9]=Keccak(k(0))
state[0][10]=Keccak(k(1))
state[0][12]=Keccak(k(2))
state[0][16]=Keccak(k(3))
state[0][17]=Keccak(k(4))
state[0][19]=Keccak(k(5))
state[0][20]=Keccak(k(6))
state[0][23]=Keccak(k(7))
state[0][26]=Keccak(k(8))

state[0][30]=Keccak(k(9))
state[0][33]=Keccak(k(10))
state[0][36]=Keccak(k(11))
state[0][37]=Keccak(k(12))
state[0][40]=Keccak(k(13))
state[0][43]=Keccak(k(14))




state[5][9]=Keccak(k(0))
state[5][10]=Keccak(k(1))
state[5][12]=Keccak(k(2))
state[5][16]=Keccak(k(3))
state[5][17]=Keccak(k(4))
state[5][19]=Keccak(k(5))
state[5][20]=Keccak(k(6))
state[5][23]=Keccak(k(7))
state[5][26]=Keccak(k(8))

state[5][30]=Keccak(k(9))
state[5][33]=Keccak(k(10))
state[5][36]=Keccak(k(11))
state[5][37]=Keccak(k(12))
state[5][40]=Keccak(k(13))
state[5][43]=Keccak(k(14))






state[5][4]=Keccak(v(0))
state[10][4]=Keccak(v(0)+v(1))
state[15][4]=Keccak(v(1))
state[5][11]=Keccak(v(63))
state[10][11]=Keccak(v(2)+v(63))
state[15][11]=Keccak(v(2))
state[5][18]=Keccak(v(3))
state[10][18]=Keccak(v(3)+v(4))
state[15][18]=Keccak(v(4))
state[10][22]=Keccak(v(5))
state[15][22]=Keccak(v(5))
state[5][25]=Keccak(v(6))
state[15][25]=Keccak(v(6))
state[10][28]=Keccak(v(7))
state[15][28]=Keccak(v(7))
state[5][29]=Keccak(v(8))
state[15][29]=Keccak(v(8))
state[5][35]=Keccak(v(62))
state[10][35]=Keccak(v(9)+v(62))
state[15][35]=Keccak(v(9))
state[5][42]=Keccak(v(10))
state[15][42]=Keccak(v(10))
state[5][47]=Keccak(v(11))
state[10][47]=Keccak(v(11))
state[5][48]=Keccak(v(12))
state[10][48]=Keccak(v(12))
state[5][54]=Keccak(v(13))
state[10][54]=Keccak(v(13)+v(14))
state[15][54]=Keccak(v(14))
state[5][55]=Keccak(v(15))
state[15][55]=Keccak(v(15))
state[5][58]=Keccak(v(16))
state[10][58]=Keccak(v(16))
state[5][61]=Keccak(v(61))
state[10][61]=Keccak(v(17)+v(61))
state[15][61]=Keccak(v(17))
state[10][62]=Keccak(v(18))
state[15][62]=Keccak(v(18))
state[12][0]=Keccak(v(19))
state[17][0]=Keccak(v(19)+v(20))
state[22][0]=Keccak(v(20))
state[12][1]=Keccak(v(60))
state[17][1]=Keccak(v(21)+v(60))
state[22][1]=Keccak(v(21))
state[12][4]=Keccak(v(22))
state[17][4]=Keccak(v(22)+v(23))
state[22][4]=Keccak(v(23))
state[12][5]=Keccak(v(24))
state[17][5]=Keccak(v(24))
state[12][7]=Keccak(v(59))
state[17][7]=Keccak(v(25)+v(59))
state[22][7]=Keccak(v(25))
state[12][10]=Keccak(v(26))
state[22][10]=Keccak(v(26))
state[12][11]=Keccak(v(27))
state[17][11]=Keccak(v(27))
state[12][13]=Keccak(v(28))
state[22][13]=Keccak(v(28))
state[17][14]=Keccak(v(29))
state[22][14]=Keccak(v(29))
state[12][17]=Keccak(v(30))
state[22][17]=Keccak(v(30))
state[12][18]=Keccak(v(31))
state[17][18]=Keccak(v(31))
state[12][20]=Keccak(v(32))
state[22][20]=Keccak(v(32))
state[12][21]=Keccak(v(33))
state[17][21]=Keccak(v(33)+v(34))
state[22][21]=Keccak(v(34))
state[12][24]=Keccak(v(58))
state[17][24]=Keccak(v(35)+v(58))
state[22][24]=Keccak(v(35))
state[12][27]=Keccak(v(36))
state[22][27]=Keccak(v(36))
state[17][28]=Keccak(v(37))
state[22][28]=Keccak(v(37))
state[12][31]=Keccak(v(38))
state[17][31]=Keccak(v(38))
state[12][34]=Keccak(v(39))
state[22][34]=Keccak(v(39))
state[17][35]=Keccak(v(40))
state[22][35]=Keccak(v(40))
state[12][38]=Keccak(v(41))
state[17][38]=Keccak(v(41))
state[17][39]=Keccak(v(42))
state[22][39]=Keccak(v(42))
state[12][41]=Keccak(v(43))
state[22][41]=Keccak(v(43))
state[12][45]=Keccak(v(44))
state[17][45]=Keccak(v(44)+v(45))
state[22][45]=Keccak(v(45))
state[17][46]=Keccak(v(46))
state[22][46]=Keccak(v(46))
state[12][51]=Keccak(v(57))
state[17][51]=Keccak(v(47)+v(57))
state[22][51]=Keccak(v(47))
state[12][52]=Keccak(v(48))
state[17][52]=Keccak(v(48)+v(49))
state[22][52]=Keccak(v(49))
state[12][56]=Keccak(v(50))
state[17][56]=Keccak(v(50))
state[12][57]=Keccak(v(57))
state[17][57]=Keccak(v(51)+v(57))
state[22][57]=Keccak(v(51))
state[12][58]=Keccak(v(52))
state[17][58]=Keccak(v(52)+v(53))
state[22][58]=Keccak(v(53))
state[12][62]=Keccak(v(54))
state[17][62]=Keccak(v(54))
state[12][63]=Keccak(v(55))
state[17][63]=Keccak(v(55))





theta(state)
rio(state)
pi(state)
chi(state)

n=0
for i in range(15):
	for j in range(64):
		for i0 in xrange(25):
			for j0 in xrange(64):
				if(state[i0][j0]/Keccak((k(i)*v(j)))):
					print 'k',i,'v',j
					n=n+1


print(n)











