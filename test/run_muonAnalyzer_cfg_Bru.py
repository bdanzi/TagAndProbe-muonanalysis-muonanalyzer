'''Author: g. karathanasis. georgios.karathanasis@cern.ch
cfg to run tag and probe ntuple for muon POG. It runs both on AOD and miniAOD
Modified by Andre Frankenthal (a.franken@cern.ch) -- September 2020
usage: cmsRun run_muonAnalyzer_cfg.py option1=value1 option2=value2
'''

from FWCore.ParameterSet.VarParsing import VarParsing
import FWCore.ParameterSet.Config as cms

options = VarParsing('python')

options.register('resonance', 'Z',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Set resonance ('Z'/'JPsi')"
)

options.register('isFullAOD', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Set to False for MiniAOD datatier"
)

options.register('isMC', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Set to True for MC"
)

options.register('globalTag', '',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Set global tag"
)

options.register('reportEvery', 1000,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Report frequency"
)

options.register('numThreads', 1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Number of CMSSW threads" 
)

# this parameter is added for Jet Branches (ID varies for different era)
options.register('era', 'Run2018_UL',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "era"
)

options.register('includeJets', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Set to False to exclude jets information in output ntuples"
)

options.register('fromCRAB', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Is config run from CRAB"
)

options.register('isStandAlone', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "run StandAlone Muon Analyzers"
)
options.parseArguments()

# defaults

if options._beenSet['globalTag'] and options.globalTag != '':
    globaltag = options.globalTag
else:
    globaltag = '102X_dataRun2_v11' if not options.isMC else '102X_upgrade2018_realistic_v15'

