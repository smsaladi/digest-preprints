[![Build Status](https://travis-ci.org/smsaladi/codonw-slim.svg?branch=master)](https://travis-ci.org/smsaladi/digest-preprints)
[![DOI](https://data.caltech.edu/badge/243304809.svg)](https://data.caltech.edu/badge/latestdoi/243304809)

digest-preprints
=================

The purpose of this project is to consume, munge, and then serve
the content of preprint in an intuitive json format for easier programmatic
parsing/downstream development. It should relieve others from needing to
parse full-text html.

This project is under active development. Please share your input via issues.


# Envisioned Usage

## Routes

1. Routes to that resolve a given doi, e.g.

```text
https://{base_url}/{doi_prefix}/{doi_suffix}{preprint_server_versioning}
https://{base_url}/{doi_prefix}/{doi_suffix}{preprint_server_versioning}
```

2. into json-parsable bits of a preprint

```text
{1}/{metadata}
{1}/{abstract}
{1}/{body}
{1}/{references}
{1}/{figures}
```

3. and even more granular bits

```text
{1}/{paragraph}/{paragraphN}
{1}/{section}/{sectionN}
```

4. With formatting specifiers, where relevant, e.g.

```text
{1}/{body}/{paragraphN}?html=1
{1}/{body}/{figures}?format=url (default url=1) vs. {1}/{body}/{figures}?format=base64
```

5. Resolves to other interfaces (e.g. cantalope iiif server) where relevant, e.g.

```text
{1}/figures/iiif/{iiif_url_structure}
{1}/pdf
{1}/pdf/iiif/{iiif_url_structure}
```

## Responses

Responses are given in two parts: metadata in 'meta' and the data payload in 'data'.

This allows us to put things like the preprint's license along with the response
for the users to figure out if their use is permissible (since some preprints are 
All Right Reserved).

We could put things like the commit/release version of this repo
in there too. 

```text
{
        'meta': {'license': ''},
        'data': ['']
}
```

# Testing

All routes must have a test case implemented with the expected output.
