from Detector import Detector
import cv2
import os
import json


def detect_img(imgs_path, out_json_path):
    det = Detector()

    for imgs in os.listdir(imgs_path):
        img_path = os.path.join(imgs_path, imgs)
        json_path = os.path.join(out_json_path, imgs.split('.')[0]+".json")

        img = cv2.imread(img_path)
        result = det.detect(img)

        # 将检测结果写为json文件
        json_all = {}
        json_all['info'] = {}
        json_all['info']['image_name'] = imgs

        anno = []
        for pred in result[1]:
            biaoqian = {}
            biaoqian['category_name'] = pred[4]
            biaoqian['score'] = pred[5].item()
            biaoqian['bbox'] = [pred[0]+(pred[2]-pred[0])//2,
                                pred[1]+(pred[3]-pred[1])//2,
                                pred[2]-pred[0],
                                pred[3]-pred[1]]
            anno.append(biaoqian)
        json_all['annotations'] = anno

        with open(json_path, 'w') as f:
            json.dump(json_all, f)

        # cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        # cv2.imshow("result", result[0])
        # cv2.waitKey()


if __name__ == '__main__':
    imgs_path = "./task5"
    out_json_path = "./task5_result/zhichuangxingmeng"

    if not os.path.exists(out_json_path):
        os.makedirs(out_json_path)

    detect_img(imgs_path, out_json_path)
