# Type stubs for PEP 739 build-details.json

This provides a basic set of TypedDict definitions for the json data.

There is no actual code here, just the stubs


## Revisions

Because PEP 739 is revisable, there is a plan in place for this.

The stubs export two module level constants:

- `PEP739_v1`: This is a union of all possible PEP 739 revisions of major version
  1, ie. 1.1, 1.2. Each revision has it's schema as a constant of `Literal['X.Y']`,
  so it should be possible to differentiate the union based on that.
- `PEP739`: This is a union of all possible PEP 739 revisions, regardless of
  major version.

As new major revisions are added, a new constant will be added for that major
version.

Additionally, if the end user knows what version they wish to output, the
versions are exposed through the `vX_Y` modules. For example, if the user
knows that they only will use version 1.0, they can import `pep749.v1_0`.
