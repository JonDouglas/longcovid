from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class ResearchFindings(BaseModel):
    summary: str = Field(..., description="Brief summary of key findings")
    methodology: str = Field(..., description="Research methodology used")
    results: List[str] = Field(..., description="List of main results")
    limitations: List[str] = Field(..., description="Study limitations")
    conclusions: str = Field(..., description="Overall conclusions")
    references: List[str] = Field(..., description="Referenced studies")

class TherapeuticAnalysis(BaseModel):
    name: str = Field(..., description="Name of therapeutic approach")
    mechanism: str = Field(..., description="Mechanism of action")
    efficacy: str = Field(..., description="Observed or expected efficacy")
    safety_profile: str = Field(..., description="Safety considerations")
    target_population: str = Field(..., description="Intended patient population")
    limitations: List[str] = Field(..., description="Limitations and contraindications")

class EpidemiologicalData(BaseModel):
    prevalence: str = Field(..., description="Disease prevalence statistics")
    demographics: Dict[str, str] = Field(..., description="Demographic breakdown")
    risk_factors: List[str] = Field(..., description="Identified risk factors")
    trends: List[str] = Field(..., description="Observed epidemiological trends")
    data_sources: List[str] = Field(..., description="Sources of epidemiological data")

class MechanismAnalysis(BaseModel):
    pathway: str = Field(..., description="Biological pathway description")
    key_molecules: List[str] = Field(..., description="Key molecules involved")
    cellular_effects: List[str] = Field(..., description="Effects on cellular function")
    systemic_impact: str = Field(..., description="Impact on body systems")
    evidence: List[str] = Field(..., description="Supporting evidence")

class ClinicalManifestations(BaseModel):
    symptoms: List[str] = Field(..., description="Primary symptoms")
    progression: str = Field(..., description="Disease progression pattern")
    severity_factors: List[str] = Field(..., description="Factors affecting severity")
    biomarkers: List[str] = Field(..., description="Relevant biomarkers")
    clinical_subtypes: List[str] = Field(..., description="Identified clinical subtypes")

class TreatmentStrategy(BaseModel):
    approach: str = Field(..., description="Treatment approach overview")
    components: List[str] = Field(..., description="Treatment components")
    timing: str = Field(..., description="Timing and duration considerations")
    patient_selection: str = Field(..., description="Patient selection criteria")
    monitoring: List[str] = Field(..., description="Monitoring requirements")
    expected_outcomes: str = Field(..., description="Expected treatment outcomes")

class FinalReport(BaseModel):
    executive_summary: str = Field(..., description="Executive summary")
    key_findings: List[str] = Field(..., description="Key research findings")
    mechanisms: List[str] = Field(..., description="Identified mechanisms")
    therapeutic_approaches: List[str] = Field(..., description="Therapeutic approaches")
    recommendations: List[str] = Field(..., description="Clinical recommendations")
    future_directions: List[str] = Field(..., description="Future research directions")

class TranscriptomicsAnalysis(BaseModel):
    summary: str = Field(..., description="Analysis summary")
    gene_expression_patterns: List[str] = Field(..., description="Key gene expression patterns")
    pathways: List[str] = Field(..., description="Affected pathways")
    differential_expression: List[str] = Field(..., description="Differential expression findings")
    methodology: str = Field(..., description="Analysis methodology")
    implications: str = Field(..., description="Clinical implications")

class ViralAnalysis(BaseModel):
    mechanism: str = Field(..., description="Viral mechanism description")
    cellular_targets: List[str] = Field(..., description="Affected cellular targets")
    persistence_factors: List[str] = Field(..., description="Factors affecting viral persistence")
    immune_evasion: str = Field(..., description="Immune evasion strategies")
    clinical_impact: str = Field(..., description="Clinical implications")
    evidence: List[str] = Field(..., description="Supporting evidence")

class MicrobiomeAnalysis(BaseModel):
    composition_changes: List[str] = Field(..., description="Microbiome composition changes")
    functional_impact: str = Field(..., description="Functional impact on host")
    mechanisms: List[str] = Field(..., description="Underlying mechanisms")
    therapeutic_implications: List[str] = Field(..., description="Therapeutic implications")
    methodology: str = Field(..., description="Analysis methodology")

class MetabolicAnalysis(BaseModel):
    pathways_affected: List[str] = Field(..., description="Affected metabolic pathways")
    biomarkers: List[str] = Field(..., description="Relevant biomarkers")
    systemic_effects: str = Field(..., description="Systemic metabolic effects")
    therapeutic_targets: List[str] = Field(..., description="Potential therapeutic targets")
    methodology: str = Field(..., description="Analysis methodology")

class DataTrendsAnalysis(BaseModel):
    key_trends: List[str] = Field(..., description="Identified trends")
    correlations: List[str] = Field(..., description="Important correlations")
    statistical_findings: Dict[str, str] = Field(..., description="Statistical analysis results")
    implications: str = Field(..., description="Clinical implications")
    limitations: List[str] = Field(..., description="Analysis limitations")

class ProjectUpdate(BaseModel):
    status: str = Field(..., description="Current status")
    progress: List[str] = Field(..., description="Progress points")
    challenges: List[str] = Field(..., description="Identified challenges")
    actions: List[str] = Field(..., description="Required actions")
    recommendations: List[str] = Field(..., description="Recommendations")

class FutureResearch(BaseModel):
    priorities: List[str] = Field(..., description="Research priorities")
    gaps: List[str] = Field(..., description="Knowledge gaps")
    methodology: List[str] = Field(..., description="Proposed methodologies")
    resources: List[str] = Field(..., description="Required resources")
    timeline: str = Field(..., description="Proposed timeline")
    impact: str = Field(..., description="Expected impact")