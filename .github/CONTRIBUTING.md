# Contributing
## Writing change log to changelog.py
When writing change log to changelog.py, follow the following markdown syntax, as NVDA add-on dialog shows changes in markdown -> HTML:
- After releasing a version, remove the changelog entries, and start adding new changelog entries for the new version as they become available. Do not wait for the next version release to write the changelog. This can be painful especially if hundreds of changes to add-on (practically) are made.
- Use list based entry changes, proceeded by a dash (`-`) character and a space followed by a changelog entry.
- Use new line delimiter, `\n`

Example:
```
value = _(
	"- Changed 1"
) + "\n" + _(
	"- Changed 2"
) + "\n" + _(
	"- Changed 3"
```
