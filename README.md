# 项目简介：
使用YOLOV5实现高速公路和城区夜晚场景下（黑天、路灯全亮）非机动车（包括二轮车、三轮车）和行人的检测。

# 项目文件说明：
competition_yolov5

    ————models       # yolov5模型和配置文件
    
    ————utils        # yolov5检测器、评价指标和数据加载文件
    
    ————weights      # yolov5模型权重
    
    ————task5        # 待测数据
    
    ————task5_result # 待测数据测试结果，保存为json文件
    
    ————Detector.py  # 将yolov5检测器封装为一个类
    
    ————demo.py      # 调用yolov5检测器类进行检测
    
    ————results.mp4  # 待测数据测试结果视频

# 使用说明：

1、运行
```bash
python demo.py
```
2、修改参数
可在 ./utils/BaseDetector.py 中对self.threshold(置信度阈值)进行修改； 
在Detector.py中第51行pred = non_max_suppression(pred, self.threshold, 0.1)对最后一个参数(nms阈值)进行修改。

# 最终效果：
可查看results.mp4













