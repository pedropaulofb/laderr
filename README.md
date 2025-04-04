# LaDeRR: **La**nguage for **De**scribing **R**isk and **R**esilience

<p align="center"><img src="https://raw.githubusercontent.com/pedropaulofb/laderr/main/resources/logo_laderr.png" width="500"></p>

The **La**nguage for **De**scribing **R**isk and **R**esilience (**LaDeRR**) is an ontology-based textual domain-specific language (DSL) for resilience modeling. It was designed to specify resilience scenarios, in a standardized format, through the specification of the participating entities and the interplay between their capabilities and vulnerabilities.


## Table of Contents

<!-- TOC -->

- [Introduction](#introduction)
- [Writing a LaDeRR Specification](#writing-a-laderr-specification)
- [Permanent URLs for LaDeRR Resources](#permanent-urls-for-laderr-resources)
  - [LaDeRR](#laderr)
  - [LaDeRR Vocabulary Resources](#laderr-vocabulary-resources)
  - [LaDeRR Engine](#laderr-engine)
- [Available Artifacts](#available-artifacts)
  - [LaDeRR Metamodel](#laderr-metamodel)
  - [LaDeRR Rules](#laderr-rules)
  - [LaDeRR Vocabulary](#laderr-vocabulary)
  - [SHACL Shapes for Data Validation](#shacl-shapes-for-data-validation)
- [License](#license)
- [How to Contribute](#how-to-contribute)
- [Contributors](#contributors)

<!-- /TOC -->

## Introduction

In an increasingly complex and interconnected world, resilience has become a fundamental concept in risk management. Organizations and systems must withstand, adapt to, and recover from disruptions caused by threats and vulnerabilities. Addressing these challenges requires precise modeling and representation of resilience-related concepts, which is essential for effective decision-making and risk assessment.

To meet this need, researchers have developed [**ResiliOnt**](https://doi.org/10.1007/978-3-031-75872-0_21) (available [here](https://www.researchgate.net/publication/383658567_Ontological_Foundations_of_Resilience)), an OntoUML ontology that provides a rich semantic foundation for resilience modeling. However, using ontologies for practical applications in risk assessment and resilience analysis often requires a structured **domain-specific language (DSL)** that enables clear and precise descriptions of risk scenarios.

While ontologies provide rigorous conceptual models, they often lack formal computational syntax that can be directly used in software tools. Similarly, traditional modeling languages, such as UML, are not expressive enough to represent all necessary logical constraints in resilience analysis. A well-defined DSL can bridge this gap by offering:

- **A structured representation of risk and resilience scenarios** with explicit rules.
- **A computationally interpretable format** for automated reasoning and decision support.
- **A user-friendly syntax** that facilitates adoption by domain experts.

These requirements motivate the development of **LaDeRR (Language for Describing Risk and Resilience)**, a DSL that integrates formal resilience modeling with computational representations. Currently, LaDeRR is primarily focused on representing resilience scenarios, but there is an intent to extend its capabilities to cover risk concepts more comprehensively in future versions.

LaDeRR is a *Domain-Specific Language (DSL)* designed to represent, analyze, and compute resilience and risk-related scenarios. It is built on top of ResiliOnt and offers a structured approach to defining resilience constructs, their relationships, and logical constraints.

The language consists of two main components:

1. **Abstract Syntax (UML + FOL):** Defines the conceptual model using UML class diagrams, complemented by First-Order Logic (FOL) rules to express derivations and constraints.
2. **Textual Concrete Syntax (TOML):** Provides a machine-readable format for defining resilience models in practice.

A third component is planned for a future release:

3. **Visual Concrete Syntax (Planned):** A future graphical representation intended to support intuitive modeling. This component will complement the textual syntax by offering a user-friendly graphical notation to manipulate LaDeRR constructs.

The following diagram illustrates the relationship between ResiliOnt and LaDeRR, highlighting the mapping process and different syntactic representations:

<p align="center"><img src="https://raw.githubusercontent.com/pedropaulofb/laderr/main/documentation/images/laderr-visual-schema.png" width="750"></p>

To support computational reasoning over LaDeRR models, the **LaDeRR Engine** has been developed. It is a Python-based tool that enables the representation, analysis, and validation of resilience scenarios.
The engine is available at the [LaDeRR Engine Repository](https://w3id.org/laderr/engine/git).

LaDeRR was designed to combine semantic precision with computational usability, ensuring that resilience-related constructs can be represented, validated, and analyzed consistently. The justification for this approach includes:

- **Semantic Foundation:** The language builds upon ResiliOnt to ensure conceptual clarity and ontological soundness.
- **Computational Reasoning:** The **abstract syntax** includes formal logical constraints (FOL) to define the conditions under which resilience and risk-related relations hold.
- **Practical Application:** The **textual syntax (TOML)** makes it easy to integrate LaDeRR with software tools, enabling automated reasoning and model validation.
- **Expressive Power:** The use of derivations, constraints, and rules enhances the modeling capabilities beyond what UML alone can offer.

By combining ontological foundations with formal rules and computational syntax, LaDeRR provides a powerful and extensible framework for describing risk and resilience in various domains.

Although LaDeRR currently focuses on resilience scenarios, future developments will incorporate broader risk analysis concepts to create a more comprehensive risk and resilience modeling language.

## Writing a LaDeRR Specification

To facilitate the adoption and correct usage of LaDeRR, we provide a detailed guide on how to create specifications of resilience scenarios using the language.

The guide includes:
- A comprehensive overview of LaDeRR specifications, covering their essential components.
- Instructions on defining Entities, Capabilities, Vulnerabilities, Threats, Controls, and Resilience.
- Illustrative examples demonstrating complete LaDeRR specifications.

**(Under development) Access the full guide here:** [How to Write a LaDeRR Specification](https://github.com/pedropaulofb/laderr/blob/main/docs/how-to-write-laderr-spec.md)

## Permanent URLs for LaDeRR Resources

To ensure persistent and stable access to LaDeRR resources, we provide permanent URLs using the [W3ID](https://w3id.org/) system. These URLs enable long-term access to the LaDeRR specification, vocabulary, and engine.

The following **W3ID redirects** provide access to LaDeRR's key artifacts:

### LaDeRR

- **Git repository:** [w3id.org/laderr/git](https://w3id.org/laderr/git)

#### Versioning & Releases
- **Latest release:** [w3id.org/laderr/latest](https://w3id.org/laderr/latest)
- **All releases:** [w3id.org/laderr/releases](https://w3id.org/laderr/releases)

### LaDeRR Vocabulary Resources
- **Homepage:** [w3id.org/laderr](https://w3id.org/laderr)
- **Vocabulary:** The generation of all formats was performed using RDFLib, with the TTL file serving as input.
  - **Turtle:** [w3id.org/laderr/format/ttl](https://w3id.org/laderr/format/ttl)
  - **RDF/XML (OWL):** [w3id.org/laderr/format/owl](https://w3id.org/laderr/format/owl)
  - **N-Triples:** [w3id.org/laderr/format/nt](https://w3id.org/laderr/format/nt)
  - **Notation3 (N3):** [w3id.org/laderr/format/n3](https://w3id.org/laderr/format/n3)
  - **JSON-LD:** [w3id.org/laderr/format/jsonld](https://w3id.org/laderr/format/jsonld)
  - **TriG:** [w3id.org/laderr/format/trig](https://w3id.org/laderr/format/trig)

### LaDeRR Engine
- **Homepage:** [w3id.org/laderr/engine](https://w3id.org/laderr/engine)
- **Repository:** [w3id.org/laderr/engine/git](https://w3id.org/laderr/engine/git)
- **Latest release:** [w3id.org/laderr/engine/latest](https://w3id.org/laderr/engine/latest)
- **All releases:** [w3id.org/laderr/engine/releases](https://w3id.org/laderr/engine/releases)


## Available Artifacts

The LaDeRR repository contains several artifacts that support the development, documentation, and computational use of the **Language for Describing Risk and Resilience (LaDeRR)**. These artifacts include the **metamodel, vocabulary, rules, SHACL shapes for validation, and documentation resources**.

### LaDeRR Metamodel

The **metamodel** of LaDeRR is provided in two formats:
- **Editable Version (VPP File):** The **Visual Paradigm Project File (`laderr-metamodel-v*.vpp`)** allows further modifications and extensions of the metamodel.
- **Images:** The **metamodel is available as images** in the `metamodel_images` folder, which contains individual diagrams for different aspects of LaDeRR, including constructs, specifications, resilience, dispositions, and entities.

### LaDeRR Rules

The metamodel is complemented by logical rules that define constraints and derivations that cannot be fully expressed in UML class diagrams. These rules are available in the file:
- `laderr-rules-v*.xlsx`: This file contains a structured set of logical rules, including derivations, constraints, and formal conditions that enhance the expressiveness of LaDeRR.


### LaDeRR Vocabulary

The **LaDeRR Vocabulary** is an OWL 2 vocabulary that provides a formal semantic schema for LaDeRR model instances. It aligns with the structure defined by the metamodel, but its purpose is distinct: the LaDeRR Vocabulary defines the **data model** used by the laderr-engine to represent, reason over, and validate LaDeRR specifications as RDF graphs.

This vocabulary implements the modeling constructs (e.g., `Entity`, `Capability`, `Threat`, `Scenario`, `Resilience`, etc.) as OWL classes and properties, enabling semantic reasoning and interoperability across systems. It serves as the **machine-processable schema** that supports LaDeRR applications.

The full documentation of the vocabulary is available at: [https://w3id.org/laderr](https://w3id.org/laderr)

The base URI [https://w3id.org/laderr/format](https://w3id.org/laderr/format) can be used to retrieve the LaDeRR vocabulary in a specific RDF serialization format by appending the desired format as a path segment. For example, to access the vocabulary in Turtle, use [https://w3id.org/laderr/format/ttl](https://w3id.org/laderr/format/ttl), or for JSON-LD, use [https://w3id.org/laderr/format/jsonld](https://w3id.org/laderr/format/jsonld).

You can access the vocabulary directly in specific formats using the links below:

- Turtle (source): [`laderr-vocabulary-v*.ttl`](https://w3id.org/laderr/format/ttl)
- Other formats:
  - [JSON-LD](https://w3id.org/laderr/format/jsonld)
  - [N-Triples](https://w3id.org/laderr/format/nt)
  - [OWL (RDF/XML)](https://w3id.org/laderr/format/owl)
  - [Notation3 (N3)](https://w3id.org/laderr/format/n3)
  - [TriG](https://w3id.org/laderr/format/trig)

### SHACL Shapes for Data Validation

To ensure that LaDeRR models conform to the defined vocabulary, **SHACL (Shapes Constraint Language) shapes** were created for validation. These are available in the `shapes` folder:
- `laderr-shape-entity-v*.shacl`
- `laderr-shape-resilience-v*.shacl`
- `laderr-shape-scenariocomponent-v*.shacl`
- `laderr-shape-scenario-v*.shacl`
- `laderr-shape-specification-v*.shacl`
- `laderr-shape-threat-v*.shacl`
- `laderr-shape-vulnerability-v*.shacl`
- `laderr-shape-asset-v*.shacl`
- `laderr-shape-capability-v*.shacl`
- `laderr-shape-construct-v*.shacl`
- `laderr-shape-control-v*.shacl`
- `laderr-shape-disposition-v*.shacl`

These SHACL files enable automated validation of LaDeRR models, ensuring that each instance adheres to the constraints defined in the vocabulary.


## License
The **LaDeRR DSL** is released under the **[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)**, a **permissive open-source license** that allows free use, modification, and distribution of the specifications. This ensures that LaDeRR can be adopted, extended, and integrated into both academic and industrial applications, while maintaining intellectual property protections.


## How to Contribute
Contributions to LaDeRR are **highly encouraged**! The language is an evolving project, and community input is essential for improving its expressiveness, usability, and computational support. You can contribute to this project in the following ways.

1. **Report Issues:** If you find bugs, inconsistencies, or unclear documentation, please open an **[issue](https://github.com/pedropaulofb/laderr/issues)** in the GitHub repository.

2. **Suggest Improvements:** If you have ideas for enhancing LaDeRR, propose them through **issues** in the repository.

3. **Submit Pull Requests (PRs):** Contributions to the vocabulary, abstract syntax, or documentation are welcome via **[pull requests](https://github.com/pedropaulofb/laderr/pulls)**.

Your feedback and contributions will help refine LaDeRR and expand its capabilities to better support risk and resilience specification.


## Contributors

This work was developed by researchers from the [Business Informatics Group of Ghent University, Belgium](https://ugent-businessinformatics.github.io/) and the [Semantics, Cybersecurity & Services Group at the University of Twente, Netherlands](https://www.utwente.nl/en/eemcs/scs/).

<table>
  <tr>
    <td><strong>Pedro Paulo F. Barcelos</strong></td>
    <td>
      <a href="https://orcid.org/0000-0003-2736-7817"><img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" alt="ORCID" width="20"/></a>
      <a href="https://github.com/pedropaulofb"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="20"/></a>
      <a href="https://www.linkedin.com/in/pedro-paulo-favato-barcelos/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="20"/></a>
    </td>
  </tr>
  <tr>
    <td><strong>Frederik Gailly</strong></td>
    <td>
      <a href="https://orcid.org/0000-0003-0481-9745"><img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" alt="ORCID" width="20"/></a>
      <a href="https://github.com/fgailly"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="20"/></a>
      <a href="https://www.linkedin.com/in/fgailly/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="20"/></a>
    </td>
  </tr>
  <tr>
    <td><strong>Geert Poels</strong></td>
    <td>
      <a href="https://orcid.org/0000-0001-9247-6150"><img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" alt="ORCID" width="20"/></a>
      <a href="https://github.com/geertpoels"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="20"/></a>
      <a href="https://www.linkedin.com/in/geert-p-039198287/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="20"/></a>
    </td>
  </tr>
  <tr>
    <td><strong>Giancarlo Guizzardi</strong></td>
    <td>
      <a href="https://orcid.org/0000-0002-3452-553X"><img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" alt="ORCID" width="20"/></a>
      <a href="https://www.linkedin.com/in/giancarlo-guizzardi/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="20"/></a>
    </td>
  </tr>
</table>
