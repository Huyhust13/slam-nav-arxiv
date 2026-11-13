# Digest arXiv SLAM/Navigation — 2026-W46
_Tạo lúc 2026-11-13 07:10 UTC · 88 bài mới · 40 bài điểm cao nhất bên dưới (ngưỡng ≥ 3)_

## Số bài theo topic
| Topic | Tuần này | TB 4 tuần trước | Δ |
|---|---:|---:|---:|
| SLAM | 19 | – | – |
| Localization | 22 | – | – |
| Navigation | 14 | – | – |
| Semantic & Language Maps | 17 | – | – |
| VLN & Embodied Nav | 8 | – | – |
| Failure & Safety | 5 | – | – |
| Mobile Manipulation | 11 | – | – |
_Chưa đủ lịch sử để so sánh (cần vài tuần chạy)._

## Bài điểm cao (đọc kỹ)
### 1. Persistent Metric-Semantic Maritime Scene Memory from Open-Vocabulary 3D Scene Graphs
- **2611.13903** · 2026-11-10 · score 22.0 · topics: Semantic & Language Maps
- Kim Alexander Christensen, Dina Zimmermann, Martin Steinert et al.
- match: open-vocabulary 3d, scene graph, indoor, vision-language
- https://arxiv.org/abs/2611.13903
- comment: Website: https://kimachristensen.github.io/maritime_3dsg
> Three-dimensional scene graphs (3DSGs) can provide robots with persistent metric-semantic representations for spatial reasoning, but the existing methods have primarily been developed for indoor and terrestrial environments. In this paper we investigate how a representative outdoor open-vocabulary method transfers to maritime environments and which adaptations are needed. Our experiments show that zero-shot representative outdoor 3DSG descriptions agree with our labeled ground truth for a majority of geometry-supported objects on our data, but the resulting map exhibits considerable physical-entity fragmentation, and its terrestrial higher-level assumptions don't capture maritime spatial …

### 2. HiPFuse: Real-Time LiDAR Semantic Segmentation for Robotic Perception on Edge Devices
- **2611.14025** · 2026-11-10 · score 20.0 · topics: Semantic & Language Maps
- Haiyang Wu, George Vosselman, Ville Lehtola
- match: lidar, semantic map, indoor, edge device, odometry
- https://arxiv.org/abs/2611.14025 · code: https://github.com/haiyang2022/HiPFuse
- comment: 13 pages, 6 figures
> Real-time robotic perception requires accurate LiDAR semantics under limited resources. Bird's-eye-view (BEV) aggregation is efficient but can mix differently labeled surfaces in columns. We present HiPFuse, a point-BEV fusion framework that exchanges point and height-partitioned BEV features across horizontal scales, combining point-wise detail with 2D spatial context from one LiDAR scan. Fixed height assignments preserve separate vertical aggregation groups, with auxiliary supervision of initial BEV features using targets from the same 3D cells. A dual-scale BEV context module adds broader context from a coarser grid. On SemanticKITTI and MCD, HiPFuse achieves 63.7% and 62.5% mIoU at 14.2 …

### 3. Reasoning-Aware Relational Representation Learning for Open-Vocabulary Scene Graph Generation
- **2611.13496** · 2026-11-10 · score 20.0 · topics: Semantic & Language Maps
- Jiawei Xiao, Boya Wang, Longtian Qiu et al.
- match: open-vocabulary scene, scene graph, llm, dataset
- https://arxiv.org/abs/2611.13496
- comment: Accepted by NeurIPS 2026, codes are available at project page https://artanic30.github.io/project_pages/RaRe
> Open-Vocabulary Scene Graph Generation (OV-SGG) requires models to recognize visual relationships beyond the training vocabulary, yet existing methods often rely on dataset-specific object--predicate co-occurrence patterns. Under long-tailed distributions and noisy object localization, such reliance leads to biased, entangled relation representations, limiting both rare-relation recognition and generalization to unseen predicates. To address these challenges, we propose RaRe, a reasoning-aware relational representation learning framework that transforms MLLM-generated chain-of-thought (CoT) rationales into structured relation embeddings. Rather than using CoT only as an intermediate …

### 4. GEMOR-GS: Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM
- **2611.13528** · 2026-11-10 · score 15.0 · topics: SLAM, Localization
- Yuchen Yang, Ming Ding, Xinyu Wu et al.
- match: relocalization, lidar, slam
- https://arxiv.org/abs/2611.13528
> Photorealistic and metrically consistent world representations are a primary requirement for LiDAR--inertial--visual SLAM systems that serve robots over continuous operation. 3D Gaussian splatting makes such representations attainable by supplying an explicit, renderable, and queryable scene model. We present GEMOR-GS (Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM) to make the Gaussian map geometrically accurate, globally refined, and re-enterable, providing a better appearance for robot perception and decision-making. To improve the 3DGS map, the LiDAR--camera extrinsic is first estimated offline by direct-method alignment over …

### 5. IncR-3DSGG: Incremental Posed RGB Image Based 3D Scene Graph Generation via Privileged Depth Supervision
- **2611.15429** · 2026-11-11 · score 14.0 · topics: SLAM, Semantic & Language Maps
- Mrunmai Phatak, Daniel Kienzle, Roman Küble et al.
- match: pose graph, scene graph, slam, dataset, real-world
- https://arxiv.org/abs/2611.15429
> Scene graphs provide a compact, structured representation of environments by capturing objects and their spatial or semantic relationships in a form suitable for embodied agents. Existing 3D scene graph generation methods often rely on depth sensing at inference, either to associate object instances across views via point cloud overlap or to compute inter-object relations from geometric cues, limiting deployment to platforms with depth sensors. We propose IncR-3DSGG, which builds 3D scene graphs incrementally from posed\footnote{RGB images with camera extrinsics estimated by an off-the-shelf visual SLAM system.} RGB images, eliminating the use of depth sensors at inference. Our method …

