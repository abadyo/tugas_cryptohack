#!/usr/bin/env python3

import sys
import base64
from Crypto.Util.number import *
from pwn import *
from binascii import unhexlify
import string

# ubah hex ke byte/ascii lalu ke string
def ubah_hex(name) :
    flag = unhexlify(name)
    flag = flag.decode("ascii")
    print(flag)

# ubah hex ke base64 ke byte/ascii lalu ke string
def ubah_h_b64(name) :
    flag = unhexlify(name)
    flag = base64.b64encode(flag)
    flag = flag.decode("ascii")
    print(flag)

# ubah bade10 to byte/ascii ke string
def ubah_b10(name) :
    flag = long_to_bytes(name)
    # flag = unhexlify(name)
    # flag = base64.b64encode(flag)
    flag = flag.decode("ascii")
    print(flag)

# 1
# sudah jelas

# 2
# sudah jelas

# 3
# ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
# print("Here is your flag:")
# print("".join(chr(o ^ 0x32) for o in ords))

# 4
# ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
# print("Here is your flag:")
# print("".join(chr(o) for o in ords))

# 5
# ubah_hex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d")

# 5
# ubah_h_b64("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")

# 6
# ubah_b10(11515195063862318899931685488813747395775516287289682636499965282714637259206269)

# 7
# print(xor("label", 13))

# 8
# KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
# KEY23 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
# OTH = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
# FLAG = xor(OTH, KEY1, KEY23)
# print(FLAG)

# 9
# string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
# hasil = [i for i in bytes.fromhex(string)]
# for j in range(256) :
#     mungkin = [i ^ j for i in hasil]
#     mungkin_hasil = "".join(chr(o) for o in mungkin)
#     if mungkin_hasil.startswith("crypto") :
#         flag = mungkin_hasil
#         break
#
# print(flag)

#10
# string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
# hasil = [i for i in bytes.fromhex(string)]
# print("".join(chr(o) for o in hasil))

# 11
# mes = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
# part_key = "crypto{"
# result = xor(mes[:7], part_key)
# result = result.decode("ascii")
# result = result + "y"
# # print(result)
# kunci = bytes(result, "utf-8")
# hasil = xor(mes, kunci)
# print(hasil.decode("ascii"))


# kEY ===========================================================
# Sudah jelas
# Sudah jelas
# crypto{z3n_0f_pyth0n}
# crypto{ASCII_pr1nt4bl3}
# crypto{You_will_be_working_with_hex_strings_a_lot}
# crypto/Base+64+Encoding+is+Web+Safe/
# crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
# aloha
# crypto{x0r_i5_ass0c1at1v3}
# crypto{0x10_15_my_f4v0ur173_by7e}
# crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}


