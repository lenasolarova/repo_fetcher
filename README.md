# GitHub Repository Fetcher

A simple Python script to fetch all repositories from a GitHub organization and save them to a CSV file.

## Usage

```bash
python3 fetch_repos.py <org_name>
```

**Examples:**
```bash
python3 fetch_repos.py ansible-collections
python3 fetch_repos.py ansible
python3 fetch_repos.py water-hole
```

## Requirements

- Python 3
- GitHub CLI (`gh`) installed and authenticated

## Output Files

The script generates CSV files with the format `{org_name}_repos.csv` containing:
- Repository name
- Repository URL

### Included Files

- `ansible-collections_repos.csv` - 150 repositories from ansible-collections org
- `ansible_repos.csv` - 381 repositories from ansible org
- `water-hole_repos.csv` - 13 repositories from water-hole org
