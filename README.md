
---

# ASR Error Correction Agent

## Project Overview
This project develops an agent to correct Automatic Speech Recognition (ASR) errors in voice-enabled assistants. The agent focuses on phoneme-based corrections, identifying phonetically similar replacements for incorrect words and optimizing the accuracy of ASR outputs.

### Key Features
- **Phoneme Table-Based Correction**: The system uses a phoneme table to identify incorrect words and find replacements based on phonetic similarity.
- **State Representation and Cost Optimization**: Each correction step is represented as a state, and the agent continuously searches for the lowest-cost state representing the best correction.
- **Inverted Phoneme Table**: This enables the agent to efficiently backtrack phoneme corrections and explore multiple correction paths.
- **Recursive Search and Sentence Expansion**: After correcting phonemes, the agent expands the sentence by adding words from a predefined vocabulary to improve sentence accuracy further.

## Workflow
1. **ASR Input**: The system receives transcribed output from the ASR system.
2. **Phoneme-Based Correction**: Using a phoneme table, the agent identifies incorrect words and suggests replacements based on phonetic similarity.
3. **State Exploration**: The system evaluates multiple possible corrections for each word, maintaining a state with the lowest correction cost.
4. **Sentence Expansion**: The agent adds words to the beginning and end of the sentence to reduce errors further, updating the best state.
5. **Corrected Output**: The corrected sentence is returned as the final output.

## Installation and Setup
1. **Clone the Repository**: Download the repository and navigate to the project directory.
2. **Configuration**: Update the configuration file (if necessary) to reflect your ASR system setup.

## Running the Agent

To run the agent, execute the `driver.py` script:

```bash
python driver.py
```

This will start the ASR Correction Agent, and you can feed in the ASR transcriptions for error correction. Ensure that all configurations and input paths are correctly set in the driver file.

## Usage
The ASR Correction Agent can be integrated into any ASR pipeline to enhance transcription accuracy by correcting phonetic errors and expanding sentence structure. You can modify the configuration and vocabulary as per your use case.

---
