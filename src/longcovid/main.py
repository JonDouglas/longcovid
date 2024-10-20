#!/usr/bin/env python
import sys
from longcovid.crew import LongCovidCrew


def run():
    inputs = {
    'research_focus': """
research_focus:
  title: >
    Comprehensive Investigation of Leading Hypotheses, Novel Therapeutics, and Innovative Combination Treatments for Long COVID

  description: >
    The objective is to conduct a thorough multidisciplinary research project culminating in a comprehensive report. This report will focus on:

    - Identifying and critically evaluating the leading hypotheses of Long COVID mechanisms, including immunological, virological, cardiovascular, neurological, microbiome-related, and metabolic aspects.
    - Identifying, evaluating, and prioritizing novel and potentially high-impact therapeutics that address these mechanisms.
    - Developing innovative combination treatment strategies with detailed rationales, allowing for repetition of highly promising therapeutics in different combinations when scientifically justified.
    - Providing mechanistic explanations and supporting evidence for each therapeutic and combination treatment.
    - Analyzing epidemiological and clinical data to identify trends, patterns, and correlations that support the conclusions.
    - Compiling actionable recommendations for clinical practice and future research directions.

    The research emphasizes pathological findings and mechanisms of action, excluding symptom management unless directly related. The final deliverable will be a detailed report on innovative treatments and their rationales, suitable for dissemination to medical professionals and stakeholders.

    Additionally, the research will:
    - Review acute COVID-19 therapeutic data to identify potential candidates for Long COVID treatment.
    - Exclude therapeutics that showed no effect in acute COVID-19 trials, unless:
      a) They have potential for combination effects with other treatments.
      b) There is a strong mechanistic rationale for their efficacy in Long COVID despite lack of effect in acute cases.
    - Document the rationale for including any acute COVID-19 therapeutics that were ineffective on their own.

  areas_of_interest:
    - Leading hypotheses of Long COVID mechanisms, including immune dysfunction, viral persistence, cardiovascular complications, neurological manifestations, gut microbiome alterations, and metabolic disruptions
    - Novel and potentially high-impact therapeutics targeting identified mechanisms
    - Innovative combination treatments addressing multiple mechanisms
    - Mechanistic rationales for novel therapeutics and combinations
    - Recent research developments and cutting-edge clinical trials
    - Epidemiological analysis of Long COVID prevalence, risk factors, and distribution
    - Data analysis of trends in Long COVID research
    - Recommendations for clinical application and future research

  specific_objectives:
    - Identify and critically evaluate up to **15 leading hypotheses** of Long COVID mechanisms, encompassing various physiological systems.
    - Identify, evaluate, and prioritize up to **20 novel therapeutics** targeting these mechanisms, focusing on innovative and potentially high-impact interventions.
    - Explore and assess **5 experimental, cutting-edge therapeutics** that push the boundaries of conventional medicine.
    - Develop and propose up to **10 innovative combination treatment strategies**, allowing for repetition of highly promising therapeutics when scientifically justified.
    - Provide detailed mechanistic rationales and supporting evidence for each novel therapeutic and combination treatment.
    - Analyze epidemiological and clinical data to identify significant trends, patterns, and correlations supporting the team's conclusions on innovative approaches.
    - Compile a comprehensive report with findings, detailed rationales, and actionable recommendations for novel treatments.
    - Review and analyze data from acute COVID-19 therapeutic trials for potential application in Long COVID treatment.
    - Identify and justify the inclusion of any acute COVID-19 therapeutics that showed no individual effect but have potential in combination treatments.

  data_sources:
    - PubMed and recent peer-reviewed journals (focus on publications within the last couple of years).
    - Clinical trial databases (e.g., ClinicalTrials.gov, WHO International Clinical Trials Registry Platform).
    - FDA drug databases and pharmacological resources (e.g., DrugBank, EMA databases).
    - Statistical data from epidemiological and clinical research studies.
    - Guidelines and protocols for innovative treatment strategies from reputable health organizations.
    - Drug interaction databases for assessing combination therapy safety.
    - International health agency reports (e.g., WHO, NIH, CDC).
    - Acute COVID-19 clinical trial results and meta-analyses.

  deliverables:
    - A comprehensive and detailed final report in markdown format (without '```'), including:
      - Title Page:
        - Project title emphasizing the focus on novel and innovative treatments.
        - Names of all contributors and their respective roles.
        - Affiliations and contact information.
        - Date of completion.
      - Table of Contents:
        - Organized listing of all sections and subsections with corresponding page numbers.
      - Executive Summary:
        - Concise overview of the entire report.
        - Brief background on Long COVID and the significance of innovative research.
        - Summary of key findings across mechanisms, novel therapeutics, and innovative combination treatments.
        - High-level recommendations for clinical practice and future research, emphasizing novel approaches.
        - Emphasis on the impact and potential benefits of the proposed innovative strategies.
      - Introduction:
        - Background information on Long COVID, including prevalence, symptoms, and current challenges.
        - Clear statement of the research aims and questions, highlighting the focus on novel interventions.
        - Explanation of the scope and limitations of the study.
        - Significance and potential impact of innovative approaches on patient outcomes and healthcare practices.
        - Brief outline of the report structure.
      - Methodology:
        - Description of the overall research design and interdisciplinary approach.
        - Detailed literature review methods, including databases searched, keywords used, and inclusion/exclusion criteria for identifying novel interventions.
        - Data collection and analysis procedures.
        - Evaluation criteria for assessing mechanisms and novel therapeutics.
        - Ethical considerations and compliance with data usage policies.
      - Findings:
        - Section A: Long COVID Mechanisms
          - Detailed analysis of up to 15 leading hypotheses.
          - For each hypothesis:
            - In-depth description of the mechanism.
            - Summary of supporting evidence with critical appraisal.
            - Diagrams or illustrations where applicable.
            - Clinical relevance and implications.
            - Identification of research gaps and potential for novel interventions.
            - Relevant citations with complete publication details.
        - Section B: Evaluation of Novel Therapeutics
          - Comprehensive analysis of up to 20 novel therapeutics.
          - For each therapeutic:
            - Name (generic and trade names).
            - Pharmacological class and innovative mechanism of action.
            - Targeted Long COVID mechanism(s).
            - Current development stage or FDA approval status.
            - Summary of efficacy data with critical appraisal, emphasizing novelty and potential impact.
            - Safety profile, including common adverse effects and contraindications.
            - Potential for repurposing existing drugs in innovative ways.
            - Cost and accessibility considerations.
            - Relevant citations from recent studies or cutting-edge clinical trials.
          - Prioritization Matrix:
            - Novel therapeutics ranked based on innovation, potential impact, and feasibility.
            - Justification for prioritization decisions, emphasizing therapeutics targeting mechanisms with multiple promising candidates.
          - Analysis of acute COVID-19 therapeutics:
            - List of acute COVID-19 therapeutics considered and their outcomes.
            - Justification for inclusion of any acute COVID-19 therapeutics that showed no individual effect.
        - Section C: Innovative Combination Treatment Strategies
          - Detailed proposals of up to 10 innovative combination treatments.
          - For each combination:
            - Components of the combination (novel therapeutics/interventions).
            - Rationale for the combination, including mechanistic synergy and innovative approach.
            - Explanation of how combining multiple therapeutics targeting the same hypothesis may enhance efficacy.
            - Potential benefits over monotherapy, highlighting the innovative aspects.
            - Safety considerations and interaction assessments.
            - Proposed dosing regimens and administration guidelines.
            - Feasibility and practical considerations for implementing novel combinations.
            - Relevant references supporting the innovative approach.
          - Integration of acute COVID-19 therapeutics:
            - Explanation of how acute COVID-19 therapeutics are incorporated into combination treatments, if applicable.
            - Justification for including any acute COVID-19 therapeutics that showed no individual effect.
        - Mechanistic Explanations and Supporting Evidence
          - Integration of findings showing how novel therapeutics and innovative combinations address specific mechanisms.
          - Detailed pathways illustrating innovative therapeutic actions.
          - Discussion of multiple novel therapeutics targeting the same hypothesis and the potential advantages.
      - Data Analysis:
        - Statistical summaries, including descriptive and inferential statistics.
        - Visualizations such as graphs, charts, network diagrams, and timelines.
        - Interpretation of significant trends, patterns, and correlations, with a focus on novel findings.
        - Identification of significant correlations or unexpected findings that support innovative approaches.
        - Limitations of data and impact on interpretations of novel interventions.
      - Discussion:
        - Synthesis of findings and how they answer the research questions, emphasizing innovative aspects.
        - Comparison with existing literature, highlighting the novelty of the proposed approaches.
        - Clinical implications and recommendations for clinicians, focusing on implementing novel treatments.
        - Research implications and directions for future studies on innovative interventions.
        - Limitations of the study and potential biases in assessing novel approaches.
      - Conclusions and Recommendations:
        - Recap of the most important findings, emphasizing novel and potentially high-impact interventions.
        - Actionable recommendations for clinicians, researchers, and policymakers, prioritizing innovative approaches.
        - Prioritization of novel therapeutics and innovative combinations for further investigation or clinical trials.
      - References:
        - Complete list of all sources cited, following a consistent citation format.
      - Appendices:
        - Appendix A: Search strategies and keywords used for identifying novel interventions.
        - Appendix B: List of databases and journals consulted for cutting-edge research.
        - Appendix C: Detailed data tables supporting the findings on novel therapeutics.
        - Appendix D: Methodological details for assessing innovative approaches.
        - Appendix E: Supplementary figures and diagrams illustrating novel mechanisms and interventions.
    - Future research proposal outlining potential studies to address identified gaps and unanswered questions, including:
      - Executive Summary:
        - Overview of proposed innovative research initiatives.
      - Detailed Proposals for Each Study:
        - Background and significance, emphasizing the need for novel approaches.
        - Specific aims and hypotheses for innovative interventions.
        - Research design and methods for investigating novel therapeutics.
        - Expected outcomes and potential impact of innovative treatments.
        - Timeline and milestones for developing and testing novel interventions.
        - Budget estimates with justification for innovative research approaches.
      - Justification:
        - How each proposal addresses identified gaps with novel solutions.
        - Potential to advance knowledge or improve patient outcomes through innovative treatments.
      - Feasibility Analysis:
        - Assessment of resource availability for novel research approaches.
        - Ethical and regulatory considerations for innovative interventions.
      - Recommendations for Implementation:
        - Suggested funding sources or partnerships for innovative research.
        - Next steps for proposal development and submission of cutting-edge studies.
    """
    }
     # Initialize the crew
    LongCovidCrew().crew().kickoff(inputs=inputs)

