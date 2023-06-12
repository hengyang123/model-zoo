<!--- SPDX-License-Identifier:  -->

# kapao

## Description

KAPAO is an efficient single-stage multi-person human pose estimation method that models keypoints and poses as objects within a dense anchor-based detection framework. KAPAO simultaneously detects pose objects and keypoint objects and fuses the detections to predict human poses.

## Model

|Model            |Download                           |AP             |AR          |
|-----------------|:----------------------------------|:--------------|:-----------|
|kapao            |[model](kapao.onnx)                |64.4           |71.5        |

## Dataset

* [coco annotations_trainval2017](http://images.cocodataset.org/annotations/annotations_trainval2017.zip)
* [coco image_info_test2017](http://images.cocodataset.org/annotations/image_info_test2017.zip)
* [coco train2017](http://images.cocodataset.org/zips/train2017.zip)
* [coco val2017](http://images.cocodataset.org/zips/val2017.zip)

## References

* [Rethinking Keypoint Representations: Modeling Keypoints and Poses as Objects for Multi-Person Human Pose Estimation](https://arxiv.org/pdf/2111.08557.pdf)
* [wmcnally/kapao](https://github.com/wmcnally/kapao)

## License

kapao is freely available for free non-commercial use, and may be redistributed under these conditions. Please, see the [license](https://github.com/wmcnally/kapao/blob/master/LICENSE) for further details.