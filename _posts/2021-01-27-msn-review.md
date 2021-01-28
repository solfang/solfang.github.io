---
layout: post
title: Morphing and Sampling Network for Dense Point Cloud Completion - A Review
published: true
tags: todo
---

In this post, we will review the paper [Morphing and Sampling Network for Dense Point Cloud Completion](https://ojs.aaai.org/index.php/AAAI/article/view/6827) presented by Liu et al. at the AAAI 2020 in New York.
We will take a quick look at the motivation behind point cloud completion and previous approaches and then take a look at the network architecture and view the experiments conducted on the network. To close off I present a conclusion and my view on the paper.

The code for this paper is available under [https://github.com/Colin97/MSN-Point-Cloud-Completion]().


# Motivation

The eyes into the world of an autonomous vehicle are the sensors installed in the vehicle. In order to understand the environment in which the vehicle is driving and to make informed decisions about potential paths of actions it's important to have reliable and complete sensor data about the scene. Such 3D data is commonly collected with Lidar sensors, which capture a scene as a set of distinct points, which are referred to as a point cloud. Even though Lidar  produces high fidelity scans,  There are two main factors which can lower the quality of the 3D scans. 

First, scans are often obtained from a single view angle. This means that any part of an object that is occluded by itself or by other objects in the scene will be missing in the obtained point cloud. 

Second, the capacity of the sensor limits the fidelity of the scan. While objects in the foreground of the scene will be represented by many points, objects in the back may only be represented by a handful of points. You can imagine that any tasks that we want to perform on the point cloud, such as segmantic segmentation or object classifcation are very difficult if parts of the data are missing. Therefore we could greatly improve the performance of these subsequent tasks by first completing objects in the points cloud. This is the idea behind point cloud completion: We get as input an incomplete point cloud and are assigned the task of completing the shapes of certain objects in the point cloud [img of incomplete and completed pc].

<img src="/images/paper review/shapenet_reordered.png" height="300">

# 3D Shape Completion
In this section, I will present some of the methods that can be usd to complete a partial 3D shape. These methods can be partitioned into three main avenues: Geometry-based, example-base and learning-based.

## Geometry-based

Geometry-based approaches aim to complete parts of the shape by extrapolating from existing parts in the input. This can be done either by interpolating between surfaces or, given the assumption that the shape of the object is symmetric in any way, complete the shape by modeling the parts of the symmetry which are not present in the input. Problematic with this approach is that interpolation does not work for large-scale incompleteness (imagine the complete back-half of a car missing from the point cloud). Similarly, symmetry assumptions do not apply to all objects. 

<img src="/images/paper review/relatedwork_symmetry.png" height="140">

## Example-based

The second approach involves example-based methods. Here, we have a database of existing shapes which we then deform and assemble to form the complete shape of the object. You can imagine that this method fails for unseen shapes which are not present in the shape database. 

<img src="/images/paper review/relatedwork_examplebased.png" height="140">

## Learning-based

The idea behind learning-based approaches is to learn a mapping between the partial shape and the object and its complete shape. The challenge with this approach is finding an operation that can learn this mapping. In image processing, convolutional layers are often used to perform such an operation. Convolutions require a regular structure but  unfortunately, point clouds have a greatly varying distribution of points so directly applying purely grid-based convolutions is out of the question. Naturally, one way to get to transform a point cloud into a structure is to represent it as a volumetric grid, which discretizes the point cloud into same-sized voxels. A downside to this method is that the resolution of the grid (i.e. how many voxels can we use to represent the scene) is limted by memory constraints and therefore we may lose fine details of the point cloud. Another way to deal with the point representation is to construct a graph on the point cloud and then perform graph-based convolutions. This method seems promising but brings its own batch of downsides such as being sensitive to the point cloud density. Finally, we could work directly with the point cloud without any discretization. Representing the input scene directly as the point cloud is very memory-efficient but we lose information about the local neighborhood of the points since the point cloud is unordered. Nevertheless, networks that operate directly on points clouds have achieved striking success in point-cloud related tasks, including point cloud completion. The paper analyzed in this post uses a network which can directly operate on a point cloud.

<img src="/images/paper review/relatedowork_pc.png" height="140">

# Related Work

In this section I will explain some of the existing work that has been done on point cloud processing and point cloud generation. To better understand why some of the papers presented are able to produce high-quality results I will introduce a set of metrics to (informally) evaluate the quality of a completed point cloud. Those metrics will also help us understand how the paper presented here achieves high-quality point clouds. Those metrics are:

### 1. Smooth surfaces
The completed shape should have continous and smooth surfaces.

<img src="/images/paper review/goals_smooth.png" height="140">

### 2. Fine details
We want to capture fine details of the object, such as an antenna on a car or the indivual blades of a propeller on an airplane.

<img src="/images/paper review/goals_details.png" height="110">

### 3. Locally even distribution of points
We want the points to be distributed evenly on the local parts of the object.

<img src="/images/paper review/goals_even.png" height="140">

### 4. Preserve input structure
All parts of the object in partial input should be preserved in the completed shape.

<img src="/images/paper review/goals_existing.png" height="140">

## Point Cloud Processing

**PointNet**

PointNet is a seminal paper in point cloud processing because of its simple yet effective architecture. PointNet directly takes in a point cloud and produces a single feature vector through an auto-encoder which describes the input point cloud very efficiently. The first few layers of the encoder scale up the input to 1024 channels through 1D convolutions and ensure that the network is indifferent to the exact order of the points within the point cloud or its rotation. At the end of the encoder a single max pool is applied which produces the feature vector of size 1x1024. This feature vector can then be used in subsequent tasks such as shape classifiation or segmantic segmentation by passing it through a decoder.

## Point Cloud Generation

**FoldingNet**

The task of point cloud generation is, given a compressed version of an input point cloud produces by an encoder (like in PointNet), to decode it back into a point cloud in 3D space. A naive way of doing that would be to directly predict each point in the point cloud. Altough simple, this approach cannot guarantee that we end up with smooth surfaces on the output shape. FoldingNet [cite] introduces a more sophisticated way of recovering the point cloud.  FoldingNet samples points from a 2D grid and then deforms this 2D grid into the 3D shape, similar to Origami (but without sharp edges). This type of decoder is referred to as a  'morphing-based' decoder. The resulting objects tend to have continuous and smooth surfaces.

**AtlasNet**

 AtlastNet [cite] uses a similar approach to FoldingNet. Instead of one 2D grid, multiple 2D grids are deformed into 3D surface elements, which then together build the final shape of the object. By using multiple grids, finer details of the shape can be captured.
 
 We can see that deforming 2D grids into 3D surfaces is a promising approach to model smooth and continuous surfaces, which was one of our goals. Therefore we could view this kind of 'morphing' based decoder as our first puzzle piece needed to build a solid network for point cloud completion.
[maybe mid-column fancy background box: First puzzle piece: Morphing-based decoder]

**Point Completion Network (PCN)**

Point Completion Network (PCN) [cite] introduces the idea of modeling the rough shape of the object in an initial pass and then refining the details in a subsequent pass. This approach tends to produce more detailed shapes than if we had tried to predict the complete shape in one go. With the coarse-to-fine network we have the second puzzle piece for our point cloud completion network. [maybe Second puzzle piece: ...]


# Contributions

Now that we have seen some method used to generate our desired point clouds, we can turn to the Morphind and Sampling (MSN) paper. The papers makes four main contributions:
1. A novel two-stage approach for point cloud estimation
2. The addition of an expansion penalty for surface elements
3. A novel sampling algorithm for point clouds with evenly distributed results
4. An Implementation of an Earth mover’s distance (EMD) approximation

We will see later how each of these parts play a role in predicting completed object shapes which satisfy the four qualities the point cloud should have. To recap, those are: smooth surfaces, fine details, a locally even distribution of points and preserving existing structure from the input.

# Architecture
The architecture of the network in the MSN paper can be divided into four parts: 

<img src="/images/paper review/structure.png" height="400">

1. The Encoder and Morphing-based Decoder
2. Merging and Sampling
3. Refining
4. The Loss Function

In the following section I'll explain the individual parts of the network in more detail.
## 1. Encoder and Morphing-based Decoder [image of section with transparency]

**Generating the Coarse Shape**

The encoder is based on PointNet. It produces a single feature feature which will be used in the decoder.
In the decoder we start with K 2D grids (16 in the paper). We then sample points from those grids which are concatenated with the feature vector. The concatenated vectors are fed into K MLPs which 'morph' them into K 3D surface elements [point at image] as we have seen in the Point Completion Network. The surface elements together make up the coarse shape of the object. In theory, the surface elements are not prohibited to overlap. To reduce overlap to a minimum, the authors introduce an 'Expansion Penalty' that is applied to the surface elements. 

<img src="/images/paper review/1_with_expansion.png" height="300">

**Expansion Penalty**

The idea here is to encourage the surface elements to shrink to their respective center. This is done by construction a minimum spanning tree from the points of each surface element, with a total of K trees. A minimum spanning tree is a tree that connects all the vertices of a graph together without any cycles and with the minimum possible edge weight, where the edge weight here is the distance between two vertices. To this spanning tree a loss function is applied which penalizes long edges in the tree. This way the vertices in the spanning tree are encouraged to migrate towards the middle vertex, which shrinks the surface elements towards its center.

<img src="/images/paper review/img_expansion.png" height="200">

## 2. Merging and Sampling

**Merging**

At this point we have modeled the coarse shape of the object which has relatively smooth surfaces and a locally even distribution of points. That's two out of the four goals checked so far. During the generation of the coarse shape structures that are present in the input might have been dropped because the fixed-size surface elements can only model so much detail. To address this problem, the coarse point cloud is merged with the input point cloud. The two point clouds overlap in some areas and therefore the merged point cloud likely has an uneven distribution. Through the merging operation we get to keep all structure from the input but the even distribution that was just there on the coarse point cloud is ruined. 

<img src="/images/paper review/2.png" height="300">

**Sampling**

To fix the distribution, the authors propose to sample from the merged point cloud in a way that the sampled point cloud has an even distribution again. Unfortunately existing sampling algorithms such as Farthest Point Sampling (FPS) or Poisson Disk Sampling (PDS) preserve the unevenness in density and are not appropriate here. The authors therefore come up with their own sampling algorithm called Minimum Density Sampling (MDS). In contrast to FPS, which samples the farthest point from the previously sampled points, MDS samples points in a way that the 'density' of the points in the sample is minimized. Density here is determined by the Gaussian-weighted distance of the point-to-sample to all previously sampled points. [point to formula]. The resulting point cloud now has a uniform distribution.
[FPS formula][maybe FPS img]

<img src="/images/paper review/img_minimumdensitysampling.png" height="200">


## 3. Refining

To generate fine-grained structures, the merged point cloud is fed into a residual network. The network consists of an encoder (based on PointNet) and a decoder which learns a refinement for each point which is then added point-by-point to the merged cloud. At this stage we have generated the final output point cloud, which represents the predicted complete shape of the object.


<img src="/images/paper review/3.png" height="300">

## 4. The Loss Function

To compare the predicted shape to the ground truth shape we need a metric that judges the simlarity between the two point clouds of the shapes. Possible candidates for the distance metric are the Chamfer Distance (CD) and the Earth Mover's Distance (EMD).

**Chamfer Distance**

The Chamfer Distance (CD) is a commonly used distance metric in point cloud completion tasks. Intuitively, for each point in one point cloud it computes the closest point in the second point cloud and then averages all the distances. The Chamfer Distance is straight-forward to calculate but when used as a loss function tends to produce shapes with blurry details and areas that are over-or underpopulated by points. 

**Earth Mover's Distance**

In contrast, the Earth Mover's Distance tends to produce point clouds of higher quality. Intuitively, the Earth Mover's Distance finds a **bijection** between the points of two point clouds and averages the distance between each pair of points. The bijection is chosen so that the average distance between corresponding points is minized. There are two downsides to the EMD. First, it requires the two point cloud to be of equal size. Second, finding the bijection is a challenging task of its own and the textbook implementation of such an algorithm requires memory in O(n²). With this kind of memory consumption, comparing point clouds of more than ~2000 points is not feasible. 
To address the memory problem, the authors propose an algorithm that approximates the EMD with memory consumption of O(n), based on an algorithm from auction theory. In essence, the algorithm treats the points as persons and objects and auctions them off iteratively with the goal of reaching an economic equilibrium. In term of computational cost, CD can be computed with O(n\*log(n)) complexity, while the EMD approximation takes O(n²) computations.

<img src="/images/paper review/img_losscomparison.png" height="300">

The final loss function is composed of the expansion loss of the coarse output as well as the EMD of the coarse and final output, compared to a point cloud sampled from the ground truth shape.

<img src="/images/paper review/img_loss_final.png" height="50">


<img src="/images/paper review/structure.png" height="300">

[maaybe putting it all together]
[puzzle piece narrative needs more tending to, maybe with putting it all together]


# Experiments

## Evaluation Results
The network was evaluated on a subset of the ShapeNet dataset wich includes eight classes of objects: table, chair, car, airplane, sofa, lamp, vessel, cabinet.
30,974 different models were used and for each model, 50 pairs of partial and completed shape were generated through 50 different camera poses, resulting in a training and testing set with a combined size of 30,974\*50 = ~1.5mil samples.

While the network was trained on the EMD distance, it was evaluated both on the CD and EMD. In both metrics, the network beats the state-of-the-art at the time of publishing the paper for each object class.

Below you can see qualitative results.
We can see that compared to the networks of previous papers, MSN tends to generate surfaces with less blur and finer details as well as getting the overall shape of the object right more often.

[qual. results] 

## Ablation studies
The authors have tested versions of the network where different parts were changed or omitted:

A) Without expansion loss 

B) Without merging and refining 

