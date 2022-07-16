import os


def mv_img(source_dir: str,  target_dir: str, img_name: str):
    if not os.path.exists(source_dir):
        raise Exception("not exist source_dir: " + source_dir)

    if not os.path.exists(target_dir):
        raise Exception("not exist target_dir: " + target_dir)

    source_img_path = os.path.join(source_dir, img_name)

    if not os.path.exists(source_img_path):
        raise Exception("not exist file path: " + source_img_path)

    target_img_path = os.path.join(target_dir, img_name)

    if os.path.exists(target_img_path):
        raise Exception("file has existed on: " + target_img_path)

    os.rename(source_img_path, target_img_path)

    print("moved file: " + img_name)


if __name__ == "__main__":

    SOURCE_DIR = '/Users/mark/Documents/mark_projects/hjxh/hjxh_express_match/.imgs/'
    TARGET_DIR = '/Users/mark/Documents/mark_keeps_learning/.imgs/'
    file_name = 'readme-1641287704584-613d44afa250b17be45e5b366487d1dbd42939da44543700b5e7fbd7f6a8ca9e.png'
    mv_img(SOURCE_DIR, TARGET_DIR, file_name)
