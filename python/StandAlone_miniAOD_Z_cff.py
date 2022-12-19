'''author: g. karathanasis
parameters for miniAOD'''

import FWCore.ParameterSet.Config as cms

muon = cms.EDAnalyzer('StandAloneMuonMiniAODAnalyzer',
           isMC=cms.bool(False),
           includeJets=cms.bool(False),
           era = cms.string('dummy'), # updated in run_muonAnalyzer_cfg.py
           genEventInfo = cms.InputTag('generator'),
           pileupInfo=cms.InputTag('slimmedAddPileupInfo'),
           Rho=cms.InputTag('fixedGridRhoFastjetAll'),
           beamSpot=cms.InputTag('offlineBeamSpot'),
           vertices=cms.InputTag("offlineSlimmedPrimaryVertices"),
           muons=cms.InputTag("slimmedMuons"),
           triggerResults=cms.InputTag("TriggerResults::HLT"),
           l1Matches = cms.InputTag("muonL1Info"),
           l1MatchesQuality = cms.InputTag("muonL1Info", "quality"),
           l1MatchesDeltaR = cms.InputTag("muonL1Info", "deltaR"),
           l1MatchesByQ = cms.InputTag("muonL1InfoByQ"),
           l1MatchesByQQuality = cms.InputTag("muonL1InfoByQ", "quality"),
           l1MatchesByQDeltaR = cms.InputTag("muonL1InfoByQ", "deltaR"),
           PFCands=cms.InputTag("packedPFCandidates"),
           lostTracks=cms.InputTag("lostTracks"),
           SAmuons=cms.InputTag("standAloneMuons"),
           gen = cms.InputTag("prunedGenParticles"),
           rhoJetsNC = cms.InputTag("fixedGridRhoFastjetCentralNeutral"),
           jets = cms.InputTag("slimmedJets"),
           genJets = cms.InputTag("slimmedGenJets"),
           triggerPaths=cms.vstring(), # updated in run_muonAnalyzer_cfg.py
           tagFilters=cms.vstring(), # updated in run_muonAnalyzer_cfg.py
           probeFilters=cms.vstring(), # updated in run_muonAnalyzer_cfg.py
           probeSelectorNames=cms.vstring(), # updated in run_muonAnalyzer_cfg.py
           probeSelectorBits=cms.vuint32(), # updated in run_muonAnalyzer_cfg.py
           tagQuality = cms.uint32(0), # quality of tag muon following muonSelector convention
           tagSelection = cms.string("pt()>27"), # string to pass cuts on tag
           ProbeHPurity = cms.bool(False), # skips non High purity probes
           probeSelection = cms.string("pt()>10"), #string for probe
           probeSelectionSA = cms.string("pt()>10"), #string for probe
           muonOnly = cms.bool(True), # allow only reco or pat Muon for probes
           probeMuonSelection = cms.string("pt()>10"), #string for probe (reco or pat Muon)
           pairMassMin = cms.double(40.0), # min mass of mu pair
           pairMassMax = cms.double(150.0), # max mss of mu pair (9999.0 for high mass C&C)
           pairDz = cms.double(1e99), #max Dz of mu1,mu2
           RequireVtxCreation = cms.bool(False), # if true kills pairs w/o vtx
           minSVtxProb = cms.double(0.01), # min prob of mu pair
           maxDzProbeTrkMuon = cms.double(1.0), # max Dz(mu1,mu2)
           maxRelPtProbeTrkMuon = cms.double(2.0),# max [pt(mu)-pt(trk)]/pt(trk) for probe/offline
           maxDRProbeTrkMuon =  cms.double(0.3), # max DR for probe/offline
           minPtTrkSA=cms.double(2.0),  # min Pt for trk matching for SA muons
           maxDzProbeTrkSAMuon = cms.double(1.0), # max Dz(trk,SAmu)
           maxRelPtProbeTrkSAMuon = cms.double(2.0),# max [pt(SAmu)-pt(trk)]/pt(trk) for probe/offline
           maxDRProbeTrkSAMuon =  cms.double(0.3), # max DR for trk / SA muon
           momPdgId = cms.uint32(23),
           genRecoDrMatch= cms.double(0.03),
           saveStandAloneTree = cms.bool(True),
           saveTnPTree = cms.bool(True),          
           propM1 = cms.PSet(
               useStation2 = cms.bool(False),
               useTrack = cms.string("tracker"),
               useState = cms.string("atVertex"),  # in AOD
               useSimpleGeometry = cms.bool(True), # use just one cylinder and two planes, not all the fancy chambers  
           ),

)

miniAODSequence=cms.Sequence(muon)