C) With FPS instead of MDS for the sampling 

D) Without refining

The ablated versions of the network were, like in the evaluation, tested on both the Chamfer Distance and Earth Mover's Distance.
Version A, B and C performed worse than the non-ablated version of the network on both distance metrics. For the sampling (C), the network evaluated on the Chamfer Distance provided better resuls with FPS than with the authors sampling algorithm (MDS). The explanation the authors give is that FPS results in a more uneven ditribution of points, which is not as heavily penalized by CD than with EMD. On the other hand, FPS tends to preserve more points from the reliable input than MDS.
[abalation img, only upper half]


# Conclusion

The authors have presented a novel way for point cloud completion where a coarse point cloud is generated in a first pass and then merged with the input point cloud and refined in a second pass.
This approach generates smooth surfaces, preserves existing structure in the input and can generate fine-grained structures. The addition of an expansion penalty and a novel sampling algorithm as well as an approximation of the Earth Mover's Distance ensure an even distribution of points. The network is able to generate realistic point clouds which reach state-of-the-art results in point cloud completion.


# My take on the paper
**Method** 

The network was evaluated on both the 'native' Earth Mover's distance as well as on the Chamger Distance. The papers used to represent state-of-the-art for the evaluation are in my eyes a fair selection. On top of that, the authors have conducted extensive ablation studies. The network was evaluated on ShapeNet, which features dense point cloud. It also would have been interesting to see the performance on sparse data such as Kitti, albeit the authors state that the focus of the paper was on dense point cloud completion.

**Architecture**

Potential ways to improve the networks performance include combining a folding-based decoder and a fully-connected decoder instead of only relying on a folding-based decoder. Also, explicitly trying to rpedict missing parts of the objects from the input point cloud  could potentally improve the quality of the completed objects.

**General Assessment**

The code is available on Github. The authors explain the network architecture concisely and in an easy to follow manner. What I find especially commendable about this paper is that the authors have presented solutions to existing problems, such as the approximation of the Earth Mover's Distance as well as the Minimum density sampling algorithm. Earth Mover's Distance, now that it has a feasible implementation, could improve the quality of future point cloud completion approaches and has been used to produce state-of-the-art results in the 'Cloud Transformers' network [cite]. Altough with a computatational cost of O(n^2) EMD is not an undisputed [wording] choice over the CD.
Furthermore, point-cloud based methods are no longer the only successful approach to point cloud comletion. Recent Voxel-based networks, such as GRNet [cite], have overcome the drawbacks of voxelization could deliver interesting results.

# References
