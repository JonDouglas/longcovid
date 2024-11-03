#!/usr/bin/env python
import sys
import time
from longcovid.crew import LongCovidCrew

inputs = {
    'num_hypotheses': 15,
    'num_therapeutics': 20, 
    'num_experimental_therapeutics': 5,
    'num_combinations': 10,
    'format_guidelines': """
    - Use Markdown format for the entire report.
    - Do not use code blocks (``` or ~~~) anywhere in the report.
    - Use appropriate Markdown syntax for headings, subheadings, bullet points, and numbered lists.
    - For any figures or diagrams, provide detailed text descriptions in lieu of actual images.
    - Use Markdown syntax for emphasis (e.g., *italics*, **bold**) where appropriate.
    - For citations, use a consistent format such as [Author, Year] in the text.
    """,
    'research_focus': """
    research_focus:
      title: >
        Critical Investigation of Long COVID Mechanisms and Treatment Development

      description: >
        Primary objective: Identify and develop effective treatments for Long COVID through:

        - Uncovering the core pathological mechanisms of Long COVID
        - Identifying and testing promising therapeutics, including experimental treatments
        - Developing synergistic combination treatments that target multiple mechanisms
        - Testing unconventional approaches and experimental therapies when justified

        The research will prioritize:
        - Any treatment showing potential efficacy, regardless of current approval status
        - Novel combination approaches, even if individual components showed limited efficacy
        - Experimental therapeutics that target newly discovered mechanisms
        - Rapid testing and validation of promising treatments
        
      specific_objectives:
        - Identify up to {num_hypotheses} key pathological mechanisms of Long COVID
        - Develop and test up to {num_therapeutics} potential therapeutics
        - Explore {num_experimental_therapeutics} experimental treatments, including those in early development
        - Create up to {num_combinations} strategic combination treatments
        - Test treatments showing promise, regardless of conventional medical paradigms

      data_sources:
        - Latest research findings, including pre-prints and early-stage studies
        - Experimental treatment protocols and emerging therapies
        - Clinical trial data, including failed trials for mechanism insights
        - Drug interaction databases for combination treatment development
        - Cutting-edge research from any field that might offer treatment insights
    """
}

def validate_inputs(inputs):
    """
    Validate required input parameters.
    """
    required_params = [
        'num_hypotheses',
        'num_therapeutics',
        'num_experimental_therapeutics',
        'num_combinations',
        'format_guidelines',
        'research_focus'
    ]
    
    missing = [param for param in required_params if param not in inputs]
    if missing:
        raise ValueError(f"Missing required input parameters: {', '.join(missing)}")
    
    # Validate numeric parameters
    numeric_params = [
        'num_hypotheses',
        'num_therapeutics', 
        'num_experimental_therapeutics',
        'num_combinations'
    ]
    for param in numeric_params:
        if not isinstance(inputs[param], int) or inputs[param] <= 0:
            raise ValueError(f"{param} must be a positive integer")

def run():
    """
    Run the crew.
    """
    validate_inputs(inputs)
    start_time = time.time()
    LongCovidCrew().crew().kickoff(inputs=inputs)
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        validate_inputs(inputs)
        LongCovidCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        validate_inputs(inputs)
        LongCovidCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    try:
        validate_inputs(inputs)
        LongCovidCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
