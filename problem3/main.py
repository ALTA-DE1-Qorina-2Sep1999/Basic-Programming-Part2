def luas_permukaan_tabung(r, T):
    luas = (2 * 3.14 * r * r) + (2 * 3.14 * r * T)
    return luas

if __name__ == "__main__":
    print(luas_permukaan_tabung(4, 20))