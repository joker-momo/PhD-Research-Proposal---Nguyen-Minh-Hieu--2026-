## TASK
Create a sourced report-version and study-family candidate audit for the frozen46-report corpus. This is a linkage investigation, not final study counting or eligibility reassessment.

## REQUIRED WORK
1. Read the46 supplied accepted identities, their source-version labels and canonical local text files. All paths below are relative to the canonical project root. Use read-only programmatic parsing/search to cover the complete inventory; do not write any file. If a file cannot be read, return the exact limitation and retain its row. The canonical texts may include NUL bytes; strip them only in memory. Do not rely on absent ignored files in task worktrees.
2. For every report return the exact supplied bibliographic identity and existing version label, with the accepted-file locator. Inspect title page and publication/preprint/accepted-manuscript statements, reporting a1–35-word verbatim quote with file,page,line_start,line_end for a version observation. If no version statement is present, use version_status=unresolved with an identity quote and explain that identity does not prove publication version. Do not equate DOI matching with textual/numerical equivalence to a Version of Record.
3. Screen all1035 unordered pairs using deterministic DOI/title normalization, exact normalized author overlap, title-token overlap and explicit extension/preliminary/demo/preprint/cites-own-work statements found in local texts. Return candidate pairs for every same DOI or same normalized title, every pair with>=2 shared normalized full author names, every pair with token Jaccard>=0.35, and any explicit local linkage. Use lowercase alphanumeric normalization with punctuation replaced by spaces; title stopwords exactly:a,an,the,of,in,on,for,and,to,with,using,by,from,via. Author names normalize lowercase alphanumeric single spaces, no initials expansion/fuzzy guessing. Return a compact screening summary with the actual pairs checked and method; if tools prevent all-pair comparison, report count and missing work rather than claiming1035.
4. For each candidate pair assess only from local evidence: same_report_version, linked_extension, shared_study_evidence, related_but_distinct, or unresolved. Citation/shared authors/shared testbed alone do not establish same study. Use quotes from BOTH reports, each1–35words with page+line range; explain the evaluated evidence overlap or gap. A pair may stay unresolved if the full text does not establish shared participants/data/experiments. An extension can contain new experiments; do not merge all its outcomes automatically. If there are many candidate pairs, prioritize mandatory DOI/title matches and explicit extension statements, report a documented shortfall for the rest, and never hide unchecked candidates.
5. Return one row for every report with candidate partner IDs and a provisional family-link status. Use no final study IDs and no final unique-study count. A singleton means no candidate under this screen, not proof of independence. Include S03 and C18 even though excluded from primary eligibility; demos/related reports can matter for linkage. Preserve all current eligibility/date/scope decisions, especially six uncertain dates and C06/SNCS scope uncertainty.
6. List exact follow-up questions and report pairs still requiring comparison or publisher-version access. No remote discovery is required for this task. Use only accepted local evidence and the supplied full texts; raw rejected A2A output is not evidence. Return structured notes only.

## REQUIRED OUTPUT
One JSON object, no prose/fences:
{"task":"family_01","records":[{"id":string,"title":string,"authors":array,"year":integer,"venue":string,"doi":string,"accepted_version_label":string,"identity_locator":string,"version_status":"supported|unresolved","version_observation":string,"version_evidence":{"file":string,"page":integer,"line_start":integer,"line_end":integer,"quote":string}|null,"candidate_partner_ids":array,"family_link_status":"linked_candidate|no_candidate_under_screen|unresolved","unresolved":array}],"pair_screen":{"report_count":46,"expected_pairs":1035,"checked_pairs":integer,"method":string,"candidate_count":integer,"unassessed_candidate_pairs":array,"shortfall":array},"candidate_pairs":[{"left_id":string,"right_id":string,"signals":array,"shared_authors":array,"title_jaccard":number,"relationship":"same_report_version|linked_extension|shared_study_evidence|related_but_distinct|unresolved","rationale":string,"evidence":[{"report_id":string,"file":string,"page":integer,"line_start":integer,"line_end":integer,"quote":string}],"unresolved":array}],"final_study_count":null,"shortfall":array,"project_files_changed":0,"final_prose_written":false}
All46 records in supplied order. Every record includes DOI or DOI_NOT_FOUND. Candidate unordered pair appears once; sort pair IDs according to supplied inventory order. Sources must resolve to supplied accepted JSON or canonical text. No fabricated quote or missing evidence silently replaced with inference.

