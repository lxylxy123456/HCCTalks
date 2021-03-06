import re
import numpy as np
from bs4 import BeautifulSoup

def p(x) :
	return '(%.3f,%.3f)' % (x[0], -x[1])

def f(x) :
	X = x.split()
	prev_cmd = None
	i = 0
	cur = 0, 0
	def read() :
		nonlocal i, cur
		dat = X[i]; i += 1
		d1, d2 = dat.split(',')
		return cur[0] + float(d1), cur[1] + float(d2)
	def read_cur() :
		nonlocal i, cur
		dat = X[i]; i += 1
		d1, d2 = dat.split(',')
		cur = cur[0] + float(d1), cur[1] + float(d2)
		return cur
	def add(x, y) :
		return x[0] + y[0], x[1] + y[1]
	while i < len(X) :
		if len(X[i]) == 1 :
			prev_cmd = cmd = X[i]; i += 1
		else :
			cmd = prev_cmd
		if cmd == 'm' :
			a = read_cur()
			print('\draw %s' % p(a))
		elif cmd == 'c' :
			a, b, c = read(), read(), read_cur()
			print('.. controls %s and %s .. %s' % (p(a), p(b), p(c)))
		elif cmd == 'l' :
			a = read_cur()
			print('-- %s' % p(a))
		elif cmd == 'z' :
			print(';')
		else :
			0/0

def g(x) :
	a = BeautifulSoup(x, 'lxml')
	ans = []
	for i in a.select('rect') :
		h = float(i.attrs['height'])
		w = float(i.attrs['width'])
		x = float(i.attrs['x'])
		y = float(i.attrs['y'])
		tr = i.attrs.get('transform')
		co, = re.search('fill:#([0-9a-f]+);', i.attrs['style']).groups()
		color = int(co[0:2], 16), int(co[2:4], 16), int(co[4:6], 16)
		xx = x + w
		yy = y + h
		if tr is not None :
			exp = 'matrix\(([^,]+),([^,]+),([^,]+),([^,]+),([^,]+),([^,]+)\)'
			mat = list(map(float, re.fullmatch(exp, tr).groups()))
			matrix = np.array([[mat[0], mat[2], mat[4]],
								[mat[1], mat[3], mat[5]],
								[0, 0, 1]])
			def transform(x, y) :
				md = matrix.dot(np.array([[x], [y], [1]]))
				return md[0][0], md[1][0]
			xy = transform(x, y)
			xxy = transform(xx, y)
			xyy = transform(x, yy)
			xxyy = transform(xx, yy)
			def mean(a, b) :
				s = (a + b) / 2
				d = abs((a - b) / 2)
				# print(d)	# 0/0
				return s
			if 0 :
				print(x, y)
				print(xx, yy)
				print(xy)
				print(xxy)
				print(xyy)
				print(xxyy)
			xxx = sorted([xy[0], xxy[0], xyy[0], xxyy[0]])
			yyy = sorted([xy[1], xxy[1], xyy[1], xxyy[1]])
			x = mean(xxx[0], xxx[1])
			xx = mean(xxx[2], xxx[3])
			y = mean(yyy[0], yyy[1])
			yy = mean(yyy[2], yyy[3])
		def rnd(x) :
			return round(x / 5, 1) * 5
		ans.append(
			'\\filldraw [color={rgb,255:red,%d; green,%d; blue,%d}]\n' % color+\
			'\t%s rectangle %s;' % (p((rnd(x), rnd(y))), p((rnd(xx), rnd(yy)))))
	for i in reversed(ans) :
		print(i)
#		print(x, y, xx, yy, tr, color)

# f("m 54.697536,20.16266 c -0.479502,-0.0899 -0.882073,-0.173702 -0.894603,-0.186234 -0.01614,-0.01614 1.537356,-8.837361 1.567609,-8.901308 0.004,-0.0085 1.903782,0.330154 1.91559,0.341583 0.0043,0.0041 -0.351867,2.007037 -0.791549,4.450771 -0.439682,2.443735 -0.800263,4.448646 -0.801292,4.45536 -0.0035,0.0227 -0.122021,0.0036 -0.995755,-0.160172 l 0,0 z")

# f("m 54.153405,27.479108 c -0.08056,-0.01027 -0.377179,-0.06158 -0.659148,-0.113991 -3.096766,-0.575626 -5.5713,-3.000914 -6.276113,-6.151211 -0.108815,-0.4864 -0.151208,-2.041513 -0.07301,-2.678493 0.325385,-2.650351 2.107616,-5.022615 4.615841,-6.143985 0.497452,-0.222399 1.441685,-0.519562 1.571482,-0.494565 0.06953,0.01339 0.116632,0.166655 0.245081,0.797359 0.221108,1.085676 0.234817,1.032439 -0.307113,1.192638 -2.095264,0.619375 -3.679526,2.354288 -4.149393,4.543972 -0.121448,0.565954 -0.143853,1.542397 -0.04869,2.121834 0.386054,2.350787 2.139541,4.24826 4.495155,4.864269 0.558722,0.146108 1.782808,0.183379 2.412662,0.07346 0.78671,-0.137295 1.666754,-0.496649 2.364655,-0.965578 0.427868,-0.28749 1.267266,-1.124179 1.548604,-1.543605 0.435943,-0.64992 0.738045,-1.380964 0.922495,-2.232315 0.187192,-0.863992 0.103411,-2.18121 -0.196099,-3.083259 -0.134755,-0.405842 -0.481746,-1.076973 -0.761822,-1.473476 -0.329195,-0.466042 -0.985595,-1.123805 -1.448443,-1.451452 -0.219395,-0.155307 -0.418098,-0.298712 -0.44156,-0.318674 -0.04472,-0.03805 0.419698,-0.959402 0.721046,-1.430485 l 0.175662,-0.274604 0.280952,0.182036 c 0.734761,0.476072 1.570037,1.228968 2.059816,1.85666 0.516011,0.66132 0.995211,1.562257 1.266595,2.381309 0.511224,1.542919 0.51913,3.354742 0.02129,4.882586 -0.520916,1.598699 -1.561923,3.031949 -2.899641,3.992197 -0.822219,0.590209 -2.046963,1.134896 -2.974613,1.322916 -0.780066,0.158108 -1.86219,0.221509 -2.465706,0.144465 z")

# g(open('/tmp/logo.svg').read())
