import matplotlib.pyplot as plt

# CNN_SFT=[0.09113409678610995, 27.058588843738452, 0.11891392685629842, 27.94902105652013, 0.15999261174732166, 28.84019209456963, 0.20923531584780192, 29.870705578130767, 0.2771702992242334, 30.957813077207234,0.36379756187661616, 32.10151459179904,0.4664942741041743, 33.32944218692279,0.5903583302548946, 34.4752124122645, 0.7220908755079425, 35.538086442556335,0.8750646472109345, 36.5743627632065,1.027853712596971, 37.471739933505724]
# Swin_FRC=[0.12752124122644987, 28.421721462874025,0.201256002955301, 29.870262282970074,0.3017731806427779, 31.459179903952712,0.44769117103804945, 33.1895086811969,0.6497598817879571, 35.145179165127445,0.928961950498707, 37.10513483561138,1.261433321019579, 39.12360546730698]
# Swin_SFT=[0.11518285925378641, 27.1432582194311,0.1455855190247506, 28.006058367196154,0.18666420391577376, 28.897229405245653, 0.23309937199852232, 29.81647580347247,0.30103435537495377, 30.903583302548945,0.38758773550055403, 31.991725157000367, 0.49290727742888807, 33.192020687107494, 0.6195419283339489, 34.42127816771333, 0.7702622829700776, 35.762984854082006, 0.9475064647210933, 37.05060953084595, 0.7729220539342446, 35.763132619135575, 1.1244551163649799, 38.115995567048394]
# Swin_PT=[0.14879940893978566, 28.422903583302542,0.21987439970446981, 29.871296638345026,0.3203915773919468, 31.460214259327664,0.4663095677872183, 33.190543036571846,0.6548577761359438, 34.978795714813444,0.888622090875508, 36.769560398965645,1.1432951606944959, 38.2837089028444]
TIC_=[0.126467,28.3711,0.196665,29.8194,0.298524,31.4323,0.442246,33.1874]
TIC_x=[]
TIC_y=[]
for i in range(int(len(TIC_)/2)):
    TIC_x.append(TIC_[i*2])
    TIC_y.append(TIC_[i*2+1])
# CNN_SFTx=[]
# CNN_SFTy=[]
# for i in range(int(len(CNN_SFT)/2)):
#     CNN_SFTx.append(CNN_SFT[i*2])
#     CNN_SFTy.append(CNN_SFT[i*2+1])
# Swin_FRCx=[]
# Swin_FRCy=[]
# for i in range(int(len(Swin_FRC)/2)):
#     Swin_FRCx.append(Swin_FRC[i*2])
#     Swin_FRCy.append(Swin_FRC[i*2+1])
# Swin_SFTx=[]
# Swin_SFTy=[]
# for i in range(int(len(Swin_SFT)/2)):
#     Swin_SFTx.append(Swin_SFT[i*2])
#     Swin_SFTy.append(Swin_SFT[i*2+1])   
# Swin_PTx=[]
# Swin_PTy=[]
# for i in range(int(len(Swin_PT)/2)):
#     Swin_PTx.append(Swin_PT[i*2])
#     Swin_PTy.append(Swin_PT[i*2+1])   

# our_bpp = [0.116958, 0.192830, 0.292070, 0.427357]
# our_psnr = [28.1017, 29.8639, 31.5183, 33.4341]
our_bpp = [0.11695787, 0.19282959, 0.29271132, 0.43838471]
our_psnr = [28.10173035, 29.86388206, 31.5223999, 33.36501694]

TICwRSB_v2 = {
    "PSNR": [28.54899597, 29.99780273, 31.55869102, 33.21263504],
    "rate": [0.13489588, 0.20202897, 0.29631785, 0.42815387],
}


mlpv1y=[28.50658, 30.02062, 31.6345, 33.34571]
mlpv1x=[0.12746, 0.19663, 0.29771, 0.4466]

v1_ffn15 = {
    "PSNR": [28.51066971, 30.03843689, 31.6205101, 33.30992889],
    "rate": [0.12689517, 0.19860163, 0.29822487, 0.43896455],
}

fig1 = plt.figure(figsize=(9,9))
fig1.patch.set_facecolor('white')
fig1.patch.set_alpha(0.6)
ax=fig1.add_subplot(111)
ax.patch.set_facecolor('black')

# plt.plot(CNN_SFTx, CNN_SFTy, marker='^', label='CNN+SFT')
# plt.plot(Swin_FRCx, Swin_FRCy, marker="X", label='Swin+FRC')
# plt.plot(Swin_SFTx, Swin_SFTy, marker='s', label='Swin+SFT')
# plt.plot(Swin_PTx, Swin_PTy, marker='o', label='Swin+PT')
plt.plot(TIC_x, TIC_y,"mediumorchid", marker='D', label='TIC (anchor)')
plt.plot(our_bpp, our_psnr,"yellow", marker='*', label='TICwRSB_v1 (0.4621)',mfc="yellow",mec="yellow")
plt.plot(TICwRSB_v2['rate'], TICwRSB_v2['PSNR'], "lime",marker='o', label='TICwRSB_v2 (0.1714)',mfc="lime",mec="lime")
plt.plot(mlpv1x, mlpv1y,"red", marker='s', label='TICwRSBwMLP_v1 (0.5862)',mfc="red",mec="red")
plt.plot(v1_ffn15['rate'], v1_ffn15['PSNR'], marker='^', label='TICwRSB_v1_ffn1.5 (0.5727)', color="deepskyblue")
plt.legend()
plt.xlabel('Bit-rate(bpp)')
plt.ylabel('PSNR(dB)')
plt.grid(True)
plt.title("Testing on Kodak",fontsize=20)
plt.show()