## ACCEPTANCE CRITERIA
F1: Exactly46 ordered report IDs with all exact bibliographic fields,46 accepted-file identity locators;DOI/title duplicate count reported after normalization;all duplicate identities explicitly linked,not silently dropped.
F2: All46 version observations have a source locator;each supplied quote is1–35words and exactly matches the stated canonical PDF page/text line span after whitespace/Unicode normalization;unreadable/missing evidence explicitly marked unresolved. Unsupported quantitative/version claims0;DOI-to-VoR equivalence assumptions0.
F3: All1035 unordered pairs checked or documented shortfall;all candidate rules applied exactly;candidate counts and partner lists reconcile;duplicate pairs0;each candidate has relationship,rationale,unresolved and evidence from both reports or explicit unassessed shortfall. Shared-author and title-Jaccard figures reproducible from inputs.
F4: Every positive version/family/extension linkage supported by quoted local evidence;0 shared-author-only same-study conclusions;0 unsupported merges;unresolved pairs explicit;final_study_count=null and0 final study IDs assigned.
F5: All46 eligibility decisions unchanged;0 project-file edits,final prose,downloads,remote submissions/messages,credentials or unrelated-file access;shortfall arrays explicit. Transport completed is unreviewed until Codex checks every criterion.

## BOUNDARIES
Read-only research/extraction/comparison. Codex owns project writes, acceptance and manuscript. Canonical project root: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma
Text page markers and line numbers must be checked from the supplied text, not guessed. Cutoff remains2026-11-25; this task cannot resolve publication dates or change scope. Do not claim searches of IEEE,ACM,Scopus,WoS from these local comparisons. No final PRISMA counts. Bibliography-level candidate screening is not proof of study independence.
Input inventory:
[
  {
    "id": "S01",
    "title": "Efficient Real-Time Image Recognition Using Collaborative Swarm of UAVs and Convolutional Networks",
    "authors": [
      "Marwan Dhuheir",
      "Emna Baccour",
      "Aiman Erbad",
      "Sinan Sabeeh",
      "Mounir Hamdi"
    ],
    "year": 2021,
    "venue": "2021 International Wireless Communications and Mobile Computing (IWCMC)",
    "doi": "10.1109/iwcmc51323.2021.9498967",
    "source_version": "preprint",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/0/accepted_record",
    "local_text": "screening_46/text/S01.txt"
  },
  {
    "id": "S02",
    "title": "Deep Reinforcement Learning for Trajectory Path Planning and Distributed Inference in Resource-Constrained UAV Swarms",
    "authors": [
      "Marwan Dhuheir",
      "Emna Baccour",
      "Aiman Erbad",
      "Sinan Sabeeh Al-Obaidi",
      "Mounir Hamdi"
    ],
    "year": 2023,
    "venue": "IEEE Internet of Things Journal",
    "doi": "10.1109/jiot.2022.3231341",
    "source_version": "preprint",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/1/accepted_record",
    "local_text": "screening_46/text/S02.txt"
  },
  {
    "id": "S03",
    "title": "Demo: IDEA: Intelligent Divine Eye on Air through Multi-UAV Collaborative Inference",
    "authors": [
      "Hao Sun",
      "Chao Dong",
      "Yuben Qu",
      "Feiyu Wu",
      "Lei Zhang",
      "Qihui Wu"
    ],
    "year": 2022,
    "venue": "The 20th Annual International Conference on Mobile Systems, Applications and Services (MobiSys ’22)",
    "doi": "10.1145/3498361.3538674",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/2/accepted_record",
    "local_text": "screening_46/text/S03.txt"
  },
  {
    "id": "S04",
    "title": "Reliable DNN Partitioning for UAV Swarm",
    "authors": [
      "Mingyue Zhao",
      "Xing Zhang",
      "Zezhao Meng",
      "Xiangwang Hou"
    ],
    "year": 2022,
    "venue": "2022 International Wireless Communications and Mobile Computing (IWCMC)",
    "doi": "10.1109/iwcmc55113.2022.9824945",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/3/accepted_record",
    "local_text": "screening_46/text/S04.txt"
  },
  {
    "id": "S05",
    "title": "Online object detection task offloading in UAV ad hoc networks",
    "authors": [
      "Shengqing Wang",
      "Zhiyong Du",
      "Yang Du",
      "Jiaqi Chen"
    ],
    "year": 2022,
    "venue": "2022 IEEE International Conference on Unmanned Systems (ICUS)",
    "doi": "10.1109/icus55513.2022.9987114",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/4/accepted_record",
    "local_text": "screening_46/text/S05.txt"
  },
  {
    "id": "S06",
    "title": "LLHR: Low Latency and High Reliability CNN Distributed Inference for Resource-Constrained UAV Swarms",
    "authors": [
      "Marwan Dhuheir",
      "Aiman Erbad",
      "Sinan Sabeeh"
    ],
    "year": 2023,
    "venue": "2023 IEEE Wireless Communications and Networking Conference (WCNC)",
    "doi": "10.1109/wcnc55385.2023.10118908",
    "source_version": "preprint",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/5/accepted_record",
    "local_text": "screening_46/text/S06.txt"
  },
  {
    "id": "S07",
    "title": "Elastic Collaborative Edge Intelligence for UAV Swarm: Architecture, Challenges, and Opportunities",
    "authors": [
      "Yuben Qu",
      "Hao Sun",
      "Chao Dong",
      "Jiawen Kang",
      "Haipeng Dai",
      "Qihui Wu",
      "Song Guo"
    ],
    "year": 2024,
    "venue": "IEEE Communications Magazine",
    "doi": "10.1109/MCOM.002.2300129",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/6/accepted_record",
    "local_text": "screening_46/text/S07.txt"
  },
  {
    "id": "S08",
    "title": "End-to-End Latency Optimization for Resilient Distributed Convolutional Neural Network Inference in Resource-Constrained Unmanned Aerial Vehicle Swarms",
    "authors": [
      "Jeongho Kim",
      "Joonho Seon",
      "Soohyun Kim",
      "Seongwoo Lee",
      "Jinwook Kim",
      "Byungsun Hwang",
      "Youngghyu Sun",
      "Jinyoung Kim"
    ],
    "year": 2024,
    "venue": "Applied Sciences",
    "doi": "10.3390/app142310832",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/7/accepted_record",
    "local_text": "screening_46/text/S08.txt"
  },
  {
    "id": "S09",
    "title": "DNN-Based Task Partitioning and Offloading with Reliability Guarantees in Multi-UAV-Assisted MEC System",
    "authors": [
      "Ling Wang",
      "Junhua Wang",
      "Chen Dai"
    ],
    "year": 2024,
    "venue": "2024 IEEE International Symposium on Product Compliance Engineering - Asia (ISPCE-ASIA)",
    "doi": "10.1109/ISPCE-ASIA64773.2024.10756252",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/8/accepted_record",
    "local_text": "screening_46/text/S09.txt"
  },
  {
    "id": "S10",
    "title": "Reinforcement Learning based Edge-Assisted Inference for Maritime UAV Networks",
    "authors": [
      "Chuxuan Wang",
      "Jieling Li",
      "Liqing Ye",
      "Yu Liu",
      "Liang Xiao"
    ],
    "year": 2024,
    "venue": "2024 IEEE International Symposium on Parallel and Distributed Processing with Applications (ISPA)",
    "doi": "10.1109/ISPA63168.2024.00222",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/9/accepted_record",
    "local_text": "screening_46/text/S10.txt"
  },
  {
    "id": "S11",
    "title": "Joint UAV Deployment and Model Partition for Efficient Collaborative Inference",
    "authors": [
      "Wenjing Xia",
      "Tao Wu",
      "Hongjun Wang",
      "Ruhao Jiang",
      "Mingjin Zhang",
      "Yuben Qu"
    ],
    "year": 2025,
    "venue": "2025 IEEE 31th International Conference on Parallel and Distributed Systems (ICPADS)",
    "doi": "10.1109/ICPADS67057.2025.11322921",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/10/accepted_record",
    "local_text": "screening_46/text/S11.txt"
  },
  {
    "id": "S12",
    "title": "Multi-UAV Collaborative Model Inference Based on Hierarchical Reinforcement Learning",
    "authors": [
      "Xinchen Li",
      "Chen Xu",
      "Lidong Ma",
      "Wenfei Yuan"
    ],
    "year": 2025,
    "venue": "2025 IEEE 25th International Conference on Communication Technology (ICCT)",
    "doi": "10.1109/ICCT67417.2025.11374232",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/11/accepted_record",
    "local_text": "screening_46/text/S12.txt"
  },
  {
    "id": "S13",
    "title": "LE-MHAPPO-Enhanced DNN Task Partitioning in Energy-harvesting Heterogeneous UAV Swarms",
    "authors": [
      "Ke Gao",
      "Jun Du",
      "Chunxiao Jiang",
      "Debashisha Mishra",
      "Chao Zhang",
      "Merouane Debbah"
    ],
    "year": 2025,
    "venue": "2025 IEEE International Conference on Communications (ICC): IoT and Sensor Networks Symposium",
    "doi": "10.1109/ICC52391.2025.11162059",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/12/accepted_record",
    "local_text": "screening_46/text/S13.txt"
  },
  {
    "id": "S14",
    "title": "Computation Offloading and Resource Allocation for Deep Neural Network Inference in UAV Wireless Networks",
    "authors": [
      "Muhammad Ismail",
      "Long Bao Le"
    ],
    "year": 2025,
    "venue": "2025 IEEE International Conference on Communications (ICC): Next-Generation Networking and Internet Symposium",
    "doi": "10.1109/ICC52391.2025.11161364",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/13/accepted_record",
    "local_text": "screening_46/text/S14.txt"
  },
  {
    "id": "S15",
    "title": "Adaptive model switching of collaborative inference for multi-CNN streams in UAV swarm",
    "authors": [
      "Yu Li",
      "Yuben Qu",
      "Chao Dong",
      "Zhen Qin",
      "Lei Zhang",
      "Qihui Wu"
    ],
    "year": 2025,
    "venue": "Chinese Journal of Aeronautics, 38(8): 103564",
    "doi": "10.1016/j.cja.2025.103564",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/14/accepted_record",
    "local_text": "screening_46/text/S15.txt"
  },
  {
    "id": "S16",
    "title": "Distributed Split Computing Using Diffusive Metrics for UAV Swarms",
    "authors": [
      "Talip Tolga Sarı",
      "Gökhan Seçinti",
      "Angelo Trotta"
    ],
    "year": 2026,
    "venue": "Journal of Systems Architecture, 176: 103804",
    "doi": "10.1016/j.sysarc.2026.103804",
    "source_version": "preprint",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/15/accepted_record",
    "local_text": "screening_46/text/S16.txt"
  },
  {
    "id": "S17",
    "title": "Distributed inference in IoT-based aerial network of UAVs",
    "authors": [
      "HyungBin Park",
      "SuKyoung Lee",
      "ShinYoung Cho"
    ],
    "year": 2025,
    "venue": "Internet of Things, 30: 101479",
    "doi": "10.1016/j.iot.2024.101479",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/16/accepted_record",
    "local_text": "screening_46/text/S17.txt"
  },
  {
    "id": "S18",
    "title": "DNN Task Partitioning and Migration Strategies in Multi-UAV-Assisted Mobile Edge Computing",
    "authors": [
      "Shuman Meng",
      "Bin Li",
      "Zhao Yi",
      "Lei Liu",
      "Zesong Fei"
    ],
    "year": 2026,
    "venue": "IEEE Internet of Things Journal, 13(13): 28758-28769",
    "doi": "10.1109/JIOT.2026.3685675",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/17/accepted_record",
    "local_text": "screening_46/text/S18.txt"
  },
  {
    "id": "S19",
    "title": "Adaptive Partition and Resource Allocation for Collaborative Inference Services in UAV Swarm",
    "authors": [
      "Ying Dong",
      "Jiebei Shi",
      "Songwei Li",
      "Yuzhou Gao",
      "Yeping Zhu",
      "Jianbing Zhang",
      "Jiwei Huang"
    ],
    "year": 2026,
    "venue": "2026 IEEE International Conference on Web Services (ICWS)",
    "doi": "10.1109/icws72778.2026.00154",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/reconciliation/results/identity_dates_01_accepted.json#records[id=S19]",
    "local_text": "screening_46/text/S19.txt"
  },
  {
    "id": "S20",
    "title": "Promise: Predictive and Cost-Optimal Migrations for Service-Continuous Edge Intelligence in Multi-UAV Networks",
    "authors": [
      "Jian Zhang",
      "Ming Tao",
      "Renping Xie",
      "Yin Zhang"
    ],
    "year": 2026,
    "venue": "2026 IEEE International Conference on Web Services (ICWS)",
    "doi": "10.1109/icws72778.2026.00067",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/reconciliation/results/identity_dates_01_accepted.json#records[id=S20]",
    "local_text": "screening_46/text/S20.txt"
  },
  {
    "id": "C01",
    "title": "Orion: A Collaborative Edge Inference Framework for Large Language Models Processing Multi-Sensor Data in UAV Swarms",
    "authors": [
      "Tianchou Yang",
      "Hongjie Guo",
      "Zhengyu Zhao",
      "Donglin Zhu"
    ],
    "year": 2026,
    "venue": "Drones",
    "doi": "10.3390/drones10060410",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/20/accepted_record",
    "local_text": "screening_46/text/C01.txt"
  },
  {
    "id": "C02",
    "title": "Multi-Agent Meta Reinforcement Learning for Reliable and Low-Latency Distributed Inference in Resource-Constrained UAV Swarms",
    "authors": [
      "Marwan Dhuheir",
      "Aiman Erbad",
      "Bechir Hamdaoui",
      "Samir Brahim Belhaouari",
      "Mohsen Guizani",
      "Thang X. Vu"
    ],
    "year": 2025,
    "venue": "IEEE Access",
    "doi": "10.1109/ACCESS.2025.3572036",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/21/accepted_record",
    "local_text": "screening_46/text/C02.txt"
  },
  {
    "id": "C03",
    "title": "A LINK-LAYER MODEL OF A UAV SWARM MESH NETWORK WITH ENCAPSULATION OF INTERMEDIATE DEEP NEURAL NETWORK ACTIVATIONS: ANALYTICAL EVALUATION OF LATENCY AND TRAFFIC VOLUME",
    "authors": [
      "Artem Kasianchuk",
      "Halyna Lastivka"
    ],
    "year": 2026,
    "venue": "Infocommunication technologies and electronic engineering",
    "doi": "10.23939/ictee2026.02.144",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/reconciliation/results/identity_dates_01_accepted.json#records[id=C03]",
    "local_text": "screening_46/text/C03.txt"
  },
  {
    "id": "C04",
    "title": "A cognitive synergetic hierarchical framework for UAV swarm combat via speculative inference and role-decoupled reinforcement learning",
    "authors": [
      "Lixa Wang",
      "Yunqing Liu",
      "Linyang Guo",
      "Ran Zhang",
      "Yu Cui",
      "Yihan Cui",
      "Chunlin Xu"
    ],
    "year": 2026,
    "venue": "Frontiers in Neurorobotics",
    "doi": "10.3389/fnbot.2026.1799054",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/23/accepted_record",
    "local_text": "screening_46/text/C04.txt"
  },
  {
    "id": "C05",
    "title": "MARL-based Reliability-aware Video Analytics in Multi-UAV-Assisted MEC Systems",
    "authors": [
      "Hao Hao",
      "Changqiao Xu",
      "Wei Zhang",
      "Shujie Yang",
      "Xiaolong Wang",
      "Huiling Shi",
      "Gabriel-Miro Muntean"
    ],
    "year": 2026,
    "venue": "IEEE Transactions on Circuits and Systems for Video Technology",
    "doi": "10.1109/tcsvt.2026.3745821",
    "source_version": "author_manuscript",
    "identity_locator": "screening_46/reconciliation/results/identity_dates_01_accepted.json#records[id=C05]",
    "local_text": "screening_46/text/C05.txt"
  },
  {
    "id": "C06",
    "title": "Joint Model Partitioning and Bandwidth Allocation for UAV-Assisted Space–Air–Ground–Sea Integrated Network: A Hybrid A3C-PPO Approach",
    "authors": [
      "Yuanmo Lin",
      "Yuanyuan Han",
      "Minmin Wu",
      "Shaoyu Lin",
      "Xia Zhang",
      "Zhiyong Xu"
    ],
    "year": 2026,
    "venue": "Entropy",
    "doi": "10.3390/e28030337",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/25/accepted_record",
    "local_text": "screening_46/text/C06.txt"
  },
  {
    "id": "C07",
    "title": "A3D: Adaptive, Accurate, and Autonomous Navigation for Edge-Assisted Drones",
    "authors": [
      "Liekang Zeng",
      "Haowei Chen",
      "Daipeng Feng",
      "Xiaoxi Zhang",
      "Xu Chen"
    ],
    "year": 2024,
    "venue": "IEEE/ACM Transactions on Networking",
    "doi": "10.1109/TNET.2023.3297876",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/26/accepted_record",
    "local_text": "screening_46/text/C07.txt"
  },
  {
    "id": "C08",
    "title": "Adaptive Heuristics for Scheduling DNN Inferencing on Edge and Cloud for Personalized UAV Fleets",
    "authors": [
      "Suman Raj",
      "Radhika Mittal",
      "Harshil Gupta",
      "Yogesh Simmhan"
    ],
    "year": 2025,
    "venue": "Future Generation Computer Systems (supplied preprint: arXiv:2412.20860v2)",
    "doi": "10.1016/j.future.2025.107874",
    "source_version": "preprint",
    "identity_locator": "screening_46/reconciliation/results/identity_dates_01_accepted.json#records[id=C08]",
    "local_text": "screening_46/text/C08.txt"
  },
  {
    "id": "C09",
    "title": "NetMoE: Joint Trajectory Planning and Distributed Mixture-of-Experts Inference for UAV Swarms",
    "authors": [
      "HyungBin Park",
      "SuKyoung Lee"
    ],
    "year": 2026,
    "venue": "IEEE Internet of Things Journal",
    "doi": "10.1109/jiot.2026.3755315",
    "source_version": "author_manuscript",
    "identity_locator": "screening_46/reconciliation/results/identity_dates_01_accepted.json#records[id=C09]",
    "local_text": "screening_46/text/C09.txt"
  },
  {
    "id": "C10",
    "title": "A DRL-Assisted Decentralized Framework for UAV Swarm Collaborative Inference",
    "authors": [
      "Songwei Li",
      "Zhihan Wang",
      "Jiebei Shi",
      "Jiwei Huang"
    ],
    "year": 2026,
    "venue": "IEEE Internet of Things Journal",
    "doi": "10.1109/jiot.2026.3740035",
    "source_version": "author_manuscript",
    "identity_locator": "screening_46/reconciliation/results/identity_dates_01_accepted.json#records[id=C10]",
    "local_text": "screening_46/text/C10.txt"
  },
  {
    "id": "C11",
    "title": "Quantum-Enhanced Multi-Agent Reinforcement Learning for Ubiquitous LLM Inference via Embodied UAV Swarms",
    "authors": [
      "Xiangdong Zheng",
      "Long Luo",
      "Hongfang Yu",
      "Haoxiang Luo"
    ],
    "year": 2026,
    "venue": "IEEE Transactions on Cognitive Communications and Networking",
    "doi": "10.1109/TCCN.2026.3716252",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/30/accepted_record",
    "local_text": "screening_46/text/C11.txt"
  },
  {
    "id": "C12",
    "title": "SwarmChain: Collaborative LLM Inference for UAV Swarm Control",
    "authors": [
      "Biao Han",
      "Yitang Chen",
      "Jinrong Li",
      "Jie Li",
      "Jinshu Su"
    ],
    "year": 2025,
    "venue": "IEEE Internet of Things Magazine",
    "doi": "10.1109/MIOT.2025.3575886",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/31/accepted_record",
    "local_text": "screening_46/text/C12.txt"
  },
  {
    "id": "C13",
    "title": "RDI-LLM: A Resilient Distributed Inference Framework for LLMs in Resource-Constrained UAV Swarm",
    "authors": [
      "Shengjie Zhong",
      "Zhongliang Zhao",
      "Jingxuan Chen",
      "Xianbin Cao",
      "Zhiyi Liu",
      "Dapeng O. Wu",
      "Tony Q. S. Quek"
    ],
    "year": 2026,
    "venue": "IEEE Transactions on Vehicular Technology",
    "doi": "10.1109/tvt.2026.3755123",
    "source_version": "author_manuscript",
    "identity_locator": "screening_46/reconciliation/results/identity_dates_01_accepted.json#records[id=C13]",
    "local_text": "screening_46/text/C13.txt"
  },
  {
    "id": "C14",
    "title": "CIDER: Collaborative Inference with Distilled Early-Exit Routing for Multi-UAV Edge Networks",
    "authors": [
      "Lianming Xu",
      "Yixue Liang",
      "Lei Jin",
      "Li Wang",
      "Ying-Jun Angela Zhang",
      "Xiaoyu Zhao",
      "Aiguo Fei"
    ],
    "year": 2026,
    "venue": "IEEE Internet of Things Journal",
    "doi": "10.1109/jiot.2026.3746980",
    "source_version": "author_manuscript",
    "identity_locator": "screening_46/reconciliation/results/identity_dates_01_accepted.json#records[id=C14]",
    "local_text": "screening_46/text/C14.txt"
  },
  {
    "id": "C15",
    "title": "Deep Reinforcement Learning-Based Task Offloading With Collaborative Inference in UAV-Assisted Mobile Edge Computing Networks",
    "authors": [
      "Xiangping Bryce Zhai",
      "Shuang Fu",
      "Changyan Yi",
      "Zhiquan Liu",
      "Chao Dong",
      "Chee Wei Tan"
    ],
    "year": 2026,
    "venue": "IEEE Transactions on Intelligent Transportation Systems",
    "doi": "10.1109/TITS.2025.3629117",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/34/accepted_record",
    "local_text": "screening_46/text/C15.txt"
  },
  {
    "id": "C16",
    "title": "Secure Split Offloading and Trajectory Design for UAV-Assisted Multi-Exit Collaborative DNN Inference",
    "authors": [
      "Mengru Wu",
      "Haonan Wu",
      "Weidang Lu",
      "Zhaolong Ning",
      "Lei Guo",
      "Abbas Jamalipour"
    ],
    "year": 2026,
    "venue": "IEEE Transactions on Mobile Computing",
    "doi": "10.1109/TMC.2026.3708394",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/35/accepted_record",
    "local_text": "screening_46/text/C16.txt"
  },
  {
    "id": "C17",
    "title": "Heading-Coupled STAR-RIS Assisted Multi-UAV Networks for Semantic ISCC",
    "authors": [
      "Menghui Shen",
      "Honggui Deng",
      "Shujiang Zeng",
      "Jingyue Fang",
      "Yuxiang Deng",
      "Dehua Wu",
      "Yun Ou"
    ],
    "year": 2026,
    "venue": "IEEE Wireless Communications Letters",
    "doi": "10.1109/LWC.2026.3743641",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/36/accepted_record",
    "local_text": "screening_46/text/C17.txt"
  },
  {
    "id": "C18",
    "title": "Joint UAV Placement and Dependent Task Offloading in Multi-UAV MEC Networks: A Graph Attention Enhanced DRL Approach",
    "authors": [
      "Cheng Zhan",
      "Wei Liu",
      "Kaifeng Song",
      "Rongfei Fan",
      "Jun Liu",
      "Han Hu"
    ],
    "year": 2026,
    "venue": "IEEE Transactions on Mobile Computing",
    "doi": "10.1109/TMC.2025.3628608",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/37/accepted_record",
    "local_text": "screening_46/text/C18.txt"
  },
  {
    "id": "C19",
    "title": "PUF-enabled Self-Certified Authentication Protocol for Secure Cooperative Inference in UAV-Assisted Internet of Vehicles Environments",
    "authors": [
      "DeokKyu Kwon",
      "Ashok Kumar Das",
      "Youngho Park"
    ],
    "year": 2026,
    "venue": "IEEE Internet of Things Journal",
    "doi": "10.1109/jiot.2026.3755176",
    "source_version": "author_manuscript",
    "identity_locator": "screening_46/reconciliation/results/identity_dates_01_accepted.json#records[id=C19]",
    "local_text": "screening_46/text/C19.txt"
  },
  {
    "id": "C20",
    "title": "Multi-UAV cooperative inference for IoVs: Dynamic partitioning and caching optimization",
    "authors": [
      "Qiutian Xu",
      "Chao Yang",
      "Xuandong Lai",
      "Yi Liu",
      "Xin Chen"
    ],
    "year": 2026,
    "venue": "Ad Hoc Networks",
    "doi": "10.1016/j.adhoc.2026.104347",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/39/accepted_record",
    "local_text": "screening_46/text/C20.txt"
  },
  {
    "id": "C21",
    "title": "Toward Inference Latency Optimization for Scalable Collaborative Multi-UAV Analytics",
    "authors": [
      "Ying Wang",
      "Jingling Yuan",
      "Wenbo Wu",
      "Quanfeng Yao",
      "Donglei Xu",
      "Zhishu Shen"
    ],
    "year": 2026,
    "venue": "IEEE Transactions on Green Communications and Networking",
    "doi": "10.1109/TGCN.2025.3625726",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/40/accepted_record",
    "local_text": "screening_46/text/C21.txt"
  },
  {
    "id": "C22",
    "title": "Energy-Efficient Collaborative DNN Inference in UAV Swarm",
    "authors": [
      "Weiqing Ren",
      "Yuben Qu",
      "Zhen Qin",
      "Chao Dong",
      "Hao Sun",
      "Lei Zhang",
      "Qihui Wu"
    ],
    "year": 2023,
    "venue": "2023 9th International Conference on Big Data Computing and Communications (BIGCOM)",
    "doi": "10.1109/BIGCOM61073.2023.00034",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/41/accepted_record",
    "local_text": "screening_46/text/C22.txt"
  },
  {
    "id": "C23",
    "title": "Efficient Pipeline Collaborative DNN Inference in Resource-constrained UAV Swarm",
    "authors": [
      "Weiqing Ren",
      "Yuben Qu",
      "Zhen Qin",
      "Chao Dong",
      "Fuhui Zhou",
      "Lei Zhang",
      "Qihui Wu"
    ],
    "year": 2024,
    "venue": "2024 IEEE Wireless Communications and Networking Conference (WCNC)",
    "doi": "10.1109/WCNC57260.2024.10570535",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/42/accepted_record",
    "local_text": "screening_46/text/C23.txt"
  },
  {
    "id": "C24",
    "title": "Dynamic DNN Model Switching for Collaborative Edge Intelligence in UAV Swarm",
    "authors": [
      "Yu Li",
      "Yuben Qu",
      "Chao Dong",
      "Fuhui Zhou",
      "Lei Zhang",
      "Qihui Wu"
    ],
    "year": 2023,
    "venue": "2023 International Conference on Wireless Communications and Signal Processing (WCSP)",
    "doi": "10.1109/WCSP58612.2023.10405273",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/43/accepted_record",
    "local_text": "screening_46/text/C24.txt"
  },
  {
    "id": "C25",
    "title": "A hybrid fast inference approach with distributed neural networks for edge computing enabled UAV swarm",
    "authors": [
      "Peng Zhang",
      "Hui Tian",
      "Hao Luo",
      "XingWang Li",
      "GaoFeng Nie"
    ],
    "year": 2023,
    "venue": "Physical Communication",
    "doi": "10.1016/j.phycom.2023.102129",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/44/accepted_record",
    "local_text": "screening_46/text/C25.txt"
  },
  {
    "id": "SNCS",
    "title": "Learning-Based UAV Swarm Video Analytics Orchestration in Disaster Response Management",
    "authors": [
      "Tiying Gao",
      "Dwight Goins",
      "Chaise Ballotti",
      "Jiaqing Liu",
      "Chengyi Qu"
    ],
    "year": 2025,
    "venue": "SN Computer Science",
    "doi": "10.1007/s42979-025-04063-5",
    "source_version": "publisher_pdf",
    "identity_locator": "screening_46/consolidated/decision_ledger.json#/records/45/accepted_record",
    "local_text": "screening_46/text/SNCS.txt"
  }
]
