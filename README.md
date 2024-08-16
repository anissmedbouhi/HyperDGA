# HyperDGA: Hyperbolic Delaunay Geometric Alignment
This repository contains the code for the paper called **"Hyperbolic Delaunay Geometric Alignment"**.

# Abstract
Hyperbolic machine learning is an emerging field aimed at representing data with a hierarchical structure. However, there is a lack of tools for evaluation and analysis of the resulting hyperbolic data representations. To this end, we propose Hyperbolic Delaunay Geometric Alignment (HyperDGA) -- a similarity score for comparing datasets in a hyperbolic space. The core idea is counting the edges of the hyperbolic Delaunay graph connecting datapoints across the given sets. We provide an empirical investigation on synthetic and real-life biological data and demonstrate that HyperDGA outperforms the hyperbolic version of classical distances between sets. Furthermore, we showcase the potential of HyperDGA for evaluating latent representations inferred by a Hyperbolic Variational Auto-Encoder.

# Information
Our main codes are in the following jupyter notebooks:
<ul>
  <li>https://github.com/anissmedbouhi/HyperDGA/blob/main/HyperDGA_notebook_Experiment_1.ipynb</li>
  <li>https://github.com/anissmedbouhi/HyperDGA/blob/main/HyperDGA_notebook_Experiment_2.ipynb</li>
  <li>https://github.com/anissmedbouhi/HyperDGA/blob/main/HyperDGA_notebook_Experiment_3.ipynb</li>
</ul> 
<br />
To get started, create a conda environment from the yaml file: HyperDGA_environment.yml <br />

For the experiments 1 and 2, one needs to first train a Hyperbolic VAE with synthetic dataset using the code at: https://github.com/pfnet-research/hyperbolic_wrapped_distribution <br />

For the experiment 3, one needs to first get the Poincaré embeddings of Olsson, Paul and Planaria datasets using the code from: https://github.com/facebookresearch/PoincareMaps/tree/main <br />
For convenience we put these embeddings as pickle files called "dict_data_xxx.pkl" in the current folder. <br />

Part of our code for the Voronoi diagram is from Devert Alexandre: https://gist.github.com/marmakoide/45d5389252683ae09c2df49d0548a627#file-laguerre-voronoi-2d-py <br />
Part of our code for the synthetic dataset and the Hyperbolic VAE is from https://github.com/pfnet-research/hyperbolic_wrapped_distribution

# License:

MIT License <br />

Copyright (c) <br />

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: <br />

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. <br />

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

