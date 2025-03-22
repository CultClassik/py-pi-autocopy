import os
import shutil
import time
import argparse


def parse_args():
  parser = argparse.ArgumentParser(description='Copy file to USB drive.')
  parser.add_argument('--source', required=True, help='Source file to copy')
  parser.add_argument('--usb', required=True, help='USB mount point')
  parser.add_argument('--destination', required=True, help='Destination file path on USB')

  return parser.parse_args()

def is_usb_inserted(usb_mount_point):
  return os.path.ismount(usb_mount_point)

def copy_file_to_usb(source_file_path, destination_file_namke):
  shutil.copy(source_file_path, destination_file_namke)
  print(f"Copied {source_file_path} to {destination_file_namke}")

def main(source_file_path, usb_mount_point, destination_file_name):
  while True:
    if is_usb_inserted(usb_mount_point):
      copy_file_to_usb(source_file_path destination_file_name)
    time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
  args = parse_args()
  main(args.source, args.usb, os.path.join(args.destination))
  