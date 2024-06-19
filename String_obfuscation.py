#===============================================#
# Title:  PowerShell String Obfuscator		#
# Author: 0xB4DC0DE				#
# Date:   19 June 2024				#
# Ver:	  1.1					#
#===============================================#

import random, base64

def create_key_arays(input_string):
    xor_key = []
    encrypted_chars = []
    return_array = []
    for i in input_string:
        current_key = random.randrange(1,255)
        xor_key.append(current_key)
        encrypted_chars.append(ord(i) ^ current_key)
    return_array = [xor_key,encrypted_chars]
    return return_array
def fcn_shuffle_array(length):
    shuffle_array = sorted(list(range(length)),key=lambda x: random.random())
    return shuffle_array 
def sort_array(input_array,shuffle_array):
    return_array = []
    for i in shuffle_array:
        return_array.append(input_array[i])
    return return_array
def random_var(size):
    rand_var_name = ""
    for i in range(10):
        if i%2 == 0:
            rand_var_name += chr(random.randrange(65,90))
        else:
            rand_var_name += chr(random.randrange(97,122))
    return rand_var_name
def create_string(input_string):
    random.seed(input_string)
    input_length = len(input_string)
    shuffle_array = fcn_shuffle_array(input_length)
    key_arrays = create_key_arays(input_string)
    xor_key = sort_array(key_arrays[0],shuffle_array)
    encrypted_chars = sort_array(key_arrays[1],shuffle_array)
    rand_var_name = random_var(10)
    output = "$" + rand_var_name + "=@("
    for i in xor_key:
        output += str(i) + ","
    output = output[:-1] + ");('"
    for i in range(input_length):
        output += "{" + str(shuffle_array.index(i)) + "}"
    output += "')-f"
    for counter,enc_char in enumerate(encrypted_chars):
        output += "[char]($" + rand_var_name + "[" + str(counter) + "]-bxor" + str(enc_char) + "),"
    output = output[:-1].encode('ascii')
    return output 
def encode_payload(input_string):
    return_string = "&([ScriptBlock]::Create([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('" + base64.b64encode(input_string).decode('ascii') +"'))))"
    return return_string

print(encode_payload(create_string("Hello World!")))
