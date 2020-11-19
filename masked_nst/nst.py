import os


def load_healthy_images(content_leaf_dir, content_mask_dir):
	content_files = [f for f in os.listdir(content_leaf_dir) if os.path.isfile(os.path.join(content_leaf_dir, f)) and os.path.splitext(f)[1]=='.JPG']
	content_files.sort()
	healthy_files = list()
	for content_file in content_files:
		leaf_file = os.path.join(content_leaf_dir, content_file)
		mask_file = os.path.join(content_mask_dir, os.path.splitext(content_file)[0] + '_final_masked.jpg')
		healthy_files.append((leaf_file, mask_file))
	return healthy_files


def run_nst(content_files, style_leaf_path, style_mask_path, output_dir):
	for content_leaf, content_mask in content_files:
		print('Transfering style to:', os.path.basename(content_leaf))
		output_file = os.path.splitext(os.path.basename(content_leaf))[0] + '_nst.jpg'
		command = "python3 stylize.py --mask_n_colors=1 --content_img='"+content_leaf+"' --target_mask='"+content_mask+"' --style_img='"+style_leaf_path+"' --style_mask='"+style_mask_path+ \
		"' --optimizer='lbfgs' --iteration=50 --output_dir='"+output_dir+"' --output_file='"+output_file+"'"
		os.system(command)


if __name__ == '__main__':
	diseased_leaf_path = '../data/PlantVillage-Dataset/raw/color/Apple___Cedar_apple_rust/b401cded-e2cb-4907-b475-5373142735d9___FREC_C.Rust 3766.JPG'
	diseased_mask_path = '../data/PlantVillage-Dataset/raw/segmented/Apple___Cedar_apple_rust/b401cded-e2cb-4907-b475-5373142735d9___FREC_C.Rust 3766_final_masked.jpg'

	healthy_leaf_dir = '../data/PlantVillage-Dataset/raw/color/Apple___healthy'
	healthy_mask_dir = '../data/PlantVillage-Dataset/raw/segmented/Apple___healthy'
	healthy_files = load_healthy_images(healthy_leaf_dir, healthy_mask_dir)

	output_dir = 'output/Apple___Cedar_apple_rust'

	run_nst(healthy_files, diseased_leaf_path, diseased_mask_path, output_dir)
