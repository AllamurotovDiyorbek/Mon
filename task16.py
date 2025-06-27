a=100000

if a>18:
    print(f"Yakuniy narx: {a} so'm (100% chegirma qo'llanildi)")
elif a<=18:
    print(f"Yakuniy narx: {a+a/100*30} so'm (50% chegirma qo'llanildi)")
elif a<=8:
    print(f"Yakuniy narx: {a+a/100*50} so'm (50% chegirma qo'llanildi)")