### 6. Maze Runner: Autonomous Maze Navigation with Line-Based Localization and Control Barrier Functions
- **2611.12949** · 2026-11-06 · score 14.0 · topics: SLAM
- Alvaro J. Gaona, Lucas Gómez-Velayos, Peter Pasuy-Quevedo
- match: 2d lidar, lidar, ros 2, slam, navigation, planning
- https://arxiv.org/abs/2611.12949 · code: https://github.com/alvgaona/maze-runner
- comment: 10 pages, 8 figures, 1 table. Code: https://github.com/alvgaona/maze-runner
> Maze navigation requires localization from sparse, repetitive geometry, planning through narrow corridors, and control that stays safe when the estimate or the map is wrong. We present Maze Runner, an open autonomy stack in C++ and ROS 2 that addresses these needs end to end on a simulated Husarion ROSbot XL with a 2D LiDAR in Gazebo. Perception extracts wall lines from each scan with RANSAC and total least squares, with per-line uncertainty. The same line front end feeds two estimators: an Extended Kalman Filter (EKF) that localizes against a line map built from the maze mesh, and an EKF SLAM variant that builds the line map online. Planning runs online on an inflated occupancy grid with …

### 7. An Integrated Open-Source Stack for Vision-Based Autonomous Navigation of Wheeled Rovers
- **2611.08100** · 2026-11-05 · score 14.0 · topics: SLAM, Navigation
- Iaroslav Kolomiets, Iaroslav Sheipak, Mikhail Reppo et al.
- match: ros 2, indoor, jetson, slam, navigation, planning, dataset
- https://arxiv.org/abs/2611.08100
- comment: Accepted at RiTA 2026
> Vision-based rover autonomy requires integrating perception, localization, planning and platform-specific control under limited sensing and computing resources. We present an open-source ROS 2 stack for following directional arrows, reaching a terminal cone and returning autonomously to the start. It connects YOLOv8n detection and geometric direction, range and bearing estimation with RGB-D SLAM, wheel-inertial state estimation, kinematics-aware planning, behavior-tree mission management and STM32 actuation. Standard interfaces separate reusable autonomy from the hardware layer; a proportional path-following plugin supports low-speed rover motion. Public resources include software, …

### 8. PoseBench: Probing Pose Awareness in Visual Foundation Models
- **2611.10347** · 2026-11-07 · score 13.0 · topics: SLAM
- Most Nilufa Yeasmin, Draix Wyatt, Ruyi Lian
- match: pose-graph, foundation model, benchmark, real-world
- https://arxiv.org/abs/2611.10347
> Pose awareness characterizes the extent to which a learned feature space aligns with the underlying object-pose manifold, such that observations with similar poses exhibit greater feature similarity than those with increasingly different poses. While such structure is desirable for pose-sensitive 3D vision tasks, visual foundation models pre-trained on individual 2D images typically lack explicit 3D or pose supervision. This raises a fundamental question: Do 2D visual foundation models exhibit pose awareness after large-scale pretraining? To answer this question, we introduce PoseBench, a systematic benchmark to probe pose awareness in pretrained visual features. Our evaluation follows a …

### 9. PSGAgent: Enhancing MLLMs' Dynamic Visual Perception for Panoptic Scene Graph Generation via Agentic Reasoning
- **2611.07408** · 2026-11-05 · score 13.0 · topics: Semantic & Language Maps
- Qingyun Liu, Yuankun Liu, Jiaye Feng et al.
- match: scene graph, llm, dataset
- https://arxiv.org/abs/2611.07408
- comment: Accepted by ACM Multimedia 2026. 10 pages, 8 figures
> Panoptic Scene Graph generation (PSG) requires holistic yet fine-grained reasoning over complex relations among objects. However, current Multimodal Large Language Models (MLLMs) applied to PSG suffer from a perception bottleneck: they function as static observers limited by fixed-resolution views. As a result, models often overlook critical relations involving small or peripheral objects and struggle to differentiate ambiguous predicates in complex scenes. To address these limitations, we propose PSGAgent, an agentic framework that enhances visual perception for PSG through a think-act-observe loop. PSGAgent allows MLLMs to dynamically refine their visual perception using two tools: a …

### 10. MessyNav: Zero-Shot Navigation via Manipulation in Messy Environments
- **2611.07417** · 2026-11-05 · score 13.0 · topics: Mobile Manipulation
- Kenneth Llontop, Cherie Ho, Dylan Zhou et al.
- match: indoor, mobile manipulat, vision-language, navigation, planning, real-world
- https://arxiv.org/abs/2611.07417
- comment: CoRL 2026
> Real-world environments are messy, with paths often blocked by everyday objects like chairs and toys, requiring robots to perform interactive navigation by manipulating obstacles to clear a path. Existing methods rely on extensive simulation-based learning or per-scene instructions specifying which objects to avoid or manipulate. They struggle to generalize across novel objects, diverse environments, and varied contexts such as a cart of fragile glassware that should be avoided while an empty one can be pushed. We formalize this problem as open-world interactive navigation and present MessyNav, a zero-shot framework based on vision-language models (VLMs). At its core, MessyNav performs …

### 11. DASH-SLAM: Calibration-Free Metric Monocular SLAM via Depth Scale Propagation
- **2611.10239** · 2026-11-06 · score 12.0 · topics: SLAM
- Otavio Ribas, Jacopo Panerati, Pierre-Yves Lajoie
- match: pose graph, foundation model, slam, odometry, dataset
- https://arxiv.org/abs/2611.10239
> Geometric foundation models estimate dense geometry and camera parameters from monocular images, but reliable SLAM also requires consistent scale and accurate data association across successive reconstructions. We present DASH-SLAM, a monocular SLAM system that integrates metric depth predictions from pretrained Depth Anything 3 into a shared-keyframe pose graph without task-specific fine-tuning. DASH-SLAM derives scale corrections from depth ratios at shared anchor images and accumulates them across reconstructions, with a damping factor controlling their influence. These corrections rescale odometry translations, loop constraints, and map geometry. Experiments on TUM, Replica, and …

