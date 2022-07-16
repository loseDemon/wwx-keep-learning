from mv_img_in_md import mv_img


SOURCE_DIR = '/Users/mark/Documents/mark_projects/hjxh/hjxh_express_match/.imgs/'
TARGET_DIR = '/Users/mark/Documents/mark_keeps_learning/.imgs/'

with open("imgs.txt") as f:
    # ~~use `in f.readlines()` instead of `in f``, since the latter would has a `\n`~~
    # should manually strip !

    for img_name in f:
        img_name = img_name.strip()
        print({"img_name": img_name})
        mv_img(SOURCE_DIR, TARGET_DIR, img_name)
print("finished")
