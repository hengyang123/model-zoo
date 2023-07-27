# LLaMA-2-7B-chat model with only one decoder

## Description

This model is a small version of LLaMA-2-7B-chat model
exported from Huggingface transformers,
with num_hidden_layers set to 1 instead of 32.

Inputs are input_ids, attention_mask and position_ids.

The input token length is set to 2048 and there is no kvcache support.

[Paper](https://arxiv.org/abs/2307.09288)

[Transformers - LLaMA2](https://huggingface.co/docs/transformers/main/model_doc/llama2)

## Model

| Model                 | Download                       | Shape                      |
| ----------------------| :------------------------------| :--------------------------|
| LLaMA-2-7B-chat.onnx  | [1.8 GB](LLaMA-2-7B-chat.onnx) | (1,2048),(1,2048),(1,2048) |

## References

* [Paper](https://arxiv.org/abs/2307.09288)

* [Transformers - LLaMA2](https://huggingface.co/docs/transformers/main/model_doc/llama2)

## License

LLAMA 2 COMMUNITY LICENSE AGREEMENT
