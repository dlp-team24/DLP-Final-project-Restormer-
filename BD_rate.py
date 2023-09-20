import numpy as np
import scipy

def BD_RATE(R1, PSNR1, R2, PSNR2, piecewise=0, lower_bound=0):
    lR1 = np.log(R1)
    lR2 = np.log(R2)

    # integration interval
    min_int = max(min(PSNR1), min(PSNR2), lower_bound)
    max_int = min(max(PSNR1), max(PSNR2))

    # find integral
    if piecewise == 0:
        # rate method
        p1 = np.polyfit(PSNR1, lR1, 3)
        p2 = np.polyfit(PSNR2, lR2, 3)

        p_int1 = np.polyint(p1)
        p_int2 = np.polyint(p2)

        int1 = np.polyval(p_int1, max_int) - np.polyval(p_int1, min_int)
        int2 = np.polyval(p_int2, max_int) - np.polyval(p_int2, min_int)
        
        # find avg diff
        avg_exp_diff = (int2-int1)/(max_int-min_int)
        avg_diff = (np.exp(avg_exp_diff)-1)*100
        return avg_diff, p1, p2
    else:
        samples, interval = np.linspace(
            min_int, max_int, num=100, retstep=True)

        v1 = scipy.interpolate.pchip_interpolate(
            np.sort(PSNR1), lR1[np.argsort(PSNR1)], samples)
        v2 = scipy.interpolate.pchip_interpolate(
            np.sort(PSNR2), lR2[np.argsort(PSNR2)], samples)
        # Calculate the integral using the trapezoid method on the samples.
        int1 = np.trapz(v1, dx=interval)
        int2 = np.trapz(v2, dx=interval)

        # find avg diff
        avg_exp_diff = (int2-int1)/(max_int-min_int)
        avg_diff = (np.exp(avg_exp_diff)-1)*100
        return avg_diff


if __name__ == "__main__":

    Anchor_PSNR = [28.37106133, 29.81934929, 31.43228149, 33.18738556]
    Anchor_RATE = [0.12646721, 0.19666508, 0.29852429, 0.4422456]

    YOURS_PSNR = [28.51066971, 30.03843689, 31.6205101, 33.30992889]
    YOURS_RATE = [0.12689517, 0.19860163, 0.29822487, 0.43896455]

    BR_RATE, _, _ = BD_RATE(Anchor_RATE, Anchor_PSNR,
                            YOURS_RATE, YOURS_PSNR,
                            piecewise=0,
                            lower_bound=0)
    
    print(BR_RATE)