#!/usr/bin/env python3
"""
Java CVE Benchmark - Vulnerability Downloader
A simple script to download all vulnerability JAR files from the verified URLs.
"""

import pandas as pd
import requests
from pathlib import Path
import sys
from urllib.parse import urlparse
import time

def download_vulnerabilities():
    """Download all vulnerability files from the CSV database."""
    
    # Check if CSV file exists
    csv_file = 'java_cve_verified_download_urls.csv'
    if not Path(csv_file).exists():
        print(f"❌ Error: {csv_file} not found!")
        print("Please make sure you're running this script in the repository root directory.")
        return False
    
    # Read the CSV file
    try:
        df = pd.read_csv(csv_file)
        print(f"📊 Found {len(df)} verified download URLs")
    except Exception as e:
        print(f"❌ Error reading CSV file: {e}")
        return False
    
    # Create download directory
    download_dir = Path('final_downloads')
    download_dir.mkdir(exist_ok=True)
    print(f"📁 Download directory: {download_dir.absolute()}")
    
    # Download each file
    success_count = 0
    failed_downloads = []
    
    for index, row in df.iterrows():
        try:
            project_name = row['project_name']
            version = row['version']
            cve_id = row['cve_id']
            download_url = row['download_url']
            
            # Generate filename
            filename = f"{project_name}_{version}_{cve_id}.jar"
            filepath = download_dir / filename
            
            # Skip if file already exists
            if filepath.exists():
                print(f"⏭️  Skipping {filename} (already exists)")
                success_count += 1
                continue
            
            print(f"📥 Downloading [{index+1}/{len(df)}]: {project_name} {version} ({cve_id})")
            
            # Download the file
            response = requests.get(download_url, timeout=30)
            response.raise_for_status()
            
            # Save the file
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            file_size = filepath.stat().st_size
            print(f"✅ Downloaded: {filename} ({file_size:,} bytes)")
            success_count += 1
            
            # Small delay to be respectful to servers
            time.sleep(0.5)
            
        except Exception as e:
            error_msg = f"Failed to download {filename}: {str(e)}"
            print(f"❌ {error_msg}")
            failed_downloads.append({
                'filename': filename,
                'url': download_url,
                'error': str(e)
            })
    
    # Print summary
    print("\n" + "="*60)
    print("📋 DOWNLOAD SUMMARY")
    print("="*60)
    print(f"✅ Successful downloads: {success_count}/{len(df)}")
    print(f"❌ Failed downloads: {len(failed_downloads)}")
    print(f"📁 Files saved to: {download_dir.absolute()}")
    
    if failed_downloads:
        print("\n❌ Failed Downloads:")
        for failed in failed_downloads:
            print(f"   • {failed['filename']}: {failed['error']}")
    
    return len(failed_downloads) == 0

if __name__ == "__main__":
    print("🚀 Java CVE Benchmark - Vulnerability Downloader")
    print("="*60)
    
    try:
        success = download_vulnerabilities()
        if success:
            print("\n🎉 All downloads completed successfully!")
        else:
            print("\n⚠️  Some downloads failed. Check the summary above.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⏹️  Download interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
