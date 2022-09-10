from Metodos_dados import Met #metodo meu próprio
ficha_seguranca = Met

class arm:
	class prod:
		def __init__(self, name):
			self.name = name
			self.quant = 30
			self.security, self.company = ficha_seguranca.fsi()
			self._propety = ficha_seguranca.return_l()

		def _changeFsi():	
			pass

	# class manual:
	# 	pass	

	def conta_product()->None:
		print(10)

Molikote = arm.prod("Molikote") #deve se passar o parametro name na definicao
#new é uma classe do tipo arm
#new tem.uma herança de iniciacao de classes
#print(Molikote.name)
print(Molikote.security)