### 12. From Depth to Safe Depth: Uncertainty-Aware Monocular Perception for Mobile Robot Navigation
- **2611.13769** · 2026-11-10 · score 12.0 · topics: Navigation
- Saeid Firouzi Daghigh, Saeed Ayat
- match: nav2, indoor, foundation model, navigation, benchmark
- https://arxiv.org/abs/2611.13769
> Monocular depth foundation models make it tempting to replace depth sensors on mobile robots with a single RGB camera. We show that, used off the shelf, this is unsafe: in a simulated indoor navigation benchmark, a standard Nav2 stack driven by Depth Anything V2 (metric) collides in 63\% of 120 episodes, because the model systematically over-estimates the distance to nearby obstacles. We propose a lightweight plug-in module that turns predicted depth into \emph{safe depth}. A 0.58\,M-parameter head on top of the \emph{frozen} depth model predicts, per pixel, a log-depth correction $μ$ and an uncertainty $σ$, trained with a $β$-weighted Gaussian negative log-likelihood. The navigation stack …

### 13. UniLoop: Unified Loop Closure Detection from Retrieval to Geometric Verification and Relative Pose Estimation
- **2611.06378** · 2026-11-04 · score 11.0 · topics: SLAM, Localization
- Jingwen Yu, Pengyu Wang, Jin Wu et al.
- match: pose-graph, foundation model, place recognition, loop closure
- https://arxiv.org/abs/2611.06378
> Loop closure detection conventionally cascades separate models for global retrieval, geometric verification, and relative pose estimation, leading to redundant computation and disconnected visual representations. We propose UniLoop, a unified framework that reuses the hierarchical representations of the pretrained geometric foundation model throughout this pipeline. A shared image encoder produces features for compact global descriptors; the same features are passed to the cross-view decoder for pairwise verification; and the original geometric predictions provide relative camera constraints for pose-graph optimization. Experiments on place recognition, loop verification, and relative pose …

### 14. Online Geometric Consistency Assessment of LiDAR Measurements via Recursive Bayesian Comparison
- **2611.10566** · 2026-11-07 · score 11.0 · topics: Localization
- Mingqiao Han, Qigeng Duan, Xuchen Liu et al.
- match: relocalization, lidar, odometry, navigation, real-world, -uav
- https://arxiv.org/abs/2611.10566
> LiDAR-based localization and mapping systems produce registered point clouds that serve as geometric measurements for downstream estimation and navigation. Registration errors introduce duplicated surfaces and structural deformation into these measurements. In the absence of an independent reference, online assessment relies on geometry accumulated from earlier measurements. Such assessment requires tolerance to sampling variation and an accumulation process in which observations enter the history only after evaluation. We therefore formulate a recursive Bayesian comparison that couples geometric assessment with history maintenance. A Normal-Inverse-Wishart model represents historical voxel …

### 15. CPNav: Calibrated Vision-Language Navigation for Object-Goal Search in Unseen Environments
- **2611.10366** · 2026-11-07 · score 11.0 · topics: VLN & Embodied Nav
- Qizhao Chen, Yuanhong Zeng, Shoh Nishino et al.
- match: vision-language, navigation, planning, real-world
- https://arxiv.org/abs/2611.10366 · code: https://github.com/practice-lab-ucla/CPnav
> Directing a robot to locate a target object in unseen environments remains a central challenge in embodied AI. Vision-Language Model (VLM)-based methods provide rich semantic reasoning but often produce uncalibrated and overconfident action decisions. We introduce CPNav, a navigation framework that combines collision-aware planning with statistically calibrated VLM action scoring for map-free object-goal navigation. From RGB-D input, CPNav constructs a navigability map, generates collision-free motion primitives, and queries two VLMs for goal detection and action scoring. The resulting scores are calibrated offline via conformal prediction (CP) using oracle actions obtained through a …

### 16. AgriSense: Vision-Language Decision Support and Robotic Intervention in a Virtual Greenhouse Copy title
- **2611.16752** · 2026-11-12 · score 11.0 · topics: Mobile Manipulation
- Lyes Saad Saoud, Oualid Doukhi, Reza Ghorbani et al.
- match: lidar, mobile manipulat, vision-language, navigation, benchmark, -quadruped
- https://arxiv.org/abs/2611.16752
> Autonomous greenhouse management increasingly requires robotic systems that integrate perception, navigation, environmental regulation, and plant-level intervention. This paper presents AgriSense, a framework combining an Isaac Sim virtual greenhouse, a quadruped mobile manipulator, RGB and LiDAR-inertial sensing, environmental control, and supervised vision-language decision support. Frozen DINOv2 and BERT encoders, together with structured environmental inputs, support joint prediction of twelve environmental references, a target zone, and an intervention flag. Checkpoint replay reproduces 41/43 zone decisions. Across five seeds on a source-grouped test set, the full, image-removed, and …

### 17. MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation
- **2611.08372** · 2026-11-05 · score 11.0 · topics: Mobile Manipulation
- Sateesh Kumar, Arnav Balaji, Arpit Bahety et al.
- match: mobile manipulat, foundation model, navigation, real-world
- https://arxiv.org/abs/2611.08372
- comment: Project page: https://robin-lab.cs.utexas.edu/momasplat
> Visuomotor policies trained through imitation learning are highly sensitive to changes in camera viewpoint. This is particularly problematic for mobile manipulation (MoMa), where robots rarely execute manipulation from the exact same base pose used during demonstration collection due to navigation uncertainty, localization drift, and environmental constraints. Recent approaches use novel-view synthesis (NVS) to augment demonstrations with unseen viewpoints, but they assume static scenes and therefore fail to re-render the manipulated object during the post-contact interaction phase, leaving the most critical parts of the demonstration unaugmented. We present MOMASPLAT, a novel-view …

