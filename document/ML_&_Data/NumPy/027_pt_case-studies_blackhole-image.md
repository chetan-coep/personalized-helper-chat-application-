---
id: "numpy_027"
technology: "NumPy"
category: "ML & Data"
title: "NumPy"
doc_order: 27
source_url: "https://numpy.org/pt/case-studies/blackhole-image"
language: "en"
retrieved_at: "2026-11-01 22:37:49"
content_hash: "1a374af3b39126f5ae47a1afc137da5726088f15d4972338c422760be70a3ccb"
---

# NumPy

Source: https://numpy.org/pt/case-studies/blackhole-image

---

Imaging the M87 Black Hole is like trying to see something that is by definition impossible to see.

—Katie Bouman, *Professora Assistente, Ciências da Computação e Matemática, Caltech*


O [telescópio Event Horizon (EHT)](https://eventhorizontelescope.org), é um conjunto de oito telescópios em solo formando um telescópio computacional do tamanho da Terra, projetado para estudar o universo com sensibilidade e resolução sem precedentes. O enorme telescópio virtual, que usa uma técnica chamada interferometria de longa linha de base (VLBI), tem uma resolução angular de [20 micro-arcossegundos](https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole) — o suficiente para ler um jornal em Nova Iorque a partir de um café em uma calçada de Paris!

**Uma nova visão do universo:** A imagem inovadora do EHT foi publicada 100 anos após [o experimento de Sir Arthur Eddington](https://en.wikipedia.org/wiki/Eddington_experiment) ter produzido as primeiras evidências observacionais apoiando a teoria da relatividade geral de Einstein.

**O Buraco Negro:** o EHT foi treinado em um buraco negro supermassivo a aproximadamente 55 milhões de anos-luz da Terra, localizado no centro do galáxia Messier 87 (M87) no aglomerado de Virgem. Sua massa é equivalente a 6,5 bilhões de vezes a do Sol. Ele vem sendo estudado [há mais de 100 anos](https://www.jpl.nasa.gov/news/news.php?feature=7385), mas um buraco negro nunca havia sido observado visualmente antes.

**Comparando observações com a teoria:** Pela teoria geral da relatividade de Einstein, os cientistas esperavam encontrar uma região de sombra causada pela distorção e captura da luz causada pela influência gravitacional do buraco negro. Os cientistas poderiam usá-la para medir a enorme massa do mesmo.

**Escala computacional**

O EHT representa um desafio imenso em processamento de dados, incluindo rápidas flutuações de fase atmosférica, uma largura grande de banda nas gravações e telescópios que são muito diferentes e geograficamente dispersos.

**Muitas informações**

A cada dia, o EHT gera mais de 350 terabytes de observações, armazenadas em discos rígidos cheios de hélio. Reduzir o volume e a complexidade desse volume de dados é extremamente difícil.

**Em direção ao desconhecido**

Quando o objetivo é algo que nunca foi visto, como os cientistas podem ter confiança de que sua imagem está correta?

E se houver um problema com os dados? Ou talvez um algoritmo seja muito dependente de uma hipótese em particular. A imagem será alterada drasticamente se um único parâmetro for alterado?

A colaboração do EHT venceu esses desafios ao estabelecer equipes independentes que avaliaram os dados usando técnicas de reconstrução de imagem estabelecidas e de ponta para verificar se as imagens resultantes eram consistentes. Quando os resultados se provaram consistentes, eles foram combinados para produzir a imagem inédita do buraco negro.

O trabalho desse grupo ilustra o papel do ecossistema científico do Python no avanço da ciência através da análise de dados colaborativa.

Por exemplo, o pacote Python [`eht-imaging`](https://github.com/achael/eht-imaging) fornece ferramentas para simular e realizar reconstrução de imagem nos dados do VLBI.
O NumPy está no coração do processamento de dados vetoriais usado neste pacote, como ilustrado pelo gráfico parcial de dependências de software abaixo.

Além do NumPy, muitos outros pacotes como [SciPy](https://www.scipy.org) e [Pandas](https://pandas.io) foram usados na *pipeline* de processamento de dados para criar a imagem do buraco negro.
Os arquivos astronômicos de formato padrão e transformações de tempo/coordenadas foram tratados pelo [Astropy](https://www.astropy.org/) enquanto a [Matplotlib](https://matplotlib.org/) foi usada na visualização de dados em todas as etapas de análise, incluindo a geração da imagem final do buraco negro.

A estrutura de dados n-dimensional que é a funcionalidade central do NumPy permitiu aos pesquisadores manipular grandes conjuntos de dados, fornecendo a base para a primeira imagem de um buraco negro. Esse momento marcante na ciência fornece evidências visuais impressionantes para a teoria de Einstein. Esta conquista abrange não apenas avanços tecnológicos, mas colaboração científica em escala internacional entre mais de 200 cientistas e alguns dos melhores observatórios de rádio do mundo. Eles usaram algoritmos e técnicas de processamento de dados inovadores, que aperfeiçoaram os modelos astronômicos existentes, para ajudar a descobrir um dos mistérios do universo.