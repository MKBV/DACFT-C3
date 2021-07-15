main_string="c an u br ea k th is we ir d en or yp ti on".split()

data = "eawethkthorthorthonutiuckirthoniskisuucthththorthanthisucthirisbruceaeathanisutheneabrkeaeathisenbrctheneacisirkonbristhwebranbrkkonbrisbranthypbrbrkonkirbrciskkoneatibrbrbrbrtheakonbrisbrckoneauisubrbreacthenkoneaypbrbrisyputi"

chck = ""
raw = ""
at = 0

for letter in data:
	chck += letter

	if chck in main_string:
	
 		if at%2 == 0:
			c1 = main_string.index(chck)*16
			at+=1

		else:
			c2 = main_string.index(chck)
			raw += chr(c1+c2)
			at+=1
		chck=""
		
print(raw)