### 18. Decide Before You Move: Diffusion-Generated Search Reference for Zero-Shot Open-Vocabulary Object Navigation in Semi-Static Environments
- **2611.15093** · 2026-11-11 · score 10.0 · topics: Localization, VLN & Embodied Nav
- Yuxuan Feng, Fujing Xie, Sören Schwertfeger et al.
- match: indoor, vision-language, navigation, benchmark, real-world
- https://arxiv.org/abs/2611.15093
- comment: 9 pages, 5 figures
> Open-world navigation requires a robot to locate a user-specified target in an indoor scene under open-vocabulary queries. Realistic indoor environments are semi-static: walls and furniture largely persist while smaller objects move, relocate, or vanish between visits. Prior-map systems answer queries from object poses recorded at reconstruction time, which expire as soon as objects move, whereas online methods re-derive where to look from current observations every few steps, often through expensive calls to a vision--language model. Assuming that walls and large furniture do not move, we keep their map to plan paths, but use a target--furniture co-occurrence prior to decide where to …

### 19. DAC-MACE: Context-Conditioned Expert Routing for Compact Scene Coordinate Regression in Camera Relocalization
- **2611.10263** · 2026-11-06 · score 10.0 · topics: Localization
- Dingying Fan, Mingkai Liu, Haohua Que et al.
- match: relocalization
- https://arxiv.org/abs/2611.10263
- comment: 10 pages, 6 figures. Submitted to IEEE Sensors Journal
> A camera becomes an absolute pose sensor when its images can be relocalized against a prebuilt map of the scene. On mobile robots and augmented-reality devices, that map must be small and quick to build. Scene coordinate regression (SCR) stores the scene in a compact network that predicts a 3D coordinate for every pixel, and mixture-of-experts (MoE) variants extend its capacity to larger outdoor scenes. In existing MoE-based SCR, however, the router assigns each pixel to an expert from the same local descriptor that the experts regress from, so repeated facades and windows at different locations receive similar routing inputs. We present DAC-MACE, which conditions soft expert routing on …

### 20. SpaceMCP: Vision Language Model Spatial Reasoning via Model Context Protocol
- **2611.15680** · 2026-11-11 · score 10.0 · topics: Semantic & Language Maps
- Ameen Izhac, Nobuko Yoshida, Ronald Clark
- match: scene graph, vision language, benchmark
- https://arxiv.org/abs/2611.15680
- comment: 13 pages, 3 figures. Accepted at the 2nd Workshop on Embodied Spatial Reasoning (ESR) at NeurIPS 2026
> Despite impressive advances in large language models (LLM), vision-language models (VLM) still exhibit limited spatial reasoning capabilities. Recent progress in feed-forward 3D reconstruction has enabled precise, real-time geometric understanding from visual inputs. In this work, we propose SpaceMCP, a framework that leverages these advances to introduce an MCP-style paradigm for spatial reasoning. Our approach augments a VLM with structured function calls, allowing it to query a scene graph for spatial information such as distances, object positioning, and camera properties. The scene graph is constructed in real time using feed-forward 3D reconstruction to recover metric geometry, …

### 21. EMS-Nav: Embodied Multi-Scale Navigation
- **2611.15589** · 2026-11-11 · score 10.0 · topics: Semantic & Language Maps, VLN & Embodied Nav
- Zenghui Yang, Xinan Wang, Danyang Li et al.
- match: open-vocabulary map, industrial, navigation
- https://arxiv.org/abs/2611.15589
- comment: 30 pages, including appendices
> Industrial inspection robots must reach work areas and specific equipment. These destinations span spatial scales from regions to objects, so robots must relate each target to its surroundings to interpret the task and determine where to go. Existing methods support multi-scale navigation through rich environment representations, but at substantial computational and storage cost. These costs limit deployment where wireless coverage is incomplete and robots must rely on onboard computation to keep navigating. We introduce EMS-Nav, a biologically inspired multi-scale navigation framework for online, on-device operation. Its core innovation is to organize perception, spatial understanding, and …

### 22. Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation
- **2611.06475** · 2026-11-04 · score 10.0 · topics: Mobile Manipulation
- Sihang Chen, Chen Ye, Wei Chen et al.
- match: mobile manipulat, planner, benchmark, real world
- https://arxiv.org/abs/2611.06475
- comment: 17 pages, 4 figures
> In the real world, mobile manipulation robots must perform complex object interactions and make multi-step decisions, often relying on task-relevant information that is no longer observable. However, existing benchmarks provide limited evaluation of such memory-dependent decision-making in mobile manipulation. To address this gap, we introduce RoboCasa-Mem, a new benchmark comprising nine mobile manipulation tasks that require agents to use interaction history at key decision points. Specifically, the tasks are grouped into two categories of memory: One is environment memory, which captures spatial locations, object attributes, and object relationships. The other is process memory, which …

### 23. RGB-D SLAM on the Edge: Benchmarking and Profiling RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5
- **2611.16472** · 2026-11-12 · score 9.0 · topics: SLAM
- Himanshu Patil, Jaideep Joshi, Rohit Saluja et al.
- match: pose graph, raspberry, slam, benchmark, -vehicle, -aerial
- https://arxiv.org/abs/2611.16472
> Micro aerial vehicles that operate without GPS often run SLAM on ARM-based edge boards, yet there is little published data on how standard RGB-D SLAM systems behave on such hardware. We benchmark RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5 using six TUM RGB-D sequences at three image resolutions, recording tracking coverage, trajectory error, time per frame, memory, CPU load and temperature for every run, and we profile both systems at the stage and function level. RTAB-Map was configured to process and keep every frame, so its back end runs on every frame rather than at its default rate of 1 Hz. On the sequences that every configuration tracked, its front end takes 38-74 ms per frame and …

