## TASK

Correct the 21 failed DOI identity or publication-notice rows for parent task f60d888e-ce8c-4895-a1de-2322204862d6 using the first-party registry snapshot included below.

## REQUIRED WORK

1. Check only the 21 IDs below. This is a small structured correction in the parent Task. Handle it directly without worker/task fan-out.
2. Verify normalized DOI and use the supplied Crossref deposit for exact title, complete author sequence, issue year and venue. Correct R0022 to Chen Xu in position 2, as confirmed by the Crossref deposit and the original PDF p. 1. R0083's third author is ShinYoung Cho. Use the verified ASCII DOI for R0121. Do not switch to third-party profiles.
3. Audit the two supplied source scopes separately. For each listed DOI the Crossref works request returned HTTP 200 and had no publisher/registry update relationship of correction, expression of concern or retraction. The Crossref Retraction Watch CSV was also matched against original and notice DOI fields and returned zero exact matches. Record the resulting source-bounded disposition. Say that these are locally captured sources supplied with the task. Do not claim you browsed a publisher/registry page live unless you did.
4. Return one consolidated completion with the exact keys and any real contradiction or access limitation. The five excluded IDs (prisma2020, R0059, R0063, R0073, R0074) are already covered and must not be returned.

## REQUIRED OUTPUT

21 compact JSONL rows, one per listed ID and one raw JSON object per line. First-row schema example (schematic metadata): `{"id":"R0001","doi":"10.1109/icws72778.2026.00154","title":"exact registered title","authors":["Name in source order"],"year":2026,"venue":"exact registered venue","identity":"VERIFIED","identity_url":"https://api.crossref.org/works/10.1109/icws72778.2026.00154","notice":"NO_NOTICE_FOUND_AT_CHECKED_SOURCES","checked_notice_urls":["https://api.crossref.org/works/10.1109/icws72778.2026.00154","https://gitlab.com/crossref/retraction-watch-data/-/raw/main/retraction_watch.csv"],"notice_url":null,"issue":"Supplied snapshots only; publisher notice page not independently verified."}`
Identity enum: VERIFIED, MISMATCH, UNRESOLVED. Notice enum: NO_NOTICE_FOUND_AT_CHECKED_SOURCES, CORRECTION_FOUND, RETRACTED, CONCERN, UNRESOLVED. Then one JSON object with returned_ids, unresolved_ids, workers_used, and source_scope, followed by SOURCE_AUDIT_COMPLETE. Do not echo previous results or the input manifest. Honor the opening and closing bridge markers.

## ACCEPTANCE CRITERIA

1. Exactly 21 allowed rows and matched DOI values, zero overlap with the five already resolved and zero duplicate IDs, DOI values or normalized titles.
2. All identities match the actual source values and complete ordered bylines. Every source locator points to the registered work. Any meaningful discrepancy is explicit.
3. All 21 publication notice dispositions cite both supplied registries or have a specific source-supported shortfall. Source coverage is explicitly limited to the supplied snapshots, with zero unsupported notice conclusions.
4. All rows use the allowed fields and enums. The footer matches exact resolved/unresolved keys and states no workers used. No fabricated or non-first-party sources.

## BOUNDARIES

Structured source verification only; no project edits or document drafting. No credentials, PDF upload, alternative host, inferred notice absence, or general claims about a publisher without evidence. Use the data below so blocked external browse does not prevent record-level verification.

