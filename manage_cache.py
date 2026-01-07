#!/usr/bin/env python3
"""
Utility script to manage the popular films cache
"""

import json
from pathlib import Path
import time

# Use absolute path
script_dir = Path(__file__).parent
CACHE_FILE = script_dir / 'letterboxd_popular_cache.json'


def check_cache():
    """Check cache status"""
    if not CACHE_FILE.exists():
        print("❌ No cache file found")
        return
    
    try:
        # Get cache age
        cache_age_seconds = time.time() - CACHE_FILE.stat().st_mtime
        cache_age_days = cache_age_seconds / 86400
        
        # Load cache data
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            cached_data = json.load(f)
        
        # Display info
        print(f"\n{'='*60}")
        print(f"POPULAR FILMS CACHE STATUS")
        print(f"{'='*60}")
        print(f"📁 File: {CACHE_FILE.absolute()}")
        print(f"📊 Films cached: {len(cached_data)}")
        print(f"🕐 Cache age: {cache_age_days:.1f} days")
        print(f"⚠️  Expires in: {7 - cache_age_days:.1f} days")
        
        if cache_age_days >= 7:
            print(f"\n⚠️  Cache is EXPIRED (older than 7 days)")
        else:
            print(f"\n✅ Cache is VALID")
        
        # Show sample films
        print(f"\n📽️  Sample films:")
        for film in cached_data[:5]:
            print(f"   - {film['title']}")
        
    except Exception as e:
        print(f"❌ Error reading cache: {e}")


def clear_cache():
    """Delete the cache file"""
    if not CACHE_FILE.exists():
        print("ℹ️  No cache file to clear")
        return
    
    try:
        CACHE_FILE.unlink()
        print("✅ Cache cleared successfully")
        print("   Next recommendation run will fetch fresh data from Letterboxd")
    except Exception as e:
        print(f"❌ Error clearing cache: {e}")


def main():
    print("\n🎬 Letterboxd Popular Films Cache Manager\n")
    print("1. Check cache status")
    print("2. Clear cache (force fresh scraping)")
    print("3. Exit")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == '1':
        check_cache()
    elif choice == '2':
        confirm = input("\n⚠️  Are you sure you want to clear the cache? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            clear_cache()
        else:
            print("ℹ️  Cache not cleared")
    elif choice == '3':
        print("👋 Goodbye!")
    else:
        print("❌ Invalid option")


if __name__ == "__main__":
    main()
