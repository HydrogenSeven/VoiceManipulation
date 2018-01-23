from pydub import AudioSegment


AA =
AE = AudioSegment.from_wav("AE.wav")
AH = AudioSegment.from_wav("AH.wav")
AO = AudioSegment.from_wav("AO.wav")
AW = AudioSegment.from_wav("AW.wav")
AY = AudioSegment.from_wav("AY.wav")
B = AudioSegment.from_wav("AB.wav")
CH = AudioSegment.from_wav("CH.wav")
D = AudioSegment.from_wav("D.wav")
DH = AudioSegment.from_wav("DH.wav")
EH = AudioSegment.from_wav("EH.wav")
ER = AudioSegment.from_wav("ER.wav")
EY = AudioSegment.from_wav("EY.wav")
F = AudioSegment.from_wav("F.wav")
G = AudioSegment.from_wav("G.wav")
HH = AudioSegment.from_wav("HH.wav")
IH = AudioSegment.from_wav("IH.wav")
IY = AudioSegment.from_wav("IY.wav")
JH = AudioSegment.from_wav("JH.wav")
K = AudioSegment.from_wav("K.wav")
L = AudioSegment.from_wav("L.wav")
M = AudioSegment.from_wav("M.wav")
N = AudioSegment.from_wav("N.wav")
NG = AudioSegment.from_wav("NG.wav")
OW = AudioSegment.from_wav("OW.wav")
OY = AudioSegment.from_wav("OY.wav")
P = AudioSegment.from_wav("P.wav")
R = AudioSegment.from_wav("R.wav")
S = AudioSegment.from_wav("S.wav")
SH = AudioSegment.from_wav("SH.wav")
T = AudioSegment.from_wav("T.wav")
TH = AudioSegment.from_wav("TH.wav")
UH = AudioSegment.from_wav("UH.wav")
UW = AudioSegment.from_wav("UW.wav")
V = AudioSegment.from_wav("V.wav")
W = AudioSegment.from_wav("W.wav")
Y = AudioSegment.from_wav("Y.wav")
Z = AudioSegment.from_wav("Z.wav")
ZH = AudioSegment.from_wav("ZH.wav")
FinalSegment = AudioSegment.from_wav("silence.wav")

CMUData = []
sentence = input('Type some text: ')
currword = ""
vowel=""
lastindex = 0
parsed = []

for i in range(sentence.length):
    if sentence[i:i+1] == " ":
        parsed.append(sentence[lastindex:i])
        lastindex = i+1

src = open("cmudict.dict")
for word in parsed:
    for line in src:
        if parsed in line:
            CMUData.append(line)
src.close()

for word in CMUData:
    for i in range(word.length, CMUData.length):
        if CMUData[i:i + 1] == " ":
            if CMUData[lastindex:i] == "AA":
                FinalSegment = FinalSegment+ AudioSegment.from_wav("AA.wav")
            elif CMUData[lastindex:i] == "AA":
                FinalSegment = FinalSegment+ AudioSegment.from_wav("AE.wav")
            elif CMUData[lastindex:i] == "AA":
                FinalSegment = FinalSegment + AudioSegment.from_wav("AE.wav")
            elif CMUData[lastindex:i] == "AA":
                FinalSegment = FinalSegment + AudioSegment.from_wav("AH.wav")
            elif CMUData[lastindex:i] == "AA":
                FinalSegment = FinalSegment + AudioSegment.from_wav("AO.wav")
                AW = AudioSegment.from_wav("AW.wav")
                AY = AudioSegment.from_wav("AY.wav")
                B = AudioSegment.from_wav("AB.wav")
                CH = AudioSegment.from_wav("CH.wav")
                D = AudioSegment.from_wav("D.wav")
                DH = AudioSegment.from_wav("DH.wav")
                EH = AudioSegment.from_wav("EH.wav")
                ER = AudioSegment.from_wav("ER.wav")
                EY = AudioSegment.from_wav("EY.wav")
                F = AudioSegment.from_wav("F.wav")
                G = AudioSegment.from_wav("G.wav")
                HH = AudioSegment.from_wav("HH.wav")
                IH = AudioSegment.from_wav("IH.wav")
                IY = AudioSegment.from_wav("IY.wav")
                JH = AudioSegment.from_wav("JH.wav")
                K = AudioSegment.from_wav("K.wav")
                L = AudioSegment.from_wav("L.wav")
                M = AudioSegment.from_wav("M.wav")
                N = AudioSegment.from_wav("N.wav")
                NG = AudioSegment.from_wav("NG.wav")
                OW = AudioSegment.from_wav("OW.wav")
                OY = AudioSegment.from_wav("OY.wav")
                P = AudioSegment.from_wav("P.wav")
                R = AudioSegment.from_wav("R.wav")
                S = AudioSegment.from_wav("S.wav")
                SH = AudioSegment.from_wav("SH.wav")
                T = AudioSegment.from_wav("T.wav")
                TH = AudioSegment.from_wav("TH.wav")
                UH = AudioSegment.from_wav("UH.wav")
                UW = AudioSegment.from_wav("UW.wav")
                V = AudioSegment.from_wav("V.wav")
                W = AudioSegment.from_wav("W.wav")
                Y = AudioSegment.from_wav("Y.wav")
                Z = AudioSegment.from_wav("Z.wav")
                ZH = AudioSegment.from_wav("ZH.wav")
            lastindex = i + 1