Local registry input keys: report ID, DOI URL path, registered title, author list in order, issue year, venue. Each item was returned by `https://api.crossref.org/works/{DOI}`. Registry update markers were checked in the returned records and the CSV:`https://gitlab.com/crossref/retraction-watch-data/-/raw/main/retraction_watch.csv`.
["R0001","10.1109/icws72778.2026.00154","Adaptive Partition and Resource Allocation for Collaborative Inference Services in UAV Swarm",["Ying Dong","Jiebei Shi","Songwei Li","Yuzhou Gao","Yeping Zhu","Jianbing Zhang","Jiwei Huang"],2026,"2026 IEEE International Conference on Web Services (ICWS)"]
["R0002","10.1109/icws72778.2026.00067","Promise: Predictive and Cost-Optimal Migrations for Service-Continuous Edge Intelligence in Multi-UAV Networks",["Jian Zhang","Ming Tao","Renping Xie","Yin Zhang"],2026,"2026 IEEE International Conference on Web Services (ICWS)"]
["R0003","10.1109/wcsp58612.2023.10405273","Dynamic DNN Model Switching for Collaborative Edge Intelligence in UAV Swarm",["Yu Li","Yuben Qu","Chao Dong","Fuhui Zhou","Lei Zhang","Qihui Wu"],2023,"2023 International Conference on Wireless Communications and Signal Processing (WCSP)"]
["R0006","10.1109/icpads67057.2025.11322921","Joint UAV Deployment and Model Partition for Efficient Collaborative Inference",["Wenjing Xia","Tao Wu","Hongjun Wang","Ruhao Jiang","Mingjin Zhang","Yuben Qu"],2025,"2025 IEEE 31th International Conference on Parallel and Distributed Systems (ICPADS)"]
["R0009","10.1109/tits.2025.3629117","Deep Reinforcement Learning-Based Task Offloading With Collaborative Inference in UAV-Assisted Mobile Edge Computing Networks",["Xiangping Bryce Zhai","Shuang Fu","Changyan Yi","Zhiquan Liu","Chao Dong","Chee Wei Tan"],2026,"IEEE Transactions on Intelligent Transportation Systems"]
["R0010","10.1109/wcnc57260.2024.10570535","Efficient Pipeline Collaborative DNN Inference in Resource-Constrained UAV Swarm",["Weiqing Ren","Yuben Qu","Zhen Qin","Chao Dong","Fuhui Zhou","Lei Zhang","Qihui Wu"],2024,"2024 IEEE Wireless Communications and Networking Conference (WCNC)"]
["R0015","10.1109/bigcom61073.2023.00034","Energy-Efficient Collaborative DNN Inference in UAV Swarm",["Weiqing Ren","Yuben Qu","Zhen Qin","Chao Dong","Hao Sun","Lei Zhang","Qihui Wu"],2023,"2023 9th International Conference on Big Data Computing and Communications (BigCom)"]
["R0019","10.1109/jiot.2022.3231341","Deep Reinforcement Learning for Trajectory Path Planning and Distributed Inference in Resource-Constrained UAV Swarms",["Marwan Abdou Dhuheir","Emna Baccour","Aiman Erbad","Sinan Sabeeh Al-Obaidi","Mounir Hamdi"],2023,"IEEE Internet of Things Journal"]
["R0022","10.1109/icct67417.2025.11374232","Multi-UAV Collaborative Model Inference Based on Hierarchical Reinforcement Learning",["Xinchen Li","Chen Xu","Lidong Ma","Wenfei Yuan"],2025,"2025 IEEE 25th International Conference on Communication Technology (ICCT)"]
["R0029","10.1109/iwcmc55113.2022.9824945","Reliable DNN Partitioning for UAV Swarm",["Mingyue Zhao","Xing Zhang","Zezhao Meng","Xiangwang Hou"],2022,"2022 International Wireless Communications and Mobile Computing (IWCMC)"]
["R0044","10.1109/ispce-asia64773.2024.10756252","DNN-Based Task Partitioning and Offloading with Reliability Guarantees in Multi-UAV-Assisted MEC System",["Ling Wang","Junhua Wang","Chen Dai"],2024,"2024 IEEE International Symposium on Product Compliance Engineering - Asia (ISPCE-ASIA)"]
["R0045","10.1109/jiot.2026.3685675","DNN Task Partitioning and Migration Strategies in Multi-UAV-Assisted Mobile Edge Computing",["Shuman Meng","Bin Li","Zhao Yi","Lei Liu","Zesong Fei"],2026,"IEEE Internet of Things Journal"]
["R0048","10.1109/tgcn.2025.3625726","Toward Inference Latency Optimization for Scalable Collaborative Multi-UAV Analytics",["Ying Wang","Jingling Yuan","Wenbo Wu","Quanfeng Yao","Donglei Xu","Zhishu Shen"],2026,"IEEE Transactions on Green Communications and Networking"]
["R0054","10.1109/lwc.2026.3743641","Heading-Coupled STAR-RIS Assisted Multi-UAV Networks for Semantic ISCC",["Menghui Shen","Honggui Deng","Shujiang Zeng","Jingyue Fang","Yuxiang Deng","Dehua Wu","Yun Ou"],2026,"IEEE Wireless Communications Letters"]
["R0062","10.1109/mcom.002.2300129","Elastic Collaborative Edge Intelligence for UAV Swarm: Architecture, Challenges, and Opportunities",["Yuben Qu","Hao Sun","Chao Dong","Jiawen Kang","Haipeng Dai","Qihui Wu","Song Guo"],2024,"IEEE Communications Magazine"]
["R0068","10.1109/access.2025.3572036","Multi-Agent Meta Reinforcement Learning for Reliable and Low-Latency Distributed Inference in Resource-Constrained UAV Swarms",["Marwan Dhuheir","Aiman Erbad","Bechir Hamdaoui","Samir Brahim Belhaouari","Mohsen Guizani","Thang X. Vu"],2025,"IEEE Access"]
["R0071","10.1109/icc52391.2025.11162059","LE-MHAPPO-Enhanced DNN Task Partitioning in Energy-Harvesting Heterogeneous UAV Swarms",["Ke Gao","Jun Du","Chunxiao Jiang","Debashisha Mishra","Chao Zhang","Merouane Debbah"],2025,"ICC 2025 - IEEE International Conference on Communications"]
["R0083","10.1016/j.iot.2024.101479","Distributed inference in IoT-based aerial network of UAVs",["HyungBin Park","SuKyoung Lee","ShinYoung Cho"],2025,"Internet of Things"]
["R0089","10.1016/j.phycom.2023.102129","A hybrid fast inference approach with distributed neural networks for edge computing enabled UAV swarm",["Peng Zhang","Hui Tian","Hao Luo","XingWang Li","GaoFeng Nie"],2023,"Physical Communication"]
["R0095","10.1016/j.adhoc.2026.104347","Multi-UAV cooperative inference for IoVs: Dynamic partitioning and caching optimization",["Qiutian Xu","Chao Yang","Xuandong Lai","Yi Liu","Xin Chen"],2026,"Ad Hoc Networks"]
["R0121","10.23939/ictee2026.02.144","A LINK-LAYER MODEL OF A UAV SWARM MESH NETWORK WITH ENCAPSULATION OF INTERMEDIATE DEEP NEURAL NETWORK ACTIVATIONS: ANALYTICAL EVALUATION OF LATENCY AND TRAFFIC VOLUME",["Artem Kasianchuk","Halyna Lastivka"],2026,"Infocommunication technologies and electronic engineering"]
