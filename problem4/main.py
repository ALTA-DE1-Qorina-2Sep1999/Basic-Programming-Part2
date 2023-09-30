def bayar(harga, discount):
    harga_int = int(harga)
    discount_int = int(discount)
    x = round(harga - (harga_int * discount_int / 100))
    return x

if __name__ == "__main__":
    print(bayar(370000, 15))