import random, base64

string = "Get-ChildItem"
random.seed(string)
length = len(string)

shuffle_array = [] * length
for i in range(length):
	shuffle_array.append(i)
random.shuffle(shuffle_array)

encrypted_chars = []
xor_key = []
for i in string:
    current_key = random.randrange(1,255)
    xor_key.append(current_key)
    encrypted_chars.append(ord(i) ^ current_key)

temp_array = []
for i in shuffle_array:
    temp_array.append(xor_key[i])

xor_key = temp_array

temp_array = []
for i in shuffle_array:
    temp_array.append(encrypted_chars[i])
encrypted_chars = temp_array

#Build Variable
rand_var_name = ""
for i in range(10):
    if i%2 == 0:
        rand_var_name += chr(random.randrange(65,90))
    else:
        rand_var_name += chr(random.randrange(97,122))

output = "$" + rand_var_name + "=@("
for i in xor_key:
    output += str(i) + ","
output = output[:-1] + ");('"

for i in range(length):
    output += "{" + str(shuffle_array.index(i)) + "}"
output += "')-f"

for counter,enc_char in enumerate(encrypted_chars):
    output += "[char]($" + rand_var_name + "[" + str(counter) + "]-bxor" + str(enc_char) + "),"
output = output[:-1].encode('ascii')
print("\n",output,"\n",sep="")   
output = "&([ScriptBlock]::Create([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('" + base64.b64encode(output).decode('ascii') +"'))))"
print(output)