### 24. MechBench: A Domain-Specific LLM Benchmark for Parallel Mechanisms
- **2611.15342** · 2026-11-11 · score 9.0 · topics: SLAM
- Zhihao Xia, Tingting Wang, Hui Li et al.
- match: llm, loop closure, benchmark
- https://arxiv.org/abs/2611.15342
> Parallel mechanisms pose distinctive challenges to large language models (LLMs), as valid reasoning depends jointly on mechanism topology, loop closure, geometry, joint types, and modeling assumptions. Yet existing LLM benchmarks provide little systematic coverage of such domain-specific knowledge, constraint-sensitive analysis, and constructive design. To fill this gap, we introduce MECHBENCH, a 2,541-question benchmark for evaluating LLMs in parallel mechanisms across professional knowledge, mechanism analysis, and design. MECHBENCH contains standard and challenge tiers spanning six capability categories and nine executable analysis and design tasks. It is constructed through MECHFORGE, a …

### 25. FREE-LIVO: Physically Decoupled Yet Tightly Coupled LiDAR-Inertial-Visual Odometry
- **2611.07463** · 2026-11-05 · score 9.0 · topics: SLAM
- Reon Tabata, Kenji Koide, Shuji Oishi et al.
- match: lidar, odometry, dataset
- https://arxiv.org/abs/2611.07463
> LiDAR-Inertial-Visual Odometry (LIVO) integrates complementary LiDAR, camera, and IMU measurements to achieve robust state estimation. However, most existing methods assume a fixed relative pose and accurate time synchronization between sensors. Toward modular and heterogeneous robotic systems, this paper presents FREE-LIVO, a tightly coupled odometry method that requires neither a rigid LiDAR-camera rig nor LiDAR-camera time synchronization. The proposed method uses a pretrained image feature matcher to establish correspondences between a camera image and a dense LiDAR intensity image generated from a single LiDAR scan using a generative model. From the resulting 3D point-to-pixel …

### 26. HSGNav: Hypothesis Scene Graphs for Multi-Scale Lifelong Navigation under Object Relocation
- **2611.10547** · 2026-11-07 · score 9.0 · topics: Localization, Semantic & Language Maps
- Kaiyao Liao, Qingfeng Li, Chen Chen et al.
- match: scene graph, navigation, benchmark
- https://arxiv.org/abs/2611.10547
- comment: 11 pages, 4 figures, 4 tables
> In real homes, assistive robots must repeatedly locate targets from large furniture to tiny tabletop items, as people move objects between household surfaces. Uniformly instantiating detections at different scales as 3D objects can be brittle for small on-surface items; without explicit object-state validation, stale entries may persist after scene changes. Our key insight is to separate persistent 3D furniture entities from revisable surface-object hypotheses, retaining their visual evidence without requiring independent object geometry. We formalize this design as the Hypothesis Scene Graph (HSG), which preserves small-object evidence and supports local revision without rebuilding the …

### 27. eSharp: Diffusion-based Sharp Monocular Metric Event-to-Depth Estimation
- **2611.08731** · 2026-11-05 · score 9.0 · topics: Navigation
- Qiushi Dai, Aniket Dashpute, Yuhao Liu et al.
- match: lidar, industrial, navigation, dataset, real-world
- https://arxiv.org/abs/2611.08731
> Depth perception is fundamental for autonomous navigation, industrial inspection, and mixed-reality systems. It often operates under strict constraints on power and form factor. In such cases, monocular depth estimation (MDE) is often used. Even as recent advances continue to improve monocular depth quality, conventional frame-based MDE systems remain challenged by fast motion and high-dynamic-range scenes. This work introduces eSharp, an MDE framework that addresses these problems using an event camera. eSharp repurposes pretrained diffusion priors for event-only MDE and produces accurate metric depth with unparalleled sharpness on real data. Real-world event datasets provide only sparse …

### 28. When to Trust the BIM: Identifiability-Aware LiDAR-Inertial--BIM Fusion under As-Built Deviations
- **2611.09045** · 2026-11-06 · score 8.0 · topics: Localization
- Yujie Zhang, Yuxuan Guo, Xinbao Sun et al.
- match: lidar, odometry, dataset
- https://arxiv.org/abs/2611.09045
- comment: 24 pages, 12 figures, 11 tables (including appendices)
> Building information models (BIM) can provide a global geometric reference for robot localization with LiDAR-inertial odometry (LIO). However, as-built deviations from the as-designed model mean that a disagreement between a scan and the BIM may arise from a pose error, an offset wall surface (an as-built deviation or an unmodeled object in front of the wall), or a shifted room, and in some geometries these explanations produce identical observations. In this paper, we formalize this attribution problem as fault identification over three fault classes and derive a geometric criterion for when attribution is possible. Building on it, we propose an identifiability-aware method that reports an …

### 29. SD-LoRA: Training-Time Structural Distillation into LoRA for Few-Shot Vision-Language Adaptation
- **2611.07063** · 2026-11-04 · score 8.0 · topics: Localization
- Mohammed Rahman Sherif Khan Mohammad, Ardhendu Behera, Sandip Pradhan et al.
- match: vision-language, benchmark
- https://arxiv.org/abs/2611.07063 · code: https://github.com/MR-Sherif/SD-LoRA.git
- comment: Accepted in NeurIPS 2026
> Few-shot adaptation of vision-language models must balance two competing goals: learning fine-grained visual distinctions from very limited supervision and preserving the efficiency that makes frozen CLIP-like models attractive for deployment. Existing lightweight adaptation methods, including prompt tuning, LoRA, and cache-based adapters, typically supervise global image embeddings and therefore underuse token-level structure. Conversely, structure-aware methods exploit local evidence but often introduce additional inference-time computation. We propose SD-LoRA, a structural distillation framework that uses token-level graph reasoning only during training and transfers its effects into a …

