# Find the mean value in quotient (comparison) function using the standard deviation on each data point
#--------------
# weighted mean
#--------------

def wm(mu,se):
	""" Find the weighed mean value in quotient (comparison) function using standard errorbar
	Parameters:
	----------
	mu: list of parameter's value (mu_PH or mu_PI)
	se: the standard error corresponding to each value (se_mu_PH or se_mu_PI)
	"""
	nomsum =[]
	w = []
	for i in range(len(mu)):
		nom = mu[i] / (se[i])**2
		nomsum.append(nom)
		w.append(1/(se[i])**2)
	wmu = sum(nomsum) / sum(w)
	return (wmu)