# Run local test if no input files provided
if len(options.inputFiles) == 0:
    if options.resonance == 'Z':
        if options.isFullAOD:
            if options.isMC:
                # options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/80002/FF9AF238-78B6-CF48-BC7C-05025D85A45C.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/00303F79-7EDF-1648-AA56-058F2F50A006.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/003425CA-8234-0542-843D-C0303E34EB7D.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/003C661C-6C0A-1C4B-B9C0-2531F66DC9B7.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/00A01824-3340-3C4F-9128-37A5EAF9C319.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/00B4E76E-177F-9D46-943B-7A9B9CB01296.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/00BEE82C-8F30-8140-9880-9826949C5F02.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/00ECBBDF-0A1D-DB4C-B708-25A07DCA39CF.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/00FBB948-5D7D-D041-A8C1-49B8F59E1266.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/012C799C-6D52-B046-B030-E7935115670C.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/015D0A1B-A8E6-8646-9FDB-2D4798709CE8.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/0172EF5B-E340-EE4A-B763-1B640294E340.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/0174B830-5D11-D74E-9F11-2295340F5C7D.root')
            else:
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/60004/FB123080-071C-F64D-BAFD-F2F292F7FC64.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/001498AA-6457-0B42-BEFA-9C72A6A91D2E.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/001D1DB9-405A-D14D-B915-55F071A76BF3.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0087BDD1-CE79-084C-8A72-CE64EE3B2B3C.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0089CA7E-648B-CF4C-A59A-4906AD3F26D8.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/008C5121-EC97-BD4C-8461-A0FA43E28DD7.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/008D63AC-B709-704C-A058-1AE819034C56.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/00B09A1D-4AC0-3943-AB47-A81AC75D158F.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/00E49621-DF30-F34E-B84C-332A2AE0B781.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/015821DF-68E2-BB4E-9B8E-D4E129C265AE.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/015A3917-A98F-4D47-9FA0-AA14F8AB6BC8.root')
                options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/016D3250-5DA8-2145-A862-862ED8F24CFA.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0195DE92-8133-0249-8A1D-676A8931EA1F.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0199FEB3-0DFB-A04C-BC05-4C1A7E3DBC2A.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/01BE8D26-F46A-9F40-969E-8D68602D0A5F.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/01F0D35D-7039-BE4F-BF6F-4DD6558F2CD0.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0237CC50-72C1-D14E-BC9B-18E584E67AA3.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0250BEDD-6910-6144-8AF5-DB8EA9D79057.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/028A254D-4BCF-A248-BC5D-D491CF441B3C.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0299B1F1-BF3A-AC4A-93D7-3C731584CE39.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/02A68556-4DD1-3A4B-A184-4CD14A941DEF.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/02EA41F6-F852-9543-8CF1-D1E85D044C34.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0307E886-1A51-AA41-B550-09E7B6692DC9.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/03110E4E-F57F-5B46-B74E-7F834725B5F0.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0315D0D3-41D3-1F4D-9F97-1B20A2A9A2B8.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/03BC2DAA-E33F-A849-847D-30C32BEA6231.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/03CF3DFA-EC9F-1F42-ADE1-48420D8945E9.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/03D355DD-113B-784C-B6AD-00F4F6294935.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/03EA2407-B40B-514A-8E5F-F35E27EA9F90.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/04130A67-F541-2D4B-8B78-C56BF0F5516B.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/043D375C-D4FD-FE4A-B573-3EE6E797EF51.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0501A525-D845-B54F-AB99-103F1276ABD5.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0554562D-2CBF-CC4D-92AD-57A027E16EC9.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/059351F5-2999-9544-AEBE-DC049F6B2016.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/05CFF9AF-DD02-4549-8130-B516F9A8835E.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/05EB3967-0FFE-7842-9C88-3BAA5C5B8F68.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/06598F25-85A5-044D-A0BD-E3076728AA5A.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/065B2DD7-EDEB-0248-9038-BB15FDA396B8.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/069993E0-3848-C14C-B80B-56443C227C21.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0733AC52-7ADB-9046-8FFF-4BAAB2CD90DB.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/0769C291-BC1A-E143-AA17-8FE1B3EA032A.root')
                # options.inputFiles.append('/store/data/Run2018C/SingleMuon/AOD/17Sep2018-v1/00000/07AC2FCD-D220-CF40-89AE-333E8BBED0C1.root')
        else:
            if options.isMC:
                # options.inputFiles.append('/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_Zpt-150toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/FAACE9E0-1D0E-204E-9960-078F095EA34C.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_Zpt-150toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/0D2C1DA9-A99B-5C4E-9F2C-7447D8EE04A7.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_Zpt-150toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/0F27280E-AF6E-3C44-A6FB-54E3DF58C8C2.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_Zpt-150toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/0F5212B6-3C86-2349-9782-A86AFEBDA5C7.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_Zpt-150toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/12E5D413-E429-494C-94B5-221684BFB954.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_Zpt-150toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/161FD155-3EC3-0A45-A901-05FF98D6C035.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_Zpt-150toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/16A893BF-FC67-1E48-BBB6-4D93519ED16B.root')
                options.inputFiles.append('/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_Zpt-150toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/1B880673-27BB-F841-B5A4-299B9285832C.root')
            else:
                options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/325/159/00000/BE9BB28C-8AEC-1B4B-A7BD-AD1C9A0D67A8.root')
                options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/500/00000/12C8CC7E-8C95-E811-BDA3-FA163EA1F576.root')
                options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/569/00000/3C8C28E7-1A96-E811-BA8D-02163E012DD8.root')
                options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/570/00000/34C040A0-4096-E811-A1B7-FA163EEC3A41.root')
                options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/571/00000/5EEB8DC6-5996-E811-8980-FA163E3920AA.root')
                options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/612/00000/B673DB82-7496-E811-96F5-FA163E60F07A.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/617/00000/EA25096D-7696-E811-B2B7-FA163E646B29.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/654/00000/B8CADEC0-9896-E811-836C-FA163E5C80AE.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/083FC6BE-F297-E811-AD1C-FA163E896A2B.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/08EF0C25-F097-E811-9B11-FA163EC31020.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/1A2FCD53-F597-E811-9B6D-FA163E946965.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/303A23CD-EB97-E811-A503-FA163EDEC23B.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/54862F68-E897-E811-AA41-FA163E43522E.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/7AB08851-E797-E811-B220-02163E013016.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/7E50DA6A-F697-E811-91EE-02163E013EFD.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/A2AD48F7-F797-E811-A1C1-FA163EEFDF57.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/BE36A9F3-F097-E811-92FA-FA163E830D14.root')
                # options.inputFiles.append('/store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/BEA7BAB4-E997-E811-AA66-FA163E104BF4.root')
    elif options.resonance == 'JPsi':
        if options.isFullAOD:
            if options.isMC:
                options.inputFiles.append('/store/mc/RunIIAutumn18DRPremix/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/270001/FFF2FC1D-18CB-7244-9663-4E36963494B7.root')
            else:
                options.inputFiles.append('/store/data/Run2018A/Charmonium/AOD/17Sep2018-v1/100001/07679496-4DEF-1B44-BA04-768765A80599.root')


options.outputFile=""

if options.outputFile == ".root":
    if options.isMC:
        options.outputFile="_mc" + options.outputFile
    else:
        options.outputFile="_data"+ options.outputFile

    if options.resonance == 'Z':
        options.outputFile="_Z"+ options.outputFile
    else:
        options.outputFile="_JPsi"+ options.outputFile

    if options.isFullAOD:
        options.outputFile="output_full"+ options.outputFile
    else:
        options.outputFile+="output_mini"+ options.outputFile

print ('Output Root file:')
print (options.outputFile)


process = cms.Process("MuonAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load('Configuration.StandardSequences.EndOfProcess_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,globaltag, '')

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(options.inputFiles),
        secondaryFileNames=cms.untracked.vstring(),
        inputCommands=cms.untracked.vstring(
            'keep *',
            'drop *_ctppsPixelClusters_*_*'
        )
)

