reps = 5000000

def compare(a, b):
    str_a = ( "0"*16 + ( bin( a )[2:] ) )[-16:]
    str_b = ( "0"*16 + ( bin( b )[2:] ) )[-16:]
    return 1 if str_a == str_b else 0

def main():
    gen_A = 277
    f_a = 16807
    gen_B = 349
    f_b = 48271
    mod = 2147483647

    ctr = 0

    for i in xrange(reps):
        gen_A = (gen_A * f_a) % mod
        while gen_A % 4 != 0:
            gen_A = (gen_A * f_a) % mod

        gen_B = (gen_B * f_b) % mod
        while gen_B % 8 != 0:
            gen_B = (gen_B * f_b) % mod
        ctr += compare(gen_A, gen_B)

    print ctr

if __name__ == "__main__":
    main()