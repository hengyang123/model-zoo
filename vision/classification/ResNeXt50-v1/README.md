<!--- SPDX-License-Identifier: Apache-2.0 -->

# ResNeXt50

## Description

ResNeXt50 is a simple, highly modularized network architecture for image classification, constructed by a template with cardinality = 32 and bottleneck width = 4d and defined by Xie et al. in their [paper](https://arxiv.org/abs/1611.05431).

## Model

|Model          |Download                                    |Top-1 accuracy (%) |Top-5 accuracy (%) |
|---------------|:-------------------------------------------|:------------------|:------------------|
|ResNeXt50_v1   |[98 MB](resnext50_32x4d_v1_dyn.onnx)        |77.618             |93.698             |

## Dataset

[ImageNet (ILSVRC2012)](http://www.image-net.org/challenges/LSVRC/2012/).

## References

* **ResNeXt50** model is from the paper titled [Aggregated Residual Transformations for Deep Neural Networks](https://arxiv.org/abs/1611.05431).
* This onnx model is converted from a pytorch [model](https://download.pytorch.org/models/resnext50_32x4d-7cdf4587.pth), which is pretrained on ImageNet in the [repository](https://pytorch.org/vision/main/_modules/torchvision/models/resnet.html#ResNeXt50_32X4D_Weights/).

## License

Apache 2.0
