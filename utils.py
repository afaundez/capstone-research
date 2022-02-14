import glob
import re
from skimage import io

EOBROWSER_BASENAME_PATTERN = r'2.*_Sentinel-2_L2A_([^_]+)(?:_.*)*.ti[f]+$'
# DEFAULT_COLORMAPS = ['Blues_r', 'Greens_r', 'Reds_r', 'hot', 'PRGn', 'BuGn', None]
# DEFAULT_COLORMAPS = ['Blues_r', 'Greens_r', 'Reds_r', 'gist_earth', 'YlGn', 'terrain', None]
IMAGE_CROP_SIZE = 400

def load(filename_pattern, basename_pattern=EOBROWSER_BASENAME_PATTERN):
  filenames = glob.glob(filename_pattern)
  pattern = re.compile(basename_pattern)
  names = [ re.split(pattern, filename)[1] for filename in filenames ]
  return {
    name: io.imread(filename)[0:IMAGE_CROP_SIZE,0:IMAGE_CROP_SIZE].astype(float)
    for name, filename in sorted(zip(names, filenames), key=lambda x: x[0])
  }
