from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, WebsiteSearchTool, PDFSearchTool
from langchain_openai import ChatOpenAI
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain_community.tools.semanticscholar.tool import SemanticScholarQueryRun

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
                PubmedQueryRun(),
                SemanticScholarQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=True,  # Allowing delegation for coordination
            verbose=True,
            llm=self.llm
        )

    @agent
    def immunology_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['immunology_specialist'],
            tools=[
                PubmedQueryRun(),
                SemanticScholarQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
                # Additional tools specific to advanced immunological techniques
            ],
            allow_delegation=True,  # Changed to True to match the original immunology_specialist
            verbose=True,
            llm=self.llm
        )

    @agent
    def virology_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['virology_expert'],
            tools=[
                PubmedQueryRun(),
                SemanticScholarQueryRun(),
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
                SemanticScholarQueryRun(),
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
                SemanticScholarQueryRun(),
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
                SemanticScholarQueryRun(),
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
                SemanticScholarQueryRun(),
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
                SemanticScholarQueryRun(),
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
                PubmedQueryRun(),
                SemanticScholarQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=True,  # Allowing delegation for therapeutic development
            verbose=True,
            llm=self.llm
        )

    @agent
    def treatment_strategy_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['treatment_strategy_analyst'],
            tools=[
                PubmedQueryRun(),
                SemanticScholarQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
                # Include additional tools if necessary
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
                PubmedQueryRun(),
                SemanticScholarQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
                # Statistical tools can be integrated if needed
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['project_manager'],
            allow_delegation=True,  # Can delegate tasks and facilitate collaboration
            verbose=True,
            llm=self.llm
        )

    @agent
    def science_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['science_writer'],
            tools=[
                PubmedQueryRun(),
                SemanticScholarQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    @agent
    def genomics_and_transcriptomics_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['genomics_and_transcriptomics_specialist'],
            tools=[
                PubmedQueryRun(),
                SemanticScholarQueryRun(),
                WebsiteSearchTool(),
                SerperDevTool(),
                PDFSearchTool(pdf="../mechanisms.pdf"),
            ],
            allow_delegation=True,  # Allowing delegation for method development
            verbose=True,
            llm=self.llm
        )

    @task
    def apply_advanced_immunological_techniques_task(self) -> Task:
        return Task(
            config=self.tasks_config['apply_advanced_immunological_techniques_task'],
            agent=self.immunology_specialist(),  # Updated to use immunology_specialist
            output_file='reports/mechanisms/apply_advanced_immunological_techniques_task.md'
        )

    @task
    def analyze_epidemiological_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_epidemiological_data_task'],
            agent=self.epidemiology_analyst(),
            output_file='reports/analysis/analyze_epidemiological_data_task.md'
        )

    @task
    def study_transcriptomics_task(self) -> Task:
        return Task(
            config=self.tasks_config['study_transcriptomics_task'],
            agent=self.genomics_and_transcriptomics_specialist(),
            context=[
                self.apply_advanced_immunological_techniques_task()
            ],
            dependencies=[
                self.apply_advanced_immunological_techniques_task()
            ],
            output_file='reports/mechanisms/study_transcriptomics_task.md'
        )

    @task
    def analyze_spike_protein_translocation_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_spike_protein_translocation_task'],
            agent=self.virology_expert(),
            context=[
                self.apply_advanced_immunological_techniques_task()
            ],
            dependencies=[
                self.apply_advanced_immunological_techniques_task()
            ],
            output_file='reports/mechanisms/analyze_spike_protein_translocation_task.md'
        )

    @task
    def investigate_immune_responses_task(self) -> Task:
        return Task(
            config=self.tasks_config['investigate_immune_responses_task'],
            agent=self.immunology_specialist(),
            context=[
                self.study_transcriptomics_task(),
                self.apply_advanced_immunological_techniques_task()
            ],
            dependencies=[
                self.study_transcriptomics_task(),
                self.apply_advanced_immunological_techniques_task()
            ],
            output_file='reports/mechanisms/investigate_immune_responses_task.md'
        )

    @task
    def investigate_NK_and_T_cell_dynamics_task(self) -> Task:
        return Task(
            config=self.tasks_config['investigate_NK_and_T_cell_dynamics_task'],
            agent=self.immunology_specialist(),
            context=[
                self.study_transcriptomics_task(),
                self.apply_advanced_immunological_techniques_task()
            ],
            dependencies=[
                self.study_transcriptomics_task(),
                self.apply_advanced_immunological_techniques_task()
            ],
            output_file='reports/mechanisms/investigate_NK_and_T_cell_dynamics_task.md'
        )

    @task
    def analyze_microbiome_impact_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_microbiome_impact_task'],
            agent=self.microbiome_specialist(),
            context=[
                self.study_transcriptomics_task()
            ],
            dependencies=[
                self.study_transcriptomics_task()
            ],
            output_file='reports/mechanisms/analyze_microbiome_impact_task.md'
        )

    @task
    def investigate_metabolic_disruptions_task(self) -> Task:
        return Task(
            config=self.tasks_config['investigate_metabolic_disruptions_task'],
            agent=self.metabolism_expert(),
            context=[
                self.study_transcriptomics_task()
            ],
            dependencies=[
                self.study_transcriptomics_task()
            ],
            output_file='reports/mechanisms/investigate_metabolic_disruptions_task.md'
        )

    @task
    def explore_viral_persistence_task(self) -> Task:
        return Task(
            config=self.tasks_config['explore_viral_persistence_task'],
            agent=self.virology_expert(),
            context=[
                self.analyze_spike_protein_translocation_task()
            ],
            dependencies=[
                self.analyze_spike_protein_translocation_task()
            ],
            output_file='reports/mechanisms/explore_viral_persistence_task.md'
        )

    @task
    def research_latent_viral_infections_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_latent_viral_infections_task'],
            agent=self.virology_expert(),
            context=[
                self.analyze_spike_protein_translocation_task()
            ],
            dependencies=[
                self.analyze_spike_protein_translocation_task()
            ],
            output_file='reports/mechanisms/research_latent_viral_infections_task.md'
        )

    @task
    def assess_cardiovascular_complications_task(self) -> Task:
        return Task(
            config=self.tasks_config['assess_cardiovascular_complications_task'],
            agent=self.cardiology_specialist(),
            output_file='reports/mechanisms/assess_cardiovascular_complications_task.md'
        )

    @task
    def investigate_neurological_manifestations_task(self) -> Task:
        return Task(
            config=self.tasks_config['investigate_neurological_manifestations_task'],
            agent=self.neurology_expert(),
            output_file='reports/mechanisms/investigate_neurological_manifestations_task.md'
        )

    @task
    def analyze_data_trends_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_data_trends_task'],
            agent=self.data_analyst(),
            context=[
                self.analyze_epidemiological_data_task(),
                self.investigate_immune_responses_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
                self.research_latent_viral_infections_task(),
            ],
            dependencies=[
                self.analyze_epidemiological_data_task(),
                self.investigate_immune_responses_task(),
                self.explore_viral_persistence_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
                self.research_latent_viral_infections_task(),
            ],
            output_file='reports/analysis/analyze_data_trends_task.md'
        )

    @task
    def conduct_mechanism_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['conduct_mechanism_research_task'],
            agent=self.lead_medical_researcher(),
            context=[
                self.analyze_data_trends_task(),
                self.analyze_epidemiological_data_task(),
                self.investigate_immune_responses_task(),
                self.investigate_NK_and_T_cell_dynamics_task(),
                self.explore_viral_persistence_task(),
                self.research_latent_viral_infections_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
                self.study_transcriptomics_task(),
                self.analyze_spike_protein_translocation_task(),
                self.apply_advanced_immunological_techniques_task(),
            ],
            dependencies=[
                self.analyze_data_trends_task(),
                self.analyze_epidemiological_data_task(),
                self.investigate_immune_responses_task(),
                self.investigate_NK_and_T_cell_dynamics_task(),
                self.explore_viral_persistence_task(),
                self.research_latent_viral_infections_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
                self.study_transcriptomics_task(),
                self.analyze_spike_protein_translocation_task(),
                self.apply_advanced_immunological_techniques_task(),
            ],
            output_file='reports/mechanisms/conduct_mechanism_research_task.md'
        )

    @task
    def identify_therapeutics_task(self) -> Task:
        return Task(
            config=self.tasks_config['identify_therapeutics_task'],
            agent=self.pharmacology_expert(),
            context=[
                self.conduct_mechanism_research_task()
            ],
            dependencies=[
                self.conduct_mechanism_research_task()
            ],
            output_file='reports/treatments/identify_therapeutics_task.md'
        )

    @task
    def develop_combination_treatments_task(self) -> Task:
        return Task(
            config=self.tasks_config['develop_combination_treatments_task'],
            agent=self.treatment_strategy_analyst(),
            context=[
                self.identify_therapeutics_task()
            ],
            dependencies=[
                self.identify_therapeutics_task()
            ],
            output_file='reports/treatments/develop_combination_treatments_task.md'
        )

    @task
    def update_shared_memory_task(self) -> Task:
        return Task(
            config=self.tasks_config['update_shared_memory_task'],
            agent=self.project_manager(),
            context=[
                # All tasks update shared memory
            ],
            dependencies=[
                # No dependencies; runs concurrently
            ],
            output_file='reports/management/update_shared_memory_task.md'
        )

    @task
    def ensure_quality_and_alignment_task(self) -> Task:
        return Task(
            config=self.tasks_config['ensure_quality_and_alignment_task'],
            agent=self.project_manager(),
            context=[
                # Monitors outputs from all tasks
            ],
            dependencies=[
                # Depends on outputs being available
                self.update_shared_memory_task()
            ],
            output_file='reports/management/ensure_quality_and_alignment_task.md'
        )

    @task
    def facilitate_collaboration_task(self) -> Task:
        return Task(
            config=self.tasks_config['facilitate_collaboration_task'],
            agent=self.project_manager(),
            context=[
                # Ongoing task to facilitate collaboration
            ],
            dependencies=[
                # No dependencies; runs concurrently
            ],
            output_file='reports/management/facilitate_collaboration_task.md'
        )

    @task
    def compile_final_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['compile_final_report_task'],
            agent=self.science_writer(),
            context=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
            ],
            dependencies=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
                self.ensure_quality_and_alignment_task(),
            ],
            output_file='reports/final/compile_final_report_task.md'
        )

    @task
    def plan_future_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_future_research_task'],
            agent=self.lead_medical_researcher(),
            context=[
                self.conduct_mechanism_research_task(),
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),
                self.compile_final_report_task(),
            ],
            dependencies=[
                self.compile_final_report_task(),
            ],
            output_file='reports/final/plan_future_research_task.md'
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
                self.genomics_and_transcriptomics_specialist(),
                self.science_writer(),
            ],
            tasks=[
                # Ongoing tasks
                self.update_shared_memory_task(),
                self.ensure_quality_and_alignment_task(),
                self.facilitate_collaboration_task(),

                # Initial data collection and methodology development
                self.apply_advanced_immunological_techniques_task(),
                self.analyze_epidemiological_data_task(),

                # Specialized research tasks
                self.study_transcriptomics_task(),
                self.analyze_spike_protein_translocation_task(),
                self.investigate_immune_responses_task(),
                self.investigate_NK_and_T_cell_dynamics_task(),
                self.analyze_microbiome_impact_task(),
                self.investigate_metabolic_disruptions_task(),
                self.explore_viral_persistence_task(),
                self.research_latent_viral_infections_task(),
                self.assess_cardiovascular_complications_task(),
                self.investigate_neurological_manifestations_task(),

                # Data analysis and trend identification
                self.analyze_data_trends_task(),

                # Mechanism research and hypothesis formation
                self.conduct_mechanism_research_task(),

                # Therapeutic development
                self.identify_therapeutics_task(),
                self.develop_combination_treatments_task(),

                # Reporting and future planning
                self.compile_final_report_task(),
                self.plan_future_research_task(),
            ],
            process=Process.sequential,
            verbose=True,
        )

