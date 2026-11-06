---
id: "numpy_010"
technology: "NumPy"
category: "ML & Data"
title: "NumPy"
doc_order: 10
source_url: "https://numpy.org/case-studies/deeplabcut-dnn"
language: "en"
retrieved_at: "2026-11-01 22:37:03"
content_hash: "d2d1aafaf76e75340965eec067645b14ff9d48b5a3c7487d5bb1afef416d4474"
---

# NumPy

Source: https://numpy.org/case-studies/deeplabcut-dnn

---

Open Source Software is accelerating Biomedicine. DeepLabCut enables automated video analysis of animal behavior using Deep Learning.

—Alexander Mathis, *Assistant Professor, École polytechnique fédérale de Lausanne* ([EPFL](https://www.epfl.ch/en/))


[DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) is an open source toolbox that empowers researchers at hundreds of institutions worldwide to track behaviour of laboratory animals, with very little training data, at human-level accuracy. With DeepLabCut technology, scientists can delve deeper into the scientific understanding of motor control and behavior across animal species and timescales.

Several areas of research, including neuroscience, medicine, and biomechanics, use data from tracking animal movement. DeepLabCut helps in understanding what humans and other animals are doing by parsing actions that have been recorded on film. Using automation for laborious tasks of tagging and monitoring, along with deep neural network based data analysis, DeepLabCut makes scientific studies involving observing animals, such as primates, mice, fish, flies etc., much faster and more accurate.

DeepLabCut’s non-invasive behavioral tracking of animals by extracting the poses of animals is crucial for scientific pursuits in domains such as biomechanics, genetics, ethology & neuroscience. Measuring animal poses non-invasively from video - without markers - in dynamically changing backgrounds is computationally challenging, both technically as well as in terms of resource needs and training data required.

DeepLabCut allows researchers to estimate the pose of the subject, efficiently enabling them to quantify the behavior through a Python based software toolkit. With DeepLabCut, researchers can identify distinct frames from videos, digitally label specific body parts in a few dozen frames with a tailored GUI, and then the deep learning based pose estimation architectures in DeepLabCut learn how to pick out those same features in the rest of the video and in other similar videos of animals. It works across species of animals, from common laboratory animals such as flies and mice to more unusual animals like [cheetahs](https://www.technologynetworks.com/neuroscience/articles/interview-a-deeper-cut-into-behavior-with-mackenzie-mathis-327618).

DeepLabCut uses a principle called [transfer learning](https://arxiv.org/pdf/1909.11229), which greatly reduces the amount of training data required and speeds up the convergence of the training period. Depending on the needs, users can pick different network architectures that provide faster inference (e.g. MobileNetV2), which can also be combined with real-time experimental feedback. DeepLabCut originally used the feature detectors from a top-performing human pose estimation architecture, called [DeeperCut](https://arxiv.org/abs/1605.03170), which inspired the name. The package now has been significantly changed to include additional architectures, augmentation methods, and a full front-end user experience. Furthermore, to support large-scale biological experiments DeepLabCut provides active learning capabilities so that users can increase the training set over time to cover edge cases and make their pose estimation algorithm robust within the specific context.

Recently, the [DeepLabCut model zoo](https://deeplabcut.github.io/DeepLabCut/docs/ModelZoo.html) was introduced, which provides pre-trained models for various species and experimental conditions from facial analysis in primates to dog posture. This can be run for instance in the cloud without any labeling of new data, or neural network training, and no programming experience is necessary.

**Automation of animal pose analysis for scientific studies:**

The primary objective of DeepLabCut technology is to measure and track posture
of animals in a diverse settings. This data can be used, for example, in
neuroscience studies to understand how the brain controls movement, or to
elucidate how animals socially interact. Researchers have observed a
[tenfold performance boost](https://www.biorxiv.org/content/10.1101/457242v1)
with DeepLabCut. Poses can be inferred offline at up to 1200 frames per second
(FPS).

**Creation of an easy-to-use Python toolkit for pose estimation:**

DeepLabCut wanted to share their animal pose-estimation technology in the form of an easy to use tool that can be adopted by researchers easily. So they have created a complete, easy-to-use Python toolbox with project management features as well. These enable not only automation of pose-estimation but also managing the project end-to-end by helping the DeepLabCut Toolkit user right from the dataset collection stage to creating shareable and reusable analysis pipelines.

Their [toolkit](https://github.com/DeepLabCut/DeepLabCut) is now available as open source.

A typical DeepLabCut Workflow includes:

**Speed**

Fast processing of animal behavior videos in order to measure their behavior and at the same time make scientific experiments more efficient, accurate. Extracting detailed animal poses for laboratory experiments, without markers, in dynamically changing backgrounds, can be challenging, both technically as well as in terms of resource needs and training data required. Coming up with a tool that is easy to use without the need for skills such as computer vision expertise that enables scientists to do research in more real-world contexts, is a non-trivial problem to solve.

**Combinatorics**

Combinatorics involves assembly and integration of movement of multiple limbs into individual animal behavior. Assembling keypoints and their connections into individual animal movements and linking them across time is a complex process that requires heavy-duty numerical analysis, especially in case of multi-animal movement tracking in experiment videos.

**Data Processing**

Last but not the least, array manipulation - processing large stacks of arrays corresponding to various images, target tensors and keypoints is fairly challenging.

NumPy addresses DeepLabCut technology’s core need of numerical computations at
high speed for behavioural analytics. Besides NumPy, DeepLabCut employs
various Python software that utilize NumPy at their core, such as
[SciPy](https://www.scipy.org), [Pandas](https://pandas.pydata.org),
[matplotlib](https://matplotlib.org),
[Tensorpack](https://github.com/tensorpack/tensorpack),
[imgaug](https://github.com/aleju/imgaug),
[scikit-learn](https://scikit-learn.org/stable/),
[scikit-image](https://scikit-image.org) and
[Tensorflow](https://www.tensorflow.org).

The following features of NumPy played a key role in addressing the image processing, combinatorics requirements and need for fast computation in DeepLabCut pose estimation algorithms:

DeepLabCut utilizes NumPy’s array capabilities throughout the workflow offered by the toolkit. In particular, NumPy is used for sampling distinct frames for human annotation labeling, and for writing, editing and processing annotation data. Within TensorFlow the neural network is trained by DeepLabCut technology over thousands of iterations to predict the ground truth annotations from frames. For this purpose, target densities (scoremaps) are created to cast pose estimation as a image-to-image translation problem. To make the neural networks robust, data augmentation is employed, which requires the calculation of target scoremaps subject to various geometric and image processing steps. To make training fast, NumPy’s vectorization capabilities are leveraged. For inference, the most likely predictions from target scoremaps need to extracted and one needs to efficiently “link predictions to assemble individual animals”.

Observing and efficiently describing behavior is a core tenant of modern
ethology, neuroscience, medicine, and technology.
[DeepLabCut](https://static1.squarespace.com/static/57f6d51c9f74566f55ecf271/t/5eab5ff7999bf94756b27481/1588289532243/NathMathis2019.pdf)
allows researchers to estimate the pose of the subject, efficiently enabling
them to quantify the behavior. With only a small set of training images,
the DeepLabCut Python toolbox allows training a neural network to within human
level labeling accuracy, thus expanding its application to not only behavior
analysis in the laboratory, but to potentially also in sports, gait analysis,
medicine and rehabilitation studies. Complex combinatorics, data processing
challenges faced by DeepLabCut algorithms are addressed through the use of
NumPy’s array manipulation capabilities.