uint32_t reverse_bits(uint32_t n) {
    uint32_t res = 0;
     for (size_t i = 0; i < 16; i++) {
         uint32_t bit = (n >> i) & 1;
         uint32_t bit2 = (n >> i+16) & 1;
         res |= (bit << (31 - i)) | (bii2 << (15 - i)); 
     }
     return res;
}