### 30. OASIS: Optimization-Aware Subgoal Inference with Safety Constraints for Autonomous Mobile Robot Navigation
- **2611.11996** · 2026-11-09 · score 8.0 · topics: Navigation
- Arian Hajizadeh, Javad Pourrafi Arabani, Negar Shenavar et al.
- match: autonomous mobile robot, navigation
- https://arxiv.org/abs/2611.11996
> Navigation in dynamic environments requires mobile robots to make progress toward their goals while respecting motion limits and avoiding surrounding obstacles. Learned subgoal policies can guide model predictive control beyond its local prediction horizon, but a geometrically suitable subgoal does not necessarily lead to a successfully solved control problem. This paper proposes OASIS, a hierarchical navigation framework that incorporates recent optimization outcomes into reinforcement learning-based subgoal generation. A high-level policy trained using Soft Actor--Critic generates local subgoals, while a nonlinear model predictive controller tracks them subject to motion limits, geometric …

### 31. QVS-LIVO RiskMap: Health- and Information-Aware View Selection for Multi-Camera LIVO and Off-Road Risk Mapping
- **2611.16205** · 2026-11-12 · score 8.0 · topics: Semantic & Language Maps
- Zihan Pan, Jinghan Wang, Hang Li et al.
- match: lidar, semantic map, jetson, odometry, -vehicle
- https://arxiv.org/abs/2611.16205 · code: https://github.com/zihanPan-HIT/QVS-LIVO
- comment: 17pages,9 figures
> Multi-camera observations in off-road environments vary significantly in reliability, posing challenges when complementing degraded geometric constraints. Motivated by this, we propose Quality-aware View Selection Lidar-Vision Odometry Risk Mapping (QVS-LIVO RiskMap), which decouples visual processing for state estimation from that for semantic mapping. The front end evaluates camera observations through read-only pretracking on a shared lidar-inertial posterior, combining observation health with geometric complementarity. Channel health memory and switching hysteresis govern selection of at most one eligible view for direct photometric correction. The posterior is retained when no view is …

### 32. V-STORM: A Structure-Aware Grounded Chain of Thought Dataset for Faithful and Fine-Grained Spatio-Temporal Video Reasoning
- **2611.09511** · 2026-11-06 · score 8.0 · topics: Semantic & Language Maps
- Dian Jiao, Yuqian Yuan, Jiaqi Zhu et al.
- match: scene graph, llm, dataset
- https://arxiv.org/abs/2611.09511
- comment: 9 Pages, 5 figures
> While MLLMs can often identify what happens in a video, they still struggle with fine-grained spatio-temporal reasoning, which requires precise grounding when and where the supporting evidence appears and composing such evidence into a coherent reasoning chain. This challenge is exacerbated by the lack of scalable data construction and evaluation pipelines that provide granular, verifiable supervision linking reasoning steps to explicit spatio-temporal evidence.To address this gap, we present V-STORM, a structure-aware framework that transforms videos into Spatio-Temporal Scene Graphs (STSGs) and derives Grounded Chain of Thought (GCoT) from validated evidence paths, making each reasoning …

### 33. URL-Sim: Unified and Regulated LiDAR Simulation for High-Fidelity Reconstruction of Dynamic Driving Scenes
- **2611.12932** · 2026-11-06 · score 8.0 · topics: Semantic & Language Maps
- Kefei Qian, Xipeng Feng, Jie Li et al.
- match: lidar, scene graph, dataset, real-world, -autonomous driving
- https://arxiv.org/abs/2611.12932
> Reconstructing high-fidelity LiDAR simulation scenes from real-world driving logs is essential for cost-effective safety validation of autonomous driving systems. While simulators based on Neural Radiance Fields (NeRF) achieve realistic scene reconstruction, their large-scale adoption is limited by slow rendering speeds. Recent 3D Gaussian splatting (3DGS) approaches have improved rendering efficiency through explicit primitive representation and differentiable rasterization. However, existing 3DGS-based methods remain largely restricted to rigid vehicles and produce redundant primitives through unconstrained densification. To address these limitations, we propose URL-Sim, a unified and …

### 34. On Agentic Manipulation Policies
- **2611.09892** · 2026-11-06 · score 8.0 · topics: Mobile Manipulation
- Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji et al.
- match: mobile manipulat, vision-language, benchmark, real-world
- https://arxiv.org/abs/2611.09892
- comment: Videos and code available at: https://apple-aiml-research.github.io/ml-amp/
> Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze agentic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged across single-arm, bimanual, and mobile manipulation. AMP1 achieves state-of-the-art results on the RoboLab-120 and CaP-Gym benchmarks, with no demonstrations or task-specific training. On …

### 35. Scale Anchoring via Implicit Semantics and Sequence-Consistent Loop Closure for VGGT-Based SLAM
- **2611.06308** · 2026-11-04 · score 7.0 · topics: SLAM
- Ziyi Jin, Kangjin Yu, Beichen Wang et al.
- match: foundation model, slam, loop closure
- https://arxiv.org/abs/2611.06308
- comment: 8 pages, 6 figures, 4 tables. Submitted to IEEE ICRA 2027
> Feed-forward geometric foundation models enable dense monocular reconstruction without requiring camera calibration, but independently reconstructed submaps can accumulate scale drift, and even a valid revisit can yield an inconsistent cross-submap measurement. We extend VGGT-SLAM 2.0 with fixed-root scale anchoring and short-sequence-assisted direct loop connections. SALAD selects an image pair between the initial submap and each eligible new submap; joint VGGT inference then uses learned implicit semantic-geometric cues to supply a scale-only anchor while preserving the original overlap chain. For loop closure, neighboring image pairs support a consistency check and translation-scale …

