Extract the following insurance document into one JSON object per the output specification and schema.

Known metadata (copy these through into the JSON):
- country: {country}
- insurer_slug: {insurer_slug}
- insurer_name: {insurer_name}
- branch: {branch}
- document_type: {document_type}
- language: {language}
- source_url: {source_url}
- source_pages: {source_pages}
- prompt_version: {prompt_version}
- schema_version: {schema_version}

Allowed branch slugs for this country (the `branch` value must be one of these): {branch_slugs}

The document text follows. Pages are marked with `[[page N]]`. Cite these page numbers in every block's `page`
field. Capture EVERY coverage and EVERY exclusion - do not stop early or summarize away detail.

--- BEGIN DOCUMENT TEXT ---
{raw_text}
--- END DOCUMENT TEXT ---

Return only the JSON object.
