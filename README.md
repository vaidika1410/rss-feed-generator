📰 RSS Feed Generator

This repository automates the generation of valid RSS feeds from structured YAML input. Designed to work alongside the rss-feed-demo repository, this tool converts YAML metadata into a fully-formed RSS XML feed — ideal for podcast publishing, article syndication, and content automation.

🔧 Features
Converts YAML files into RSS-compliant XML feeds

Automatically updates podcast.xml on push

GitHub Actions integration for CI/CD automation

Easy to extend for blogs, podcasts, and media platforms

📁 Structure
feed.yaml – Source content in YAML format

feed.py – Python script that generates the RSS feed

podcast.xml – Output RSS feed (auto-generated)

🚀 How It Works
Every time changes are pushed to this repo:

A GitHub Actions workflow runs.

feed.py reads from feed.yaml.

It generates or updates podcast.xml.

The updated feed is committed and pushed back.
