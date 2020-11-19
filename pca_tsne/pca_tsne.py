import os
import numpy as np
from PIL import Image


def load_images(img_dir, num_imgs):
	img_files = [os.path.join(img_dir, f) for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]
	img_files.sort()
	img_files = img_files[:num_imgs]
	return img_files


def img_to_tsv(imgs):
	tsv_items = list()
	for img in imgs:
		tsv_vals = np.asarray(Image.open(img)).flatten().tolist()
		tsv_str_vals = [str(tsv_val) for tsv_val in tsv_vals]
		tsv_items.append('\t'.join(tsv_str_vals))
	return tsv_items


def write_to_tsv(tsv_items, tsv_img_path):
	tsv_file = open(tsv_img_path, 'a')
	for tsv_item in tsv_items:
		tsv_file.write(tsv_item + '\n')


def generate_img_tsv(dirs, tsv_img_path, num_data_pts):
	for directory in dirs:
		img_files = load_images(directory, num_data_pts)
		tsv_items = img_to_tsv(img_files)
		write_to_tsv(tsv_items, tsv_img_path)


def generate_tsv_labels(tsv_label_path, num_data_pts):
	labels = ['healthy', 'apple_scab', 'black_rot', 'cedar_apple_rust']
	tsv_file = open(tsv_label_path, 'a')
	for label in labels:
		for idx in range(num_data_pts):
			tsv_file.write(label + '\n')


if __name__ == '__main__':
	num_data_pts = 100

	healthy_dir = '../data/PlantVillage-Dataset/raw/color/Apple___healthy'
	apple_scab_dir = '../masked_nst/output/Apple___Apple_scab'
	black_rot_dir = '../masked_nst/output/Apple___Black_rot'
	cedar_apple_rust_dir = '../masked_nst/output/Apple___Cedar_apple_rust'
	dirs = [healthy_dir, apple_scab_dir, black_rot_dir, cedar_apple_rust_dir]

	tsv_img_path = 'output/nst_imgs.tsv'
	tsv_label_path = 'output/nst_labels.tsv'

	generate_img_tsv(dirs, tsv_img_path, num_data_pts)
	generate_tsv_labels(tsv_label_path, num_data_pts)
