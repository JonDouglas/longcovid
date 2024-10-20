from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, WebsiteSearchTool, PDFSearchTool
from langchain_openai import ChatOpenAI
from langchain_community.tools.pubmed.tool import PubmedQueryRun

@CrewBase
class LongCovidCrew():
    """Collaborative Multi-Agent System for Long COVID Research Report"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o-mini")

    @agent
    def lead_medical_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_medical_researcher'],
            tools=[
                PubmedQueryRun(),     # Access to PubMed for literature review
                WebsiteSearchTool(),      # Enables general web searches
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),       # Enables advanced web search capabilities
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )
    
    @agent
    def immunology_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['immunology_specialist'],
            tools=[
                PubmedQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def virology_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['virology_expert'],
            tools=[
                PubmedQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def epidemiology_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['epidemiology_analyst'],
            tools=[
                PubmedQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def cardiology_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['cardiology_specialist'],
            tools=[
                PubmedQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def neurology_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['neurology_expert'],
            tools=[
                PubmedQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def microbiome_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['microbiome_specialist'],
            tools=[
                PubmedQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def metabolism_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['metabolism_expert'],
            tools=[
                PubmedQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def pharmacology_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['pharmacology_expert'],
            tools=[
                PubmedQueryRun(),     # Access to PubMed for pharmacological studies
                WebsiteSearchTool(),      # Enables web searches for drug information
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),       # Advanced searches for clinical trials and drug databases
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def treatment_strategy_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['treatment_strategy_analyst'],
            tools=[
                WebsiteSearchTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),       # Optional: Enables searches for treatment guidelines
                # You may add Drug Interaction Checker tools if available
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analyst'],
            tools=[
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],  # Statistical tools can be integrated if needed
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            allow_code_execution=True,
        )

    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['project_manager'],
            # tools=[MarkdownSaveTool()],
            allow_delegation=True,  # Can delegate tasks and facilitate collaboration
            verbose=True,
            llm=self.llm
        )

    @task
    def conduct_mechanism_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['conduct_mechanism_research_task'],
            agent=self.lead_medical_researcher(),
            # context=[
            #     self.immunology_specialist(),
            #     self.virology_expert(),
            #     self.cardiology_specialist(),
            #     self.neurology_expert(),
            #     self.microbiome_specialist(),
            #     self.metabolism_expert(),
            # ],
            output_file='reports/conduct_mechanism_research_task.md'
        )

    @task
    def identify_therapeutics_task(self) -> Task:
        return Task(
            config=self.tasks_config['identify_therapeutics_task'],
            agent=self.pharmacology_expert(),
            context=[
                self.conduct_mechanism_research_task(),
                self.investigate_immune_responses_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task()
            ],
            dependencies=[
                self.conduct_mechanism_research_task(),
                self.investigate_immune_responses_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task()
            ],
            output_file='reports/identify_therapeutics_task.md'
        )

    @task
    def develop_combination_treatments_task(self) -> Task:
        return Task(
            config=self.tasks_config['develop_combination_treatments_task'],
            agent=self.treatment_strategy_analyst(),
            context=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
            ],
            dependencies=[
                self.identify_therapeutics_task(),
                self.conduct_mechanism_research_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
            ],
            output_file='reports/develop_combination_treatments_task.md'
        )

    @task
    def analyze_data_trends_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_data_trends_task'],
            agent=self.data_analyst(),
            context=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
            ],
            dependencies=[
                self.develop_combination_treatments_task(),
                self.identify_therapeutics_task(),
                self.conduct_mechanism_research_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
            ],
            output_file='reports/analyze_data_trends_task.md'
        )

    @task
    def update_shared_memory_task(self) -> Task:
        return Task(
            config=self.tasks_config['update_shared_memory_task'],
            agent=self.project_manager(),
            context=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
                self.analyze_data_trends_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
                # Removed self.facilitate_collaboration_task() to prevent circular dependency
            ],
            dependencies=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
                self.analyze_data_trends_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
            ]
        )

    @task
    def ensure_quality_and_alignment_task(self) -> Task:
        return Task(
            config=self.tasks_config['ensure_quality_and_alignment_task'],
            agent=self.project_manager(),
            context=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
                self.analyze_data_trends_task(),
                self.update_shared_memory_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
                # Removed self.facilitate_collaboration_task() to prevent circular dependency
            ],
            dependencies=[
                self.update_shared_memory_task()
                # Removed self.facilitate_collaboration_task() to prevent circular dependency
            ],
            output_file='reports/ensure_quality_and_alignment_task.md'
        )

    @task
    def compile_final_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['compile_final_report_task'],
            agent=self.project_manager(),
            context=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
                self.analyze_data_trends_task(),
                self.ensure_quality_and_alignment_task(),
                self.update_shared_memory_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
            ],
            dependencies=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
                self.analyze_data_trends_task(),
                self.ensure_quality_and_alignment_task(),
                self.update_shared_memory_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
            ],
            output_file='reports/compile_final_report_task.md'
        )

    @task
    def facilitate_collaboration_task(self) -> Task:
        return Task(
            config=self.tasks_config['facilitate_collaboration_task'],
            agent=self.project_manager(),
            context=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
                self.analyze_data_trends_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
                # Removed self.compile_final_report_task() to prevent circular dependency
            ],
            dependencies=[
                # Include dependencies if necessary
            ]
        )
    
    @task
    def analyze_epidemiological_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_epidemiological_data_task'],
            agent=self.epidemiology_analyst(),
            output_file='reports/analyze_epidemiological_data_task.md'
        )

    @task
    def investigate_immune_responses_task(self) -> Task:
        return Task(
            config=self.tasks_config['investigate_immune_responses_task'],
            agent=self.immunology_specialist(),
            context=[self.conduct_mechanism_research_task()],
            dependencies=[self.conduct_mechanism_research_task()],
            output_file='reports/investigate_immune_responses_task.md'
        )

    @task
    def explore_viral_persistence_task(self) -> Task:
        return Task(
            config=self.tasks_config['explore_viral_persistence_task'],
            agent=self.virology_expert(),
            context=[self.conduct_mechanism_research_task()],
            dependencies=[self.conduct_mechanism_research_task()],
            output_file='reports/explore_viral_persistence_task.md'
        )

    @task
    def assess_cardiovascular_complications_task(self) -> Task:
        return Task(
            config=self.tasks_config['assess_cardiovascular_complications_task'],
            agent=self.cardiology_specialist(),
            context=[self.conduct_mechanism_research_task()],
            dependencies=[self.conduct_mechanism_research_task()],
            output_file='reports/assess_cardiovascular_complications_task.md'
        )

    @task
    def investigate_neurological_manifestations_task(self) -> Task:
        return Task(
            config=self.tasks_config['investigate_neurological_manifestations_task'],
            agent=self.neurology_expert(),
            context=[self.conduct_mechanism_research_task()],
            dependencies=[self.conduct_mechanism_research_task()],
            output_file='reports/investigate_neurological_manifestations_task.md'
        )

    @task
    def analyze_microbiome_impact_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_microbiome_impact_task'],
            agent=self.microbiome_specialist(),
            context=[self.conduct_mechanism_research_task()],
            dependencies=[self.conduct_mechanism_research_task()],
            output_file='reports/analyze_microbiome_impact_task.md'
        )

    @task
    def investigate_metabolic_disruptions_task(self) -> Task:
        return Task(
            config=self.tasks_config['investigate_metabolic_disruptions_task'],
            agent=self.metabolism_expert(),
            context=[self.conduct_mechanism_research_task()],
            dependencies=[self.conduct_mechanism_research_task()],
            output_file='reports/investigate_metabolic_disruptions_task.md'
        )

    @task
    def plan_future_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_future_research_task'],
            agent=self.lead_medical_researcher(),
            dependencies=[
                self.compile_final_report_task(),
                self.ensure_quality_and_alignment_task()
            ]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Long COVID research crew for producing a comprehensive report"""
        return Crew(
            agents=[
                self.lead_medical_researcher(),
                self.pharmacology_expert(),
                self.treatment_strategy_analyst(),
                self.data_analyst(),
                self.project_manager(),
                self.immunology_specialist(),
                self.virology_expert(),
                self.epidemiology_analyst(),
                self.cardiology_specialist(),
                self.neurology_expert(),
                self.microbiome_specialist(),
                self.metabolism_expert(),
            ],
            tasks=[
                self.conduct_mechanism_research_task(),
                self.analyze_epidemiological_data_task(),
                self.investigate_immune_responses_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
                self.analyze_data_trends_task(),
                self.update_shared_memory_task(),
                self.ensure_quality_and_alignment_task(),
                self.compile_final_report_task(),
                self.facilitate_collaboration_task(),
                self.plan_future_research_task()
            ],
            process=Process.sequential,
            verbose=True,
        )
