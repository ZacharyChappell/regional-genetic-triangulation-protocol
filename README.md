# Regional Genetic Triangulation Protocol

Public protocol and synthetic-data scaffold for cross-modal triangulation of regional genetic liability axes in neurodegenerative disease.

Project page: [Open Science Framework](https://osf.io/y2zf5/overview)

## Overview

This repository documents a staged research framework for evaluating whether disease-prioritised regional genetic components can be followed as reproducible liability-indexing axes across imaging, molecular and clinical domains.

The project is motivated by post-GWAS interpretation challenges in late-onset neurodegenerative disease. Common genetic susceptibility is distributed, linkage disequilibrium creates regional dependence, and downstream phenotypes such as diagnosis and MRI-derived measures are indirect markers of underlying biology.

The central question is:

> Can pre-specified regional genetic components be tested for convergent evidence across independent imaging cohorts, transcriptomic and epigenomic resources, proteomic data, fine-mapping analyses and clinical phenotypes?

## PhD context

This project grows out of my PhD research at King's College London, which developed and applied LD-constrained local independent component analysis (LD-CLICA): an LD-aware framework for modelling structured local genotype variation in neurodegenerative disease.

The thesis used LD-CLICA to learn regional genetic components, evaluate disease associations, assess conditional robustness, perform representation-level localisation, and test whether disease-prioritised components showed multimodal white-matter imaging associations in an independent UK Biobank imaging cohort.

This repository does not reproduce protected analyses or release individual-level data. Instead, it provides a public-facing protocol, synthetic-data examples and workflow scaffolds for the next stage of work: testing whether selected disease-prioritised components can be characterised through independent replication and cross-modal biological triangulation.

## Scientific framing

This is a conservative biological triangulation framework. It does **not** claim that regional genetic components prove causal mechanisms. 

Instead, the framework treats such components as pre-specified genetic indices that can be followed through a staged validation hierarchy:

1. component-to-molecular annotation;
2. independent imaging replication and extension;
3. molecular-imaging convergence analysis;
4. conditional and causal refinement only after replication.

## Immediate purpose

This repository is intended to provide a transparent public scaffold for:

- research planning;
- synthetic-data demonstrations;
- reproducible workflow templates;
- validation hierarchy design;
- reviewer risk assessment;
- dataset access planning;
- technical notes and protocol development.

## Documentation

- [Project rationale](docs/project_rationale.md)
- [Validation hierarchy](docs/validation_hierarchy.md)
- [Dataset access plan](docs/dataset_access_plan.md)
- [Limitations and design risks](docs/limitations_and_design_risks.md)
- [Public/private boundary](docs/public_private_boundary.md)

## Data governance

This repository does **not** contain individual-level genetic, imaging, clinical or phenotypic data.

It does **not** contain UK Biobank data, participant identifiers, protected genotype files, MRI-derived individual-level outputs, controlled-access data, or private component score files.

Any examples in this repository will use synthetic or openly shareable data only.

## Repository structure

```text
docs/
  project_rationale.md
  validation_hierarchy.md
  dataset_access_plan.md
  limitations_and_design_risks.md
  public_private_boundary.md

notebooks/
  .gitkeep

src/
  .gitkeep

reports/
  .gitkeep

```

## Author

Zachary Lee Chappell 
PhD researcher in statistical genetics, computational neuroimaging and neurodegenerative disease modelling. .gitkeep

## License

Code in this repository is released under the MIT License. 
Written protocol materials should be cited if reused.
