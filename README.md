# [Digital Brain Seminar](https://digitalbrainproject.github.io/seminar/)

The aim of the Digital Brain Seminar series is to bring toghether people who are interested in creating Digital Brain, a digital reconstruction of the brain in structural, dynamic and functional aspects at difference scales in different species.

All seimnars are online or hybrid. Please *[REGISTER](https://docs.google.com/forms/d/1duZBmrP8-1nVFSevK-VwitDGuL3oonJRR4SJCReSnrM/viewform?edit_requested=true)* to get a zoom link for the series.

Most of the talks are archived on the [YouTube channel](https://www.youtube.com/@kennakae2779/videos).

# Upcoming Seminars

### 2025/12/10 Wed 14:30-16:30 (JST)

**Presentator**: [Honda Naoki](https://sites.google.com/view/data-driven-biology/) (Nagoya University)

**Date**:  2025/12/10 Wed 14:30-16:30 (JST)

**Place**: Zoom (The registered page is above and same as usual link)

**Title**: Revisiting Sperry in the Age of Connectomics: Genetic Rules of Brain-Wide Wiring


**Abstract**: 
Understanding how brain-wide neural circuits are genetically organized remains one of the fundamental challenges in neuroscience. Roger Sperry’s classical chemoaffinity theory proposed that molecular gradients provide positional cues for axonal wiring, yet its application has been largely limited to localized sensory systems. Here, we introduce SPERRFY (Spatial Positional Encoding for Reconstructing Rules of axonal Fiber connectivitY), a data-driven framework to examine whether Sperry’s concept can be generalized to the entire brain. By integrating mesoscale connectomic data with spatial transcriptomic maps from the Allen Mouse Brain Atlas, SPERRFY applies canonical correlation analysis (CCA) to identify latent correlated structures between gene-expression and connectivity spaces, thereby inferring positional gradients that may reflect molecular constraints underlying long-range axonal organization. This framework bridges molecular and anatomical levels of organization, providing a quantitative basis for reinterpreting Sperry’s chemoaffinity theory in the context of whole-brain connectomics.

### 2026/1/13 Tue 13:00

**Presentator**: [Tadashi Yamazaki](https://researchmap.jp/tyam) (The University of Electro-Communications)

**Date**:  2026/1/13 Tue 13:00-14:30(JST)

**Place**: Zoom (https://docs.google.com/forms/d/1duZBmrP8-1nVFSevK-VwitDGuL3oonJRR4SJCReSnrM/viewform?edit_requested=true)

**Title**: Development of a biophysically detailed neural circuit simulator and its application to whole mouse cortex simulations


**Abstract**: 
Understanding the brain requires linking microscopic biophysical properties (e.g., ion channel dynamics and dendritic morphology) to emergent macroscopic phenomena (e.g., neural oscillations and network dynamics). While biologically detailed models are instrumental for this mechanistic insight, their inherent computational cost is substantial. While conventional simulators like NEURON and Arbor are highly effective for general use, in simulating models at the extreme scale, they could become inefficient. This is primarily in terms of their scalability and optimization to fully leverage modern High-Performance Computing (HPC) architectures.

We introduce Neulite (https://numericalbrain.org/neulite/), a light-weight biophysically detailed neural circuit simulator. It is architecturally defined by two core components: a frontend compliant with the Allen Institute's Brain Modeling ToolKit (BMTK), and a portable numerical kernel. The frontend facilitates biological plausibility and reproducibility through the utilization of standardized data. The kernel, which can be specifically tuned for different computing architectures, allows us to overcome the limitations of conventional simulators through optimized, domain-specific algorithms.

Neulite has been utilized to successfully execute the Allen Institute's whole mouse cortex model on the Supercomputer Fugaku. We used the entire Fugaku system to simulate 9 million biologically detailed neurons and 26 billion synapses, demonstrating a significant scale of computation. This work is the result of an international collaboration with the team of Dr. Anton Arkhipov at the Allen Institute, where their comprehensive model met our high-performance simulation technology, with support from key domestic contributors (RIKEN R-CCS, RIST, and Yamaguchi University). Neulite is therefore a valuable tool for achieving data-driven, large-scale modeling and advancing the understanding of how cellular properties influence overall neural circuit function.

The content of this talk has been published in a conference paper [1].

[1] Rin Kuriyama*, Kaaya Akira*, Laura Green, Beatriz Herrera, Kael Dai, Mari Iura, Gilles Gouaillardet, Asako Terasawa, Taira Kobayashi, Jun Igarashi, Anton Arkhipov, Tadashi Yamazaki (*: equally contributed). Microscopic-Level Mouse Whole Cortex Simulation Composed of 9 Million Biophysical Neurons and 26 Billion Synapses on the Supercomputer Fugaku. in The International Conference for High Performance Computing, Networking, Storage and Analysis (SC ’25), November 16–21, 2025, St Louis, MO, USA. ACM, New York, NY, USA, 11 pages. doi: 10.1145/3712285.3759819.



# Past Seminars

### 2025/10/7 Tue 13:00-14:30 (JST)

**Presentator**: [Kentaro Miyamoto](https://www.kentaromiyamoto-lab.com/) (RIKEN CBS)

**Date**:  2025/10/7 Tue 13:00-14:30 (JST)

**Place**: Zoom (The registered page is above and same as usual link)

**Title**: Behavioural and neural mechanism of social metacognition in predicting others' performance

**Abstract**: 
When we collaborate with others to tackle new challenges, we anticipate the roles that each team member will play, consider our own role based on these predictions, and adjust our behaviour accordingly. Because each member differs in experience and skills, it is necessary to flexibly adapt the strategy used for prediction. For example, when interacting with beginners who have less career experience, we can make reasonable predictions about their performance by projecting adjusting introspection ('social metacognition'). In contrast, the same strategy cannot be applied to experts with more extensive experience. In this talk, I will introduce our latest research addressing this issue. Specifically, we found that the anterior lateral prefrontal cortex (area 47) is engaged when predicting the thoughts of beginners through social metacognition, whereas the temporoparietal junction (TPJ) is recruited when predicting the thoughts of experts based on heuristics. The lecture will begin with an overview of the foundations of metacognition and then present the studies that led to these findings.


### 2025/8/27 Wed 15:00-16:30 (JST)

**Presentator**: [Stefano Panzeri](https://www.uke.de/english/departments-institutes/institutes/department-of-excellence-for-neural-information-processing/team/index.html) (Institute of Neural Information Processing, University Medical Center Hamburg-Eppendorf)

**Date**:  2025/8/27 Wed 15:00-16:30 (JST), 8/27 Wed 8:00-9:30 (CET)

**Place**: Zoom (The registered page is above and same as usual link)

**Title**: Dissecting the contribution to perceptual decisions of encoding and readout of neural information

**Abstract**: 
Perceptual decisions require that neural populations encode information about the sensory environment and that other downstream populations read it out to inform behavioral outputs.  Here we present our computational work to provide methods that individuate and tease apart the contribution of these two neural operations to the formation of perceptual decisions. We exemplify these methods with the study of several datasets from sensory and parietal cortices and we discuss their implications for understanding the emergent computations of neural population codes. 

**Presentator**: [Anton Arkhipov](https://alleninstitute.org/person/anton-arkhipov/) (Allen Institute)

**Dat**e:  2025/6/13 Fri 10:30-12:00 (JST), 6/12 Thr 18:30-20:00 at Seattle time

**Place**: Zoom (The registered page is above and same as usual link)

**Title**: Integrating multimodal data for bio-realistic simulations of brain circuits   

Recent Nature Neuroscience Paper: https://www.nature.com/articles/s41593-025-01904-7.pdf

**Abstract**: 
A central question in neuroscience is how the structure of the brain determines its activity and function. To explore this systematically, we develop large-scale bio-realistic simulations of brain circuits, which integrate a broad array of experimental data: Distribution and morpho-electric properties of different neuron types; Connection probabilities, synaptic weights, axonal delays, and dendritic targeting rules; And a representation of inputs into the simulated circuits from other parts of the brain. We will discuss this approach focusing on the 230,000-neuron model of mouse primary visual cortex (area V1). Simulations of neural activity in the model match experimental recordings in vivo on a number of metrics, such as firing rates, direction selectivity, and others. Applications include the following problems of broad interest: Understanding how architecture of brain circuit gives rise to the observed functional activity; Learning of behavioral and computational tasks in biological and artificial networks; Generation of the extracellular electric potential due to synaptic activity in the cortex. The model is shared freely with the community via brain-map.org, as are the datasets it is based on.

### 2025/3/27 Thu 17:30-19:00 JST (not 17:00-18:30 JST, sorry)
[**Alain Destexhe**](https://neuropsi.cnrs.fr/en/departments/icn/group-leader-alain-destexhe/) (NeuroPSI)

A computational approach to evaluate how molecular mechanisms impact large-scale brain activity (TBC)

This seminar will present the authors' [recent preprint](https://doi.org/10.21203/rs.3.rs-4610184/v1)


### 2025/2/25 Tue 17:00-18:30 JST
[**EBRAINS Seminar D: High Performance Computing and Co-Design**](20250225_EBRAINS_D.html)

[Registration link](https://us06web.zoom.us/meeting/register/fZcX37xZT0ee1L26NNNtaA) for this semnar

**Jan Bjaalie** and **Ekaterina Zossimova**  
Co-Design & Science Support

**Lena Oden**  
EBRAINS Base infrastructure and HPC services
### 2025/2/18 Tue 17:00-18:30 JST
[**EBRAINS Seminar C: Research Infrastructure and Education**](20250218_EBRAINS_C.html)

[Registration link](https://us06web.zoom.us/meeting/register/tZ0qdeyrpzotE9c5jm0wQlY0Zu2nm3eKlbyi) for this seimnar

**Wouter Klijn**  
EBRAINS-RI architecture, multiple scales of complexity

**Franziska Vogel**  
EBRAINS Education and events for early career researcher

### 2025/2/17 10:30-12:00 JST

[**Kei Hirose**](https://keihirose.com/) (Kyushu University)  
High-dimensional interpretable factor analysis via penalization**

### 2025/1/30 Thu 9:00-16:00 JST
[**Allen Neural Dynamics Workshop at OIST**](https://www.oist.jp/conference/allen-neural-dynamics-workshop)  
[Okinawa Institute of Science ant Technology](https://www.oist.jp/campus/access-map) (on-site only)

[**James Berg**](https://alleninstitute.org/person/jim-berg/) (Allen Institute for Neural Dynamics)  
[**Saskia de Vries**](https://alleninstitute.org/person/saskia-de-vries/) (Allen Institute for Neural Dynamics)  
[Movie 1](https://youtu.be/KwIbGYFokyM)
[Movie 2](https://youtu.be/Qh1y_ix8gXE)

### 2025/1/28 Tue 17:00-18:30 JST
[**EBRAINS Seminar B: Simulation Capabilities**](20250128_EBRAINS_B.html)

**Susanne Kunkel** (Jülich Research Centre)  
The NEST ecosystem: A key enabler of efficient brain-scale spiking network simulation and sustainable neuroscience research

**Thorsten Hater** (Jülich Research Centre)  
Multiscale Simulations of Full Brain Models using Arbor and TVB

**Flashlight talks of developing integrated EBRAINS-RI workflows**  
*	**Sharon Yates** (University of Oslo): QUINT workflow
*	**Giulia De Bonis** (INFN): CobraWAP workflow
*	**Wouter Klijn** (Jülich Research Centre): Virtual Brain Twin workflow

### 2025/1/16 13:00-14:30 JST

[**Daisuke Tagami**](https://hyoka.ofc.kyushu-u.ac.jp/html/100023049_ja.html) (Kyushu University)  
Introduction of Mathematics for Industry Platform (in Japanese)  
[Movie](https://www.youtube.com/watch?v=nZx3RaYovHE)

### 2025/1/16 9:00-10:30 JST

[**Karel Svoboda**]([20250116_Svoboda.html](https://alleninstitute.org/person/karel-svoboda-2/)) (Allen Institute for Neural Dynamics)  
[Science at the Allen Institute for Neural Dynamics (AIND)](20250116_Svoboda.html)

### 2025/1/7 15:00-16:30 JST

[**Se-Bum Paik**](https://cogi.kaist.ac.kr/) (Korea Advanced Institute of Science and Technology)  
Emergence of Cognitive Functions in Natural and Artificial Neural Networks**

### 2024/12/3 17:00-18:30 JST, 9:00 - 10:30 CET
[**EBRAINS Seminar A: Overview, Data Sharing and Brain Atlases**](20241203_EBRAINS_A.html)

[**Katrin Amunts**](https://www.fz-juelich.de/profile/amunts_k)  
EBRAINS – concepts, services and applications

[**Trygve Leergaard**](https://www.med.uio.no/imb/english/people/aca/leergaar/)  
Brain Atlases

[**Oliver Schmid**](https://www.cscs.ch/about/staff)  
The EBRAINS Knowledge Graph - a scientific metadata management solution  
[Movie](https://www.youtube.com/watch?v=5axlpdjX8FU)

### 2024/11/12 Tue 18:00-19:30 JST

[**Viktor Jirsa**](https://ins-amu.fr/jirsaviktor)(Institut de Neurosciences des Systèmes)  
Virtual Brain Twins in Medicine  
[Movie](https://www.youtube.com/watch?v=4duX5dLS19Y)

### 2024/10/22 Tue 13:00-14:00 JST

**Yukako Yamane** (OIST)  
Hands-on tutorial for OptiNiSt  
[Movie](https://www.youtube.com/watch?v=3Z7SIKhO26M)

### 2024/9/30 13:00-14:00 JST
**Rui Gong** (ExCELLS, NINS)  
Tutorial on NIfTI Files, 3D Slicer and Image Registration using ANTs  
[Movie](https://www.youtube.com/watch?v=c3TsjtgU0lU)

### 2024/9/19-21
[**1st Digital Brain Workshop**](https://boatneck-weeder-7b7.notion.site/1st-Digital-Brain-Workshop-131a68936dda4867a88fedd25dfaac92)  
[Kyushu University Nihonbashi Satellite](https://www.kyushu-u.ac.jp/ja/university/facility/nihonbashi/) (on-site only)

### 2024/7/4 Thu 13:30-17:00 JST
**Data sharing and standardization in human neuroscience**  
Main conference room, ATR and Online

13:30 - 14:30: **Franco Pestilli** (University of Texas)  
Putting brain data and cloud technology to good use

14:45 - 15:45: **Jean-Baptiste Poline** (McGill University)  
Changing the landscape of datasharing in brain research with standardized distributed infrastructures: a Neurobagel journey

16:00 - 17:00: **Panel Discussion**

### 2024/6/13 Thr 12:00-13:00 JST

**Takuya Isomura** (RIKEN Center for Brain Science)  
Creating neuromorphic artificial intelligence using reverse engineering of generative models

### 2024/5/10 Fri 13:00-14:30 JST

**Thomas Diego** (Kyushu University)  
Creating bridges between the digital and physical realms with 3D vision

### 2024/4/22 Mon 13:00-15:40

13:00-13:30 **Ken Nakae** (ExCELLS, NINS)  
How to use the Brian/MINDS data portal  
[Movie](https://www.youtube.com/watch?v=83YRBKRUdxk)

13:30-14:00 **Hiromichi Tsukada** (CMSAI, Chubu Univ.)  
Connectome-based modeling using marmoset MRI and gene expression data

14:10-14:40 **Hiroshi Ishii** (Research Institute for Electronic Science, Hokkaido University)  
Pattern formation in mathematical models including neuronal interaction effects

14:40-15:10 **Keiichi Ueda** (Faculty of Science, Academic Assembly, University of Toyama)  
Decentralized distributed parameter tuning model for coupled oscillator systems

15:10-15:40 **Yoshitaro Tanaka** (School of Systems Information Science, Future University Hakodate)  
Proposal of a mathematical model of a reservoir computing using the diffusive chemical reaction

### 2024/4/1 Mon 15:00-17:00 JST
Kyoto University and Online

15:00-16:30 [**Takeru Miyato**](https://takerum.github.io/) (University of Tübingen)  
Learning of hidden principled structures behind observations

16:30-17:00 **Kenji Doya** (Okinawa Institute of Science and Technology Graduate University)  
What is the Digital Brain of Brain/MINDS 2.0  
[Slides](https://www.dropbox.com/scl/fi/x0eeqy623p8sx3lvqv6v3/Doya2024DigitalBrain.pdf?rlkey=t1eb3b90fw2zp6pann5yn5688&dl=0)
[Movie](https://www.youtube.com/watch?v=hDqiOSKc8Ks)

### [Early Web Site](https://boatneck-weeder-7b7.notion.site/Digital-Brain-Seminar-90cc94badac64d32a281cba4245ed66d)

## Organizers
* Ken Nakae (ExCELLS)
* Daisuke Tagami (Kyushu University)
* Kenji Doya (OIST)

## Sponsors
* [Japan Agency for Medical Research and Development (AMED)](https://www.amed.go.jp/en/) (TBC)
* [Mathematics for Industory Platform (MfIP)](https://mfip.jp/)
* [Biology of Behaviro Change, Grant-in-Aid for Transformative Research Areas, MEXT](https://braidyn-bc.jp/)

## Supported by
* [International Brain Initiative (IBI)](https://www.internationalbraininitiative.org)
* [Union of Brain Science Associations in Japan](https://www.brainscience-union.jp/)
* [Japanease Neural Network Society](https://jnns.org/)
