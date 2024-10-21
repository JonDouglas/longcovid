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

1. **Lead Medical Researcher**: Conducts comprehensive literature reviews on Long COVID mechanisms.
2. **Pharmacology Expert**: Identifies and evaluates novel therapeutics for Long COVID.
3. **Treatment Strategy Analyst**: Develops innovative combination treatment strategies.
4. **Data Analyst**: Processes and analyzes data to identify trends and patterns.
5. **Project Manager**: Oversees the project and ensures collaboration among agents.
6. **Immunology Specialist**: Investigates immune responses associated with Long COVID.
7. **Virology Expert**: Explores viral persistence in Long COVID cases.
8. **Epidemiology Analyst**: Analyzes epidemiological data related to Long COVID.
9. **Cardiology Specialist**: Investigates cardiovascular complications in Long COVID.
10. **Neurology Expert**: Examines neurological manifestations of Long COVID.
11. **Microbiome Specialist**: Studies the impact of Long COVID on the gut microbiome.
12. **Metabolism Expert**: Investigates metabolic disruptions in Long COVID patients.

## Tasks
The project is divided into several key tasks:

1. Conduct mechanism research
2. Identify therapeutics
3. Develop combination treatments
4. Analyze data trends
5. Update shared memory
6. Ensure quality and alignment
7. Compile final report
8. Facilitate collaboration
9. Analyze epidemiological data
10. Investigate immune responses
11. Explore viral persistence
12. Assess cardiovascular complications
13. Investigate neurological manifestations
14. Analyze microbiome impact
15. Investigate metabolic disruptions
16. Plan future research

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
It uses GPT-4o-mini by default, so you should have access to that to run it.

- **Configure Environment**: Copy `.env.example` and set up the environment variables for [OpenAI](https://platform.openai.com/api-keys) and other tools as needed.
- **Install Dependencies**: Run `poetry lock && poetry install`.
- **Customize**: Modify `src/longcovid/main.py` to add custom inputs for your agents and tasks.
- **Customize Further**: Check `src/longcovid/config/agents.yaml` to update your agents and `src/longcovid/config/tasks.yaml` to update your tasks.
- **Custom Tools**: You can find custom tools at `src/longcovid/tools/`.
- **Execute the Script**: Run `poetry run longcovid` and input your project details.

## Details & Explanation
- **Running the Script**: Execute `poetry run longcovid`. The script will leverage the CrewAI framework to automate research tasks and generate a detailed report on Long COVID.
- **Key Components**:
  - `src/longcovid/main.py`: Main script file.
  - `src/longcovid/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/longcovid/config/agents.yaml`: Configuration file for defining agents (e.g., lead medical researcher, pharmacology expert).
  - `src/longcovid/config/tasks.yaml`: Configuration file for defining tasks (e.g., conduct mechanism research, identify therapeutics).
  - `src/longcovid/tools`: Contains tool classes used by the agents, including custom tools like MarkdownSaveTool.
  - `mechanisms.pdf`: A resource file in the root directory containing information on Long COVID mechanisms by Peluso and Deeks.

## Contributing
We welcome contributions to enhance the capabilities of this Long COVID research project. Please feel free to submit pull requests or open issues for discussion.

## Support and Contact
For questions, issues, or collaboration opportunities, please [contact information or link to issues page].

## License
This project is released under the MIT License.
