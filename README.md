git clone --branch TICwRSBwMLP_v1 https://github.com/dlp-team24/DLP-Final-project-Restormer-

cd DLP-Final-project-Restormer-
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install -c anaconda pillow=9.2.0
conda install -c conda-forge shapely=1.7.1
pip3 install -U pip
pip3 install -e .
conda install -c conda-forge timm
conda install -c conda-forge tqdm
conda install -c conda-forge click
python3.9 -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

# complementary
conda install -c comet_ml comet_ml
conda install -c conda-forge einops
pip install thop
pip install ptflops

# original
pip install -U pip
pip install torch torchvision # have to match with the cuda version (we use 1.12.0+cu113)
pip install pillow==9.2.0
pip install shapely==1.7.1
pip install -e .
pip install timm tqdm click
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
