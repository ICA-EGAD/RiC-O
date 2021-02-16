# Example for converting a METS-based Information Package

Examples prepared by: Tobias Wildi, member of ICA EGAD

Date of this example set: February 16, 2021

Language(s) used: German

These example files are under CC BY 4.0 license (https://creativecommons.org/licenses/by/4.0/).

For any question, please contact: Tobias Wildi (tobias.wildi@fhgr.ch).

This example is based on a simple Matterhorn METS Information Package, which has been converted to Matterhorn RDF by using RiC-O, PREMIS and Ebucore. The example shows a way to not only convert descriptive metadata, but a whole information package with technical and administrative metadata to a semantic model. Matterhorn RDF is a data model for digital preservation that covers the whole OAIS information model and it can for example be used with the Fedora 6 repository: https://duraspace.org/fedora/.

The folder contains:
- **IP-Matterhorn-METS:** A METS-based information package. METS is being used for structuring the package and contains very little semantic information. Within the descriptive metadata-sections (dmd-Sec) EAD is used and for the technical metadata (amd-Sec) you'll find Premis metadata.
- **IP-RiC-O:** The same package, but converted to RDF. METS is no longer necessary, since the structure is represented through the semantic network. The descriptive metadata were converted to RiC-O, the technical metadata to the PREMIS3-ontology: http://www.loc.gov/standards/premis/ontology/

More info about Matterhorn METS and Matterhorn RDF can be found here: http://matterhorn.tools/