def train():
    inputs = {
        'research_focus': """
research_focus:
title: >
    Comprehensive Investigation of Leading Hypotheses, Novel Therapeutics, and Innovative Combination Treatments for Long COVID

description: >
    The objective is to conduct a thorough multidisciplinary research project culminating in a comprehensive report. This report will focus on:

    - Identifying and critically evaluating the leading hypotheses of Long COVID mechanisms, including immunological, virological, cardiovascular, neurological, microbiome-related, and metabolic aspects.
    - Identifying, evaluating, and prioritizing novel and potentially high-impact therapeutics that address these mechanisms.
    - Developing innovative combination treatment strategies with detailed rationales, allowing for repetition of highly promising therapeutics in different combinations when scientifically justified.
    - Providing mechanistic explanations and supporting evidence for each therapeutic and combination treatment.
    - Analyzing epidemiological and clinical data to identify trends, patterns, and correlations that support the conclusions.
    - Compiling actionable recommendations for clinical practice and future research directions.

    The research emphasizes pathological findings and mechanisms of action, excluding symptom management unless directly related. The final deliverable will be a detailed report on innovative treatments and their rationales, suitable for dissemination to medical professionals and stakeholders.

    Additionally, the research will:
    - Review acute COVID-19 therapeutic data to identify potential candidates for Long COVID treatment.
    - Exclude therapeutics that showed no effect in acute COVID-19 trials, unless:
      a) They have potential for combination effects with other treatments.
      b) There is a strong mechanistic rationale for their efficacy in Long COVID despite lack of effect in acute cases.
    - Document the rationale for including any acute COVID-19 therapeutics that were ineffective on their own.

areas_of_interest:
    - Leading hypotheses of Long COVID mechanisms, including immune dysfunction, viral persistence, cardiovascular complications, neurological manifestations, gut microbiome alterations, and metabolic disruptions
    - Novel and potentially high-impact therapeutics targeting identified mechanisms
    - Innovative combination treatments addressing multiple mechanisms
    - Mechanistic rationales for novel therapeutics and combinations
    - Recent research developments and cutting-edge clinical trials
    - Epidemiological analysis of Long COVID prevalence, risk factors, and distribution
    - Data analysis of trends in Long COVID research
    - Recommendations for clinical application and future research

specific_objectives:
    - Identify and critically evaluate up to **15 leading hypotheses** of Long COVID mechanisms, encompassing various physiological systems.
    - Identify, evaluate, and prioritize up to **20 novel therapeutics** targeting these mechanisms, focusing on innovative and potentially high-impact interventions.
    - Explore and assess **5 experimental, cutting-edge therapeutics** that push the boundaries of conventional medicine.
    - Develop and propose up to **10 innovative combination treatment strategies**, allowing for repetition of highly promising therapeutics when scientifically justified.
    - Provide detailed mechanistic rationales and supporting evidence for each novel therapeutic and combination treatment.
    - Analyze epidemiological and clinical data to identify significant trends, patterns, and correlations supporting the team's conclusions on innovative approaches.
    - Compile a comprehensive report with findings, detailed rationales, and actionable recommendations for novel treatments.
    - Review and analyze data from acute COVID-19 therapeutic trials for potential application in Long COVID treatment.
    - Identify and justify the inclusion of any acute COVID-19 therapeutics that showed no individual effect but have potential in combination treatments.

data_sources:
    - PubMed and recent peer-reviewed journals (focus on publications within the last couple of years).
    - Clinical trial databases (e.g., ClinicalTrials.gov, WHO International Clinical Trials Registry Platform).
    - FDA drug databases and pharmacological resources (e.g., DrugBank, EMA databases).
    - Statistical data from epidemiological and clinical research studies.
    - Guidelines and protocols for innovative treatment strategies from reputable health organizations.
    - Drug interaction databases for assessing combination therapy safety.
    - International health agency reports (e.g., WHO, NIH, CDC).
    - Acute COVID-19 clinical trial results and meta-analyses.

deliverables:
    - A comprehensive and detailed final report in markdown format (without '```'), including:
      - Title Page:
        - Project title emphasizing the focus on novel and innovative treatments.
        - Names of all contributors and their respective roles.
        - Affiliations and contact information.
        - Date of completion.
      - Table of Contents:
        - Organized listing of all sections and subsections with corresponding page numbers.
      - Executive Summary:
        - Concise overview of the entire report.
        - Brief background on Long COVID and the significance of innovative research.
        - Summary of key findings across mechanisms, novel therapeutics, and innovative combination treatments.
        - High-level recommendations for clinical practice and future research, emphasizing novel approaches.
        - Emphasis on the impact and potential benefits of the proposed innovative strategies.
      - Introduction:
        - Background information on Long COVID, including prevalence, symptoms, and current challenges.
        - Clear statement of the research aims and questions, highlighting the focus on novel interventions.
        - Explanation of the scope and limitations of the study.
        - Significance and potential impact of innovative approaches on patient outcomes and healthcare practices.
        - Brief outline of the report structure.
      - Methodology:
        - Description of the overall research design and interdisciplinary approach.
        - Detailed literature review methods, including databases searched, keywords used, and inclusion/exclusion criteria for identifying novel interventions.
        - Data collection and analysis procedures.
        - Evaluation criteria for assessing mechanisms and novel therapeutics.
        - Ethical considerations and compliance with data usage policies.
      - Findings:
        - Section A: Long COVID Mechanisms
          - Detailed analysis of up to 15 leading hypotheses.
          - For each hypothesis:
            - In-depth description of the mechanism.
            - Summary of supporting evidence with critical appraisal.
            - Diagrams or illustrations where applicable.
            - Clinical relevance and implications.
            - Identification of research gaps and potential for novel interventions.
            - Relevant citations with complete publication details.
        - Section B: Evaluation of Novel Therapeutics
          - Comprehensive analysis of up to 20 novel therapeutics.
          - For each therapeutic:
            - Name (generic and trade names).
            - Pharmacological class and innovative mechanism of action.
            - Targeted Long COVID mechanism(s).
            - Current development stage or FDA approval status.
            - Summary of efficacy data with critical appraisal, emphasizing novelty and potential impact.
            - Safety profile, including common adverse effects and contraindications.
            - Potential for repurposing existing drugs in innovative ways.
            - Cost and accessibility considerations.
            - Relevant citations from recent studies or cutting-edge clinical trials.
          - Prioritization Matrix:
            - Novel therapeutics ranked based on innovation, potential impact, and feasibility.
            - Justification for prioritization decisions, emphasizing therapeutics targeting mechanisms with multiple promising candidates.
          - Analysis of acute COVID-19 therapeutics:
            - List of acute COVID-19 therapeutics considered and their outcomes.
            - Justification for inclusion of any acute COVID-19 therapeutics that showed no individual effect.
        - Section C: Innovative Combination Treatment Strategies
          - Detailed proposals of up to 10 innovative combination treatments.
          - For each combination:
            - Components of the combination (novel therapeutics/interventions).
            - Rationale for the combination, including mechanistic synergy and innovative approach.
            - Explanation of how combining multiple therapeutics targeting the same hypothesis may enhance efficacy.
            - Potential benefits over monotherapy, highlighting the innovative aspects.
            - Safety considerations and interaction assessments.
            - Proposed dosing regimens and administration guidelines.
            - Feasibility and practical considerations for implementing novel combinations.
            - Relevant references supporting the innovative approach.
          - Integration of acute COVID-19 therapeutics:
            - Explanation of how acute COVID-19 therapeutics are incorporated into combination treatments, if applicable.
            - Justification for including any acute COVID-19 therapeutics that showed no individual effect.
        - Mechanistic Explanations and Supporting Evidence
          - Integration of findings showing how novel therapeutics and innovative combinations address specific mechanisms.
          - Detailed pathways illustrating innovative therapeutic actions.
          - Discussion of multiple novel therapeutics targeting the same hypothesis and the potential advantages.
      - Data Analysis:
        - Statistical summaries, including descriptive and inferential statistics.
        - Visualizations such as graphs, charts, network diagrams, and timelines.
        - Interpretation of significant trends, patterns, and correlations, with a focus on novel findings.
        - Identification of significant correlations or unexpected findings that support innovative approaches.
        - Limitations of data and impact on interpretations of novel interventions.
      - Discussion:
        - Synthesis of findings and how they answer the research questions, emphasizing innovative aspects.
        - Comparison with existing literature, highlighting the novelty of the proposed approaches.
        - Clinical implications and recommendations for clinicians, focusing on implementing novel treatments.
        - Research implications and directions for future studies on innovative interventions.
        - Limitations of the study and potential biases in assessing novel approaches.
      - Conclusions and Recommendations:
        - Recap of the most important findings, emphasizing novel and potentially high-impact interventions.
        - Actionable recommendations for clinicians, researchers, and policymakers, prioritizing innovative approaches.
        - Prioritization of novel therapeutics and innovative combinations for further investigation or clinical trials.
      - References:
        - Complete list of all sources cited, following a consistent citation format.
      - Appendices:
        - Appendix A: Search strategies and keywords used for identifying novel interventions.
        - Appendix B: List of databases and journals consulted for cutting-edge research.
        - Appendix C: Detailed data tables supporting the findings on novel therapeutics.
        - Appendix D: Methodological details for assessing innovative approaches.
        - Appendix E: Supplementary figures and diagrams illustrating novel mechanisms and interventions.
    - Future research proposal outlining potential studies to address identified gaps and unanswered questions, including:
      - Executive Summary:
        - Overview of proposed innovative research initiatives.
      - Detailed Proposals for Each Study:
        - Background and significance, emphasizing the need for novel approaches.
        - Specific aims and hypotheses for innovative interventions.
        - Research design and methods for investigating novel therapeutics.
        - Expected outcomes and potential impact of innovative treatments.
        - Timeline and milestones for developing and testing novel interventions.
        - Budget estimates with justification for innovative research approaches.
      - Justification:
        - How each proposal addresses identified gaps with novel solutions.
        - Potential to advance knowledge or improve patient outcomes through innovative treatments.
      - Feasibility Analysis:
        - Assessment of resource availability for novel research approaches.
        - Ethical and regulatory considerations for innovative interventions.
      - Recommendations for Implementation:
        - Suggested funding sources or partnerships for innovative research.
        - Next steps for proposal development and submission of cutting-edge studies.
    """
    }
    try:
        # Add a filename argument for the trained agents data
        filename = 'trained_agents_data.pkl'
        LongCovidCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs, filename=filename)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

if __name__ == "__main__":
    run()

