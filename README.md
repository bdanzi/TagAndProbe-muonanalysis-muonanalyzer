# MuonAnalysis-MuonAnalyzer

Package to run tag/probe ntuples for Muon POG on both AOD and miniAOD format.

Requires CMSSW_10_6_X or higher.

## Setup
```bash
$ cmsrel CMSSW_10_6_18 
$ cd CMSSW_10_6_18/src
$ cmsenv
$ git cms-init
$ git clone https://github.com/bdanzi/TagAndProbe-muonanalysis-muonanalyzer.git MuonAnalysis/MuonAnalyzer
$ scram b -j 8
```

## Usage
```bash
$ cmsRun MuonAnalysis/MuonAnalyzer/test/run_muonAnalyzer_cfg.py
```

## Running StandAlone Analyzer
```bash
$ cmsRun MuonAnalysis/MuonAnalyzer/test/run_muonAnalyzer_cfg.py isStandAlone=True
# Note only works with Z Resonance at the moment no JPsi config files set yet

## Contributing

Before creating a Merge Request, make sure the code is properly formatted with:

```bash
$ find . -regex '.*\.\(cpp\|hpp\|cc\|cxx\|h\)' | xargs clang-format -i
```

Run this from the base directory. It should go through all source code files in the repository and format them according to CMSSW's style (the `Google` style).
