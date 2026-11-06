---
id: "numpy_038"
technology: "NumPy"
category: "ML & Data"
title: "NumPy"
doc_order: 38
source_url: "https://numpy.org/pt/install"
language: "en"
retrieved_at: "2026-11-01 22:37:57"
content_hash: "1d0aed9d41ed936f267428f35dd0289c9e0b3674b2cd57becbe828d4029802ff"
---

# NumPy

Source: https://numpy.org/pt/install

---

Esta página assume que você está confortável usando um terminal e está familiarizado com gerenciadores de pacotes.
O único pré-requisito para instalar o NumPy é o próprio Python. Se você ainda não tem
Python e quer a maneira mais simples de começar, recomendamos que use a
[Distribuição Anaconda](https://www.anaconda.com/download) - ela inclui
Python, NumPy e muitos outros pacotes comumente usados para computação científica
e ciência de dados.

O método recomendado de instalar o NumPy depende do seu fluxo de trabalho preferido. A seguir, dividimos os métodos de instalação entre as seguintes categorias:

Escolha o método mais adequado às suas necessidades. Se não tiver certeza, comece com um método **baseado em ambientes** usando `conda` ou `pip`.

Recomendado para novos usuários que queiram um fluxo de trabalho simplificado.

**uv:** Um gerenciador de pacotes Python moderno projetado para velocidade e simplicidade.

`uv pip install numpy`
**pixi:** Um gerenciador de pacotes multiplataforma para Python e outras linguagens.

`pixi add numpy`
As duas principais ferramentas que instalam pacotes do Python são `pip` e `conda`. Para o desenvolvimento web e de propósito geral em Python, há uma [série de ferramentas](https://packaging.python.org/guides/tool-recommendations/) complementares ao pip. Para computação de alto desempenho (HPC), vale a pena considerar o [Spack](https://github.com/spack/spack).

A primeira diferença é que conda é multilinguagens e pode instalar o Python, enquanto o pip é instalado em um determinado Python em seu sistema e instala outros pacotes apenas para essa mesma instalação de Python. Elas têm algumas funcionalidades em comum (por exemplo, ambas podem instalar o `numpy`). No entanto, elas também podem trabalhar juntas.

A segunda diferença é que o pip instala do Python Packaging Index (PyPI), enquanto o conda instala de seus próprios canais (tipicamente “defaults” ou “conda-forge”). O PyPI é a maior coleção de pacotes, no entanto, todos os pacotes populares estão disponíveis para conda também.

A terceira diferença é que conda é uma solução integrada para gerenciar pacotes, dependências e ambientes, enquanto com pip você pode precisar de outra ferramenta (há muitas!) para lidar com ambientes ou dependências complexas.

```
conda create -n my-env
conda activate my-env
conda install numpy
```
`pip install numpy`
**Dica:** Use um ambiente virtual para melhor gerenciamento de dependências

```
python -m venv my-env
source my-env/bin/activate  # macOS/Linux
my-env\Scripts\activate     # Windows
pip install numpy
```
Não recomendado para a maioria dos usuários, mas disponível por conveniência.

**macOS (Homebrew):**

`brew install numpy`
**Linux (APT):**

`sudo apt install python3-numpy`
**Windows (Chocolatey):**

`choco install numpy`
Para usuários avançados e desenvolvedores que querem personalizar ou depurar o **NumPy**.

Um pequeno aviso: construir o Numpy a partir do código-fonte pode ser um exercício não-trivial.
Recomendamos o uso de binários se eles estiverem disponíveis para a sua plataforma através de um dos métodos anteriores.
Para obter detalhes sobre como construir a partir do código-fonte, consulte [o guia de construção a partir do código-fonte na documentação do Numpy](https://numpy.org/devdocs/building/).

Depois de instalar o NumPy, verifique a instalação, executando o seguinte em um shell ou script Python:

```
import numpy as np
print(np.__version__)
```
Isto deve imprimir a versão instalada do NumPy sem erros.

Se sua instalação falhar com a mensagem abaixo, consulte [Solucionando ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

```
IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!
Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.
```