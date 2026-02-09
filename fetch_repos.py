#!/usr/bin/env python3
"""
Fetch GitHub repositories from an organization and save to CSV.
Usage: python fetch_repos.py <org_name>
"""

import csv
import json
import subprocess
import sys


def fetch_repos(org_name):
    """Fetch all repositories from a GitHub organization."""
    print(f"Fetching repositories from {org_name}...")

    try:
        # Use gh CLI to fetch repos
        result = subprocess.run(
            ['gh', 'repo', 'list', org_name, '--limit', '1000', '--json', 'name,url'],
            capture_output=True,
            text=True,
            check=True
        )

        repos = json.loads(result.stdout)
        return repos

    except subprocess.CalledProcessError as e:
        print(f"Error fetching repositories: {e.stderr}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        sys.exit(1)


def save_to_csv(repos, org_name):
    """Save repositories to a CSV file."""
    filename = f"{org_name}_repos.csv"

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'URL'])

        for repo in repos:
            writer.writerow([repo['name'], repo['url']])

    print(f"Saved {len(repos)} repositories to {filename}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python fetch_repos.py <org_name>")
        print("Example: python fetch_repos.py ansible-collections")
        sys.exit(1)

    org_name = sys.argv[1]
    repos = fetch_repos(org_name)
    save_to_csv(repos, org_name)


if __name__ == '__main__':
    main()
