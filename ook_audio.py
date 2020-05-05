from pydub import AudioSegment

bit_0 = AudioSegment.from_wav("bit_0.wav")
bit_1 = AudioSegment.from_wav("bit_1.wav")
combinedbits = AudioSegment.from_wav("bit_0.wav")

binary = "0000000000100000000110000000101000000011100000010010000001011000000110100000011110000010001000001001100000101010000010111000001100100000110110000011101000001111100001000010001100001001010000100111000010100100001010110000101101000010111100001100010000110011000011010100001101110000111001000011101100001111010000111111000100010100010001110001001001000100101100010011010001001111000101001100010101010001010111000101100100010110110001011101000101111100011000110010100011001110001101001000110101100011011010001101111000111001100011101010001110111000111100100011110110001111101000111111100100100110010010101001001011100100110110010011101001001111100101001010011100101010110010101101001010111100101100110010110101001011011100101110110010111101001011111100110011010011001111001101010100110101110011011011001101110100110111110011100111010110011101101001110111100111101010011110111001111101100111111010011111111010101010111010101101101010111110101101011011110101110111010111101101011111110110110111011011111101110111110111101111111111"
i = 0

while i < len(binary):
    if binary[i] == '0':
        combinedbits += bit_0
        i += 1
    else:
        combinedbits += bit_1
        i += 1

print("Completed OOK Merge.")

combinedbits.export("test.wav", format="wav")