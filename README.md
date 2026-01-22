# Java CVE Benchmark [![DOI](https://img.shields.io/badge/DOI-10.1145/3611643.3616262-blue.svg)](https://doi.org/10.1145/3611643.3616262) [![Visit Our Website](https://img.shields.io/badge/Website-Java_CVE_Bench-green)](https://sites.google.com/view/java-sast-study/home) [![](https://img.shields.io/badge/ESEC/FSE-2023-blue?style=flat-square)](https://2023.esec-fse.org/)

**Comparison and Evaluation on Static Application Security Testing (SAST) Tools for Java**

## Overview

This repository contains a **real-world Java vulnerability benchmark** comprising **165 unique CVEs** across popular Java open-source projects. Our benchmark is designed for comprehensive evaluation and comparison of Static Application Security Testing (SAST) tools, providing researchers and practitioners with a standardized dataset for vulnerability detection research.

## 🚀 Quick Start

> [!NOTE]
> **Current Status**: We currently provide **112 verified download URLs** out of 165 total CVEs. We are actively working to complete all 165 URLs and will update the database soon. Stay tuned for the complete dataset!

For your convenience, we provide a **ready-to-use download database** that allows you to quickly obtain all vulnerability data:

### Option 1: Direct Download (Recommended)
```bash
# Install required dependencies
pip install pandas requests

# Run the download script
python3 download_vulnerabilities.py
```

The script will:
- ✅ Read all 112 verified URLs from `java_cve_verified_download_urls.csv`
- ✅ Download JAR files to `final_downloads/` directory
- ✅ Show progress and handle errors gracefully
- ✅ Skip already downloaded files

### Option 2: Manual Selection
Browse `java_cve_verified_download_urls.csv` to select specific projects and versions for your research needs.

### Option 3: GitHub Repository Source Links
We also provide direct links to the original GitHub repositories and their version tags in `vulnerable_version_repo_info.json`. This allows you to:
- 🔗 Access the original source code repositories
- 🏷️ Checkout specific vulnerable versions using git tags
- 📂 Clone and build projects locally for deeper analysis

```bash
# Example: Clone a specific vulnerable version
git clone https://github.com/FasterXML/jackson-databind.git
cd jackson-databind
git checkout jackson-databind-2.9.10.7
```

> [!WARNING]
> **Disclaimer**: The GitHub repository links and version tag mappings are provided on a **best-effort basis**. THE INFORMATION IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. Repository availability and tag accuracy may vary over time.

## 📊 Benchmark Statistics

| Metric | Count |
|--------|-------|
| **Unique CVEs** | 165 |
| **Java Projects** | 165 |
| **CWE Weaknesses** | 37 |
| **CWE Classes** | 8 |
| **Vulnerable Methods** | 768 |
| **Fixed Methods** | 891 |
| **Average GitHub Stars** | 3,108 |
| **Verified Download URLs** | 112 |

## 🏗️ Repository Structure

```bash
.
├── README.md                              # This file
├── java_cve_verified_download_urls.csv    # Ready-to-use download database
├── vulnerable_version_repo_info.json      # GitHub repo URLs and version tags
├── vuln_data/                             # Vulnerability dataset
│   ├── README.md                          # Detailed dataset documentation
│   └── [165 CSV files]                    # Individual CVE data files
├── smart_vulnerability_downloader.py      # Advanced download tool
├── cve_patch_extractor.py                 # Patch extraction utilities
├── version_mapping_corrector.py           # Version mapping tools
└── paper/                                 # Research paper and supplementary materials
```

## 📈 Usage Scenarios

This benchmark is designed for:

- **🔍 SAST Tool Evaluation**: Comprehensive comparison of vulnerability detection capabilities
- **📚 Security Research**: Academic research on Java vulnerability patterns
- **🏭 Industry Benchmarking**: Standardized evaluation for commercial SAST tools

### Quick Download Database
- **`java_cve_verified_download_urls.csv`**: 112 verified download URLs
- **100% Success Rate**: All URLs tested and validated
- **Multiple Sources**: Maven Central (109) + GitHub (3)
- **Ready-to-Use**: No additional URL searching required

