# AI Crew for Long COVID Research

## Introduction
This project demonstrates the use of the CrewAI framework to conduct comprehensive research on Long COVID. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently in the field of medical research.

By Jon Douglas

## Table of Contents
- [CrewAI Framework](#crewai-framework)
- [Project Overview](#project-overview)
- [Agents](#agents)
- [Tasks](#tasks)
- [Goals](#goals)
- [Running the Script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Contributing](#contributing)
- [Support and Contact](#support-and-contact)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this project, these agents work together to investigate leading hypotheses, therapeutics, and combination treatments for Long COVID.

## Project Overview
This AI-driven research project aims to:
- Identify and evaluate leading hypotheses of Long COVID mechanisms
- Assess potential therapeutics targeting these mechanisms
- Develop unique combination treatment strategies
- Analyze data trends in Long COVID research
- Compile a comprehensive report with findings and recommendations

## Agents
The project utilizes several specialized AI agents, each with a unique role:

1. **Lead Medical Researcher** (Michael J. Peluso): Conducts comprehensive literature reviews on Long COVID mechanisms.
2. **Pharmacology Expert** (Big Pharma): Identifies and evaluates novel therapeutics for Long COVID.
3. **Treatment Strategy Analyst** (Steven G. Deeks): Develops innovative combination treatment strategies.
4. **Data Analyst** (Hannah Davis): Processes and analyzes data to identify trends and patterns.
5. **Project Manager** (Amy Proal): Oversees the project and ensures collaboration among agents.
6. **Immunology Specialist** (Akiko Iwasaki): Investigates immune responses associated with Long COVID.
7. **Virology Expert** (Diane Griffin): Explores viral persistence in Long COVID cases.
8. **Epidemiology Analyst** (Ziyad Al-Aly): Analyzes epidemiological data related to Long COVID.
9. **Cardiology Specialist** (Eric Topol): Investigates cardiovascular complications in Long COVID.
10. **Neurology Expert** (Serena Spudich): Examines neurological manifestations of Long COVID.
11. **Microbiome Specialist** (Maayan Levy): Studies the impact of Long COVID on the gut microbiome.
12. **Metabolism Expert** (David Systrom): Investigates metabolic disruptions in Long COVID patients.
13. **Science Writer** (Ed Yong): Communicates research findings in an accessible way for a general audience.
14. **Genomics and Transcriptomics Specialist** (Nevan Krogan): Analyzes gene expression profiles in Long COVID patients.

## Tasks
The project is divided into several key tasks:

1. Analyze epidemiological data
2. Apply advanced immunological techniques
3. Analyze spike protein translocation
4. Study transcriptomics
5. Investigate immune responses
6. Explore viral persistence
7. Investigate metabolic disruptions
8. Investigate NK and T cell dynamics
9. Research latent viral infections
10. Analyze microbiome impact
11. Assess cardiovascular complications
12. Investigate neurological manifestations
13. Analyze data trends
14. Conduct mechanism research
15. Update shared memory
16. Ensure quality and alignment
17. Facilitate collaboration
18. Identify therapeutics
19. Develop combination treatments
20. Compile final report
21. Plan future research

## Goals
The main goals of this project are to:

1. Identify and critically evaluate up to 15 leading hypotheses of Long COVID mechanisms.
2. Identify, evaluate, and prioritize up to 20 novel therapeutics targeting these mechanisms.
3. Explore and assess 5 experimental, cutting-edge therapeutics.
4. Develop and propose up to 10 innovative combination treatment strategies.
5. Provide detailed mechanistic rationales and supporting evidence for each therapeutic and combination treatment.
6. Analyze epidemiological and clinical data to identify significant trends and patterns.
7. Compile a comprehensive report with findings, rationales, and actionable recommendations.
8. Review and analyze data from acute COVID-19 therapeutic trials for potential application in Long COVID treatment.
9. Identify and justify the inclusion of any acute COVID-19 therapeutics that showed no individual effect but have potential in combination treatments.

## Running the Script
It uses `gpt-4o-mini` by default, so you should setup an [OpenAI developer account](https://platform.openai.com/docs/overview) to run it.

- **Configure Environment**: Copy `.env.example` or configure your environment variables for [OpenAI](https://platform.openai.com/api-keys) and other tools as needed.
- **Install Dependencies**: Run `crewai install` and read the [CLI documentation](https://docs.crewai.com/concepts/cli).
- **Customize**: Modify `src/longcovid/main.py` to add custom inputs for your agents and tasks.
- **Customize Further**: Check `src/longcovid/config/agents.yaml` to update your agents and `src/longcovid/config/tasks.yaml` to update your tasks.
- **Custom Tools**: You can find custom tools at `src/longcovid/tools/`.
- **Execute the Script**: Run `crewai run`

## Details & Explanation
- **Running the Script**: Execute `crewai run`. The script will leverage the CrewAI framework to automate research tasks and generate a detailed report on Long COVID.
- **Key Components**:
  - `src/longcovid/main.py`: Main script file.
  - `src/longcovid/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/longcovid/config/agents.yaml`: Configuration file for defining agents (e.g., lead medical researcher, pharmacology expert).
  - `src/longcovid/config/tasks.yaml`: Configuration file for defining tasks (e.g., conduct mechanism research, identify therapeutics).
  - `src/longcovid/tools`: Contains tool classes used by the agents, currently empty as we don't use any custom tools.
  - `mechanisms.pdf`: A resource file in the root directory containing information on Long COVID mechanisms by Peluso and Deeks.

## Mermaid Diagram
[![](https://mermaid.ink/img/pako:eNqNVctu2zAQ_BWCQHpKAkm2_DoUMOIENVq3aez2ULkHRtrYRCiSJakgSpB_75KyHSmPohfClmZ2Z2dH0iPNVQF0QjeG6S1ZzdZyLY-OyDe5UVxuyIrZW7uWtrpuAC-uE7JKsx-6YA7IcssMFGQBpTJ1APwOgEF2jnwD5HvFBHc1YbIgU8E3sgTpGiA5OfmIpQJ-lF2wnCPSFz1TQrBrZZjjSu6Lgix2MueSO84EmTHHAhbyAPQtFuC2qlBCbWoygzsQSvuGrWHeY394n4v6kjibai1qMi3umMxx5HlZVtKDeY7VVpBvJf9TgW2ZMM6mkon6Aci55gWU_AAPzV8NttSQozT-gOWvwAIz-fbVMv4Fwp7xMFu6qsBdGCZtbrh2quS5bVuexM1M0UHfUvNbIJdGOeCyoQqVt_zvEOMom8s7sI5v_LqCE-DFaCUtdFrFQzT2wBt1eF8_h5WtyBkItKSW7KXQLrt_kLvguVHXXJW-uWa565IaeNpphsvFSAmekxm3ptJ-NPsWLc7O77VQGN2f3OCqLsFYbh3g0jtWRA18nB2W8AX7YLYb2lzeNMGyb7GSbGrRKUvOmCm4umM2rwQzmMdSo0bWIjaEXtc5qMwhSwsm-Q3e6pKeUxWyFpzDORrHDd4l8wLV8ptdt7VcPfvbxNOjOurHfhtxFM44nEk4e-HshzMN5yic452CBT4cKNKWz4H1Mj7VWrkteFUXypR7GXF2pmRR4VLf4LXUhH7_L2nYFhZiFe3DFUSutoDPF1TOR6T99K-SbGdV3QZ1w4OwXraj-S1ec7l7egww5wt1c7BregVaGeffrd6Qi8r5V-alYFLiNaw5zHwiuABygQXFDt_pHIbwRxh54A0cZL7Evtxb3g3pMS0BPecFfgYefcbWFHdRwppO8GfBzO2aruUT4ljl1LKWOZ04U8ExNarabOnkhgmL_6rwHZhxhm-ncg_RTP5Sqv2XTh7pPZ2c9AanvSiKxoNRP037yah_TGs6SdPTaJyM0yHeS_uDQb__dEwfQoX4NB6nvXSYjEbDQS9Onv4CUKo3SQ?type=png)](https://mermaid.live/edit#pako:eNqNVctu2zAQ_BWCQHpKAkm2_DoUMOIENVq3aez2ULkHRtrYRCiSJakgSpB_75KyHSmPohfClmZ2Z2dH0iPNVQF0QjeG6S1ZzdZyLY-OyDe5UVxuyIrZW7uWtrpuAC-uE7JKsx-6YA7IcssMFGQBpTJ1APwOgEF2jnwD5HvFBHc1YbIgU8E3sgTpGiA5OfmIpQJ-lF2wnCPSFz1TQrBrZZjjSu6Lgix2MueSO84EmTHHAhbyAPQtFuC2qlBCbWoygzsQSvuGrWHeY394n4v6kjibai1qMi3umMxx5HlZVtKDeY7VVpBvJf9TgW2ZMM6mkon6Aci55gWU_AAPzV8NttSQozT-gOWvwAIz-fbVMv4Fwp7xMFu6qsBdGCZtbrh2quS5bVuexM1M0UHfUvNbIJdGOeCyoQqVt_zvEOMom8s7sI5v_LqCE-DFaCUtdFrFQzT2wBt1eF8_h5WtyBkItKSW7KXQLrt_kLvguVHXXJW-uWa565IaeNpphsvFSAmekxm3ptJ-NPsWLc7O77VQGN2f3OCqLsFYbh3g0jtWRA18nB2W8AX7YLYb2lzeNMGyb7GSbGrRKUvOmCm4umM2rwQzmMdSo0bWIjaEXtc5qMwhSwsm-Q3e6pKeUxWyFpzDORrHDd4l8wLV8ptdt7VcPfvbxNOjOurHfhtxFM44nEk4e-HshzMN5yic452CBT4cKNKWz4H1Mj7VWrkteFUXypR7GXF2pmRR4VLf4LXUhH7_L2nYFhZiFe3DFUSutoDPF1TOR6T99K-SbGdV3QZ1w4OwXraj-S1ec7l7egww5wt1c7BregVaGeffrd6Qi8r5V-alYFLiNaw5zHwiuABygQXFDt_pHIbwRxh54A0cZL7Evtxb3g3pMS0BPecFfgYefcbWFHdRwppO8GfBzO2aruUT4ljl1LKWOZ04U8ExNarabOnkhgmL_6rwHZhxhm-ncg_RTP5Sqv2XTh7pPZ2c9AanvSiKxoNRP037yah_TGs6SdPTaJyM0yHeS_uDQb__dEwfQoX4NB6nvXSYjEbDQS9Onv4CUKo3SQ)

## Contributing
We welcome contributions to enhance the capabilities of this Long COVID research project. Please feel free to submit pull requests or open issues for discussion.

## Support and Contact
For questions, issues, or collaboration opportunities, please https://x.com/atranscendedman or @JonDouglas on GitHub.

## License
This project is released under the MIT License. See [LICENSE.md](./LICENSE.md) for details.
