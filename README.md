# Background

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

One thousand years ago, Ḥasan Ibn al-Haytham (965-1039 AD) studied
optics through experimentation and observation. He advocated that a
hypothesis must be supported by experiments based on confirmable
procedures or mathematical reasoning—an early pioneer in the scientific
method *five centuries* before Renaissance scientists
([Website](https://www.ibnalhaytham.com/),
[Wikipedia](https://en.wikipedia.org/wiki/Ibn_al-Haytham), [Tbakhi &
Amir 2007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6074172/)).

We use the latinized form of his name (‘Alhazen’) as the name of this
project to honor his contribution (which goes largely unrecognized from
within non-Islamic communities).

Famously, he was quoted as saying:

> The duty of the man who investigates the writings of scientists, if
> learning the truth is his goal, is to make himself an enemy of all
> that he reads, and, applying his mind to the core and margins of its
> content, attack it from every side. He should also suspect himself as
> he performs his critical examination of it, so that he may avoid
> falling into either prejudice or leniency.

Here, we seek to develop an AI capable of applying scientific knowledge
engineering to support CZI’s mission. We seek to honor Ibn al-Haytham’s
critical view of published knowledge by creating a AI-powered system for
scientific discovery.

## Install

This tool depends on the MLC.AI project (<https://mlc.ai/>) and
primarily functions by executing a local LLM on the user’s machine - and
then call that system via a REST API.

### Installing Llama2 locally

Instructions: <https://mlc.ai/mlc-llm/docs/>

1.  Download and install pre-built pip wheels for mlc-ai and mlc-llm
    from <https://mlc.ai/package/>

    For Metal installation on Mac, run this command:

    `pip install --pre --force-reinstall mlc-ai-nightly mlc-chat-nightly -f https://mlc.ai/wheels/`

2.  Verify installation

    `python -m mlc_chat.rest --help`

    This should print help information for the REST API.

3.  Download the quantized Llama2 model from github and place it in the
    dist/prebuilt directory.

        mkdir -p dist/prebuilt
        git clone https://github.com/mlc-ai/binary-mlc-llm-libs.git dist/prebuilt/lib
        cd dist/prebuilt
        git clone https://huggingface.co/mlc-ai/mlc-chat-Llama-2-70b-chat-hf-q4f16_1

4.  Run the REST API

    `python -m mlc_chat.rest --device-name metal  --model Llama-2-70b-chat-hf  --quantization q4f16_1`

    This should print output from the server that should end with:

    `INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)`

## How to use

At this stage, development and use of Alhazen will be performed via
local Jupyter notebooks.

``` python
1+1
```

    2