### GitHub Repository Source Links
- **`vulnerable_version_repo_info.json`**: Direct links to 60+ GitHub repositories
- **Version Tag Mapping**: Git tags for each vulnerable version
- **Source Code Access**: Clone and checkout specific vulnerable versions

## 📋 Data Format

Each CSV file in `vuln_data/` follows the naming convention:
```
{project_name}_{cve_id}_{version}.csv
```

**Example**: `jackson-databind_CVE-2020-36188_2.9.10.7.csv`

### CSV Content Structure
- **Vulnerability Path**: File paths, line ranges, method names
- **Fixed Path**: Corresponding fix locations and methods
- **Metadata**: CVE details, affected versions, CWE mappings

## 🎯 Key Features

- ✅ **Largest Scale**: 165 real-world Java CVEs
- ✅ **Expert Validated**: Rigorous three-expert validation process
- ✅ **Method-Level Granularity**: Precise vulnerability localization
- ✅ **Popular Projects**: High-star GitHub projects ensuring relevance
- ✅ **Ready-to-Use**: Pre-verified download URLs for immediate access
- ✅ **GitHub Source Links**: Direct access to original repositories with version tags
- ✅ **Comprehensive Coverage**: 37 CWE weaknesses across 8 classes
- ✅ **Research-Grade Quality**: Suitable for academic and industrial research

## 📚 Citation

If you use this benchmark in your research, please cite our paper:

```bibtex
@inproceedings{10.1145/3611643.3616262,
author = {Li, Kaixuan and Chen, Sen and Fan, Lingling and Feng, Ruitao and Liu, Han and Liu, Chengwei and Liu, Yang and Chen, Yixiang},
title = {Comparison and Evaluation on Static Application Security Testing (SAST) Tools for Java},
year = {2023},
isbn = {9798400703270},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3611643.3616262},
doi = {10.1145/3611643.3616262},
abstract = {Static application security testing (SAST) takes a significant role in the software development life cycle (SDLC). However, it is challenging to comprehensively evaluate the effectiveness of SAST tools to determine which is the better one for detecting vulnerabilities. In this paper, based on well-defined criteria, we first selected seven free or open-source SAST tools from 161 existing tools for further evaluation. Owing to the synthetic and newly-constructed real-world benchmarks, we evaluated and compared these SAST tools from different and comprehensive perspectives such as effectiveness, consistency, and performance. While SAST tools perform well on synthetic benchmarks, our results indicate that only 12.7\% of real-world vulnerabilities can be detected by the selected tools. Even combining the detection capability of all tools, most vulnerabilities (70.9\%) remain undetected, especially those beyond resource control and insufficiently neutralized input/output vulnerabilities. The fact is that although they have already built the corresponding detecting rules and integrated them into their capabilities, the detection result still did not meet the expectations. All useful findings unveiled in our comprehensive study indeed help to provide guidance on tool development, improvement, evaluation, and selection for developers, researchers, and potential users.},
booktitle = {Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering},
pages = {921–933},
numpages = {13},
keywords = {Benchmarks, Empirical study, Static application security testing},
location = {San Francisco, CA, USA},
series = {ESEC/FSE 2023}
}
```

## 🌐 Website

More details, interactive visualizations, and supplementary materials can be found on our [project website](https://sites.google.com/view/java-sast-study/home).

## 🤝 Contributing

We welcome contributions to improve and extend this benchmark:

- **🐛 Bug Reports**: Found an issue? Please open an issue
- **📊 Data Contributions**: Additional CVEs or improved annotations
- **🔧 Tool Improvements**: Enhancements to download and processing scripts
- **📖 Documentation**: Help improve documentation and examples

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

---

> [!IMPORTANT]
>
> 🚀 **Ready to start?** Download `java_cve_verified_download_urls.csv` and begin your SAST tool evaluation journey!
>
> 💡 **Questions or suggestions?** Feel free to open issues or submit PRs. We're here to help! :)
