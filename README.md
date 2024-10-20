# AI Crew for Long COVID Research

## Introduction
This project demonstrates the use of the CrewAI framework to conduct comprehensive research on Long COVID. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently in the field of medical research.

By Jon Douglas

- [CrewAI Framework](#crewai-framework)
- [Project Overview](#project-overview)
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
  - `mechanisms.pdf`: A resource file in the root directory containing information on Long COVID mechanisms.

## Contributing
We welcome contributions to enhance the capabilities of this Long COVID research project. Please feel free to submit pull requests or open issues for discussion.

## Support and Contact
For questions, issues, or collaboration opportunities, please [contact information or link to issues page].

## License
This project is released under the [Your chosen license, e.g., MIT License].