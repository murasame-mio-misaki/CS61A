S_BOX_FROM_DUMP = [
   0x35, 0xE9, 0x55, 0xD7, 0x6E, 0x5F, 0x47, 0x3D, 0xCC, 0x9D, 
  0xD2, 0x6B, 0xEB, 0x52, 0x97, 0x19, 0xD5, 0xC5, 0x80, 0x0B, 
  0x64, 0x2B, 0xCD, 0xF6, 0x95, 0xB1, 0x31, 0x34, 0x31, 0x08, 
  0x43, 0xBE, 0x8C, 0x86, 0x16, 0x70, 0xFE, 0x36, 0x11, 0xFD, 
  0xA7, 0xB9, 0x55, 0xA0, 0x4E, 0x40, 0xDA, 0x08, 0x1F, 0x4B, 
  0xA2, 0x4C, 0x50, 0x47, 0x15, 0xCE, 0xC3, 0x8D, 0xB5, 0x00, 
  0xFB, 0x43, 0x07, 0x32, 0x1D, 0x5E, 0xDC, 0x4D, 0xF5, 0x19, 
  0x98, 0x0F, 0x8D, 0xB0, 0xEC, 0x48, 0xAB, 0x92, 0x15, 0xD6, 
  0xDA, 0x6F, 0x1B, 0x85, 0x45, 0x04, 0x84, 0x8A, 0x5B, 0x0E, 
  0x66, 0xB6, 0xA0, 0x1E, 0x2A, 0x6D, 0x3C, 0x8F, 0x26, 0xC7, 
  0x90, 0x89, 0xDC, 0x8B, 0x87, 0xE0, 0x82, 0x57, 0xCE, 0x66, 
  0x13, 0x4B, 0x49, 0x6A, 0x1F, 0x1A, 0x09, 0x32, 0x8E, 0x36, 
  0xAD, 0x65, 0x58, 0xBC, 0xD4, 0x5E, 0xD0, 0x2C, 0x68, 0xBF, 
  0xBD, 0xA1, 0x45, 0x17, 0x16, 0x05, 0x9A, 0x4C, 0xFC, 0x0B, 
  0xB9, 0x49, 0xDB, 0x6F, 0x37, 0x27, 0x30, 0x51, 0x69, 0x61, 
  0xD5, 0x75, 0xD3, 0x74, 0xEB, 0x4F, 0x23, 0x54, 0x0C, 0x1C, 
  0x70, 0xDE, 0xE9, 0x7F, 0x62, 0x25, 0xF4, 0x84, 0x3E, 0x2F, 
  0x76, 0x03, 0x7A, 0x79, 0x5F, 0xCA, 0x01, 0x07, 0x41, 0x57, 
  0xC4, 0x97, 0x04, 0x33, 0x6C, 0x42, 0x4E, 0x38, 0x0E, 0xE7, 
  0x93, 0xE2, 0x64, 0x3F, 0xB7, 0x5C, 0x5D, 0xE5, 0x59, 0x8C, 
  0x6D, 0xED, 0x34, 0x85, 0xDF, 0x62, 0x91, 0x09, 0x94, 0xB3, 
  0x05, 0x2E, 0x18, 0xD8, 0xBF, 0x7E, 0xAC, 0xAE, 0x9E, 0xD6, 
  0xC1, 0x3B, 0x54, 0x72, 0x22, 0x5C, 0xE7, 0xD0, 0x6B, 0x25, 
  0xFE, 0xFF, 0xFB, 0x3B, 0x2D, 0x7C, 0x65, 0x5A, 0xCD, 0xF0, 
  0xBD, 0x67, 0x74, 0x17, 0x02, 0x42, 0x2C, 0x2E, 0x5A, 0xA7, 
  0xD1, 0x73, 0x94, 0xAF, 0x89, 0x06
]

def decrypt_new_algorithm(initial_s_box: list[int], ciphertext: bytes) -> bytes:
    """
    根据新的加密逻辑实现解密。
    
    Args:
        initial_s_box: 加密开始前的256字节S盒状态。
        ciphertext: 需要解密的密文。
        
    Returns:
        解密后的明文字节串。
    """
    # 验证S盒的有效性
    if not initial_s_box or len(initial_s_box) != 256:
        print("错误：S盒数据无效或不完整！请在 S_BOX_FROM_DUMP 列表中填入256个字节。")
        return b""

    # 创建S盒的可变副本，解密过程会修改它
    S = initial_s_box.copy()
    
    # 初始化伪随机生成算法(PRGA)的状态变量
    i_prga = 0
    j_prga = 0
    
    plaintext = bytearray()

    # 遍历密文的每一个字节，i 是当前字节的索引
    for i, c_byte in enumerate(ciphertext):
        # --- 1. 生成与加密时完全相同的密钥流字节 ---
        
        # v9 = (v9 + 1) % 256;
        i_prga = (i_prga + 1) & 0xFF
        
        # v8 = (v8 + v9 * *(unsigned __int8 *)(v9 + a1)) % 256;
        j_prga = (j_prga + i_prga * S[i_prga]) & 0xFF
        
        # swap(S[v9], S[v8])
        S[i_prga], S[j_prga] = S[j_prga], S[i_prga]
        
        # v4 = (*(S[v8]) + *(S[v9])) % 256;
        t = (S[i_prga] + S[j_prga]) & 0xFF
        keystream_byte = S[t]
        
        # --- 2. 应用与加密操作相反的解密逻辑 ---
        
        # 加密:
        # if i is even: C = P - K
        # if i is odd:  C = P + K
        
        # 解密 (逆运算):
        # if i is even: P = C + K
        # if i is odd:  P = C - K
        
        if i % 2 == 0:  # 偶数索引
            p_byte = (c_byte + keystream_byte) & 0xFF
        else:  # 奇数索引
            p_byte = (c_byte - keystream_byte) & 0xFF
            
        plaintext.append(p_byte)
        
    return bytes(plaintext)
v7_signed = [
        ord('P'), ord('Y'), -94, -108, 46, -114, 92, -107, 121, 22, -27, 54, 96,
        -57, -24, 6, 51, 120, -16, -48, 54, -56, 115, 27, 101, 64, -75, -44,
        -24, -100, 101, -12, -70, 98, -48
    ]
ciphertext = bytes([c & 0xFF for c in v7_signed])
flag = decrypt_new_algorithm(S_BOX_FROM_DUMP, ciphertext)
print(flag)
