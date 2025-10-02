# Java CVE Benchmark - Vulnerability Data

This folder contains the **165 vulnerable Java projects** that comprise our real-world vulnerability benchmark dataset. To the best of our knowledge, this is the **largest real-world Java vulnerability benchmark** available.

## 📊 Dataset Overview

Our benchmark includes:
- **165 unique CVEs** across 165 Java open-source programs
- **37 CWE weaknesses** and **8 CWE Classes** (CWE-1000 View)
- **768 vulnerable methods** and **891 corresponding fixed methods**
- Programs with an average of **3,108 GitHub stars** (as of August 2022)

## 🔬 Data Collection Methodology

We conducted the vulnerability data collection in four comprehensive steps:

### 1. Java Programs Collection
We searched Java open-source programs with disclosed CVEs and corresponding patch commits from advisory sources such as:
- **NVD** (National Vulnerability Database)
- **Debian** Security Advisories
- **Red Hat Bugzilla**

This initial search yielded a list of **680 programs**.

### 2. Version Range Extraction and Method-Level Locating
- **V-SZZ Algorithm**: Used to extract the vulnerable version range of programs affected by each CVE, ensuring accurate identification of affected software versions
- **Universal Ctags**: Employed to locate method-level information for both vulnerable and fixed versions, essential for detailed vulnerability analysis

### 3. Program Packaging
Since evaluation tools accept different input types (source code and binaries), we excluded programs that failed to be packaged, resulting in our final dataset of **165 packageable open-source programs**.

### 4. Cross-Validation by Security Experts
To ensure benchmark accuracy, we engaged **three security experts** from our industry partner with:
- **7+ years** of Java programming experience
- **5+ years** of vulnerability knowledge

#### Validation Process:
1. **Tool Results Validation**: Each expert independently verified vulnerability locations identified by our automated process
2. **Code Context Understanding**: Deep analysis of reported vulnerability code, examining functionality, role within the program, and component interactions
3. **Vulnerability and Patch Review**: Thorough review of vulnerability details and patch information from NVD, Debian, and Red Hat Bugzilla
4. **Independent Cross-Validation**: Experts cross-validated each other's results
5. **Consensus Building**: Majority voting for decisions, with discussions to resolve conflicts
6. **Final Voting and Labeling**: Confirmed decisions through final voting, with detailed labeling of vulnerability locations, affected versions, and specific methods

## 📁 Data Structure

### File Naming Convention
Each CSV file follows this structure: `"Program Name"_"CVE-ID"_"Version".csv`

**Example**: `active-directory-plugin_CVE-2017-2649_active-directory-plugin-active-directory-2.2.csv`
- **Program**: active-directory-plugin
- **CVE**: CVE-2017-2649
- **Version**: active-directory-plugin-active-directory-2.2

### CSV File Content
Each CSV file contains label information for a specific CVE, including:

#### Vulnerability Path
- **Vulnerable files**: Source file paths
- **Line ranges**: Specific line numbers containing vulnerabilities
- **Method names**: Methods containing vulnerable code

#### Fixed Path
- **Fixed files**: Source file paths with patches applied
- **Line ranges**: Specific line numbers with fixes
- **Method names**: Methods containing fixed code

### Example Entry
For **CVE-2017-2649**:
- **Vulnerable File**: `src/main/java/hudson/plugins/active_directory/ActiveDirectorySecurityRealm.java`
- **Line Range**: 208-210
- **Method**: `ActiveDirectorySecurityRealm`
- **Fixed Path**: Similar structure with corresponding fix information

## 🎯 Benchmark Significance

This benchmark represents:
- **Real-world vulnerabilities** from production Java applications
- **Comprehensive coverage** across multiple CWE categories
- **Expert-validated** vulnerability locations and fixes
- **Method-level granularity** for precise analysis
- **Popular projects** ensuring practical relevance

## 📈 Usage

This dataset is designed for:
- **Vulnerability detection tool evaluation**
- **Security research** on Java applications
- **Machine learning** model training for vulnerability prediction
- **Comparative analysis** of security tools and techniques

## 🔍 Quality Assurance

Every vulnerability in this benchmark has been:
- ✅ **Automatically detected** using V-SZZ algorithm
- ✅ **Method-level located** using Universal Ctags
- ✅ **Expert validated** by three security professionals
- ✅ **Cross-validated** through independent review
- ✅ **Consensus approved** through majority voting

---

*For more details about the benchmark construction and validation process, please refer to our research paper.*