if options.includeJets:
    # for b-tagging
    process.load("RecoBTag.ImpactParameter.impactParameter_cff")
    process.load("RecoBTag.SecondaryVertex.secondaryVertex_cff")
    process.load("RecoBTag.SoftLepton.softLepton_cff")
    process.load("RecoBTag.Combined.combinedMVA_cff")
    process.load("RecoBTag.CTagging.cTagging_cff")
    process.load("RecoBTag.Combined.deepFlavour_cff")
    process.load("JetMETCorrections.Configuration.JetCorrectors_cff")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    numberOfThreads = cms.untracked.uint32(options.numThreads)
)

from MuonAnalysis.MuonAnalyzer.tools.ntuple_tools import *
if options.isStandAlone:
    if options.isFullAOD:
        if options.resonance == 'Z':
            process = muonAnalysis_customizeStandAloneFullAOD_Z(process)
        else:
            process = muonAnalysis_customizeFullAOD_JPsi(process) # No JPsi Standalone config set yet
        if not options.isMC:
            process.muon.jetCorrector = cms.InputTag(
                "ak4PFCHSL1FastL2L3ResidualCorrector")
    else:
        if options.resonance == 'Z':
            process = muonAnalysis_customizeStandAloneMiniAOD_Z(process)
        else:
            process = muonAnalysis_customizeMiniAOD(process)  # No JPsi Standalone config set yet

else:
    if options.isFullAOD:
        if options.resonance == 'Z':
            process = muonAnalysis_customizeFullAOD_Z(process)
        else:
            process = muonAnalysis_customizeFullAOD_JPsi(process)
        if not options.isMC:
            process.muon.jetCorrector = cms.InputTag(
                "ak4PFCHSL1FastL2L3ResidualCorrector")
    else:
        if options.resonance == 'Z':
            process = muonAnalysis_customizeMiniAOD_Z(process)
        else:
            process = muonAnalysis_customizeMiniAOD(process)


process.muon.isMC = options.isMC
process.muon.includeJets = options.includeJets
process.muon.era = options.era

# Trigger matching
muonSrc = "muons" if options.isFullAOD else "slimmedMuons"
from MuonAnalysis.MuonAssociators.muonL1Match_cfi import muonL1Match as _muonL1Match
process.muonL1Info = _muonL1Match.clone(
    src = cms.InputTag(muonSrc),
    useMB2InOverlap = cms.bool(True),
    useStage2L1 = cms.bool(True),
    preselection = cms.string(""),
    matched = cms.InputTag("gmtStage2Digis:Muon:")
)
process.muonL1InfoByQ = process.muonL1Info.clone(
    sortBy = cms.string("quality"),
    sortByQuality  = cms.bool(True),
    sortByDeltaPhi = cms.bool(False),
    sortByDeltaEta = cms.bool(False),
    sortByPt       = cms.bool(False)
)

from MuonAnalysis.MuonAnalyzer.hltInfo_cff import getHLTInfo, selectTriggers
hltInfo = getHLTInfo(options.resonance, options.era)
excludeDSA = (not options.isFullAOD)
process.muon.triggerPaths = cms.vstring(selectTriggers(hltInfo['triggerPaths'], True, False, excludeDSA))
process.muon.tagFilters = cms.vstring(selectTriggers(hltInfo['tagFilters'], not options.isFullAOD, True, excludeDSA))
process.muon.probeFilters = cms.vstring(selectTriggers(hltInfo['probeFilters'], not options.isFullAOD, True, excludeDSA))

# Standard selectors
from MuonAnalysis.MuonAnalyzer.selectorInfo_cff import getSelectorNamesAndBits
selectorNames, selectorBits = getSelectorNamesAndBits(options.era, options.isFullAOD)
process.muon.probeSelectorNames = cms.vstring(selectorNames)
process.muon.probeSelectorBits = cms.vuint32(selectorBits)

if options.includeJets:
    if not options.isMC:
        process.analysis_step = cms.Path(
            process.muonL1Info +
            process.muonL1InfoByQ +
            process.ak4PFCHSL1FastL2L3ResidualCorrectorChain +
            process.muSequence
        )
    else:
        process.analysis_step = cms.Path(
            process.muonL1Info +
            process.muonL1InfoByQ +
            process.ak4PFCHSL1FastL2L3CorrectorChain +
            process.muSequence
        )
else:
    process.analysis_step = cms.Path(
        process.muonL1Info +
        process.muonL1InfoByQ +
        process.muSequence
    )

process.TFileService = cms.Service("TFileService",
        fileName = cms.string(options.outputFile)
)
process.endjob_step = cms.EndPath(process.endOfProcess)

# process.fevt = cms.OutputModule("PoolOutputModule",
#     outputCommands = cms.untracked.vstring(),
#     fileName = cms.untracked.string("edm_output.root")
# )

process.schedule = cms.Schedule(process.analysis_step, process.endjob_step)

from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
