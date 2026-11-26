const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
        Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType } = require('/tmp/node_modules/docx');
const fs = require('fs');

const NAVY = "1E2761";
const FONT = "Calibri";

const P = (text, opts = {}) => new Paragraph({
  spacing: { after: opts.after ?? 140, line: 276 },
  alignment: opts.align,
  indent: opts.indent,
  children: [ new TextRun({ text, font: FONT, size: opts.size ?? 22,
                            bold: opts.bold, italics: opts.italics, color: opts.color }) ]
});

const RICH = (runs, opts = {}) => new Paragraph({
  spacing: { after: opts.after ?? 140, line: 276 },
  children: runs.map(r => new TextRun({ text: r.t, font: FONT, size: r.size ?? 22,
                                        bold: r.b, italics: r.i, color: r.c }))
});

const H1 = (text) => new Paragraph({
  spacing: { before: 260, after: 140 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: NAVY, space: 4 } },
  children: [ new TextRun({ text, font: FONT, size: 26, bold: true, color: NAVY }) ]
});

const H2 = (text) => new Paragraph({
  spacing: { before: 200, after: 90 },
  children: [ new TextRun({ text, font: FONT, size: 23, bold: true, color: "2A3355" }) ]
});

const REF = (n, text) => new Paragraph({
  spacing: { after: 40, line: 240 },
  indent: { left: 400, hanging: 400 },
  children: [ new TextRun({ text: `[${n}] ${text}`, font: FONT, size: 18 }) ]
});

const cell = (text, opts = {}) => new TableCell({
  width: { size: opts.w, type: WidthType.DXA },
  shading: opts.shade ? { type: ShadingType.CLEAR, fill: opts.shade } : undefined,
  margins: { top: 60, bottom: 60, left: 100, right: 100 },
  children: [ new Paragraph({
    spacing: { after: 0, line: 240 },
    alignment: opts.align,
    children: [ new TextRun({ text, font: FONT, size: 18, bold: opts.b, italics: opts.i }) ]
  })]
});

const W = [1750, 6050, 1200];
const row = (a, b, c, opts = {}) => new TableRow({ children: [
  cell(a, { w: W[0], b: opts.b, i: opts.i, shade: opts.shade }),
  cell(b, { w: W[1], b: opts.b, i: opts.i, shade: opts.shade }),
  cell(c, { w: W[2], b: opts.b, align: AlignmentType.RIGHT, shade: opts.shade })
]});

