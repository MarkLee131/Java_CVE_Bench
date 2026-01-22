## 📋 Pull Request: Add GitHub Repository Source Links

### Description

This PR adds GitHub repository source links and version tag mappings to the Java CVE Benchmark dataset, enabling users to directly access the original source code repositories for each vulnerable project.

### Changes

- ✅ Added `vulnerable_version_repo_info.json` containing:
  - Direct GitHub repository URLs for 60+ Java projects
  - Version-to-tag mappings for vulnerable versions
- ✅ Updated `README.md` with:
  - New "Option 3: GitHub Repository Source Links" section
  - Updated repository structure documentation
  - Added GitHub source links to Key Features

### New Data Format

The `vulnerable_version_repo_info.json` file contains:
```json
{
  "library_name_to_github_url": {
    "library-name": "https://github.com/org/repo"
  },
  "library_version_to_tags": {
    "library-name": {
      "version": "git-tag"
    }
  }
}
```

### Usage Example

```bash
# Clone and checkout a specific vulnerable version
git clone https://github.com/FasterXML/jackson-databind.git
cd jackson-databind
git checkout jackson-databind-2.9.10.7
```

### ⚠️ Disclaimer

THE GITHUB REPOSITORY LINKS AND VERSION TAG MAPPINGS ARE PROVIDED ON A **BEST-EFFORT BASIS**.

THE INFORMATION IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE INFORMATION OR THE USE OR OTHER DEALINGS IN THE INFORMATION.

- Repository URLs may become unavailable if projects are moved, renamed, or deleted
- Version tags may not exist for all vulnerable versions
- Tag names may change over time
- Some repositories may require authentication or have access restrictions

### Checklist

- [ ] I have verified the GitHub repository URLs are accessible
- [ ] I have tested the version tag mappings where possible
- [ ] I have updated the README.md documentation
- [ ] I have read and agree to the disclaimer above

### Related Issues

Closes #<!-- issue number if applicable -->

---

💡 **Note**: If you find any incorrect or broken links, please open an issue so we can update the database.
