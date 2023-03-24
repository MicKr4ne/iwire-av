from sewar import full_ref as sw
from os import listdir
from os.path import isfile, join
import pandas as pd
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import psnr_hvsm as psnr

result_path = r".\metrics_example.csv"
#result_path_psnr = r"D:\DEV\Thesis\Denoising\mixed_syn_rain2_psnr.csv"

# df = pd.DataFrame(columns=['Image', 'Restormer_UQI', 'Restormer_SSIM', 'Rescan_UQI', 'Rescan_SSIM'])

def psnr_hvsm_rgb(img1, img2):
    if img1.ndim == 3:
        psnr_1 = psnr.psnr_hvsm(img1[:,:,0]/255, img2[:,:,0]/255);
        psnr_2 = psnr.psnr_hvsm(img1[:,:,1]/255, img2[:,:,1]/255);
        psnr_3 = psnr.psnr_hvsm(img1[:,:,2]/255, img2[:,:,2]/255);
        return ((psnr_1 + psnr_2 + psnr_3) / 3)
    else:
        return psnr.psnr_hvsm(img1/255., img2/255.)
    
def calc_benchmark():
    if(isfile(result_path)):
        try:
            df = pd.read_csv(result_path, index_col=0)
        except:
            print('Error reading result file')
            exit()
    else:
        reference_path = r".\Denoiser\Benchmark\metrics_examples\clean"
        restormer_path = r".\Denoiser\Benchmark\metrics_examples\rain"
        rescan_path = r".\Denoiser\Benchmark\metrics_examples\rain"
        ext = '.png'

        images = [f.replace(ext, '') for f in listdir(reference_path) if f.endswith(ext) and isfile(join(reference_path, f))]

        scores = []
        scores_psnr = []
        pics = []

        for img in images:
            ref = np.asarray(Image.open(join(reference_path, img + ext)))
            restormer = np.asarray(Image.open(join(restormer_path, img + ext)))
            rescan = np.asarray(Image.open(join(rescan_path, img + ext)))

            #restormer_uqi = sw.uqi(ref, restormer)
            restormer_ssim = sw.ssim(ref, restormer)
            restormer_psnr = psnr_hvsm_rgb(ref, restormer)

            #rescan_uqi = sw.uqi(ref, rescan)
            rescan_ssim = sw.ssim(ref, rescan)
            rescan_psnr = psnr_hvsm_rgb(ref, rescan)
            
            scores.append([restormer_ssim[0], rescan_ssim[0], restormer_psnr, rescan_psnr])
            #scores_psnr.append([restormer_psnr, rescan_psnr])
            pics.append(img+ext)

        df = pd.DataFrame(scores, columns=['Restormer_SSIM', 'Rescan_SSIM', 'Restormer_PSNR', 'Rescan_PSNR'], index=pics)
        #df_psnr = pd.DataFrame(scores_psnr, columns=['Restormer_PSNR', 'Rescan_PSNR'], index=pics)
        df.to_csv(result_path, index=True)
        #df_psnr.to_csv(result_path_psnr, index=True)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    bp1 = df.boxplot(column=['Restormer_SSIM', 'Rescan_SSIM'], ax=ax[0])
    bp2 = df.boxplot(column=['Restormer_PSNR', 'Rescan_PSNR'], ax=ax[1])
    
    fig.suptitle('Benchmark results for mixed_syn_rain2 dataset')
    bp1.set_title('SSIM scores')
    bp1.set_ylabel('Score')
    bp2.set_title('PSNR-HVS-M scores')
    bp2.set_ylabel('Score')
    # boxplot.set_ylabel('Score')
    # boxplot.set_xlabel('Denoiser')
    # boxplot.set_xticklabels(['Restormer UQI', 'Restormer SSIM', 'Restormer PSNR', 'Rescan UQI', 'Rescan SSIM', 'Rescan PSNR'])
    plt.show()

def main():
    calc_benchmark()
    exit()

if __name__ == "__main__":
    main()