const doc = new Document({
  creator: "Nguyen Minh Hieu",
  title: "AVSTC Seed Grant Application — Sections 5, 6 and 8",
  description: "Keeping inference alive: joint computation-communication optimisation and mid-inference recovery for UAV swarms",
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
  sections: [{
    properties: { page: { margin: { top: 1134, right: 1134, bottom: 1134, left: 1134 } } },
    children: [

      // ============ HEADER ============
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
        children: [ new TextRun({ text: "Australia–Vietnam Strategic Technologies Centre",
                                  font: FONT, size: 26, bold: true, color: NAVY }) ] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: NAVY, space: 6 } },
        children: [ new TextRun({ text: "Seed Grant Application — Sections 5, 6 and 8",
                                  font: FONT, size: 22, bold: true }) ] }),

      RICH([{ t: "Project title: ", b: true },
            { t: "Keeping inference alive: joint computation–communication optimisation and mid-inference recovery for UAV swarms" }]),
      RICH([{ t: "Dates (6 months): ", b: true }, { t: "1 November 2026 – 30 April 2027" }], { after: 200 }),

      // ============ SECTION 5 ============
      H1("SECTION 5 — PROJECT PROPOSAL"),

      H2("Why this problem"),
      P("Every storm season, ground communications in Vietnam fail in exactly the places that need them most. Rescue teams arrive. The network does not. That setting is what I care about, and it rules out the two obvious ways of giving a UAV useful AI. Running a modern detection model on one small aircraft breaks its size, weight and power budget. Streaming the video to a server assumes a link that has just gone down."),
      P("The alternative is to split the model across several aircraft, so the swarm runs what no single machine can [1]–[3]. People have shown this works. Two problems remain, and they are why I am asking for this grant."),
      P("The first is that you cannot choose where to cut a model without also deciding what you will pay to transmit. Cut early and the intermediate tensor is large, sometimes larger than the input image. Cut deep and one aircraft ends up carrying most of the computation. Over a flying ad-hoc network whose links change as the aircraft move, those two costs are tangled [4], [5], and optimising them separately gives something up."),
      P("The second problem interests me more, and less has been written about it. Work on reliability here either picks a robust configuration before take-off [6], [7], or re-plans for the next task once conditions change [8]–[10]. Neither helps the inference that was already running when an aircraft went down. There is no defined way to recover it. In practice it starts again from the first layer, and work that was already finished correctly is thrown away."),

      H2("What I am proposing to do in six months, and what I am not"),
      P("I defended my doctoral proposal on this problem in July 2026, over a three-year horizon. This grant would fund its first slice, and I want to be honest about how big that slice is."),
      P("In scope: a measurement-based evaluation setup, a working joint optimiser, and a first attempt at recovering an inference that was interrupted."),
      P("Out of scope: full robotics co-simulation with ROS and Gazebo, and a properly validated online control plane. Both belong to later years of the thesis. Six months of a first-year student's time does not buy them, and I would rather promise less and deliver it."),

      H2("The work"),
      RICH([{ t: "Months 1–2. ", b: true },
            { t: "Measure before modelling. I will profile detection models from the YOLO and ResNet families on Jetson-class hardware to get per-layer latency, energy draw and activation size. Those measurements then drive an NS-3 simulation of the swarm, so that the compute delays in my experiments come from a real board rather than an assumption. The milestone is plain: an end-to-end inference pipeline running across simulated aircraft on measured costs." }]),
      RICH([{ t: "Months 3–4. ", b: true },
            { t: "Write the objective down properly — latency plus a weighted energy term, over the cut points and the assignment of segments to aircraft, subject to what each machine can hold and how good the links are. Solve it exactly for small K by enumeration and greedily above that; the closely related problem has been shown to be NP-hard [11], which is why K stays bounded. Then sweep K, swarm size and link quality to find where the trade-off flips from \"more cuts help\" to \"more cuts cost\". I do not know where that boundary sits. Finding it is the point." }]),
      RICH([{ t: "Months 5–6. ", b: true },
            { t: "Kill an aircraft in the middle of a running inference and try to save the job: work out new cut boundaries for the part of the model that has not run yet, over whatever topology is left, and carry on from the last activation that got through. Compare that against restarting from scratch, and report how much recomputation was avoided and under what conditions it stopped being worth doing. Then write the paper with my Australian collaborator and release the code and the profiling data." }]),

      H2("What comes out of it"),
      P("Two artefacts I expect other people to use: the profiling dataset, and the NS-3 harness with the scenario files that go with it. Both public. On top of those, the optimiser and a first empirical picture of how K behaves, and the recovery demonstration with numbers attached to it. One conference paper, co-authored. A technical report and a demonstration for industry partners."),

      H2("Why it matters, and what could go wrong"),
      P("Saving your place and carrying on is ordinary in datacentre training. It is missing from inference on aerial networks, where the saved place is a tensor sitting on an aircraft that is still moving, and where the replanning is itself an optimisation problem. A recent systematic review reports that the joint handling of computation and networking in UAV offloading remains open [12]. For Vietnam the practical version is blunt: when the ground network is gone, the swarm has to keep seeing, and it has to keep seeing after it loses a member."),
      P("Two things could go wrong. If the hardware is slow to arrive, months 1 and 2 run on published benchmarks and I substitute measured traces once the boards land; the design of the harness does not change. If recovery turns out to be too slow to be practical inside six months, then the deliverable becomes an honest measurement of how slow it is — which is still worth knowing, and feeds directly into the next phase of the thesis."),

      new Paragraph({ spacing: { before: 200, after: 100 },
        children: [ new TextRun({ text: "References", font: FONT, size: 21, bold: true, color: NAVY }) ] }),
      REF(1, "Y. Kang et al., “Neurosurgeon: Collaborative intelligence between the cloud and mobile edge,” in Proc. ASPLOS, 2017, pp. 615–629."),
      REF(2, "C. Hu, W. Bao, D. Wang, and F. Liu, “Dynamic adaptive DNN surgery for inference acceleration on the edge,” in Proc. IEEE INFOCOM, 2019, pp. 1423–1431."),
      REF(3, "Y. Qu et al., “Elastic collaborative edge intelligence for UAV swarm: Architecture, challenges, and opportunities,” IEEE Commun. Mag., vol. 62, no. 1, pp. 62–68, 2024."),
      REF(4, "G. Amponis et al., “A survey on FANET routing from a cross-layer design perspective,” J. Syst. Archit., vol. 120, p. 102281, 2021."),
      REF(5, "J. Shao, Y. Mao, and J. Zhang, “Learning task-oriented communication for edge inference: An information bottleneck approach,” IEEE J. Sel. Areas Commun., vol. 40, no. 1, pp. 197–211, 2022."),
      REF(6, "M. Zhao, X. Zhang, Z. Meng, and X. Hou, “Reliable DNN partitioning for UAV swarm,” in Proc. IWCMC, 2022."),
      REF(7, "M. Dhuheir, A. Erbad, and S. Sabeeh, “LLHR: Low latency and high reliability CNN distributed inference for resource-constrained UAV swarms,” in Proc. IEEE WCNC, 2023, pp. 1–6."),
      REF(8, "K. Gao et al., “Cooperative DNN partitioning in energy-harvesting and MEC-enabled AAV networks,” IEEE Internet Things J., 2025."),
      REF(9, "S. Meng, B. Li, Z. Yi, L. Liu, and Z. Fei, “DNN task partitioning and migration strategies in multi-UAV-assisted mobile edge computing,” IEEE Internet Things J., vol. 13, no. 13, pp. 28758–28769, 2026."),
      REF(10, "J. Kim et al., “End-to-end latency optimization for resilient distributed CNN inference in resource-constrained UAV swarms,” Appl. Sci., vol. 14, no. 23, p. 10832, 2024."),
      REF(11, "L. Wang, J. Wang, and C. Dai, “DNN-based task partitioning and offloading with reliability guarantees in multi-UAV-assisted MEC system,” in Proc. IEEE ISPCE-ASIA, 2024."),
      REF(12, "A. Baktayan, A. T. Zahary, A. Sikora, and D. Welte, “Computational offloading into UAV swarm networks: A systematic literature review,” EURASIP J. Wireless Commun. Netw., vol. 2024, p. 69, 2024."),

      // ============ SECTION 6 ============
      new Paragraph({ pageBreakBefore: true, children: [] }),
      H1("SECTION 6 — IMPACT AND COLLABORATION"),

      H2("How this benefits the Australia–Vietnam collaboration  (max 300 words)"),
      P("I have tried to design this so that neither side could finish it alone, and so that something concrete survives the six months."),
      P("The concrete thing is the harness and the profiling data: documented, public, with the scenario files that produced the numbers. Once that exists, anyone in the AVSTC network working on aerial edge intelligence has a common starting point instead of building one from nothing. On its own that is a small contribution. It compounds."),
      P("The division of labour is real rather than nominal. The Australian side brings depth in wireless networking and in optimisation methods that I do not have yet. I bring the embedded and UAV platform work, and the problem itself. Vietnam's storm season supplies failure conditions that are hard to justify inventing if you work somewhere the infrastructure stays up. That asymmetry is what makes the collaboration worth having in both directions rather than one."),
      P("For continuity I have built in three things that leave evidence behind: a paper written together, a repository we both commit to, and a demonstration shown to industry partners rather than only to academics. Intentions to collaborate are cheap. A shared commit history is not."),
      P("The topic sits inside the Centre's priority areas and inside the resilience theme of Phase II. If it works, the next proposal is the obvious larger one: from simulation to full co-simulation and then to flight trials, with results, code and a working relationship already in hand to justify asking."),

      H2("What this would do for my career  (max 200 words)"),
      P("I am in the first year of a PhD at Ho Chi Minh City University of Technology, working on adaptive computation–communication orchestration for UAV swarms. I defended the proposal in July."),
      P("Three things would change."),
      P("My work would stop being a single-institution thesis. Publishing with an Australian co-author at an international venue matters most now, before there is a record to speak for me."),
      P("I would learn things a thesis does not teach: releasing software that other people depend on, running a funded project against deliverables and a payment schedule, and reporting to a committee that is allowed to say no. That is the difference between someone who can do research and someone who can run it."),
      P("And I would have a working relationship with a group in Australia in my own area. That is the realistic route to joint supervision, to a postdoctoral position, and eventually to leading a bilateral proposal myself. I would like to keep doing research in Vietnam while working inside an international network. This is the first concrete step I can take toward that."),

      // ============ SECTION 8 ============
      new Paragraph({ pageBreakBefore: true, children: [] }),
      H1("SECTION 8 — BUDGET (6 MONTHS)"),
      P("Everything below is R&D spending required by the activities in Section 5. I have arranged it so the two payment tranches line up with two distinct phases of the work.", { after: 180 }),

      new Table({
        columnWidths: W,
        width: { size: W[0] + W[1] + W[2], type: WidthType.DXA },
        rows: [
          row("Item", "Why it is needed", "AUD", { b: true, shade: "E8EDFB" }),

          new TableRow({ children: [ new TableCell({
            columnSpan: 3, width: { size: 9000, type: WidthType.DXA },
            shading: { type: ShadingType.CLEAR, fill: "F5F7FC" },
            margins: { top: 50, bottom: 50, left: 100, right: 100 },
            children: [ new Paragraph({ spacing: { after: 0 }, children: [
              new TextRun({ text: "Tranche 1 — on signing (Months 1–4)", font: FONT, size: 18, bold: true, italics: true }) ] }) ]
          })]}),

          row("Edge computing hardware",
              "Three Jetson-class developer kits with storage, power and wireless modules. The whole method is measurement-driven: every compute delay in the harness comes from these boards. Without them the evaluation rests on assumption instead of data.",
              "2,200"),
          row("Power and radio measurement",
              "Power measurement modules, antennas and radio accessories, so per-layer energy comes from a meter and link behaviour is calibrated against something physical rather than a simulator default.",
              "1,200"),
          row("Simulation compute",
              "GPU workstation upgrade or cloud compute for the parameter sweeps in Months 3–4. Mapping the trade-off surface across K, swarm size, mobility and link quality takes thousands of runs.",
              "3,000"),
          row("Research assistant",
              "A part-time undergraduate or master's assistant for six months, on harness development, scenario scripting and experiment automation. This is what frees my own time for the formulation and the analysis.",
              "3,600"),
          row("", "Subtotal, Tranche 1 (two thirds)", "10,000", { b: true }),

          new TableRow({ children: [ new TableCell({
            columnSpan: 3, width: { size: 9000, type: WidthType.DXA },
            shading: { type: ShadingType.CLEAR, fill: "F5F7FC" },
            margins: { top: 50, bottom: 50, left: 100, right: 100 },
            children: [ new Paragraph({ spacing: { after: 0 }, children: [
              new TextRun({ text: "Tranche 2 — on final report (Months 5–6)", font: FONT, size: 18, bold: true, italics: true }) ] }) ]
          })]}),

          row("Publication",
              "Conference registration and the open-access charge for the co-authored paper. Open access matters here because the point is for AVSTC partners to be able to read and reuse it without a subscription.",
              "2,200"),
          row("Collaboration travel",
              "One economy return airfare and accommodation for a two-week working visit with the Australian collaborator: joint experiment design, handing over the harness, and writing the paper. This is the part that turns a nominal partnership into a working one.",
              "2,400"),
          row("Data and code release",
              "Documentation, dataset hosting with a persistent identifier, and demonstration material for industry partners.",
              "400"),
          row("", "Subtotal, Tranche 2 (one third)", "5,000", { b: true }),
          row("", "TOTAL REQUESTED", "15,000", { b: true, shade: "E8EDFB" }),
        ]
      }),

      P("", { after: 120 }),
      P("A few notes. Nothing here duplicates equipment the host institution already has; the boards are specific to SWaP-representative profiling and stay in the lab afterwards for follow-on work. Tranche 1 covers everything needed to produce the harness, the optimiser and its evaluation, so a delay in the second payment cannot stall the technical work. And if any category turns out to be ineligible under the grant conditions, I would move that amount to simulation compute, which deepens the parameter study without changing what I have promised to deliver.", { size: 20 }),
    ]
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("AVSTC_SeedGrant_Proposal.docx", buf);
  console.log("written");
});
