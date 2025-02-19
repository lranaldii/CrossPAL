# Empowering Multi-step Reasoning across Languages via Program-Aided Language Models

This repository provides a the scripts for reproducing tha experiments presented in the paper [Empowering Multi-step Reasoning across Languages via Program-Aided Language Models](https://aclanthology.org/2024.emnlp-main.678.pdf)


## Reference

If you find this project useful for your research, please consider citing the following paper:

```
@inproceedings{ranaldi-etal-2024-empowering-multi,
    title = "Empowering Multi-step Reasoning across Languages via Program-Aided Language Models",
    author = "Ranaldi, Leonardo  and
      Pucci, Giulia  and
      Haddow, Barry  and
      Birch, Alexandra",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.emnlp-main.678/",
    doi = "10.18653/v1/2024.emnlp-main.678",
    pages = "12171--12187",
    abstract = "In-context learning methods are popular inference strategies where Large Language Models (LLMs) are elicited to solve a task using provided demonstrations without parameter updates. Among these approaches are the reasoning methods, best exemplified by Chain-of-Thought (CoT) and Program-Aided Language Models (PAL), which elicit LLMs to generate reasoning paths, thus promoting accuracy and attracting increasing attention. However, despite the success of these methods, the ability to deliver multi-step reasoning remains limited to a single language, making it challenging to generalize to other languages and hindering global development.In this work, we propose Cross-lingual Program-Aided Language Models (CrossPAL), a method for aligning reasoning programs across languages. In particular, our method delivers programs as intermediate reasoning steps in different languages through a double-step cross-lingual prompting mechanism inspired by the Program-Aided approach. In addition, we introduce Self-consistent CrossPAL (SCrossPAL) to ensemble different reasoning paths across languages. Our experimental evaluations show that our method significantly outperforms existing prompting methods, reducing the number of interactions and achieving state-of-the-art performance."
}
```
