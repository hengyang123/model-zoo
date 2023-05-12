# MMagic BasicVSR

## Description

BasicVSR: The Search for Essential Components in Video Super-Resolution and Beyond

[basicvsr](https://mmagic.readthedocs.io/en/latest/model_zoo/video_super_resolution.html#basicvsr-cvpr-2021)

## Model

| Model                | Download                       | Shape                                       |
| -------------------- | :----------------------------- | :------------------------------------------ |
| basicvsr_backward.pt | [25 MB](basicvsr_backward.pt)  | (1,3,144,176),(1,64,144,176)                |
| basicvsr_forward.pt  | [25 MB](basicvsr_forward.pt)   | (1,3,144,176),(1,64,144,176)                |
| basicvsr_spynet.pt   | [25 MB](basicvsr_spynet.pt)    | (1,3,160,192),(1,3,160,192)                 |
| basicvsr_upsample.pt | [5.7 MB](basicvsr_upsample.pt) | (1,3,144,176),(1,64,144,176),(1,64,144,176) |

## Dataset

[Vid4](https://mmagic.readthedocs.io/en/latest/dataset_zoo/vid4.html?highlight=vid4)

## References

* [basicvsr_reds4](https://mmagic.readthedocs.io/en/latest/model_zoo/video_super_resolution.html#basicvsr-cvpr-2021)

## License

GPL 3.0
