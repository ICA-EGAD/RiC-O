# RiC-O PROF Profile (draft)

Draft work towards [issue #157](https://github.com/ICA-EGAD/RiC-O/issues/157) -
describing the RiC-O ecosystem as a [W3C PROF](https://www.w3.org/TR/dx-prof/)
`prof:Profile`, so its supporting resources (ontology, modules, SKOS
vocabularies, documentation, examples, validators, mappings) can be listed,
versioned, validated, and content-negotiated as first-class resources with roles.

- `RiC-O_profile-draft.ttl` - the profile stub. Not normative; a starting point
  for review.

Each artefact is a `prof:ResourceDescriptor` tagged with a `prof:hasRole`
(`role:schema`, `role:vocabulary`, `role:guidance`, `role:example`, `role:core`,
`role:validation`, `role:mapping`). Artefact IRIs currently point at the v1.1
locations on `ica-egad.github.io` / `ica.org`; these should be replaced with
stable resource IRIs (PURL / w3id) once settled.

Cross-references: the `role:validation` resource ties to the SHACL discussion in
[#156](https://github.com/ICA-EGAD/RiC-O/issues/156); the `role:mapping` resource
ties to the schema.org discussion in
[#72](https://github.com/ICA-EGAD/RiC-O/issues/72).
