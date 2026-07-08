InfoCheck
InfoCheck is a custom Python automation toolkit for batch calculation of information-theoretic gene tree quality scores across large phylogenomic datasets.
Overview
InfoCheck implements two complementary approaches for evaluating gene-by-gene reliability for phylogenetic inference.
1. Tree Certainty Score (TCA/ICA)
The Relative Tree Certainty Allpartitions (TCA) score is an information-theoretic metric quantifying the overall degree of conflict among trees in a given tree set (Salichos et al., 2014). For each ortholog gene tree, 200 bootstrap replicates are generated using IQ-TREE2 v2.3.6 under the GTR+G model. The TCA score is computed as the sum of Internode Certainty All (ICA) scores across all bipartitions. Each ICA score measures how similar a given bipartition in the gene tree is to the intersecting bipartitions in the bootstrap treeset. A score of 1.0 indicates complete concordance, a score of -1.0 indicates complete conflict, and values near 0 indicate high disagreement among intersecting bipartitions. TCA scores are computed using RAxML v8.2.12 (Stamatakis, 2014) and batch processed across all gene trees using this toolkit.
2. Pythia Difficulty Score
Pythia 2.0 (Haag and Stamatakis, 2025) uses RAxML-NG v1.2.2 and a Gradient Boosted Trees regressor to predict the likelihood that multiple independent maximum-likelihood tree inferences will converge on a single topology for a given alignment. Scores range from 0.0 (easy, where inferences will reliably converge) to 1.0 (difficult, where inferences will diverge into conflicting topologies). InfoCheck automates Pythia scoring across all alignment files in a dataset.
Usage
Both scoring approaches were applied across 4,845 ortholog alignments as part of a phylogenomic analysis of Aizoaceae.

Citations

Salichos, L. et al. (2014). Novel information theory-based measures for quantifying incongruence among phylogenetic trees. Molecular Biology and Evolution 31(5): 1261–1271.
Stamatakis, A. (2014). RAxML version 8. Bioinformatics 30(9): 1312–1313.
Haag, J. and Stamatakis, A. (2025). Pythia 2.0.
Kozlov, A.M. et al. (2019). RAxML-NG. Bioinformatics 35(21): 4453–4455.
