import math
from hashlib import sha256
from sympy.ntheory import factorint
from Crypto.Util.number import long_to_bytes
import numpy as np 
from gmpy2 import iroot

# 1
# print(pow(101,17,22663))

# 2
e = 65537
p = 17
q = 23
n = p * q
# print(pow(12,e,n))

# 3
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
# print((p-1)*(q-1))

# 4
def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_euclidean_algorithm(b % a, a)
        return g, x - (b // a) * y, y
    
def modular_inverse(e, t):
    g, x, y = extended_euclidean_algorithm(e, t)

    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % t

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
n = p*q
t = (p-1)*(q-1)
# print(n)
# print(modular_inverse(e,t)) # d

# 5
n = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932
d = modular_inverse(e, t)
# print(pow(c,d,n))

# 6
N = 15216583654836731327639981224133918855895948374072384050848479908982286890731769486609085918857664046075375253168955058743185664390273058074450390236774324903305663479046566232967297765731625328029814055635316002591227570271271445226094919864475407884459980489638001092788574811554149774028950310695112688723853763743238753349782508121985338746755237819373178699343135091783992299561827389745132880022259873387524273298850340648779897909381979714026837172003953221052431217940632552930880000919436507245150726543040714721553361063311954285289857582079880295199632757829525723874753306371990452491305564061051059885803
d = 11175901210643014262548222473449533091378848269490518850474399681690547281665059317155831692300453197335735728459259392366823302405685389586883670043744683993709123180805154631088513521456979317628012721881537154107239389466063136007337120599915456659758559300673444689263854921332185562706707573660658164991098457874495054854491474065039621922972671588299315846306069845169959451250821044417886630346229021305410340100401530146135418806544340908355106582089082980533651095594192031411679866134256418292249592135441145384466261279428795408721990564658703903787956958168449841491667690491585550160457893350536334242689
a_string = b'crypto{Immut4ble_m3ssag1ng}'
hashed_string = int(sha256(a_string).hexdigest(), 16)
# print(hashed_string)
sign = pow(hashed_string, d, N)
# print(hex(sign))

# 7
n = 510143758735509025530880200653196460532653147
# for i in range(2,n + 1):
#     if n % i == 0:
#         count = 1
#         for j in range(2,(i//2 + 1)):
#             if(i % j == 0):
#                 count = 0
#                 break
#         if(count == 1):
#             print(i)
# pakai http://factordb.com/index.php aja # 19704762736204164635843

# 8
n = 171731371218065444125482536302245915415603318380280392385291836472299752747934607246477508507827284075763910264995326010251268493630501989810855418416643352631102434317900028697993224868629935657273062472544675693365930943308086634291936846505861203914449338007760990051788980485462592823446469606824421932591                                                                  
e = 65537
ct = 161367550346730604451454756189028938964941280347662098798775466019463375610700074840105776873791605070092554650190486030367121011578171525759600774739890458414593857709994072516290998135846956596662071379067305011746842247628316996977338024343628757374524136260758515864509435302781735938531030576289086798942  
t = n - 1
d = modular_inverse(e, t)
# print(long_to_bytes(pow(ct, d, n)))

# 9
n = 580642391898843192929563856870897799650883152718761762932292482252152591279871421569162037190419036435041797739880389529593674485555792234900969402019055601781662044515999210032698275981631376651117318677368742867687180140048715627160641771118040372573575479330830092989800730105573700557717146251860588802509310534792310748898504394966263819959963273509119791037525504422606634640173277598774814099540555569257179715908642917355365791447508751401889724095964924513196281345665480688029639999472649549163147599540142367575413885729653166517595719991872223011969856259344396899748662101941230745601719730556631637
e = 65537
ct = 320721490534624434149993723527322977960556510750628354856260732098109692581338409999983376131354918370047625150454728718467998870322344980985635149656977787964380651868131740312053755501594999166365821315043312308622388016666802478485476059625888033017198083472976011719998333985531756978678758897472845358167730221506573817798467100023754709109274265835201757369829744113233607359526441007577850111228850004361838028842815813724076511058179239339760639518034583306154826603816927757236549096339501503316601078891287408682099750164720032975016814187899399273719181407940397071512493967454225665490162619270814464
t = 1
found_prime = [9282105380008121879 , 9303850685953812323 , 9389357739583927789 , 10336650220878499841 , 10638241655447339831 , 11282698189561966721 , 11328768673634243077 , 11403460639036243901 , 11473665579512371723 , 11492065299277279799 , 11530534813954192171 , 11665347949879312361 , 12132158321859677597 , 12834461276877415051 , 12955403765595949597 , 12973972336777979701 , 13099895578757581201 , 13572286589428162097 , 14100640260554622013 , 14178869592193599187 , 14278240802299816541 , 14523070016044624039 , 14963354250199553339 , 15364597561881860737 , 15669758663523555763 , 15824122791679574573 , 15998365463074268941 , 16656402470578844539 , 16898740504023346457 , 17138336856793050757 , 17174065872156629921 , 17281246625998849649]
# pakai http://factordb.com/index.php aja
for x in found_prime:
    t *= (x-1)
d = modular_inverse(e, t)
# print(long_to_bytes(pow(ct, d, n)))

# 10
n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767                                                                  
e = 1
ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
# print(long_to_bytes(ct))

# 11
a = 27
n = 17258212916191948536348548470938004244269544560039009244721959293554822498047075403658429865201816363311805874117705688359853941515579440852166618074161313773416434156467811969628473425365608002907061241714688204565170146117869742910273064909154666642642308154422770994836108669814632309362483307560217924183202838588431342622551598499747369771295105890359290073146330677383341121242366368309126850094371525078749496850520075015636716490087482193603562501577348571256210991732071282478547626856068209192987351212490642903450263288650415552403935705444809043563866466823492258216747445926536608548665086042098252335883
e = 3
ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957
print(iroot(ct, 3))
print(long_to_bytes(iroot(ct, 3)[0]))