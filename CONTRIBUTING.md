## How to contribute
So you want to write code and get it landed in my Github Repo and want to help Data Scientists? Then first fork our repository into your own Github account, and create a local clone of it! 
The latter will be used to get new features implemented or bugs fixed. 
Once done and you have the code locally on the disk, you can get started. 
We advice to not work directly on the master branch, but to create a separate branch for each issue you are working on. 
That way you can easily switch between different work, and you can update each one for latest changes on upstream master individually. 
Check also our best practices for Git.

## Writing Code
For writing the code just follow our Python style guide, and also test with pylama. 
If there is something unclear of the style, just look at existing code which might help you to understand it better.

## Submitting Patches
When you think the code is ready for review a pull request should be created on Github. 
Owners of the repository will watch out for new PR‘s and review them in regular intervals. 
By default for each change in the PR we automatically run all the tests via Travis CI. 
If tests are failing make sure to address the failures immediately. Otherwise you can wait for a review. 
If comments have been given in a review, they have to get integrated. 
For those changes a separate commit should be created and pushed to your remote development branch. 
Don’t forget to add a comment in the PR afterward, so everyone gets notified by Github. 
Keep in mind that reviews can span multiple cycles until the owners are happy with the new code.

## Merging Pull Requests
Once a PR is in its final state it needs to be merged into the upstream master branch. For that please DO NOT use the Github merge button! 
But merge it yourself on the command line. Reason is that we want to hvae a clean history.
Before pushing the changes to upstream master make sure that all individual commits have been squashed into a single one with a 
commit message ending with the issue number, e.g. “Fix for broken download behavior (#45)”. Also check with git log to not push merge commits. O
nly merge PRs where Travis does not report any failure!
