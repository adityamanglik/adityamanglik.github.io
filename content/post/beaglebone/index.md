---
title: Flashing the BeagleBone Black
# subtitle: Standing Invitation

# Summary for listings and search engines
summary: Flashing the BeagleBone Black

# Link this post with a project
# projects: []

# Date published
date: '2016-05-13T00:00:00Z'

# Date updated
lastmod: '2016-05-13T00:00:00Z'

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/CpkOjOcXdUY)'
#   focal_point: ''
#   placement: 2
#   preview_only: false

authors:
  - admin

# tags:
#   - Academic

# categories:
---
There are many ways to flash a [BeagleBone Black](https://beagleboard.org/black):

1. Boot off of SD Card
2. Flash from a Flasher image
3. Flash using the BBBlfs

Here is a bit of a hardcore way to do it if all else fails.

First of all boot using the SD card and ensure that your system works. This should not be a problem.

Next step is to dd the SD card's image to the on board eMMC. Since the SD card works, if we simply copy the disks, the onboard memory should work perfectly as well!

Unmount the filesystem(all disks) using this command:


`mount -o remount,ro / `

If it says / is busy, we have to make the root filesystem boot in read only. To do this, go to /etc/fstab and make the following changes


Change the entry

`/dev/sda1 / ext2 relatime,rw,errors=remount-ro 0 1`

to

`/dev/sda1 / ext2 noatime,ro 0 1`



Restart the BBB and boot from the SD once again.
Now issue the following command:


`dd if=/dev/mmcblk0 of=/dev/mmcblk1`

The above command assumes SD located at blk0 and eMMC located at blk1. Please check this using the fdisk -l output and issue the correct command.
At the end of this process,remount your filesystem using this command


`mount -o remount,rw /`

Now undo the changes you made to fstab file and enjoy!

## Common Mistakes

Check if your BBB has 2 GB(Rev B) on board memory of 4 GB(Rev C). Please select and download the appropriate image from the image download page.