from pydub import AudioSegment

FinalSegment = AudioSegment.from_wav("pause.wav")

CMUData = []
sentence = input('Type some text: ')
currword = ""
vowel = ""
lastindex = 0
parsed = []

for i in range(sentence.length):
    if sentence[i:i+1] == " ":
        parsed.append(sentence[lastindex:i])
        lastindex = i+1

src = open("cmudict.dict")
for word in parsed:
    for line in src:
        if word in line:
            CMUData.append(line)
src.close()

for word in CMUData:
    i = word.length
    while i in range(word.length, CMUData.length):
        if CMUData[i:i + 1] == " ":
            if CMUData[lastindex:i] == "AA":
                FinalSegment = FinalSegment + AudioSegment.from_wav("AA.wav")
            elif CMUData[lastindex:i] == "AE":
                FinalSegment = FinalSegment+ AudioSegment.from_wav("AE.wav")
            elif CMUData[lastindex:i] == "AH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("AH.wav")
            elif CMUData[lastindex:i] == "AO":
                FinalSegment = FinalSegment + AudioSegment.from_wav("AO.wav")
            elif CMUData[lastindex:i] == "AW":
                FinalSegment = FinalSegment + AudioSegment.from_wav("AW.wav")
            elif CMUData[lastindex:i] == "AY":
                FinalSegment = FinalSegment + AudioSegment.from_wav("AY.wav")
            elif CMUData[lastindex:i] == "AB":
                FinalSegment = FinalSegment + AudioSegment.from_wav("AB.wav")
            elif CMUData[lastindex:i] == "CH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("CH.wav")
            elif CMUData[lastindex:i] == "D":
                FinalSegment = FinalSegment + AudioSegment.from_wav("D.wav")
            elif CMUData[lastindex:i] == "DH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("DH.wav")
            elif CMUData[lastindex:i] == "EH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("EH.wav")
            elif CMUData[lastindex:i] == "ER":
                FinalSegment = FinalSegment + AudioSegment.from_wav("ER.wav")
            elif CMUData[lastindex:i] == "EY":
                FinalSegment = FinalSegment + AudioSegment.from_wav("EY.wav")
            elif CMUData[lastindex:i] == "F":
                FinalSegment = FinalSegment + AudioSegment.from_wav("F.wav")
            elif CMUData[lastindex:i] == "G":
                FinalSegment = FinalSegment + AudioSegment.from_wav("G.wav")
            elif CMUData[lastindex:i] == "HH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("HH.wav")
            elif CMUData[lastindex:i] == "IH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("IH.wav")
            elif CMUData[lastindex:i] == "IY":
                FinalSegment = FinalSegment + AudioSegment.from_wav("IY.wav")
            elif CMUData[lastindex:i] == "JH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("JH.wav")
            elif CMUData[lastindex:i] == "K":
                FinalSegment = FinalSegment + AudioSegment.from_wav("K.wav")
            elif CMUData[lastindex:i] == "L":
                FinalSegment = FinalSegment + AudioSegment.from_wav("L.wav")
            elif CMUData[lastindex:i] == "M":
                FinalSegment = FinalSegment + AudioSegment.from_wav("M.wav")
            elif CMUData[lastindex:i] == "N":
                FinalSegment = FinalSegment + AudioSegment.from_wav("N.wav")
            elif CMUData[lastindex:i] == "NG":
                FinalSegment = FinalSegment + AudioSegment.from_wav("NG.wav")
            elif CMUData[lastindex:i] == "OW":
                FinalSegment = FinalSegment + AudioSegment.from_wav("OW.wav")
            elif CMUData[lastindex:i] == "OY":
                FinalSegment = FinalSegment + AudioSegment.from_wav("OY.wav")
            elif CMUData[lastindex:i] == "P":
                FinalSegment = FinalSegment + AudioSegment.from_wav("P.wav")
            elif CMUData[lastindex:i] == "R":
                FinalSegment = FinalSegment + AudioSegment.from_wav("R.wav")
            elif CMUData[lastindex:i] == "S":
                FinalSegment = FinalSegment + AudioSegment.from_wav("S.wav")
            elif CMUData[lastindex:i] == "SH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("SH.wav")
            elif CMUData[lastindex:i] == "T":
                FinalSegment = FinalSegment + AudioSegment.from_wav("T.wav")
            elif CMUData[lastindex:i] == "TH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("TH.wav")
            elif CMUData[lastindex:i] == "UH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("UH.wav")
            elif CMUData[lastindex:i] == "UW":
                FinalSegment = FinalSegment + AudioSegment.from_wav("UW.wav")
            elif CMUData[lastindex:i] == "V":
                FinalSegment = FinalSegment + AudioSegment.from_wav("V.wav")
            elif CMUData[lastindex:i] == "W":
                FinalSegment = FinalSegment + AudioSegment.from_wav("W.wav")
            elif CMUData[lastindex:i] == "Y":
                FinalSegment = FinalSegment + AudioSegment.from_wav("Y.wav")
            elif CMUData[lastindex:i] == "Z":
                FinalSegment = FinalSegment + AudioSegment.from_wav("Z.wav")
            elif CMUData[lastindex:i] == "ZH":
                FinalSegment = FinalSegment + AudioSegment.from_wav("ZH.wav")
            else:
                break
            lastindex = i + 1
            i += 1
