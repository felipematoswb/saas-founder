from django.core.management.base import BaseCommand
from typing import Any
from django.conf import settings
import helpers
import helpers.downloader

VENDOR_STATICFILES = {'output.css': 'https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.min.css',
                      'output.js': 'https://cdn.tailwindcss.com',
                      }

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files")
        completed_urls = []

        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.downloader.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to download {url}')
                )

        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.style.SUCCESS('Successfully updated all vendor static files')
        else:
            self.style.WARNING('Some files were not updated')
