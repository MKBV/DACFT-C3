# DACTF-C3  
### Write up of 2020 DarkArmy CTF Cryptography 3rd challenge  
  
In the challenge they gave us an encrypted data and a encryption algorithm.  
  
#### Encrypter Algorithm  
  
```python
prefix="Hello. Your flag is DarkCTF{"
suffix="}."
main_string="c an u br ea k th is we ir d en or yp ti on".split()

clear_text = prefix + flag + suffix
enc_text = ""
for letter in clear_text:
		 c1 = ord(letter) / 16
		 c2 = ord(letter) % 16
		 enc_text += main_string[c1]
		 enc_text += main_string[c2]

print enc_text
```
  
The python code doesn't work because there is no defined flag variable.  
But we can understand the algorithm.  
  
>Firstly there is a list defined as *main_string*.  
>At for loop, every byte is setting to *latter* orderly.  
>Then bytes's unicode number divided into 16 and quotient set as c1, remainder set as c2.  
>In the list select an item by c1 and c2 values, then add it to *enc_text* variable.  
>When all bytes were converted then the encrypted data will appear.  
  
Here is the encrypted data:  
`eawethkthorthorthonutiuckirthoniskisuucthththorthanthisucthirisbruceaeathanisutheneabrkeaeathisenbrctheneacisirkonbristhwebranbrkkonbrisbranthypbrbrkonkirbrciskkoneatibrbrbrbrtheakonbrisbrckoneauisubrbreacthenkoneaypbrbrisyputi`

When we look at that we can understand how made it.  
Lets code the reverse encryption script.  

#### Decrypter Algorithm

```python
main_string="c an u br ea k th is we ir d en or yp ti on".split()
data = "**ENCRYPTED_DATA**"

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
```
  
  
>Again for loop set data's bytes to *latter* variable.  
>Bytes were added to check list then if the check string is in the *main_string* list, *chck* can continue.   
>If not the loop appends another byte to *chck* string.  
>When reading the data script, we need to seperate to the c1 and c2 variables.  
>c1 variable multiplied by 16, c2 added to the c1.  
>The integer gives a unicode number, when it's converted to the ascii type we get the decrypted letter.  
>When all latters are added to *raw* list, decrypted data appears.  
  

And the final message is: **Hello. Your flag is DarkCTF{0k@y_7h15_71m3_Y0u_N33d_70_Br3@k_M3}.**