### 36. Beyond Infraction Scores: Failure-Boundary Profiles for Closed-Loop Evaluation of Driving and Robot Navigation Agents
- **2611.06453** · 2026-11-04 · score 7.0 · topics: Navigation
- Milan Bulat, Gino Ardelean, Ellington Kirby
- match: warehouse, navigation, benchmark
- https://arxiv.org/abs/2611.06453 · code: https://github.com/speedym/failure-boundary-profiles
- comment: 16 pages, 12 figures, 3 tables. Code: https://github.com/speedym/failure-boundary-profiles. Data: https://doi.org/10.57967/hf/11195
> Closed-loop driving benchmarks in CARLA rank agents by a driving score that multiplies route completion by an infraction penalty. This score does not distinguish an agent that stops in front of an obstacle from one that pushes past it. In a corridor closed by two parked cars, for example, one agent that drives through with contact averages 52.2 on the blocked widths, while the agents that stop average between 37.8 and 40.6. We propose failure-boundary profiles, an evaluation in which each scenario family varies one measured factor, such as corridor width or the time gap in oncoming traffic, and each variant is certified from measurement as one where the agent should proceed or one where it …

### 37. Coupled Scene Graph Anticipation: When With-Constraint Recall Hides Structural Inconsistency
- **2611.06738** · 2026-11-04 · score 7.0 · topics: Semantic & Language Maps
- Zeno Nongmaithem, Anushttha Srivastava, Anshit Sinha et al.
- match: scene graph
- https://arxiv.org/abs/2611.06738 · code: https://github.com/zenoNong/CoupledSGA
- comment: Accepted at ICVGIP 2026 (Indian Conference on Computer Vision, Graphics, and Image Processing), December 21-24, 2026, Kolkata, India. 9 pages, 2 figures, 4 tabl
> Scene Graph Anticipation (SGA) predicts object relationships in future video frames. Continuous-time SGA models evolve each subject-object pair with an independent Neural ODE, so relationships sharing an entity cannot influence one another during integration, and nothing prevents mutually exclusive predictions, such as "sitting on" and "standing on", for the same pair. We introduce CoupledSGA, which links such relationships through a Relationship Interaction Graph with graph attention inside the ODE vector field, and adds a Structural Consistency Loss ($\mathcal{L}_{SC}$) based on a matrix of mutually exclusive predicates. Developing CoupledSGA revealed a limitation of the evaluation …

### 38. META-IR: Meta-Introspective Reasoning for Adaptive Safety Alignment in LLM
- **2611.10089** · 2026-11-06 · score 7.0 · topics: Failure & Safety
- Mahabubur Rahman Miraj, Hongyu Huang, Nankun Mu et al.
- match: llm
- https://arxiv.org/abs/2611.10089 · code: https://github.com/Miraj-Rahman-AI/Meta-IR
- comment: 6 pages, 5 figures. Accepted at the 2026 IEEE International Conference on Multimedia & Expo (ICME 2026), Bangkok, Thailand. Source code: https://github.com/Mira
> Large Language Models (LLMs) remain vulnerable to jailbreak attacks and harmful-content prompts, particularly under adversarial distribution shifts where static alignment pipelines fail to generalize. Although introspective methods such as STAIR strengthen refusal consistency, they depend on fixed self-evaluation policies that cannot rapidly adapt to evolving manipulation strategies. To overcome these limitations, this paper introduces META-IR, a meta-introspective reasoning framework that enhances safety alignment through meta-learning-driven adaptation. It employs a dual-loop architecture: an inner introspective loop that performs structured risk analysis, self-assessment, and reflective …

### 39. Benchmarking Real-World Robotic Manipulation through Stochastic Challenges
- **2611.12804** · 2026-11-09 · score 7.0 · topics: Mobile Manipulation
- Elias Gläßer, Gülhan Şikaroğlu, Pavlo Kupyn et al.
- match: mobile manipulat, benchmark, real-world
- https://arxiv.org/abs/2611.12804
- comment: Accepted at the 10th Conference on Robot Learning (CoRL 2026). 15 pages, 3 figures
> A challenging bottleneck in manipulation research is reproducibility and comparability of methods in real-world environments. Since manipulation is an interactive task, it cannot be evaluated on a static dataset of observations. Benchmarking in simulation is a common remedy, but cannot cover the whole complexity of real-world tests. This paper proposes a new paradigm of stochastic challenges. Like the well-known YCB objects, it is based on reproducible real-world scenes and therefore allows system-level innovation and comparability between different platforms. Due to their stochastic nature, our challenges however, mimic the rigor and surprise of hidden test sets. To this end, we show how …

### 40. Map2SLAM: From Streaming Map Prediction to Real-Time SLAM
- **2611.11169** · 2026-11-08 · score 6.0 · topics: SLAM
- Jian Gao, Lin-Zhuo Chen, Yihang Chen et al.
- match: foundation model, slam, loop closure
- https://arxiv.org/abs/2611.11169
- comment: 17 pages, 10 figures. Project page: https://robbyant-research.github.io/Map2SLAM/
> Streaming 3D foundation models (3DFMs) estimate camera poses and dense geometry online, but they fall short of SLAM: their predictions are fixed once emitted, so loop closures cannot correct accumulated drift. With such models already providing strong geometric capability, a central question for SLAM becomes how to schedule their inference and how to keep its results as revisable state. We present Map2SLAM, which keeps LingBot-Map frozen, trains only a lightweight retrieval head, and builds SLAM on the model's inference interface, turning its predictions into observations of an external persistent SLAM state. The front-end tracks every incoming frame with the model's causal streaming …

