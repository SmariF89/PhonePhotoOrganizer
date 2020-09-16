# PhonePhotoOrganizer
  A script which scans through a folder of unorganized photos, reads their metadata (date modified) and organizes them neatly in another folder.

  This script should work fine with DCIM (camera photos) folders of Android phones - where all photos are stored in a single folder, unorganized. 

## Usage
  Using your favorite shell, type in "./PhonePhotoOrganizer.py \<photo folder name\> \<organized folder name\>"

  The first argument is the name of the unorganized photo folder, the second argument is the folder which to the organized photos will be moved. The script will create the folder if it does not exist.

  The script will create a folder structure like this \/<Year>\/<Month>\/\<Day #\>.
  
## Future improvements
  - The script should be modified such that it would look at the photos' "Date taken" metadata rather than "Date modified". This is very important as some photos' "Date modified" does not match "Date taken".
  - The script should be more generalized and not only work for Android camera folders - By simply having it support more filetypes than jpg, mp4 and gif. It should, for       instance also support cr2 files.
