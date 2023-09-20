import matplotlib.pyplot as plt
from BD_rate import BD_RATE

TIC = {
    "PSNR": [28.37106133, 29.81934929, 31.43228149, 33.18738556],
    "rate": [0.12646721, 0.19666508, 0.29852429, 0.4422456],
}

TICwRSB_v1 = {
    "PSNR": [28.10173035, 29.86388206, 31.5223999, 33.36501694],
    "rate": [0.11695787, 0.19282959, 0.29271132, 0.43838471],
}

TICwRSB_v2 = {
    "PSNR": [28.54899597, 29.99780273, 31.55869102, 33.21263504],
    "rate": [0.13489588, 0.20202897, 0.29631785, 0.42815387],
}

wMLP_v1 = {
    "PSNR": [28.50658, 30.02062, 31.6345, 33.34571],
    "rate": [0.12746, 0.19663, 0.29771, 0.4466],
}

v1_ffn15 = {
    "PSNR": [28.51066971, 30.03843689, 31.6205101, 33.30992889],
    "rate": [0.12689517, 0.19860163, 0.29822487, 0.43896455],
}

BD_rate = {
    "TIC": "anchor",
    "TICwRSB_v1": BD_RATE(TIC['rate'], TIC['PSNR'], TICwRSB_v1['rate'], TICwRSB_v1['PSNR'], piecewise=0, lower_bound=0)[0],
    "TICwRSB_v2": BD_RATE(TIC['rate'], TIC['PSNR'], TICwRSB_v2['rate'], TICwRSB_v2['PSNR'], piecewise=0, lower_bound=0)[0],
    "wMLP_v1": BD_RATE(TIC['rate'], TIC['PSNR'], wMLP_v1['rate'], wMLP_v1['PSNR'], piecewise=0, lower_bound=0)[0],
    "v1_ffn15": BD_RATE(TIC['rate'], TIC['PSNR'], v1_ffn15['rate'], v1_ffn15['PSNR'], piecewise=0, lower_bound=0)[0],
}


plt.figure()
plt.plot(TIC["rate"], TIC["PSNR"], label=f"TIC ({BD_rate['TIC']})", marker='o', color="blue")
plt.plot(TICwRSB_v1["rate"], TICwRSB_v1["PSNR"], label=f"TICwRSB_v1 ({BD_rate['TICwRSB_v1']:.3f})", marker='v', color="#FFBE00")
plt.plot(TICwRSB_v2["rate"], TICwRSB_v2["PSNR"], label=f"TICwRSB_v2 ({BD_rate['TICwRSB_v2']:.3f})", marker='s', color="lime")
plt.plot(wMLP_v1["rate"], wMLP_v1["PSNR"], label=f"TICwRSBwMLP_v1 ({BD_rate['wMLP_v1']:.3f})", marker='^', color="red")
plt.plot(v1_ffn15["rate"], v1_ffn15["PSNR"], label=f"TICwRSB_v1_ffn1.5 ({BD_rate['v1_ffn15']:.3f})", marker='*', color="turquoise")

plt.title("TIC with Restormer Block")
plt.xlabel("Bit-rate (bpp)")
plt.ylabel("PSNR (dB)")
plt.grid()
plt.legend()
plt.savefig("./v2.png")
plt.show()

print(BD_rate)