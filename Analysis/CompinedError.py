#==================
# Compined error
#==================


def coer(a,x,erx,y,ery,z=None,erz=None):
	""" Find the error in quotient function of 2 variables a = x/y
	parameters:
	----------
	a the dependant variable
	x first independant variable
	y second independant variable
	erx error in x
	ery error in y """
	error =[]
	for i , val in enumerate(a):
		if z == None:
			j = np.sqrt((erx[i])**2 + (ery[i]/y[i])**2)/y[i]
		else:
			j = val * ((erx[i]/x[i]) + (ery[i]/y[i]) + (erz[i]/z[i]))
		error.append(j)
	return error

