def ksa(key: bytes) -> list[int]:
    """
    密钥调度算法 (KSA)，与我们之前使用的一样。
    """
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) & 0xFF
        temp = S[i]
        S[i] = S[j]
        S[j] = temp ^ 0xad
    return S

def encrypt(S: list[int], plaintext: bytes) -> bytes:
    """
    加密函数，执行 C = P % K 的操作。
    """
    i = 0
    j = 0
    ciphertext = bytearray()

    for p_byte in plaintext:
        # 生成密钥流字节
        i = (i + 1) & 0xFF
        j = (j + S[i]) & 0xFF
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) & 0xFF
        keystream_byte = S[t]

        # 处理密钥流字节为0的特殊情况
        if keystream_byte == 0:
            # 真实情况下，P % 0 会导致程序崩溃。
            # 这里我们假设加密结果为0，以避免脚本中断。
            cipher_byte = 0
        else:
            # 执行加密操作
            cipher_byte = p_byte % keystream_byte
        
        ciphertext.append(cipher_byte)

    return bytes(ciphertext)

if __name__ == "__main__":
    # 使用与之前相同的密钥
    key = b"Y0u_Can't_F1nd_Me!"
    
    # 准备35个'b'作为明文 (字母'b'的ASCII码是98)
    plaintext = b'nepctf{ddddddddddddddddddddddddddd}'
    
    print(f"🔑 使用密钥: {key.decode()}")
    print(f"明文 (前10字节): {plaintext[:10]}...")
    print(f"明文长度: {len(plaintext)} 字节")

    # 1. 初始化S-盒
    S_box = ksa(key)
    
    # 2. 加密明文
    #    传递 S_box 的副本，因为加密过程会修改它
    encrypted_data = encrypt(S_box.copy(), plaintext)

    print("\n✅ 加密完成!")
    # 将加密后的字节串以十六进制(hex)格式输出，这是查看密文的标准方式
    print(f"密文 (hex): {encrypted_data.hex()}")

#5059a2942e 8e 5c95 79 16 e5 36 60 c7 e8 063378 f0d0 36 c873 1b 6540b5d4e89c65f4ba 62d0
#5059a2942e 2b 5c95 09 16 01 36 14 c7 3a 063378 4d06 36 071c 1b 00131b005500651a58 62d0


#4e65704354467b642c640464186464646464646464640d1b000a17006416646402647d

#4e65704354467b642c640464186464646464646464640d1b000a17006416646402647d