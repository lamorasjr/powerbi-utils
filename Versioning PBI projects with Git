# Power BI Desktop versioning with Git
## Requirements
* Power BI files saved as .pbip format
    * Go to File > Options and settings > Options > Preview features and check the box next to 'Power BI Project (.pbip) save option'
    * Keep unchecked the options:
        * 'Store semantic model using TMDL format'
        * 'Store reports using enhanced metadata format (PBIR)' 

## Basic Git Commands
`<to-be-defined>`

## Repository Schema
* Root\
    * \pbi-dataset
        * \dataset-project-1
        * \dataset-project-2
        * \dataset-project-n
    * \pbi-report
        * \report-project-1
        * \report-project-2
        * \report-project-n

## Development Workflows
### 1. Creation of new Power BI file in Power BI Desktop
* Scenarios: 
    * Creation of new Power BI files in Power BI desktop
    * Isolated changes of Power BI files in Power BI Desktop
* Worflow:
    * Create a branch from main using VSCode/GithubDesktop (feature/datasetchange)
    * Make changes to semantic model using Power BI Desktop
    * Commit changes to remote repository branch using VSCode/GithubDesktop
    * Create Pull Request to main branch using the Git provider
    * The team leader reviews the Pull Requests and synchronizes the changes to the team workspace

### 2. Changes in linked Power BI files in Power BI Desktop
* Scenarios:
    * Change in a Report linked to a semantic model in Power BI Service
* Worflokw:
    * Create branch from main using VSCode/GithubDesktop (feature/reportchange)
    * Make changes to semantic model using Power BI Desktop and publish it to My Workspace
    * Make changes to report:
        * Change the connection to semantic model in 'My Workspace'
        * Once finished, retrieve the connection to team workspace
    * Commit changes to remote repository branch using VSCode/GithubDesktop
    * Create Pull Request to main branch using the Git provider
    * The team leader reviews the Pull Requests and synchronizes the changes to the team workspace

## Templates
`<to-be-defined>`

## Reference
* (Azure DevOps Build Pipelines)[https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-build-pipelines]