## Các bài còn lại (chỉ tiêu đề)
- [6.0] Robot Navigation and Obstacle Avoidance from Randomly Positioned External Cameras — 2611.16282
- [6.0] Hibikino-Musashi@Home 2026 Team Description Paper — 2611.16297
- [6.0] Align3D: Image-Structure Co-Aligned 3D Scene Generation with Observability-Aware Fidelity-Preserving Guidance — 2611.08861
- [6.0] What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation — 2611.16246
- [6.0] CSG-Nav: Confidence-Aware Semantic-Geometric Fusion for Robust Exploration and Accurate Zero-Shot Object-Goal Navigation — 2611.11978
- [6.0] Reaching Is Not Finding: Map-Anchored Visual Prompting for the Last Mile of Aerial Vision-Language Navigation — 2611.11510
- [6.0] Did I See It or Think It? Probing Reality Monitoring in Vision-Language Models with Concept Injection — 2611.09014
- [6.0] HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation — 2611.16439
- [6.0] PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach — 2611.15117
- [6.0] Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation — 2611.09864
- [5.0] Reflection-Robust Stereo Visual-Inertial Odometry via Kalman-Filtered Ground-Height Estimation — 2611.05938
- [5.0] GLCR: Global-Local Collaborative Routing for Multi-Task Electromagnetic Signal Processing — 2611.15609
- [5.0] ChartGalaxy++: A Richly Annotated Dataset for Chart Understanding and Generation — 2611.15418
- [5.0] Entropogram-guided Visual Realignment Decoding: Capturing the Rhythm of Multimodal Reasoning — 2611.06415
- [4.0] DexDICE: Reconciling Safety and Performance via Dual-Expert Offline Imitation Learning — 2611.09433
- [4.0] Embodied RAG++: Retrieval-Augmented Generation From What Exists to What Works in Embodied Scenes — 2611.07517
- [4.0] Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos — 2611.12087
- [4.0] Fast and Reliable Open-Vocabulary Object Search with Absence Detection from Robot Memory — 2611.07493
- [3.0] NIF-VIO: Visual--Inertial Odometry Across Inertial and Non-Inertial Reference Frames — 2611.13662
- [3.0] V3DSAM: Semantic-Geometric Loop Verification and Geometry-Anchored Persistent Instance Mapping for Feed-Forward Dense SLAM — 2611.12452
- [3.0] DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing — 2611.12038
- [3.0] Scale-Consistent Monocular Fisheye Visual Odometry via Spherical Bundle Adjustment-Guided Unsupervised Depth Learning — 2611.11934
- [3.0] AcrossPlace: Do Vision--Language Models Recognize Places Beyond Their Source Views? A Comprehensive Benchmark — 2611.15314
- [3.0] Curie's Jarvis: Autonomous Robotic Chemistry Experiments from Printed Protocols — 2611.13251
- [3.0] Bridging Task Planning and Execution for Language-Conditioned Bimanual Manipulation — 2611.12409
- [3.0] FedIA: Instance-Aware Cross-Modal Representations for Federated Prompt Learning — 2611.05994
- [3.0] SAM-VTP: Video Memory and Measured Geometry for Continuous Traversability Segmentation — 2611.12099
- [3.0] WAM is capable in BEHAVIOR-1K: the 2nd-place solution to the 2026 BEHAVIOR Challenge — 2611.13818
- [2.0] Action Representation for Spatial Generalization in Robot World Models — 2611.11869
- [2.0] Graph-Sparse Distributed Predictive Control for Multi-Robot Motion Planning vianEdge-Consensus ADMM — 2611.11755
- [2.0] Prediction-Error-Tightened MPC for Socially Compliant Crowd Navigation — 2611.15781
- [2.0] ThermalSplat: Generalizable Pose-Free Gaussian Splatting for Sparse-View Thermal 3D Reconstruction — 2611.15435
- [2.0] BRACE: Belief-guided Residual Adaptive Control for Safe Navigation under Unknown Disturbances — 2611.10938
- [1.0] ACROSSVAM3.0: Resource-Bounded 4D Scene Construction and Adaptive Surface Association — 2611.11825
- [1.0] Global-Local and Window-Concatenated Functional Random Forests: Early and Late Fusion of Window-Specific Functional Principal Components — 2611.15816
- [1.0] AdaAlloc: Adaptive Visual Token Allocation for Long-Video Question Answering — 2611.09092
- [1.0] GRAC: Graph-Based Retrieval-Augmented Captioning for Surgical Scene Description — 2611.09866
- [0.0] VeV: Video-Enhanced Vibration Data Augmentation For Structural Difference — 2611.10257
- [0.0] MSR-ABC: Complementary Feature Fusion for Clear Cell Renal Cell Carcinoma Classification — 2611.09583
- [0.0] Hierarchical Incremental Beta Splatting for Online Reconstruction — 2611.08288
- [0.0] SPARC: RoboCup Standard Platform for Autonomous Rescue Competition with Initial Datasets, Software, and Simulation Environments — 2611.15443
- [0.0] PegasusAI Studio: Legible Cyberinfrastructure and Accountable AI Agents for Scientific Workflows — 2611.13309
- [0.0] All Quiet on the Neural Front: Language Models Do Not Report Injected Pain States — 2611.10123
- [-1.0] FASTFUNNELS: Agile Multi Robot Navigation in Narrow Spaces via Adaptive Dynamic Funnels — 2611.09005
- [-1.0] Polarization calibration of fisheye cameras using skylight in the wild — 2611.08911
- [-1.0] ProtoVis-Nav: Prototypical Visual Imagination for Visual-Spatial Aligned UAV Navigation — 2611.17330
- [-2.0] Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach — 2611.07122
- [-4.0] Not Losing Your Way: Mitigating Visual-Inertial Odometry Drift through On-Demand Visual Feature Creation — 2611.07687
